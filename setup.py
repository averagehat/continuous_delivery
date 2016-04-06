from setuptools import setup, find_packages

import continous_delivery

setup(
    name = continous_delivery.__projectname__,
    version = continous_delivery.__release__,
    packages = find_packages(),
    author = continous_delivery.__authors__,
    author_email = continous_delivery.__authoremails__,
    description = continous_delivery.__description__,
    license = "GPLv2",
    keywords = continous_delivery.__keywords__,
)
