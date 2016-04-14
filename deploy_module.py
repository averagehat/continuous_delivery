#!/usr/bin/env python

import sys
import argparse
import os
import string
import logging

import sh
from path import Path
import requests

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)

GITHUB_URL = 'https://github.com'
GITHUB_API_URL = 'https://api.github.com'

module_template = string.Template('''#%Module 1.0
#
#  ngs_mapper pipeline module
#
prepend-path    PATH    ${project_dir}/miniconda/bin
''')

def parse_args():
    parser = argparse.ArgumentParser(
        description='''Do environmental module via continuous deployment''',
        epilog='Manages -stable and -latest by ensuring -latest is always' \
            ' up-to-date with the latest commit in master branch. Stable is the' \
            ' latest release on github'
    )
    parser.add_argument(
        'software',
        type=Path,
        help='Path where software gets installed'
    )
    parser.add_argument(
        'modules',
        type=Path,
        help='Path where modules are installed'
    )
    parser.add_argument(
        'git_project_uri',
        type=Path,
        help='Path to git repo to clone from'
    )
    return parser.parse_args()

def get_gh_(api_slug, gh_project):
    '''
    Fetch gh api for api_slug
    
    :param api_slug string: repos or tags
    :param gh_project string: owner/reponame on github.com
    '''
    url = '{0}/repos/{2}/{1}'.format(GITHUB_API_URL, api_slug, gh_project)
    r = requests.get(url)
    if r.status_code not in (200,):
        raise ValueError("Fetching {0} failed for url {1}".format(api_slug, url))
    return r.json()

def get_gh_tags(gh_project):
    '''
    fetch all tags for project
    https://developer.github.com/v3/repos/#list-tags
    '''
    return get_gh_('tags', gh_project)

def get_gh_releases(gh_project):
    '''
    fetch all releases for project
    https://developer.github.com/v3/repos/releases/#list-releases-for-a-repository
    '''
    return get_gh_('releases', gh_project)

def update_project(project_dir):
    logging.info('Updating {0} remotes'.format(project_dir))
    sh.git('remote', 'update', _out=sys.stdout, _cwd=project_dir)

def reset_branch(project_dir, branch):
    logging.info('Resetting {0} to {1}'.format(project_dir, branch))
    sh.git('reset', '--hard', branch, _out=sys.stdout, _cwd=project_dir)

def clone_project(git_project_uri, where):
    logging.info('Cloning {0} to {1}'.format(git_project_uri, where))
    sh.git('clone', git_project_uri, where, _out=sys.stdout)

def install_project(project_dir):
    _cwd = os.getcwd()
    os.chdir(project_dir)
    installer = Path('install.sh').abspath()
    if installer.exists():
        logging.info('Running {0}'.format(installer))
        install = sh.Command(installer)
        install(_out=sys.stdout)
    else:
        logging.info('{0} does not contain install.sh'.format(project_dir))
    os.chdir(_cwd)

def clone_update(project_dir, git_project_uri):
    if not project_dir.exists():
        clone_project(git_project_uri, project_dir)
    update_project(project_dir)

def update_origin(project_dir, upstream_uri):
    logging.info(
        "Resetting origin url in {0} to {1}".format(
            project_dir, upstream_uri
        )
    )
    sh.git('remote', 'set-url', 'origin', upstream_uri, _cwd=project_dir)

def make_software(project_dir, git_project_uri, branch, upstream_uri):
    clone_update(project_dir, git_project_uri)
    update_origin(project_dir, upstream_uri)
    reset_branch(project_dir, branch)
    install_project(project_dir)

def make_module(project_dir, modulesdir, modulename=None):
    '''
    :param Path project_dir: path to project directory that is installed
    :param Path modulesdir: where modules should go
    '''
    projname = project_dir.basename()
    proj = projname.split('-')[0]
    if modulename:
        module_path = modulesdir / proj / modulename
    else:
        module_path = modulesdir / proj / projname
    module_path.dirname().makedirs_p()
    module_path.write_text(
        module_template.substitute(project_dir=project_dir.abspath())
    )

def install(project_dir, git_project_uri, branch, modulesdir, upstream_uri):
    #make_software(project_dir, git_project_uri, branch, upstream_uri)
    make_module(project_dir, modulesdir)

def main():
    args = parse_args()
    args.modules.makedirs_p()
    project = '/'.join(args.git_project_uri.split('/')[-2:])
    proj = args.git_project_uri.basename()
    project_cache = args.software / '.' + proj
    git_project_uri = project_cache
    # Should be ordered with latest tag first(assumption/observation)
    tags = map(lambda json: json['name'], get_gh_tags(project))

    # Stable is latest develop branch commit
    projdir_stable = args.software / proj / proj + '-{0}'.format(tags[0])
    # Latest is latest release/tag
    projdir_latest = args.software / proj / proj + '-latest'
    
    logging.info(
        "Updating/Cloning {0} into {1}".format(
            args.git_project_uri, project_cache
        )
    )
    clone_update(project_cache, args.git_project_uri)
    # Install/reset/update to latest in develop from origin
    install(
        projdir_latest, git_project_uri, 'origin/develop',
        args.modules, args.git_project_uri
    )
    # Install latest tag(stable)
    install(
        projdir_stable, git_project_uri, tags[0],
        args.modules, args.git_project_uri
    )

if __name__ == '__main__':
    main()
