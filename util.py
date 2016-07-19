import struct


def f2i(float):
    return struct.unpack('<Q', struct.pack('<d', float))[0]


def f2h(float):
    return hex(struct.unpack('<Q', struct.pack('<d', float))[0])


def h2f(hex):
    return struct.unpack('<d', struct.pack('<Q', int(hex, 16)))[0]


def request_envelope_handler(func):
    request_envelope_handler.handles_request_envelope = func
    return func


def response_envelope_handler(func):
    response_envelope_handler.handles_response_envelope = func
    return func


def request_handler(request_type):
    def decorator(func):
        if not hasattr(func, 'handles_requests'):
            func.handles_requests = []
        func.handles_requests.append(request_type)
        return func

    return decorator


def response_handler(request_type):
    def decorator(func):
        if not hasattr(func, 'handles_responses'):
            func.handles_responses = []
        func.handles_responses.append(request_type)
        return func

    return decorator
