#!/usr/bin/env python

# https://docs.python.org/2/library/subprocess.html
# https://www.asciiart.eu/animals/cats
# https://blog.sleeplessbeastie.eu/2013/01/11/how-to-change-the-mac-address-of-an-ethernet-interface/
# https://www.lifewithpython.com/2015/06/python-check-python-version.html
# https://docs.python.org/2/library/optparse.html

import subprocess
import sys

print('''
_____________________________________________________

            ("`-''-/").___..--''"`-._ 
             `6_ 6  )   `-.  (     ).`-.__.`) 
             (_Y_.)'  ._   )  `._ `. ``-..-' 
 HELLO         _..`--'_..-_/  /--'_.'
              ((((.-''  ((((.'  (((.-'
_____________________________________________________
''')

if sys.version_info.major != 2:
    command = input('COMMAND -> ')
elif sys.version_info.major == 2:
    command = raw_input('COMMAND -> ')

print('Your Python version: {}\n'.format(sys.version_info.major))
subprocess.call([command], shell=True)