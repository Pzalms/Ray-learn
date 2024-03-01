from ray import serve
import ray

ray.init()

# Define the serving function
def add(request):
    # Extracting parameters from the request
    params = request.body().to_pybytes().decode().split(",")
    num1 = float(params[0])
    num2 = float(params[1])
    
    # Addition computation
    result = num1 + num2
    
    # Returning the result
    return str(result)

# Deploy the serving function
serve.create_backend("add_service", add)
serve.create_endpoint("add", backend="add_service", route="/add")

# Start the server
serve.start()
