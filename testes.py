import requests
headers = {
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZTMiLCJleHAiOjE3NTQwMTcyNjh9.CV-JiKTtZKtWsuZmA60WomB55hSKShyAbX9aNWx7uqw"
}

response = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)

print(response)
print(response.json())