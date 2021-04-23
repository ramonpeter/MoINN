from setuptools import setup

HTTPS_GITHUB_URL = "https://github.com/ramonpeter/MoINN"

with open("README.md", "r") as fh:
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
    long_description_content_type="text/markdown",
    url=HTTPS_GITHUB_URL,

    # dependencies
    packages=['MoINN'],
)
