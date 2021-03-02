import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="etsy-python-api",
    version="0.1.0",
    author="Vadim Makarov",
    author_email="add4che@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/run4w4y/etsy-python-api",
    packages=setuptools.find_packages(),
    install_requires=[
        'httpx',
        'authlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)