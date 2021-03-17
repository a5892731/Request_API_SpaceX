'''
version 3.0 - in preparation!!! get version 2.0 if you want to get some spacex data ;)
author: a5892731
date: 2021-03-17

https://python-statemachine.readthedocs.io/en/latest/readme.html#getting-started

'''
from statemachine import StateMachine, State

from statemachine import StateMachine, State

class TrafficLightMachine(StateMachine):
    "A traffic light machine"
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    cycle = green.to(yellow) | yellow.to(red) | red.to(green)

    def on_enter_green(self):
        print('Valendo!')

    def on_enter_yellow(self):
        print('Calma, lá!')

    def on_enter_red(self):
        print('Parou.')




if __name__ == "__main__":

    stm = TrafficLightMachine()
    stm.cycle()
    stm.cycle()
    stm.cycle()
    stm.cycle()