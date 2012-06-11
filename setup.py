import os
from distutils.core import setup
from ccgallery import VERSION

root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

setup(
    name='ccgallery',
    version=VERSION,
    license='BSD 3 Clause',
    description='',
    long_description=open('README.rst').read(),
    author='',
    author_email='',
    url='',
    package_data={
        'ccgallery' : [
            'templates/ccgallery/*.html',
            'static/ccgallery/css/*.css',
        ],
    },
    packages=[
        'ccgallery',
        'ccgallery.templatetags',
        'ccgallery.tests'
    ],
    install_requires=[])
