import requests
import funciones_preguntas
import json

url = "https://opentdb.com/api.php?amount=1"
json_raw = requests.get(url).json()['results'][0]
#print(json_raw)
print(funciones_preguntas.get_respuestas(json_raw))