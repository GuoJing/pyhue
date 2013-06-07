# -*- coding: utf-8 -*-

import socket
import json
import hashlib
from time import sleep

try:
    import requests
except:
    from warnings import warn
    warn('You should install requests, try pip install colorpy')

REQUEST_URI = 'http://%s/api'

class HueHttpMixin:

    username = hashlib.md5('ph-%s' % socket.getfqdn()).hexdigest()

    def request(self, method='GET', uri='', data={}):
        uri = 'http://%s/api/%s%s' % (
            self.station_ip,
            self.username,
            uri
        )

        resp = requests.request(method, uri, data=data)
        resp = json.loads(resp.content)

        if isinstance(resp, list) and resp[0].get('error'):
            error = resp[0]['error']
            if error['type'] == 1:
                print error
                return error
        else:
            return resp

    def auth(self, retry=10):
        uri = REQUEST_URI % self.station_ip

        auth = dict(devicetype=self.device_type, username=self.username)
        resp = requests.post(uri, data=json.dumps(auth))
        resp = json.loads(resp.content)

        print 'Press the your button!'

        if resp and isinstance(resp, list) and resp[0].get('error'):
            if retry:
                print 'retry...'
                sleep(5)
                self.auth()
            return True

        return True

