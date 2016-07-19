pokego-mitm
======

A Pokemon Go MITM framework implemented using mitmproxy.

Quick Start
------

Run `mitmdump -p 1337 -s interceptor.py --ignore '^(?!pgorelease\.nianticlabs\.com)'` and point your device at it.

Alternatively, if you would like an interface to inspect requests/responses with, use `mitmproxy -p 1337 -s interceptor.py --ignore '^(?!pgorelease\.nianticlabs\.com)'`.

Adding Handlers
------

To add handlers, use the decorators provided in `util.py` and write handlers in `handlers.py`.

The following handlers are available:
- `request_envelope_handler`
- `response_envelope_handler`
- `request_handler(request_code)`
- `response_handler(response_code)`

Handlers should be in the form:

```python
@request_envelope_handler
def handler(context, request_obj):
    pass
```

Copyright and License
------

Copyright 2016 by David Hou.
Don't sue me please... :(


Credits
------

AeonLucid for the `.proto`s
mitmproxy for mitmproxy
