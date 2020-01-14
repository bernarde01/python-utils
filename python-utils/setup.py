import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-bernarde01", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="bernard.esterhuyse@gmail.com",
    description="A small python utilities package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bernarde01/python-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)