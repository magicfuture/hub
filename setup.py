from setuptools import setup

setup(
    name='hub',
    version='1.0',
    packages=['hub'],
    install_requires=[
        'requests', 'evaluate', 'langchain'
    ],
)