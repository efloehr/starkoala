#
# examples/echo.py
#


import asyncio
from starkoala import App, TelnetResponder, TelnetProtocol


class EchoTelnetResponder(TelnetResponder):
    """
    Prints incoming telnet data and replies with same data prefixed
    with '> '.

    TODO: How do you implement something like this with an easily
    extendable `app` object?
    """
    def on_data(self, data):
        print(data, '=>', data.decode())
        self._handler.transport.write(b"> " + data)

# sent to asyncio's create_server method
server_params = {
    'host': '127.0.0.1',
    'port': 8000,
}

# no app object yet in this example
app = None

loop = asyncio.get_event_loop()

# We need to change responder target from TelnetResponder to our
# custom class.
proto_factory = TelnetProtocol.get_factory(app,
                                           responder_factory=EchoTelnetResponder,
                                           loop=loop)

# create the server
make_server = loop.create_server(proto_factory, **server_params)
server = loop.run_until_complete(make_server)

# what port was that, again?
print("listening on {}:{}".format(*server.sockets[0].getsockname()))

# let asyncio run the server until ctrl-c is pressed
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
