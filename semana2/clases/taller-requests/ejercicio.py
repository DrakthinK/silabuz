import requests

def obterner_data(data:dict):
    return [data['weight'],data['abilities']]
  
res = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
posts = res.json()
print(obterner_data(posts))
""" bruno@guvery.com """
