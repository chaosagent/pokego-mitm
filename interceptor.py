from __future__ import print_function

import os
import sys

from netlib.encoding import encode_gzip, decode_gzip

from protos.Networking.Envelopes_pb2 import Envelopes

if os.path.abspath('protos') not in sys.path:
    sys.path.append(os.path.abspath('protos'))

request_decoders = {
    103: 'CatchPokemon',
}

response_decoders = {
    2: 'GetPlayer',
    4: 'GetInventory',
    104: 'FortDetails',
    103: 'CatchPokemon',
    106: 'GetMapObjects',
}

request_envelope_handler = None

response_envelope_handler = None

request_handlers = {}

response_handlers = {}

requested = {}


def start(context, argv):
    # Register handlers
    import handlers
    reload(handlers)
    for attr in dir(handlers):
        func = getattr(handlers, attr)
        if not hasattr(func, '__call__'):
            continue

        if hasattr(func, 'handles_request_envelope'):
            global request_envelope_handler
            request_envelope_handler = func.handles_request_envelope
            context.log('Got request envelope handler {}.'.format(func.__name__))
        if hasattr(func, 'handles_response_envelope'):
            global response_envelope_handler
            response_envelope_handler = func.handles_response_envelope
            context.log('Got request envelope handler {}.'.format(func.__name__))

        if hasattr(func, 'handles_requests'):
            for request_type in func.handles_requests:
                request_handlers[request_type] = func
                context.log('Got request handler {} for request type {}.'.format(func.__name__, request_type))
        if hasattr(func, 'handles_responses'):
            for request_type in func.handles_responses:
                response_handlers[request_type] = func
                context.log('Got response handler {} for request type {}.'.format(func.__name__, request_type))


def request(context, flow):
    if not flow.request.url.startswith('https://pgorelease.nianticlabs.com/plfe'):
        return

    request_body = flow.request.content
    try:
        envelope = Envelopes.RequestEnvelope()
        envelope.ParseFromString(request_body)
    except:
        return

    context.log('Got request {}.'.format(envelope.request_id))
    if request_envelope_handler:
        context.log('Handling request {}...'.format(envelope.request_id))
        request_envelope_handler(context, envelope)

    requested[envelope.request_id] = [request.request_type for request in envelope.requests]

    for i, request in enumerate(envelope.requests):
        request_type = request.request_type
        context.log('Got request type {}.'.format(request.request_type))
        if request_type not in request_decoders or request_type not in request_handlers:
            continue

        context.log('Handling request for request type {}...'.format(request_type))
        request_proto_name = '{}Message'.format(request_decoders[request_type])
        message_proto_import = __import__('protos.Networking.Requests.Messages.{}_pb2'.format(request_proto_name),
                                          globals(),
                                          locals(), fromlist=[request_proto_name])
        message = getattr(message_proto_import, request_proto_name)

        request_obj = message()
        request_obj.ParseFromString(request.request_message)

        request_handlers[request_type](context, request_obj)

        envelope.requests[i].request_message = request_obj.SerializeToString()

    processed_request_body = envelope.SerializeToString()
    flow.request.content = processed_request_body


def response(context, flow):
    if not flow.request.url.startswith('https://pgorelease.nianticlabs.com/plfe'):
        return

    try:
        response_body = decode_gzip(flow.response.content)
        envelope = Envelopes.ResponseEnvelope()
        envelope.ParseFromString(response_body)
    except:
        return

    context.log('Got response for request {}.'.format(envelope.request_id))
    if envelope.request_id not in requested:
        context.log('Unknown request {}.'.format(envelope.request_id))
        return
    if response_envelope_handler:
        context.log('Handling response {}...'.format(envelope.response_id))
        response_envelope_handler(context, envelope)

    for i, response in enumerate(envelope.returns):
        request_type = requested[envelope.request_id][i]
        context.log('Got response for request type {}.'.format(request_type))
        if request_type not in response_decoders or request_type not in response_handlers:
            continue

        context.log('Handling response for request type {}...'.format(request_type))
        response_proto_name = '{}Response'.format(response_decoders[request_type])
        message_proto_import = __import__('protos.Networking.Responses.{}_pb2'.format(response_proto_name), globals(),
                                          locals(), fromlist=[response_proto_name])
        message = getattr(message_proto_import, response_proto_name)

        response_obj = message()
        response_obj.ParseFromString(response)

        response_handlers[request_type](context, response_obj)

        envelope.returns[i] = response_obj.SerializeToString()

    processed_response_body = envelope.SerializeToString()
    processed_content = encode_gzip(processed_response_body)
    flow.response.content = processed_content
