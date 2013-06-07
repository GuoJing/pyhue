#!/usr/bin/env python

from setuptools import setup, find_packages


install_description = '''
pyhue
=====

Python library for the Philips Hue.

Installation
------------

You can get the code from `https://github.com/GuoJing/pyhue`


Example
-------

::

    from pyhue import hue
    hue = Hue()

or

    hue = Hue(ip, devicetype)

or

    from pyhue.nupnp import get_hue
    hue = get_hue(device_type)

'''


setup(
    name = 'pyhue',
    version = '0.1.2',
    license = 'GPLv3',
    description = 'Python library for the Philips Hue',
    long_description = install_description,
    author = 'GuoJing',
    author_email = 'soundbbg@gmail.com',
    url = 'http://github.com/GuoJing/pyhue',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'requests',
        'pyyaml'
    ],
)
