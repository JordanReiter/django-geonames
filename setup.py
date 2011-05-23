#!/usr/bin/env python

from distutils.core import setup

setup(name='django-geonames',
      description='Models for using the geonames database with Django',
      url='https://github.com/JordanReiter/django-geonames',
      packages=['geonames', 'geonames.gis', 'geonames.gis.mysql', 'geonames.gis.postgres', 'geonames.management', 'geonames.management.commands'],
     )