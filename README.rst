=========
Starkoala
=========

Asynchronous telnet server using the `Growler framework`_.


Examples
--------

The Starkoala repository comes with some examples, and may be run
in the project's root directory by using :code:`python -m examples.tryme`.

There is only an echo server implemented right now: :code:`python -m examples.echo`.


Structure
---------

There are currently three main components of this project:

Protocol
  This is a subclass of ``GrowlerProtocol`` and therefore also an
  ``asyncio.Protocol`` of which documentation may be found.
  This is where all asyncio specific code should end up, as is it recommended
  that code should remain event-loop agnostic.
  This goal does not need to be enforced strictly, and convenience should trump
  adherence at this point.

  Growler adds a level of abstraction above asyncio, so the 'protocol' is not
  actually implemented here, but the ``Responder``.
  It was implemented in this way because an asyncio Protocol object is tightly
  coupled to the client, and if a change of protocol is required for some
  reason, there was no way to switch classes.
  The GrowlerProtocol has a stack of these responders, and incoming data gets
  sent to the object at the top of the stack.
  This way there is a standard method for changing protocol - just push a new
  responder object and then pop it when done to drop back to the previous.

  The only customization should be how it handles errors, and what default
  responder should be created upon client connection.

Responder
  This class implements the bulk of the actual byte-handling protocol
  interpretation.
  For example, the HTTP Responder parses the request into request path, method,
  and headers, then creates the request-response pair, and ***then*** passes
  these to the application object setup by the user.

  The most important method is ``on_data``, which is called by the parent
  protocol object whenever client data is avaiable; what to do after that is up
  to the implementation.

  It is up to the responder to send the request and response to the application.

  I think this project would benefit from having multiple responders to choose
  from, but these will probably grow organically over time.
  I'm thinking right now of a text-base game responder and another being
  something like a lisp interpreter where the responder would interpret the
  command or s-expression and somehow pass this to the application, which
  returns an updated state.

Application
  This is the class with which the developer should actually interact, the
  other two having enough sane defaults that the user doesn't need to
  subclass without 'complicated' needs.

  The Growler HTTP application object contains the middleware tree, and when
  the asynchronous method ``handle_client_request`` is called with the
  responder's req and res objects, each node matching the request is called
  in turn, until the client responds.

  Constructing the middleware tree is done by mapping a HTTP-method + path
  pair with a callback method, convieniently done with decorators:

  .. code:: python

     @app.get("/photos")
     def get_photos(req, res):
          res.send_photograph()

     @app.put("/photo/new")
     async def create_photos(req, res):
          photo_data = await req.body()
          req.user.file_storage.add_file(photo_data)
          res.send_json({"success": True})


  I recommend keeping this interface (decorating functions) when implementing
  other Application classes, but obviously with other methods than ``.get`` /
  ``.put`` / ``.post`` etc.


  It is imporant to note that the application object is pretty static (i.e.
  immutable) thoughout the program - it is the request and response objects
  that contain the state of the connection.



Work To Do
----------

A telnet application is fundamentally different from the HTTP applications that
Growler was designed for.
I'd venture to guess the typical Telnet model is a user interactive prompt,
whereas HTTP is a stateless request with a very definite structure.

Growler's strength is in its "piping" of user requests though a series of
middleware, so each request is essentially a traversal through a tree the user
has designed.
This is facilitated by the fact that requests must specify a path, so it
litterally imitates a file system traversal.
Whether this analogy works depends entirely on the app.


License
-------

TBD


.. _Growler framework: https://github.com/pyGrowler/growler
