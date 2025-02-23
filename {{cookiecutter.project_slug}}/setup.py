from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.0.300",
        "flask>=2.0.0",
        "pyyaml>=5.1",
        "requests>=2.25.0",
    ],
    author="Duplo",
    author_email="",
    description="A package containing Langchain tools for Kubernetes operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cvpranav/duplo-tool-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
