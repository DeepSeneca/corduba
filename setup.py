from setuptools import setup, find_packages
from setuptools.config.expand import entry_points

from corduba import __version__

setup(
    name="Corduba Provisioning Server",
    version=__version__,
    author="Marco Hertwig",
    author_email="info@concentric-scale.com",
    description="A provisioning server based on FasAPI for the Deep Seneca project. Is used to provide the "
                "SenecaApp with data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DeepSeneca/corduba",
    packages=find_packages(),
    install_requires=[
        "annotated-types",
        "anyio",
        "click",
        "colorama",
        "eceptiongroup",
        "fastapi",
        "h11",
        "httptools",
        "idna",
        "pydantic",
        "pydantic_core",
        "python-dotenv",
        "PyYAML",
        "sniffio",
        "starlette",
        "typing_extensions",
        "uvicorn",
        "watchfiles",
        "websockets"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12"
)


