# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/EvolvePokemonResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Data import PokemonData_pb2 as Data_dot_PokemonData__pb2
Enums_dot_PokemonId__pb2 = Data_dot_PokemonData__pb2.Enums_dot_PokemonId__pb2
Enums_dot_PokemonMove__pb2 = Data_dot_PokemonData__pb2.Enums_dot_PokemonMove__pb2

from Data.PokemonData_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/EvolvePokemonResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n0Networking/Responses/EvolvePokemonResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x16\x44\x61ta/PokemonData.proto\"\xf9\x02\n\x15\x45volvePokemonResponse\x12M\n\x06result\x18\x01 \x01(\x0e\x32=.POGOProtos.Networking.Responses.EvolvePokemonResponse.Result\x12:\n\x14\x65volved_pokemon_data\x18\x02 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12\x1a\n\x12\x65xperience_awarded\x18\x03 \x01(\x05\x12\x15\n\rcandy_awarded\x18\x04 \x01(\x05\"\xa1\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x46\x41ILED_POKEMON_MISSING\x10\x02\x12!\n\x1d\x46\x41ILED_INSUFFICIENT_RESOURCES\x10\x03\x12 \n\x1c\x46\x41ILED_POKEMON_CANNOT_EVOLVE\x10\x04\x12\x1e\n\x1a\x46\x41ILED_POKEMON_IS_DEPLOYED\x10\x05P\x00\x62\x06proto3')
  ,
  dependencies=[Data_dot_PokemonData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_EVOLVEPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.EvolvePokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_POKEMON_MISSING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_INSUFFICIENT_RESOURCES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_POKEMON_CANNOT_EVOLVE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_POKEMON_IS_DEPLOYED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=326,
  serialized_end=487,
)
_sym_db.RegisterEnumDescriptor(_EVOLVEPOKEMONRESPONSE_RESULT)


_EVOLVEPOKEMONRESPONSE = _descriptor.Descriptor(
  name='EvolvePokemonResponse',
  full_name='POGOProtos.Networking.Responses.EvolvePokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.EvolvePokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolved_pokemon_data', full_name='POGOProtos.Networking.Responses.EvolvePokemonResponse.evolved_pokemon_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experience_awarded', full_name='POGOProtos.Networking.Responses.EvolvePokemonResponse.experience_awarded', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy_awarded', full_name='POGOProtos.Networking.Responses.EvolvePokemonResponse.candy_awarded', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVOLVEPOKEMONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=487,
)

_EVOLVEPOKEMONRESPONSE.fields_by_name['result'].enum_type = _EVOLVEPOKEMONRESPONSE_RESULT
_EVOLVEPOKEMONRESPONSE.fields_by_name['evolved_pokemon_data'].message_type = Data_dot_PokemonData__pb2._POKEMONDATA
_EVOLVEPOKEMONRESPONSE_RESULT.containing_type = _EVOLVEPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['EvolvePokemonResponse'] = _EVOLVEPOKEMONRESPONSE

EvolvePokemonResponse = _reflection.GeneratedProtocolMessageType('EvolvePokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _EVOLVEPOKEMONRESPONSE,
  __module__ = 'Networking.Responses.EvolvePokemonResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.EvolvePokemonResponse)
  ))
_sym_db.RegisterMessage(EvolvePokemonResponse)


# @@protoc_insertion_point(module_scope)