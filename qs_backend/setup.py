from setuptools import setup

setup(name='qs_backend',
      version='0.1.1.devel',
      description='Backend for Praneesh s Quick Stocks',
      author='Praneesh Kataru',
      author_email='pranuvitmsse05@gmail.com',
      packages=['qs_backend',
                'qs_backend.controllers',
                'qs_backend.exceptions',
                'qs_backend.tests'],
      install_requires=['flask >= 0.8',
                        'flask-restful >= 0.3.5',
                        'dicttoxml >= 1.7.4',
                        'flask-swagger >= 0.2.12',
                        'jsonpickle >= 0.9.3'],
      classifiers=['Development Status :: 1 Beta'])

__author__ = 'Praneesh Kataru'
