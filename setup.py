import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Toggle", # Replace with your own username
    version="1.1.1",
    author="Laxman Khatri",
    author_email="hackerlaxu@gmail.com",
    description="Toggle is a python package for string to toggle the given string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JKL404/Toggle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
