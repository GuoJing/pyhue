# -*- coding: utf-8 -*-

STATION_IP = '0.0.0.0'
DEVICE_TYPE = 'pyhue'
DEFAULT_TRANSITIONTIME = 3
import yaml

import os

def get_home(*path):
    try:
        from win32com.shell import shellcon, shell
    except ImportError:
        home = os.path.expanduser("~")
    else:
        home = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0)
    return os.path.join(home, *path)

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

class HueConf:

    def __repr__(self):
        return '<pyhue Config %s %s>' % (self.station_ip,
                self.device_type)

    def __init__(self, station_ip='', device_type='', filename=None):
        ensure_dir(get_home('.hue'))
        filename = filename if filename else 'config.yml'
        filename = get_home('.hue', filename)
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                f.write("""#Config of pyhue
station_ip:  %s
device_type: %s
default_transitiontime: %s""" % (station_ip or STATION_IP,
                    device_type or DEVICE_TYPE,
                    DEFAULT_TRANSITIONTIME))
        with open(filename, 'r') as cfg:
            self._conf = yaml.load(cfg)
        self._filename = filename

    @property
    def station_ip(self):
        return str(self._conf.get('station_ip', STATION_IP))

    @property
    def device_type(self):
        return str(self._conf.get('device_type', DEVICE_TYPE))

    @property
    def default_transitiontime(self):
        try:
            return int(self._conf.get('default_transitiontime',
                DEFAULT_TRANSITIONTIME))
        except:
            return DEFAULT_TRANSITIONTIME
