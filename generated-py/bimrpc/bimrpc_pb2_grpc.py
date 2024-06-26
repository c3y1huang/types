# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bimrpc import bimrpc_pb2 as bimrpc_dot_bimrpc__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class BackingImageManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Delete = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/Delete',
                request_serializer=bimrpc_dot_bimrpc__pb2.DeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Get = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/Get',
                request_serializer=bimrpc_dot_bimrpc__pb2.GetRequest.SerializeToString,
                response_deserializer=bimrpc_dot_bimrpc__pb2.BackingImageResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/List',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=bimrpc_dot_bimrpc__pb2.ListResponse.FromString,
                )
        self.VersionGet = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/VersionGet',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=bimrpc_dot_bimrpc__pb2.VersionResponse.FromString,
                )
        self.Sync = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/Sync',
                request_serializer=bimrpc_dot_bimrpc__pb2.SyncRequest.SerializeToString,
                response_deserializer=bimrpc_dot_bimrpc__pb2.BackingImageResponse.FromString,
                )
        self.Send = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/Send',
                request_serializer=bimrpc_dot_bimrpc__pb2.SendRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Fetch = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/Fetch',
                request_serializer=bimrpc_dot_bimrpc__pb2.FetchRequest.SerializeToString,
                response_deserializer=bimrpc_dot_bimrpc__pb2.BackingImageResponse.FromString,
                )
        self.PrepareDownload = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/PrepareDownload',
                request_serializer=bimrpc_dot_bimrpc__pb2.PrepareDownloadRequest.SerializeToString,
                response_deserializer=bimrpc_dot_bimrpc__pb2.PrepareDownloadResponse.FromString,
                )
        self.BackupCreate = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/BackupCreate',
                request_serializer=bimrpc_dot_bimrpc__pb2.BackupCreateRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.BackupStatus = channel.unary_unary(
                '/bimrpc.BackingImageManagerService/BackupStatus',
                request_serializer=bimrpc_dot_bimrpc__pb2.BackupStatusRequest.SerializeToString,
                response_deserializer=bimrpc_dot_bimrpc__pb2.BackupStatusResponse.FromString,
                )
        self.Watch = channel.unary_stream(
                '/bimrpc.BackingImageManagerService/Watch',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class BackingImageManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VersionGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Send(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareDownload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackupCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackupStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Watch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackingImageManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.DeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.GetRequest.FromString,
                    response_serializer=bimrpc_dot_bimrpc__pb2.BackingImageResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=bimrpc_dot_bimrpc__pb2.ListResponse.SerializeToString,
            ),
            'VersionGet': grpc.unary_unary_rpc_method_handler(
                    servicer.VersionGet,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=bimrpc_dot_bimrpc__pb2.VersionResponse.SerializeToString,
            ),
            'Sync': grpc.unary_unary_rpc_method_handler(
                    servicer.Sync,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.SyncRequest.FromString,
                    response_serializer=bimrpc_dot_bimrpc__pb2.BackingImageResponse.SerializeToString,
            ),
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.SendRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Fetch': grpc.unary_unary_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.FetchRequest.FromString,
                    response_serializer=bimrpc_dot_bimrpc__pb2.BackingImageResponse.SerializeToString,
            ),
            'PrepareDownload': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareDownload,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.PrepareDownloadRequest.FromString,
                    response_serializer=bimrpc_dot_bimrpc__pb2.PrepareDownloadResponse.SerializeToString,
            ),
            'BackupCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.BackupCreate,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.BackupCreateRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BackupStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.BackupStatus,
                    request_deserializer=bimrpc_dot_bimrpc__pb2.BackupStatusRequest.FromString,
                    response_serializer=bimrpc_dot_bimrpc__pb2.BackupStatusResponse.SerializeToString,
            ),
            'Watch': grpc.unary_stream_rpc_method_handler(
                    servicer.Watch,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bimrpc.BackingImageManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BackingImageManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/Delete',
            bimrpc_dot_bimrpc__pb2.DeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/Get',
            bimrpc_dot_bimrpc__pb2.GetRequest.SerializeToString,
            bimrpc_dot_bimrpc__pb2.BackingImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/List',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bimrpc_dot_bimrpc__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VersionGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/VersionGet',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bimrpc_dot_bimrpc__pb2.VersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/Sync',
            bimrpc_dot_bimrpc__pb2.SyncRequest.SerializeToString,
            bimrpc_dot_bimrpc__pb2.BackingImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/Send',
            bimrpc_dot_bimrpc__pb2.SendRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Fetch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/Fetch',
            bimrpc_dot_bimrpc__pb2.FetchRequest.SerializeToString,
            bimrpc_dot_bimrpc__pb2.BackingImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PrepareDownload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/PrepareDownload',
            bimrpc_dot_bimrpc__pb2.PrepareDownloadRequest.SerializeToString,
            bimrpc_dot_bimrpc__pb2.PrepareDownloadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackupCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/BackupCreate',
            bimrpc_dot_bimrpc__pb2.BackupCreateRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackupStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bimrpc.BackingImageManagerService/BackupStatus',
            bimrpc_dot_bimrpc__pb2.BackupStatusRequest.SerializeToString,
            bimrpc_dot_bimrpc__pb2.BackupStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Watch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/bimrpc.BackingImageManagerService/Watch',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
