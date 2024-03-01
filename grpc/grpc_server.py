# gRPC server code (grpc_server.py)
import grpc
import time
from concurrent import futures
import simple_pb2
import simple_pb2_grpc

class SimpleService(simple_pb2_grpc.SimpleServiceServicer):
    def PerformComputation(self, request, context):
        result = request.x + request.y
        return simple_pb2.ComputationResult(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_pb2_grpc.add_SimpleServiceServicer_to_server(SimpleService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started...")
    try:
        while True:
            time.sleep(3600)  # One hour
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
