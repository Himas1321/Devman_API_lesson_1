import requests


def func_url(url): 
	response = requests.get(url, params={
        "MnqT": "",
        "lang": "ru",
    })
	response.raise_for_status()
	print(url)
	print(response.text)

urls = [
	"https://wttr.in/Череповец",
	"https://wttr.in/Лондон",
	"https://wttr.in/Нерюнгри"
]

if __name__ == '__main__':
	for url in urls:
		func_url(url)
