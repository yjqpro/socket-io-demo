#/usr/bin/env python
#-*- coding: utf-8 -*-

import asyncio
from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

async def background_task():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        await sio.sleep(1)
        count += 1
        await sio.emit('execute_order_status', {'order': str(count)}) #4



@sio.event
async def connect(sid, environ): #2
    await sio.emit('execute_order_list', [{'order_id':'0'},
				{'order_id':'1'}], room=sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    sio.start_background_task(background_task)
    web.run_app(app, port=5000)
