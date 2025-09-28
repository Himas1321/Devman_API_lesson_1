import requests

url = 'https://wttr.in/Череповец?MnqT&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)


url = 'https://wttr.in/Лондон?MnqT&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)


url = 'https://wttr.in/Шереметьево?MnqT&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)
