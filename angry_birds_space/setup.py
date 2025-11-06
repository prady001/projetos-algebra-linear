from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="angry-birds-space",
    version="1.0.0",
    author="Grupo de Álgebra Linear",
    description="Jogo estilo Angry Birds no espaço com física gravitacional",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/angry-birds-space",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pygame>=2.6.0",
        "numpy>=1.24.0",
    ],
    entry_points={
        "console_scripts": [
            "angry-birds-space=angry_birds_space.main:main",
        ],
    },
)

