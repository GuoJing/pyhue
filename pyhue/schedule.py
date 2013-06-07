# -*- coding: utf-8 -*-

class HueSchedule:
    id = None

    def __init__(self, hue, id):
        self.hue = hue
        self.id = id

    def __repr__(self):
        return '<HueSchedule %s %s>' % (self.id, self.name)

    @property
    def info(self):
        info = self.hue.request(uri='/schedules/%s' % self.id,
                method='GET')
        return info

    def set_state(self):
        self.hue.request(uri='/schedules/%s' % self.id,
                method='PUT')
        return self

    def delete(self):
        self.hue.request(uri='/schedules/%s' % self.id,
                method='DELETE')

    @property
    def name(self):
        return self.info['name']


    @property
    def description(self):
        return self.info['description']

    @property
    def command(self):
        return self.info['command']

    @property
    def time(self):
        return self.info['time']
