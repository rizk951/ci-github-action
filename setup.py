from setuptools import setup, find_packages

setup(
    name="ci-github-action",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
    ],
    python_requires=">=3.6",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CI/CD project using GitHub Actions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rizk951/ci-github-action",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 