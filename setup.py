from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='nfldfs',
      version='0.0.1',
      author='Brian Doucet',
      author_email='doucetba@gmail.com',
      description='A simple package to scrape NFL daily fantasy data.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/briandoucet01/nfldfs',
      packages=['nfldfs'],
      tests_require=['pytest'],
      install_requires=[
          'beautiflsoup==4.8.2',
          'click==7.1.1',
          'lxml==4.5.0',
          'pandas==1.0.3',
          'requests==2.23.0'])
