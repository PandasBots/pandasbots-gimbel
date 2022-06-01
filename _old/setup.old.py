''' read the contents of your README file '''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gimbel",
    version="0.0.1",
    license='MIT',
    author="Rafael Klanfer Nunes",
    author_email="comercial@pandasbots.com",
    description="This package allows you to scrap Gimbel Mexicana website and return product infos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='gimbel project',
    url="https://pandasbots.com/",
    project_urls={
        "Git Hub": "https://github.com/PandasBots/gimbel-pypi",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
