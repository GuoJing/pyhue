# -*- coding: utf-8 -*-

import json
from utils import storify
from controller import HueControllerMixin

class HueGroup(HueControllerMixin):
    def __init__(self, hue, id):
        self.hue = hue
        self.id = id

    def __repr__(self):
        return '<HueGroup %s %s>' % (self.id, self.name)

    def set_state(self, state):
        self.hue.request(
            uri='/groups/%s/action' % self.id,
            method='PUT',
            data=json.dumps(state))
        return self

    @property
    def info(self):
        info = self.hue.request(uri='/groups/%s' % self.id,
                method='GET')
        return info

    @property
    def action(self):
        return storify(self.info['action'])

    @property
    def lights(self):
        return self.info['lights']

    @property
    def name(self):
        return self.info['name']

    @property
    def scenes(self):
        return storify(self.info['scenes'])
