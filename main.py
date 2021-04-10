'''
version 3.0
author: a5892731
date: 2021-03-17

required modules:

pip install terminaltables
pip install requests
pip install json
pip install mysql

os , platform, datetime
'''

from state_machine.simple_device import SimpleDevice


#--------------------------------------------------------------------------------------- <<<< MAIN MENU



if __name__ == "__main__":
    device = SimpleDevice()

    while True:
        device.on_event('device_locked')
