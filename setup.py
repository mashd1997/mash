from setuptools import setup, find_packages

setup(
    name='mash',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url= 'https://github.com/mashd1997/mash',
    author='Mashudu Molefe',
    author_email='mashmolefe97@gmail.com'

)
