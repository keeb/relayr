from os import environ

properties = {}

properties['RETHINK_HOST'] = environ['RETHINK_HOST']
properties['RETHINK_PORT'] = environ['RETHINK_PORT']
properties['RELAY_URL'] = environ['RELAY_URL']

