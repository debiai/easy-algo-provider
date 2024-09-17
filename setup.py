from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="algo_provider_module_name",
    version="0.1.0",
    description="A Python package for running and managing AlgoProvider",
    long_description=long_description,
    long_description_content_type="",  # README
    url="https://github.com/debiai/algo-provider-module",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "Flask==2.0.3",
        "flask_cors==3.0.8",
        "connexion==2.6.0",
        "requests==2.25.1",
        "swagger-ui-bundle==0.0.5",
        "openapi_spec_validator==0.2.8",
        "jsonschema==3.2.0",
        "Werkzeug==2.2.2",
    ],
    entry_points={},
    include_package_data=True,
)
