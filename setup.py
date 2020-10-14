from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Toggle',
    url='https://github.com/JKL404/Toggle',
    author='Laxman Khatri',
    author_email='hackerlaxu@gmail.com',
    # Needed to actually package something
    packages=['Toggle'],
    # Needed for dependencies
    #install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='1.1',
    # The license can be anything you like
    license='JKL404',
    description='Toggle is a python package for string to toggle the given string',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
