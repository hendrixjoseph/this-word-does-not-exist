# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wordservice.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wordservice.proto',
  package='endpoints.word_service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11wordservice.proto\x12\x16\x65ndpoints.word_service\"d\n\x0eWordDefinition\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\ndefinition\x18\x02 \x01(\t\x12\x0b\n\x03pos\x18\x03 \x01(\t\x12\x10\n\x08\x65xamples\x18\x04 \x03(\t\x12\x11\n\tsyllables\x18\x05 \x03(\t\"!\n\x11\x44\x65\x66ineWordRequest\x12\x0c\n\x04word\x18\x01 \x01(\t\"J\n\x12\x44\x65\x66ineWordResponse\x12\x34\n\x04word\x18\x01 \x01(\x0b\x32&.endpoints.word_service.WordDefinition2t\n\x0bWordService\x12\x65\n\nDefineWord\x12).endpoints.word_service.DefineWordRequest\x1a*.endpoints.word_service.DefineWordResponse\"\x00\x62\x06proto3')
)




_WORDDEFINITION = _descriptor.Descriptor(
  name='WordDefinition',
  full_name='endpoints.word_service.WordDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.WordDefinition.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='definition', full_name='endpoints.word_service.WordDefinition.definition', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='endpoints.word_service.WordDefinition.pos', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examples', full_name='endpoints.word_service.WordDefinition.examples', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='syllables', full_name='endpoints.word_service.WordDefinition.syllables', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=145,
)


_DEFINEWORDREQUEST = _descriptor.Descriptor(
  name='DefineWordRequest',
  full_name='endpoints.word_service.DefineWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.DefineWordRequest.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=180,
)


_DEFINEWORDRESPONSE = _descriptor.Descriptor(
  name='DefineWordResponse',
  full_name='endpoints.word_service.DefineWordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.DefineWordResponse.word', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=256,
)

_DEFINEWORDRESPONSE.fields_by_name['word'].message_type = _WORDDEFINITION
DESCRIPTOR.message_types_by_name['WordDefinition'] = _WORDDEFINITION
DESCRIPTOR.message_types_by_name['DefineWordRequest'] = _DEFINEWORDREQUEST
DESCRIPTOR.message_types_by_name['DefineWordResponse'] = _DEFINEWORDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WordDefinition = _reflection.GeneratedProtocolMessageType('WordDefinition', (_message.Message,), dict(
  DESCRIPTOR = _WORDDEFINITION,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.WordDefinition)
  ))
_sym_db.RegisterMessage(WordDefinition)

DefineWordRequest = _reflection.GeneratedProtocolMessageType('DefineWordRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEFINEWORDREQUEST,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.DefineWordRequest)
  ))
_sym_db.RegisterMessage(DefineWordRequest)

DefineWordResponse = _reflection.GeneratedProtocolMessageType('DefineWordResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEFINEWORDRESPONSE,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.DefineWordResponse)
  ))
_sym_db.RegisterMessage(DefineWordResponse)



_WORDSERVICE = _descriptor.ServiceDescriptor(
  name='WordService',
  full_name='endpoints.word_service.WordService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=258,
  serialized_end=374,
  methods=[
  _descriptor.MethodDescriptor(
    name='DefineWord',
    full_name='endpoints.word_service.WordService.DefineWord',
    index=0,
    containing_service=None,
    input_type=_DEFINEWORDREQUEST,
    output_type=_DEFINEWORDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORDSERVICE)

DESCRIPTOR.services_by_name['WordService'] = _WORDSERVICE

# @@protoc_insertion_point(module_scope)