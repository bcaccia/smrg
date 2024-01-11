from setuptools import setup

setup(
    name='smrg',
    version='1.0.0',
    py_modules=['smrg'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'smrg = smrg:cli',
        ],
    },
)