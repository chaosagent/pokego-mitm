# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Inventory/EggIncubatorType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Inventory/EggIncubatorType.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n Inventory/EggIncubatorType.proto\x12\x14POGOProtos.Inventory*?\n\x10\x45ggIncubatorType\x12\x13\n\x0fINCUBATOR_UNSET\x10\x00\x12\x16\n\x12INCUBATOR_DISTANCE\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EGGINCUBATORTYPE = _descriptor.EnumDescriptor(
  name='EggIncubatorType',
  full_name='POGOProtos.Inventory.EggIncubatorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INCUBATOR_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCUBATOR_DISTANCE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=58,
  serialized_end=121,
)
_sym_db.RegisterEnumDescriptor(_EGGINCUBATORTYPE)

EggIncubatorType = enum_type_wrapper.EnumTypeWrapper(_EGGINCUBATORTYPE)
INCUBATOR_UNSET = 0
INCUBATOR_DISTANCE = 1


DESCRIPTOR.enum_types_by_name['EggIncubatorType'] = _EGGINCUBATORTYPE


# @@protoc_insertion_point(module_scope)
