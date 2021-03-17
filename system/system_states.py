'''
version 3.0 - in preparation!!! get version 2.0 if you want to get some spacex data ;)
author: a5892731
date: 2021-03-17

https://python-statemachine.readthedocs.io/en/latest/readme.html#getting-started

'''
from statemachine import StateMachine, State

class TrafficLightMachine(StateMachine):
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    slowdown = green.to(yellow)
    stop = yellow.to(red)
    go = red.to(green)