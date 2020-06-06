from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='m3-project',
    version='1.0.0',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    packages=find_packages(),
    install_requires=(
        'Django==1.11.29',
        'm3-builder==1.2.0',
        'm3-core==2.2.22',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.25',
        'm3-ui==2.2.84',
        'pypiserver==1.3.2',
        'pytz==2019.3',
        'six==1.14.0',
    ),
)
