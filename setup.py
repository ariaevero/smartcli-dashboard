from setuptools import setup, find_packages

setup(
    name="smartcli",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "psutil",
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "smartcli=smartcli.main:app",
        ],
    },
    author="Aria",
    description="A smart CLI utility with dashboard",
)
