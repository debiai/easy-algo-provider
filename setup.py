from setuptools import setup, find_packages
from easy_algo_provider.app import APP_VERSION

# Import the README and use it as the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setup the package
setup(
    name="easy_algo_provider",
    version=APP_VERSION,
    description="A Python package for running AlgoProviders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debiai/eaty-algo-provider",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "fastapi==0.115.4",
        "uvicorn==0.32.0",
    ],
    entry_points={},
)
