//
//Copyright 2018-2022 Mailgun Technologies Inc
//
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//
//http://www.apache.org/licenses/LICENSE-2.0
//
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.

// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v3.21.7
// source: peers.proto

package gubernator

import (
	context "context"

	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	PeersV1_GetPeerRateLimits_FullMethodName = "/pb.gubernator.PeersV1/GetPeerRateLimits"
	PeersV1_UpdatePeerGlobals_FullMethodName = "/pb.gubernator.PeersV1/UpdatePeerGlobals"
)

// PeersV1Client is the client API for PeersV1 service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PeersV1Client interface {
	// Used by peers to relay batches of requests to an authoritative peer
	GetPeerRateLimits(ctx context.Context, in *GetPeerRateLimitsReq, opts ...grpc.CallOption) (*GetPeerRateLimitsResp, error)
	// Used by peers send global rate limit updates to other peers
	UpdatePeerGlobals(ctx context.Context, in *UpdatePeerGlobalsReq, opts ...grpc.CallOption) (*UpdatePeerGlobalsResp, error)
}

type peersV1Client struct {
	cc grpc.ClientConnInterface
}

func NewPeersV1Client(cc grpc.ClientConnInterface) PeersV1Client {
	return &peersV1Client{cc}
}

func (c *peersV1Client) GetPeerRateLimits(ctx context.Context, in *GetPeerRateLimitsReq, opts ...grpc.CallOption) (*GetPeerRateLimitsResp, error) {
	out := new(GetPeerRateLimitsResp)
	err := c.cc.Invoke(ctx, PeersV1_GetPeerRateLimits_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *peersV1Client) UpdatePeerGlobals(ctx context.Context, in *UpdatePeerGlobalsReq, opts ...grpc.CallOption) (*UpdatePeerGlobalsResp, error) {
	out := new(UpdatePeerGlobalsResp)
	err := c.cc.Invoke(ctx, PeersV1_UpdatePeerGlobals_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PeersV1Server is the server API for PeersV1 service.
// All implementations must embed UnimplementedPeersV1Server
// for forward compatibility
type PeersV1Server interface {
	// Used by peers to relay batches of requests to an authoritative peer
	GetPeerRateLimits(context.Context, *GetPeerRateLimitsReq) (*GetPeerRateLimitsResp, error)
	// Used by peers send global rate limit updates to other peers
	UpdatePeerGlobals(context.Context, *UpdatePeerGlobalsReq) (*UpdatePeerGlobalsResp, error)
	mustEmbedUnimplementedPeersV1Server()
}

// UnimplementedPeersV1Server must be embedded to have forward compatible implementations.
type UnimplementedPeersV1Server struct {
}

func (UnimplementedPeersV1Server) GetPeerRateLimits(context.Context, *GetPeerRateLimitsReq) (*GetPeerRateLimitsResp, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPeerRateLimits not implemented")
}
func (UnimplementedPeersV1Server) UpdatePeerGlobals(context.Context, *UpdatePeerGlobalsReq) (*UpdatePeerGlobalsResp, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdatePeerGlobals not implemented")
}
func (UnimplementedPeersV1Server) mustEmbedUnimplementedPeersV1Server() {}

// UnsafePeersV1Server may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PeersV1Server will
// result in compilation errors.
type UnsafePeersV1Server interface {
	mustEmbedUnimplementedPeersV1Server()
}

func RegisterPeersV1Server(s grpc.ServiceRegistrar, srv PeersV1Server) {
	s.RegisterService(&PeersV1_ServiceDesc, srv)
}

func _PeersV1_GetPeerRateLimits_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetPeerRateLimitsReq)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PeersV1Server).GetPeerRateLimits(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PeersV1_GetPeerRateLimits_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PeersV1Server).GetPeerRateLimits(ctx, req.(*GetPeerRateLimitsReq))
	}
	return interceptor(ctx, in, info, handler)
}

func _PeersV1_UpdatePeerGlobals_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdatePeerGlobalsReq)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PeersV1Server).UpdatePeerGlobals(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PeersV1_UpdatePeerGlobals_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PeersV1Server).UpdatePeerGlobals(ctx, req.(*UpdatePeerGlobalsReq))
	}
	return interceptor(ctx, in, info, handler)
}

// PeersV1_ServiceDesc is the grpc.ServiceDesc for PeersV1 service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var PeersV1_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "pb.gubernator.PeersV1",
	HandlerType: (*PeersV1Server)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetPeerRateLimits",
			Handler:    _PeersV1_GetPeerRateLimits_Handler,
		},
		{
			MethodName: "UpdatePeerGlobals",
			Handler:    _PeersV1_UpdatePeerGlobals_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "peers.proto",
}
