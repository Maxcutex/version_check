import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="version-analyzer-maxcutex",
    version="0.0.1",
    author="Eno Bassey",
    author_email="ennyboy@gmail.com",
    description="A version analyzing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
)