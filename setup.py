import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="seerbit-python-v2",
    version="1.0.2",
    author="Seerbit",
    author_email="developers@seerbit.com",
    description="A Seerbit API Library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seerbit/seerbit-python-api-library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7',
)
