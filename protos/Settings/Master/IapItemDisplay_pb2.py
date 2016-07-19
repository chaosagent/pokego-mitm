# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Settings/Master/IapItemDisplay.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import IapItemCategory_pb2 as Enums_dot_IapItemCategory__pb2
from Inventory import ItemId_pb2 as Inventory_dot_ItemId__pb2

from Enums.IapItemCategory_pb2 import *
from Inventory.ItemId_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Settings/Master/IapItemDisplay.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n$Settings/Master/IapItemDisplay.proto\x12\x1aPOGOProtos.Settings.Master\x1a\x1b\x45nums/IapItemCategory.proto\x1a\x16Inventory/ItemId.proto\"\xaa\x01\n\x0eIapItemDisplay\x12\x0b\n\x03sku\x18\x01 \x01(\t\x12\x37\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32%.POGOProtos.Enums.HoloIapItemCategory\x12\x12\n\nsort_order\x18\x03 \x01(\x05\x12.\n\x08item_ids\x18\x04 \x03(\x0e\x32\x1c.POGOProtos.Inventory.ItemId\x12\x0e\n\x06\x63ounts\x18\x05 \x03(\x05P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[Enums_dot_IapItemCategory__pb2.DESCRIPTOR,Inventory_dot_ItemId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IAPITEMDISPLAY = _descriptor.Descriptor(
  name='IapItemDisplay',
  full_name='POGOProtos.Settings.Master.IapItemDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sku', full_name='POGOProtos.Settings.Master.IapItemDisplay.sku', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='POGOProtos.Settings.Master.IapItemDisplay.category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='POGOProtos.Settings.Master.IapItemDisplay.sort_order', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_ids', full_name='POGOProtos.Settings.Master.IapItemDisplay.item_ids', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counts', full_name='POGOProtos.Settings.Master.IapItemDisplay.counts', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=292,
)

_IAPITEMDISPLAY.fields_by_name['category'].enum_type = Enums_dot_IapItemCategory__pb2._HOLOIAPITEMCATEGORY
_IAPITEMDISPLAY.fields_by_name['item_ids'].enum_type = Inventory_dot_ItemId__pb2._ITEMID
DESCRIPTOR.message_types_by_name['IapItemDisplay'] = _IAPITEMDISPLAY

IapItemDisplay = _reflection.GeneratedProtocolMessageType('IapItemDisplay', (_message.Message,), dict(
  DESCRIPTOR = _IAPITEMDISPLAY,
  __module__ = 'Settings.Master.IapItemDisplay_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.IapItemDisplay)
  ))
_sym_db.RegisterMessage(IapItemDisplay)


# @@protoc_insertion_point(module_scope)
