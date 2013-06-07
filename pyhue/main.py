# -*- coding: utf-8 -*-

from time import sleep
from hue import Hue
from schedule import HueSchedule

def auth():
    '''
    Press the hue button!
    '''
    h = Hue()
    h.auth()

def main():
    on_and_off()

def get_lights():
    print 'Get the lights...'
    h = Hue()
    print h.lights
    l = h.lights[1]
    print l

def create_schedule():
    h = Hue()
    body = dict(on=False)
    command = dict(address='/api/<your user name here>/lights/3/state',
            method='PUT',
            body=body)
    h.create_schedule('Tests', 'this is test', command)

def delete_schedule(id):
    h = Hue()
    s = HueSchedule(h, id)
    s.delete()

def on_and_off():
    h = Hue()
    if not h.lights:
        return
    l = h.lights[0]
    print 'Turn off the lights...'
    l.off()
    sleep(2)
    print 'Sleep 2 seconds...'
    l.on()
    print 'Lights on!'

def alert():
    l = Hue()
    l.alert()

if __name__ == '__main__':
    main()
