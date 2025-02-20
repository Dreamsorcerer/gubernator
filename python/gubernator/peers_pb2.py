# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gubernator import gubernator_pb2 as gubernator__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bpeers.proto\x12\rpb.gubernator\x1a\x10gubernator.proto\"E\n\x14GetPeerRateLimitsReq\x12-\n\x08requests\x18\x01 \x03(\x0b\x32\x1b.pb.gubernator.RateLimitReq\"J\n\x15GetPeerRateLimitsResp\x12\x31\n\x0brate_limits\x18\x01 \x03(\x0b\x32\x1c.pb.gubernator.RateLimitResp\"H\n\x14UpdatePeerGlobalsReq\x12\x30\n\x07globals\x18\x01 \x03(\x0b\x32\x1f.pb.gubernator.UpdatePeerGlobal\"z\n\x10UpdatePeerGlobal\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x1c.pb.gubernator.RateLimitResp\x12+\n\talgorithm\x18\x03 \x01(\x0e\x32\x18.pb.gubernator.Algorithm\"\x17\n\x15UpdatePeerGlobalsResp2\xcd\x01\n\x07PeersV1\x12`\n\x11GetPeerRateLimits\x12#.pb.gubernator.GetPeerRateLimitsReq\x1a$.pb.gubernator.GetPeerRateLimitsResp\"\x00\x12`\n\x11UpdatePeerGlobals\x12#.pb.gubernator.UpdatePeerGlobalsReq\x1a$.pb.gubernator.UpdatePeerGlobalsResp\"\x00\x42\"Z\x1dgithub.com/mailgun/gubernator\x80\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\035github.com/mailgun/gubernator\200\001\001'
  _globals['_GETPEERRATELIMITSREQ']._serialized_start=48
  _globals['_GETPEERRATELIMITSREQ']._serialized_end=117
  _globals['_GETPEERRATELIMITSRESP']._serialized_start=119
  _globals['_GETPEERRATELIMITSRESP']._serialized_end=193
  _globals['_UPDATEPEERGLOBALSREQ']._serialized_start=195
  _globals['_UPDATEPEERGLOBALSREQ']._serialized_end=267
  _globals['_UPDATEPEERGLOBAL']._serialized_start=269
  _globals['_UPDATEPEERGLOBAL']._serialized_end=391
  _globals['_UPDATEPEERGLOBALSRESP']._serialized_start=393
  _globals['_UPDATEPEERGLOBALSRESP']._serialized_end=416
  _globals['_PEERSV1']._serialized_start=419
  _globals['_PEERSV1']._serialized_end=624
# @@protoc_insertion_point(module_scope)
