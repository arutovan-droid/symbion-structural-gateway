import requests

# Тест основного endpoint
response = requests.get("http://localhost:8000/")
print("Root endpoint:", response.json())

# Тест health check
response = requests.get("http://localhost:8000/health") 
print("Health check:", response.json())
