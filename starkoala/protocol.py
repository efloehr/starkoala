#
# starkoala/protocol.py
#


from growler import GrowlerProtocol
from .responder import TelnetResponder


class TelnetProtocol(GrowlerProtocol):
    """
    The :class:`asyncio.Protocol` class handling the low-level
    connection to the client.

    Some properties, such as the bare socket to the client and the
    asyncio Transport object are inherited from the GrowlerProtocol
    class.

    The handle_error method should be implemented to handle any
    uncaught exceptions occuring in the application.

    Note: This is an asyncio-only class, so it is advised to keep
    this slim and contain the only asyncio-dependent code in the
    library if future support for alternative event loop libraries,
    such as cuio, may be wanted.
    """

    def __init__(self, app, **protocol_args):
        """
        Create the protocol with an application object.

        Any keyword arguments are passed to the super's constructor.

        Valid keyword arguments are `loop`, the event loop; and
        `responder_factory`, a callable that takes only this protocol
        object as parameter and returns the responder object will be
        called when client data is sent.
        """
        self.telnet_application = app
        super().__init__(**protocol_args)


    def begin_application(self, req, res):
        """
        Entry point for the application middleware chain for an asyncio
        event loop.
        """
        raise NotImplementedError
