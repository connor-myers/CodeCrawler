from setuptools import setup

setup(
    name='CodeCrawler',
    url='https://github.com/connor-myers/CodeCrawler',
    author='Connor Myers',
    author_email='connor-j-myers@protonmail.com',
    packages=['codecrawler'],
    install_requires=['requests'],
    version='0.1',
    license='MIT',
    description='Grabs Java code and documentation from GitHub repositories'
)