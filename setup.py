from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in venturitech/__init__.py
from venturitech import __version__ as version

setup(
	name="venturitech",
	version=version,
	description="Customisation",
	author="Venturitech",
	author_email="doreenmwapekatebe8@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
