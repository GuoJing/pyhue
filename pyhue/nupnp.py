import urllib2
import socket
import json

socket.setdefaulttimeout(10)

error = 'Need the same wifi rout. (No VPN)'

def get_nupnp_info():
    response = urllib2.urlopen('http://www.meethue.com/api/nupnp', timeout=10)
    r = json.loads(response.read())
    return r

def get_id(device_index=0):
    try:
        info = get_nupnp_info()
        id = info[device_index].get('id')
        return str(id)
    except:
        print error

def get_internalipaddress(device_index=0):
    try:
        info = get_nupnp_info()
        internalipaddress = info[device_index].get('internalipaddress')
        return str(internalipaddress)
    except:
        print error

def get_macaddress(device_index=0):
    try:
        info = get_nupnp_info()
        macaddress = info[device_index].get('macaddress')
        return str(macaddress)
    except:
        print error

def get_hue(device_type='pyhue', ip=''):
    try:
        from hue import Hue
        from config import HueConf
        ip = ip or get_internalipaddress()
        conf = HueConf(station_ip=ip,
                device_type=device_type)
        return Hue(station_ip=conf.station_ip,
                device_type=conf.device_type)
    except:
        print error
