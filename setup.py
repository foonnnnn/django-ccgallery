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
    description='A minimal Gallery application for Django',
    long_description=open('README.rst').read(),
    author='c&c Design Consultants LTD',
    author_email='studio@designcc.co.uk',
    url='https://github.com/designcc/django-ccgallery',
    package_data={
        'ccgallery' : [
            'templates/ccgallery/*.html',
            'static/ccgallery/*.jpg',
            'static/ccgallery/css/*.css',
        ],
    },
    packages=[
        'ccgallery',
        'ccgallery.templatetags',
        'ccgallery.tests'
    ],
    install_requires=['django-ccthumbs',])
