# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Inventory/InventoryDelta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Inventory import InventoryItem_pb2 as Inventory_dot_InventoryItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Inventory/InventoryDelta.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n\x1eInventory/InventoryDelta.proto\x12\x14POGOProtos.Inventory\x1a\x1dInventory/InventoryItem.proto\"\x87\x01\n\x0eInventoryDelta\x12\x1d\n\x15original_timestamp_ms\x18\x01 \x01(\x03\x12\x18\n\x10new_timestamp_ms\x18\x02 \x01(\x03\x12<\n\x0finventory_items\x18\x03 \x03(\x0b\x32#.POGOProtos.Inventory.InventoryItemb\x06proto3')
  ,
  dependencies=[Inventory_dot_InventoryItem__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INVENTORYDELTA = _descriptor.Descriptor(
  name='InventoryDelta',
  full_name='POGOProtos.Inventory.InventoryDelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_timestamp_ms', full_name='POGOProtos.Inventory.InventoryDelta.original_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_timestamp_ms', full_name='POGOProtos.Inventory.InventoryDelta.new_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_items', full_name='POGOProtos.Inventory.InventoryDelta.inventory_items', index=2,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=223,
)

_INVENTORYDELTA.fields_by_name['inventory_items'].message_type = Inventory_dot_InventoryItem__pb2._INVENTORYITEM
DESCRIPTOR.message_types_by_name['InventoryDelta'] = _INVENTORYDELTA

InventoryDelta = _reflection.GeneratedProtocolMessageType('InventoryDelta', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYDELTA,
  __module__ = 'Inventory.InventoryDelta_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryDelta)
  ))
_sym_db.RegisterMessage(InventoryDelta)


# @@protoc_insertion_point(module_scope)
