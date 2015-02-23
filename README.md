# django-tornado
Run a Django project from Tornado server

This is a simple django project to run a django project from a Tornado server. 

I was working on another project where we needed to use Tornado since it comes with Websocket handlers and Web application handlers. I tried using Apache Server, but was not very successful in using it, given the complication in integration zeromq for message queues that communicated outside of Apache project for providing getting data and websockets that also communicated via zeromq. This code snippet is useful to get started with.

Tornado is a more straightforward solution to integrating all of this seamlessly.
