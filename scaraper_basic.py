from bs4 import BeautifulSoup
import requests
import subprocess
from os import listdir,mkdir
from pathlib import Path
from shutil import move
from sys import exit

##GENERAL
ubicacion_actual=Path("/home/leofar/Desktop/archivos_py/limpieza_Xd/nuevo_archivo_py/") ##intercambiable


##############################
def FUNCION_DESCARGANDO(Imagen):
    try:
        print("instalando...")
        subprocess.run(["curl","-O",Imagen])
    except Exception:
        print("error")
        exit(1)

def Funcion_ver_carpeta_existe():
    ubicacion_descargas=Path("/home/leofar/Downloads/")
    uniendo_carpeta_descargas=ubicacion_descargas / "carpeta_scrapeado"
    if not uniendo_carpeta_descargas.is_dir():
        uniendo_carpeta_descargas.mkdir()
        print("creado")
    else:
        print("existe")    

def CREANDO_carpeta():
##recorriendo carpeta principal donde estamos
    for recorriendo_principal in listdir(ubicacion_actual):
        uniendo_carpetas=ubicacion_actual/recorriendo_principal
        if uniendo_carpetas.suffix == ".jpg":
            print(f"encontrado: {uniendo_carpetas}")
            #########
        else:
            print("fallo3")
            break
        ubicacion_descargas=("/home/leofar/Downloads/carpeta_scrapeado/")

        move(str(uniendo_carpetas),str(ubicacion_descargas))   
        print("moviendo")

###################################
url="https://snowball06.straw.page/"
encabezera="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:155.0) Gecko/20100101 Firefox/155.0"

obteninedo_web=requests.get(url)
if obteninedo_web.status_code == 200:
    print("existe URL \n")
    print("*"*100)
else:
    print("no existe")
convirtiendo_text_parser_html=BeautifulSoup(obteninedo_web.text,"html.parser")

##filtrando
for recorriendo in convirtiendo_text_parser_html:
    if convirtiendo_text_parser_html:
        c=convirtiendo_text_parser_html.find("img")
        src=c.get("src")
        print(f"TIENES A: {src}")
        FUNCION_DESCARGANDO(src)

        Funcion_ver_carpeta_existe()

        CREANDO_carpeta()
    elif c == None:
        break
    else:
        print("no se encontro")
        continue
    