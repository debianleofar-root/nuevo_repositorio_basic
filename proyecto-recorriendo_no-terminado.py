import shutil
import os
import pathlib

ubicacion=pathlib.Path("/home/leofar/Downloads/")
comando=os.listdir(ubicacion)

for recorriendo_carpetas in comando:
    carpeta=ubicacion / recorriendo_carpetas
    if carpeta.suffix == ".txt":
        print(f"encontrado {carpeta}")