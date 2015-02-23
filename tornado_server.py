#!/usr/bin/env python
# Serves by default at
# http://localhost:8080/hello-django

from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import os
import sys

define('port', type=int, default=8080)

def main():
    #parse_command_line()
  os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
  wsgi_app = tornado.wsgi.WSGIContainer(
    get_wsgi_application())
  tornado_app = tornado.web.Application(
    [
      ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
      ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
