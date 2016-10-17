#
# starkoala/__init__.py
#
"""
Asynchronous Telnet Server
"""

from .__meta__ import (
    version as __version__,
    author as __author__,
    date as __date__,
)

from .responder import TelnetResponder
from .application import Application
from .protocol import TelnetProtocol

# alias Application as friendlier 'App'
App = Application
