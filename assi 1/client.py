import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take input from the user
num = int(input("Enter an integer: "))

# Call the remote function
result = proxy.calculate_factorial(num)

# Display result
print("Factorial is:", result)
