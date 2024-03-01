import pyarrow.flight as flight
import pyarrow as pa

# Define the connection parameters
client = flight.FlightClient("grpc://localhost:50051")

# Define the request payload
data = pa.array([b"5,10"], type=pa.utf8())

# Make the request to the server
info = flight.FlightInfo.list_flights(client)
flight_info, = info
endpoint = flight_info.endpoints[0]
ticket = client.do_put(endpoint.ticket, data)
result = client.do_get(ticket)
print(result.body.to_pybytes().decode())
