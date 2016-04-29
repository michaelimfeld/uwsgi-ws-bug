# -*- coding: utf-8 -*-
"""
    WSGI part with web.py for the uwsgi websocket
    bug demo application.
"""
import uwsgi
import select
import datetime
import web

URLS = ("/", "Index", "/websocket", "WebSocket")

APP = web.application(URLS, globals())


class Index(object):
    """Handles requests for the route '/'."""
    def GET(self):
        return web.template.frender("index.html")()


class WebSocket(object):
    """Handles requests for the route '/websocket'."""
    def GET(self):
        env = web.ctx.env
        uwsgi.websocket_handshake(env['HTTP_SEC_WEBSOCKET_KEY'],
                                  env.get('HTTP_ORIGIN', ''))
        websocket_fd = uwsgi.connection_fd()
        inputs = [websocket_fd]

        while True:
            readable, _, _ = select.select(inputs, [], [], 1.0)

            for fid in readable:
                if fid == websocket_fd:
                    data = uwsgi.websocket_recv_nb()
                    now = datetime.datetime.now()
                    print("{0}: Received ws message: '{1}'".format(now, data))


application = APP.wsgifunc()
