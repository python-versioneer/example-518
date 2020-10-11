import os

from setuptools import find_namespace_packages, setup

import versioneer

os.chdir(os.path.abspath(os.path.dirname(__file__)))

setup(
    name="example",
    version=versioneer.get_version(),
    description="SomeDescription",
    long_description="{0}".format(open("README.rst").read()),
    author="Nathan Buckner",
    author_email="example@example.com",
    url="git@github.com:bucknerns/examplerepo",
    packages=find_namespace_packages("src"),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python"],
    package_dir={"": "src"},
    entry_points={"console_scripts": []},
    cmdclass=versioneer.get_cmdclass())
