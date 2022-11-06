"""Setup configuration."""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    README_CONTENTS = fh.read()

setuptools.setup(
    name="alpinepkgs",
    version="1.1.6",
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description=README_CONTENTS,
    install_requires=["requests"],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/alpinepkgs",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
