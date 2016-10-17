#
# starkoala/responder.py
#
"""
Module containing the growler responder which interprets the client
data.
"""


class TelnetResponder:
    """
    The GrowlerResponder object handling the browser request.

    """

    def __init__(self, handler):
        """
        Construct a telnet responder with the client handler that
        managers this responder.
        """
        self._handler = handler
        self._storage = []

    def on_data(self, data):
        """
        Called upon receiving client data - right now just saves in
        a list - for no reason in particular.
        """
        # store the data
        self._storage.append(data)
