# -*- coding: utf-8 -*-

import json
from request import HueHttpMixin
from config import HueConf
from datetime import datetime

from light import HueLight
from group import HueGroup
from schedule import HueSchedule
from utils import storify

class Hue(HueHttpMixin):
    is_authd = False

    def __init__(self, station_ip='', device_type='', filename=None):
        self._conf = HueConf(station_ip=station_ip, device_type=device_type,
                filename=filename)
        self.station_ip = station_ip or self._conf.station_ip
        self.device_type = device_type or self._conf.device_type

    def __repr__(self):
        return '<Hue %s>' % self.station_ip

    def _get_state(self):
        state = self.request()
        return state

    @property
    def state(self):
        return self._get_state()

    @property
    def lights(self):
        state = self.state
        return [HueLight(self, l) for l in state['lights']]

    @property
    def config(self):
        return storify(self.state['config'])

    @property
    def schedules(self):
        state = self.state
        return [HueSchedule(self, s) for s in state['schedules']]

    @property
    def groups(self):
        state = self.state
        return [HueGroup(self, g) for g in state['groups']]

    def _search_lights(self):
        return self.request(uri='/lights',
                method='POST',
                data={})

    def get_new_lights(self):
        self._search_lights()
        lights = self.request(uri='/lights/new',
                method='GET',
                data={})
        hue_lights = []
        for k, v in lights.items():
            if isinstance(v, dict):
                hue_lights.append(HueLight(self, k))
        return hue_lights

    def set_config(self, config_dict):
        if not isinstance(config_dict):
            return
        config_keys = ['proxyport', 'name', 'swupdate', 'proxyaddress',
                'linkbutton', 'ipaddress', 'netmask', 'gateway', 'dhcp',
                'portalservices']
        for k in config_dict.keys():
            if not (k in config_keys):
                config_dict.pop(k, None)
        if config_dict:
            self.request(uri='/config', method='PUT', data=config_dict)

    def create_schedule(self, name, description, command, time=None):
        time = time or datetime.now()
        time = time.strftime('%Y-%m-%dT%H:%M:%S')
        if not isinstance(command, dict):
            return False
        data = dict(name=name,
                description=description,
                command=command,
                time=time)
        self.request(uri='/schedules',
                method='POST',
                data=json.dumps(data))
        return True

    def create_group(self):
        '''
        This method is not supported in the 1.0 version of the API.
        It is scheduled for release in the next version of the API.
        '''
        return False
