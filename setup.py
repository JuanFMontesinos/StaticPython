import re
from setuptools import setup, find_packages

VERSIONFILE = "staticpython/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
setup(
    name='staticpython',
    version=verstr,
    packages=find_packages(),
    install_requires=[],
    author='Juan Montesinos',
    author_email='jfmontgar@gmail.com',
    description='A Python package for enforcing type hints at runtime.',
    keywords='type hints enforcement',
    url='https://github.com/JuanFMontesinos/StaticPython',  # Optional: if you have a GitHub repository
)