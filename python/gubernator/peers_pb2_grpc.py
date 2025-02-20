# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gubernator import peers_pb2 as peers__pb2


class PeersV1Stub(object):
    """NOTE: For use by gubernator peers only
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPeerRateLimits = channel.unary_unary(
                '/pb.gubernator.PeersV1/GetPeerRateLimits',
                request_serializer=peers__pb2.GetPeerRateLimitsReq.SerializeToString,
                response_deserializer=peers__pb2.GetPeerRateLimitsResp.FromString,
                )
        self.UpdatePeerGlobals = channel.unary_unary(
                '/pb.gubernator.PeersV1/UpdatePeerGlobals',
                request_serializer=peers__pb2.UpdatePeerGlobalsReq.SerializeToString,
                response_deserializer=peers__pb2.UpdatePeerGlobalsResp.FromString,
                )


class PeersV1Servicer(object):
    """NOTE: For use by gubernator peers only
    """

    def GetPeerRateLimits(self, request, context):
        """Used by peers to relay batches of requests to an authoritative peer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePeerGlobals(self, request, context):
        """Used by peers send global rate limit updates to other peers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PeersV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPeerRateLimits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeerRateLimits,
                    request_deserializer=peers__pb2.GetPeerRateLimitsReq.FromString,
                    response_serializer=peers__pb2.GetPeerRateLimitsResp.SerializeToString,
            ),
            'UpdatePeerGlobals': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePeerGlobals,
                    request_deserializer=peers__pb2.UpdatePeerGlobalsReq.FromString,
                    response_serializer=peers__pb2.UpdatePeerGlobalsResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.gubernator.PeersV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PeersV1(object):
    """NOTE: For use by gubernator peers only
    """

    @staticmethod
    def GetPeerRateLimits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.gubernator.PeersV1/GetPeerRateLimits',
            peers__pb2.GetPeerRateLimitsReq.SerializeToString,
            peers__pb2.GetPeerRateLimitsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePeerGlobals(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.gubernator.PeersV1/UpdatePeerGlobals',
            peers__pb2.UpdatePeerGlobalsReq.SerializeToString,
            peers__pb2.UpdatePeerGlobalsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
