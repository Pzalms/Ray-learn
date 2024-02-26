# Ray client code (ray_client.py)
import grpc
import simple_pb2
import simple_pb2_grpc
import ray

@ray.remote
def remote_compute(x, y):
    # Connect to the gRPC server
    channel = grpc.insecure_channel('localhost:50051')
    stub = simple_pb2_grpc.SimpleServiceStub(channel)
    
    # Make a gRPC request
    request = simple_pb2.ComputationRequest(x=x, y=y)
    response = stub.PerformComputation(request)
    
    return response.result

def main():
    ray.init()

    # Perform computation remotely
    result_id = remote_compute.remote(12, 4)
    result = ray.get(result_id)
    print("Result of computation:", result)

if __name__ == '__main__':
    main()
