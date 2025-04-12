from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pulsating-data-pipeline",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Create data pipeline flow diagrams with pulsating arrows using Python code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chrisfoz/pulsating-data-pipeline",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "diagrams>=0.23.3",
        "graphviz>=0.20.1",
    ],
    extras_require={
        "gif": [
            "cairosvg>=2.7.0",
            "imageio>=2.31.1",
            "numpy>=1.24.3",
            "pillow>=10.0.0",
        ],
    },
)