from setuptools import setup, find_packages

install_requires = open('requirements.txt', 'r').readlines()

setup(
    name='gittranslate',
    version='1.0',
    description='A package that facilitates the translation of files in local and remote git repositories',
    author='Péter Ferenc Gyarmati',
    author_email='dev.petergy@gmail.com',
    python_requires='>=3.10',
    install_requires=install_requires,
    packages=find_packages(),
    project_urls={
        'GitHub': 'https://github.com/peter-gy/git-translate',
    },
)
