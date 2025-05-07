from xmlrpc.server import SimpleXMLRPCServer

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return str(result)  # ← Convert result to string


# Set up server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the factorial function to be accessible remotely
server.register_function(factorial, "calculate_factorial")

# Keep server running
server.serve_forever()
