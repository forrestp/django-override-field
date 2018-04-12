import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-override-field',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django override fields with admin support',
    long_description=README,
    url='https://github.com/forrestp/django-override-field',
    author='Forrest Pieper',
    author_email='forrest.pieper@gmail.com',
    classifiers=[
	'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
