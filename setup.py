from setuptools import setup

desc = 'piptestb'
setup(
    name='piptestb',
    description=desc,
    packages=['piptestb'],
    install_requires=open('requirements.txt', 'r').read().split(),
    long_description=desc,
)
