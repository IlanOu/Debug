import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="debug",
    version="0.1.2",
    author="IlanOu",
    author_email="author@example.com",
    description="Une librairie Python pour le débogage et les couleurs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IlanOu/Debug",
    py_modules=["debug"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)