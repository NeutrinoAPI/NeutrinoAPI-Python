from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='neutrino_api',
    version='3.4.1',
    description='The general-purpose API',
    long_description=long_description,
    author='NeutrinoAPI',
    author_email='tech@neutrinoapi.com',
    url='https://www.neutrinoapi.com/contact-us/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ]
)