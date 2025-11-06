"""
Setup script para instalação da biblioteca Enigma.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="enigma-lib",
    version="0.1.0",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Biblioteca Python para criptografia usando máquina Enigma com álgebra linear",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/enigma-lib",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Security :: Cryptography",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)

