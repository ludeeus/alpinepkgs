"""Setup configuration."""
import setuptools

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="alpinepkgs",
    version="1.1.6",
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description=LONG,
    install_requires=["requests", "click"],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/alpinepkgs",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={"console_scripts": ["alpinepkgs = alpinepkgs.cli:cli"]},
)
