# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import simple_pb2 as simple__pb2


class SimpleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PerformComputation = channel.unary_unary(
                '/SimpleService/PerformComputation',
                request_serializer=simple__pb2.ComputationRequest.SerializeToString,
                response_deserializer=simple__pb2.ComputationResult.FromString,
                )


class SimpleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PerformComputation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PerformComputation': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformComputation,
                    request_deserializer=simple__pb2.ComputationRequest.FromString,
                    response_serializer=simple__pb2.ComputationResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SimpleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PerformComputation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/PerformComputation',
            simple__pb2.ComputationRequest.SerializeToString,
            simple__pb2.ComputationResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)