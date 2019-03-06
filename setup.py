from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='CNN can get the same accuracy (or higher) with much less data when trained using stacked convolutional autoencoders on patches of the dataset.',
    author='Shay Geller',
    license='MIT',
)
