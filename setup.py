from setuptools import setup, find_packages

import continuous_delivery

setup(
    name = continuous_delivery.__projectname__,
    version = continuous_delivery.__release__,
    packages = find_packages(),
    author = continuous_delivery.__authors__,
    author_email = continuous_delivery.__authoremails__,
    description = continuous_delivery.__description__,
    license = "GPLv2",
    keywords = continuous_delivery.__keywords__,
)
