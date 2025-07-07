from setuptools import setup, find_packages

setup(
    name="fpseq",            # package name users will pip install
    version="0.1.0",              # bump as you release updates
    description=" package for working with protein sequences and mutations, and FPbase API wrapper to retrieve fluorescent protein sequences Resources",
    packages=find_packages(),     # finds my_helpers
    python_requires=">=3.11.9",      # adjust as needed
)