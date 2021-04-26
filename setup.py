from setuptools import setup, find_packages

HTTPS_GITHUB_URL = "https://github.com/ramonpeter/MoINN"

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="MoINN",
    version="1.0",
    description="Modules for Invertible Neural Networks",
    license="MIT",

    # meta data
    author="Ramon Winterhalder",
    author_email="",
    long_description=long_description,
    long_description_content_type="text/rst",
    url=HTTPS_GITHUB_URL,

    # dependencies
    packages=find_packages(),
    install_requires=['numpy>=1.15.0', 'scipy>=1.5', 'tensorflow>=2.1.0'],
)
