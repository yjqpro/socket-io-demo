#/usr/bin/env python
#-*-coding: utf-8 -*-

import socketio

# standard Python
sio = socketio.Client()

@sio.event
def execute_order_list(orders): #3
    print(orders)

@sio.event
def execute_order_status(order):
    print(order)


sio.connect('http://localhost:5000') #1
sio.wait()

