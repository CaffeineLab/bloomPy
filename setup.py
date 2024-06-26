import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.9'
PACKAGE_NAME = 'bloomcredit-python'
AUTHOR = 'Glenn'
AUTHOR_EMAIL = 'glenn@caffeinelab.com'
URL = ''
LICENSE = 'MIT License'
DESCRIPTION = 'Use the Bloom Credit API with Python'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'python-dotenv',
      'requests'
]


setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      include_package_data=True,
      )
