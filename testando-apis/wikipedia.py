import requests

pagina = "https://pt.wikipedia.org/api/rest_v1/page/summary/Counter-Strike"
baixar = requests.get(pagina)
dados = baixar.json()
print(dados["extract"])
