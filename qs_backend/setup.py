from setuptools import setup

setup(name='qs_backend',
      version='1.0.1.devel',
      description='Backend for Praneesh s Quick Stocks',
      author='Praneesh Kataru',
      author_email='pranuvitmsse05@gmail.com',
      packages=['qs_backend',
                'qs_backend.controllers',
                'qs_backend.dal',
                'qs_backend.decorators',
                'qs_backend.exceptions',
                'qs_backend.logger',
                'qs_backend.models',
                'qs_backend.publisher',
                'qs_backend.queues',
                'qs_backend.workers'],
      install_requires=['flask >= 0.8',
                        'flask-cors >= 3.0.2',
                        'flask-restful >= 0.3.5',
                        'yahoo-finance >= 1.1.4',
                        'dicttoxml >= 1.7.4',
                        'flask-swagger >= 0.2.12',
                        'jsonpickle >= 0.9.3',
                        'autobahn >= 0.16.0',
                        'requests >= 2.11.1'],
      classifiers=['Development Status :: 1 Beta'])

__author__ = 'Praneesh Kataru'
