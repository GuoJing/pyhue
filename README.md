pyhue
=====

This is a simple python sdk for philips hue (personal lightting system).

Version 0.1.2 is RELEASED

How to use
=====

This should be very easy.

Prepare
------

1. git clone the code
2. python setup.py install

Config
------

If you are not write the config file, it will generate auto with ip 0.0.0.0 . You need to config it.

Simple way:

    python
    from pyhue.nupnp import get_hue
    h = get_hue()

This will gen config.yml auto and auto fill the station_ip and deveice_type.

Or:

    python
    from pyhue import Hue
    h = Hue()

Then there will be a config.yml file in $HOMEDIR/.hue/.

Auth
-----
This will geb/load the config file at $HOMEDIR

    from pyhue import hue
    hue = Hue()

or

    hue = Hue(filename='test.yml')

or

    hue = Hue(ip, devicetype)

Then run (only the first time)

    hue = auth()

__get to your hue and press the BUTTON__

and Done

Usage
-----

next time you just can do like the main.py

    lights = hue.lights
    light = lights[0]
    light.on()
    light.off()
    light.set_state()

can you also could use hue object

    hue.create_schedule()
    hue.get_new_lights()

Next
-----

main.py have some simple samples.

Chinese
-----

1. 下载代码
2. 去 [www.meethue.com/api/nupnp](http://www.meethue.com/api/nupnp) 页面获取信息
3. 修改config文件, $HOMEDIR/.hue/config.yml
4. 使用代码，h=Hue()
5. h.auth()认证，并按下hue的按钮
6. 认证完毕

Contact
-----
soundbbg at gmail
