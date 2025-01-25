import requests

response = requests.get('https://cruzterrasanta.com.br/nossa-senhora-abadia/20/101/#google_vignette')

print(response.status_code)

print('')

print(response.headers)

print('')

print(response.content)