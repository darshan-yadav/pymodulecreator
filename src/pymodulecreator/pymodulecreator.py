import os
from pathlib import Path

'''Package/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── setup.cfg
    ├── src/
    │   └── package/
    │       └── __init__.py
    └── tests/'''

def init(modulename : str) :
    Path("./"+modulename+"/src/"+ modulename).mkdir(parents=True, exist_ok=True)
    Path("./"+modulename+"/tests").mkdir(parents=True, exist_ok=True)

    filepath = Path("./"+modulename+"/src/"+ modulename + "/" +"__init__.py")
    filepath.open("w", encoding ="utf-8")

    filepath = Path("./"+modulename + "/" +"LICENSE")
    filepath.open("w", encoding ="utf-8")

    filepath = Path("./"+modulename + "/" +"README.md")
    filepath.open("w", encoding ="utf-8")

    filepath = Path("./"+modulename + "/" +"setup.py")
    fp = filepath.open("w", encoding ="utf-8")

    fp.write('import setuptools\n')

    fp.write('with open("README.md", "r", encoding="utf-8") as fh:\n')
    fp.write('    long_description = fh.read()\n')
    fp.write('    setuptools.setup(\n')
    fp.write('    name="'+ modulename +'",\n')
    fp.write('    version="0.0.1",\n')
    fp.write('    author="YourName",\n')
    fp.write('    author_email="your@email.com",\n')
    fp.write('    description="description",\n')
    fp.write('    classifiers=[\n')
    fp.write('        "Programming Language :: Python :: 3",\n')
    fp.write('        "License :: OSI Approved :: MIT License",\n')
    fp.write('        "Operating System :: OS Independent",\n')
    fp.write('    ],\n')
    fp.write('    package_dir={"": "src"},\n')
    fp.write('    packages=setuptools.find_packages(where="src"),\n')
    fp.write('    python_requires=">=3.6",\n')
    fp.write('    install_requires=[],\n')
    fp.write(    ')\n')
    fp.close()

    filepath = Path("./"+modulename + "/" +"pyproject.toml")
    fp = filepath.open("w", encoding ="utf-8")
    fp.write('[build-system]\n')
    fp.write('requires = [\n')
    fp.write('    "setuptools>=42",\n')
    fp.write('    "wheel"\n')
    fp.write(']\n')
    fp.write('build-backend = "setuptools.build_meta"\n')