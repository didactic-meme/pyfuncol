from setuptools import setup, find_packages

setup(
    name="pyfuncol",
    description="Functional collections extension functions for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/didactic-meme/pyfuncol",
    author="Andrea Veneziano",
    author_email="andrea.veneziano@icloud.com",
    maintainer="Andrea Veneziano",
    maintainer_email="andrea.veneziano@icloud.com",
    license="MIT",
    keywords="functional pipeline data collection chain parallel",
    packages=find_packages(exclude=["contrib", "docs", "*tests*", "test"]),
    version="1.3.1",
    install_requires=["forbiddenfruit", "dask"],
    extras_requires={
        "dev": [
            "pytest",
            "pytest-cov",
            "myst-parser",
            "black",
            "Sphinx",
            "sphinx-rtd-theme",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
