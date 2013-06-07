# -*- coding: utf-8 -*-

import json
from utils import storify
from controller import HueControllerMixin

class HueLight(HueControllerMixin):
    id = None
    _saved_state = None

    def __init__(self, hue, id):
        self.hue = hue
        self.id = id
        self._conf = hue._conf

    def __repr__(self):
        return '<HueLight %s %s>' % (self.id, self.name)

    def set_state(self, state):
        self.hue.request(uri='/lights/%s/state' % self.id,
            method='PUT',
            data=json.dumps(state))
        return self

    @property
    def info(self):
        info = self.hue.request(uri='/lights/%s' % self.id,
                method='GET')
        return info

    @property
    def state(self):
        return storify(self.state_dict)

    @property
    def state_dict(self):
        return self.info['state']

    @property
    def is_on(self):
        return self.state.on

    @property
    def type(self):
        return self.info['type']

    @property
    def name(self):
        return self.info['name']

    @property
    def modelid(self):
        return self.info['modelid']

    @property
    def swversion(self):
        return self.info['swversion']

    @property
    def pointsymbol(self):
        return storify(self.info['pointsymbol'])

    def rename(self, new_name):
        data = dict(name=new_name)
        self.hue.request(uri='/lights/%s' % self.id,
                method='PUT',
                data=json.dumps(data))

