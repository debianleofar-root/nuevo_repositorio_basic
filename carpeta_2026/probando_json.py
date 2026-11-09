##importando informacion con cargarlo load
import json

ubicacion="/home/leofar/Desktop/archivos_py/limpieza_Xd/archivo_segundo/proyectos/chat_bot/API.json"
with open(ubicacion,"r") as e:
    az=json.load(e)
a=type(az["api"])

print(az["api"])
print(az["base_url"])

print(a)
