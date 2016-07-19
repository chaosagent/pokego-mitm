# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Settings/Master/MoveSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import PokemonType_pb2 as Enums_dot_PokemonType__pb2
from Enums import PokemonMovementType_pb2 as Enums_dot_PokemonMovementType__pb2

from Enums.PokemonType_pb2 import *
from Enums.PokemonMovementType_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Settings/Master/MoveSettings.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n\"Settings/Master/MoveSettings.proto\x12\x1aPOGOProtos.Settings.Master\x1a\x17\x45nums/PokemonType.proto\x1a\x1f\x45nums/PokemonMovementType.proto\"\xb9\x03\n\x0cMoveSettings\x12:\n\x0bmovement_id\x18\x01 \x01(\x0e\x32%.POGOProtos.Enums.PokemonMovementType\x12\x14\n\x0c\x61nimation_id\x18\x02 \x01(\x05\x12\x33\n\x0cpokemon_type\x18\x03 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonType\x12\r\n\x05power\x18\x04 \x01(\x02\x12\x17\n\x0f\x61\x63\x63uracy_chance\x18\x05 \x01(\x02\x12\x17\n\x0f\x63ritical_chance\x18\x06 \x01(\x02\x12\x13\n\x0bheal_scalar\x18\x07 \x01(\x02\x12\x1b\n\x13stamina_loss_scalar\x18\x08 \x01(\x02\x12\x19\n\x11trainer_level_min\x18\t \x01(\x05\x12\x19\n\x11trainer_level_max\x18\n \x01(\x05\x12\x10\n\x08vfx_name\x18\x0b \x01(\t\x12\x13\n\x0b\x64uration_ms\x18\x0c \x01(\x05\x12\x1e\n\x16\x64\x61mage_window_start_ms\x18\r \x01(\x05\x12\x1c\n\x14\x64\x61mage_window_end_ms\x18\x0e \x01(\x05\x12\x14\n\x0c\x65nergy_delta\x18\x0f \x01(\x05P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[Enums_dot_PokemonType__pb2.DESCRIPTOR,Enums_dot_PokemonMovementType__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MOVESETTINGS = _descriptor.Descriptor(
  name='MoveSettings',
  full_name='POGOProtos.Settings.Master.MoveSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='movement_id', full_name='POGOProtos.Settings.Master.MoveSettings.movement_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='animation_id', full_name='POGOProtos.Settings.Master.MoveSettings.animation_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_type', full_name='POGOProtos.Settings.Master.MoveSettings.pokemon_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='POGOProtos.Settings.Master.MoveSettings.power', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accuracy_chance', full_name='POGOProtos.Settings.Master.MoveSettings.accuracy_chance', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='critical_chance', full_name='POGOProtos.Settings.Master.MoveSettings.critical_chance', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heal_scalar', full_name='POGOProtos.Settings.Master.MoveSettings.heal_scalar', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina_loss_scalar', full_name='POGOProtos.Settings.Master.MoveSettings.stamina_loss_scalar', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_level_min', full_name='POGOProtos.Settings.Master.MoveSettings.trainer_level_min', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_level_max', full_name='POGOProtos.Settings.Master.MoveSettings.trainer_level_max', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vfx_name', full_name='POGOProtos.Settings.Master.MoveSettings.vfx_name', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_ms', full_name='POGOProtos.Settings.Master.MoveSettings.duration_ms', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_window_start_ms', full_name='POGOProtos.Settings.Master.MoveSettings.damage_window_start_ms', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_window_end_ms', full_name='POGOProtos.Settings.Master.MoveSettings.damage_window_end_ms', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy_delta', full_name='POGOProtos.Settings.Master.MoveSettings.energy_delta', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=125,
  serialized_end=566,
)

_MOVESETTINGS.fields_by_name['movement_id'].enum_type = Enums_dot_PokemonMovementType__pb2._POKEMONMOVEMENTTYPE
_MOVESETTINGS.fields_by_name['pokemon_type'].enum_type = Enums_dot_PokemonType__pb2._POKEMONTYPE
DESCRIPTOR.message_types_by_name['MoveSettings'] = _MOVESETTINGS

MoveSettings = _reflection.GeneratedProtocolMessageType('MoveSettings', (_message.Message,), dict(
  DESCRIPTOR = _MOVESETTINGS,
  __module__ = 'Settings.Master.MoveSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.MoveSettings)
  ))
_sym_db.RegisterMessage(MoveSettings)


# @@protoc_insertion_point(module_scope)
