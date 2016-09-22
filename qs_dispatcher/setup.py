from setuptools import setup

setup(name='qs_disptacher',
      version='1.1.2.devel',
      description='Dispatcher for Praneesh s Quick Stocks',
      author='Praneesh Kataru',
      author_email='pranuvitmsse05@gmail.com',
      packages=['qs_dispatcher',
                'qs_dispatcher.qs_wamp'],
      install_requires=['autobahn >= 0.16.0'],
      classifiers=['Development Status :: 1 Beta'])

__author__ = 'Praneesh Kataru'
