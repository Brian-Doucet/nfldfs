from setuptools import setup

# Get the long description from the README
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='nfldfs',
      version='0.0.5',
      author='Brian Doucet',
      author_email='doucetba@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      description='A simple package to scrape NFL daily fantasy data.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      keywords='nfl daily fantasy sports dfs sports analytics draftkings fanduel yahoo',
      python_requires='>=3.0',
      url='https://github.com/briandoucet01/nfldfs',
      packages=['nfldfs'],
      tests_require=['pytest'],
      install_requires=[
          'beautifulsoup4==4.8.2',
          'click==7.1.1',
          'lxml==4.5.0',
          'pandas==1.0.3',
          'requests==2.23.0'],
     entry_points={
        'console_scripts': [
            'cli = cli:cli',
            ],
     },
)
