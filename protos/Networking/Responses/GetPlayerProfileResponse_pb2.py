# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/GetPlayerProfileResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Data import Player_pb2 as Data_dot_Player__pb2
from Data import PlayerBadge_pb2 as Data_dot_PlayerBadge__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/GetPlayerProfileResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n3Networking/Responses/GetPlayerProfileResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x11\x44\x61ta/Player.proto\x1a\x16\x44\x61ta/PlayerBadge.proto\"\xd0\x01\n\x18GetPlayerProfileResponse\x12P\n\x06result\x18\x01 \x01(\x0e\x32@.POGOProtos.Networking.Responses.GetPlayerProfileResponse.Result\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12,\n\x06\x62\x61\x64ges\x18\x03 \x03(\x0b\x32\x1c.POGOProtos.Data.PlayerBadge\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[Data_dot_Player__pb2.DESCRIPTOR,Data_dot_PlayerBadge__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETPLAYERPROFILERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.GetPlayerProfileResponse.Result',
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
  ],
  containing_type=None,
  options=None,
  serialized_start=308,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_GETPLAYERPROFILERESPONSE_RESULT)


_GETPLAYERPROFILERESPONSE = _descriptor.Descriptor(
  name='GetPlayerProfileResponse',
  full_name='POGOProtos.Networking.Responses.GetPlayerProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.GetPlayerProfileResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='POGOProtos.Networking.Responses.GetPlayerProfileResponse.start_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='badges', full_name='POGOProtos.Networking.Responses.GetPlayerProfileResponse.badges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETPLAYERPROFILERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=340,
)

_GETPLAYERPROFILERESPONSE.fields_by_name['result'].enum_type = _GETPLAYERPROFILERESPONSE_RESULT
_GETPLAYERPROFILERESPONSE.fields_by_name['badges'].message_type = Data_dot_PlayerBadge__pb2._PLAYERBADGE
_GETPLAYERPROFILERESPONSE_RESULT.containing_type = _GETPLAYERPROFILERESPONSE
DESCRIPTOR.message_types_by_name['GetPlayerProfileResponse'] = _GETPLAYERPROFILERESPONSE

GetPlayerProfileResponse = _reflection.GeneratedProtocolMessageType('GetPlayerProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERPROFILERESPONSE,
  __module__ = 'Networking.Responses.GetPlayerProfileResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.GetPlayerProfileResponse)
  ))
_sym_db.RegisterMessage(GetPlayerProfileResponse)


# @@protoc_insertion_point(module_scope)
