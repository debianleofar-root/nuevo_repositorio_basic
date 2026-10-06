import json
import os
import pathlib
import shutil
import platform


lista_de_tareas=[]

diccionario=    {

    
        "user"  : "",
        "sys"   : "",
        "lista_palabras" : [""]


                }


##FUNCIONES

def añadir_tarea(x):
    print(f"agregando -- > {x}")
    try:
        lista_de_tareas.append(x)
        print("lista añadida")
    except Exception as c:
        print(f"hubo un error {c}")

def eleminar_lista_numero(num):
    print(lista_de_tareas)
    try:
        print("eleminando..")
        lista_de_tareas.pop(num)
    except Exception:
        print("error,prueba con numero")


##usando JSON:
def json_import():
    ##sacar el archivo
    ###hace un with open y usa "w"
    with open("archivo.txt","r") as c:
        cargado=json.load(c)
        conviriendo=dict(cargado)
        print("archivos: ")
        print(conviriendo["lista_palabras"])
        lista_de_tareas.append(list(conviriendo))

        
def exportar_json():
##leer el archivo
###añade todo eso al diccionario de arriba,uso "r"
    diccionario={
        "user"  : "",
        "sys"   : "",
        "lista_palabras" : ["dadadad","dadadad","dadada"]
                }
    diccionario["lista_palabras"]=lista_de_tareas.copy()
    diccionario["sys"]=platform.system()
    diccionario["user"]= "anonim"
    
    print(f"usuario extrajo")

### un diccionario de palabras ##EN PRUEBA
def exportar_txt():
    ###ubicacion
    pregunta_path=input("path con archivo -->    ")
    convertiendo_path=pathlib.Path(pregunta_path)
    ###nombre del archivo
    pregunta_nombre_archivo=input("nombre del archivo: ")
    convertiendo_nombre_path=pathlib.Path(pregunta_nombre_archivo)

    UNIENDO=convertiendo_path / convertiendo_nombre_path
    with open(UNIENDO,"r") as c:
        try:
            a=c.read()
            modificando=a.splitlines()
            lista_de_tareas.append(modificando)
            print(modificando)
            print("hecho...")
        except Exception:
            print("fallo..")

##EN PRUEBA 

def confirmacion_archivo_confirmacion():
    ubicacion_descargas=pathlib.Path("/home/leofar/Downloads")
    carpeta="archivo_carpeta"
    archivo="archivo.txt"
    uniendolo_ubicacion_archivo=ubicacion_descargas / archivo

    for a in ubicacion_descargas.rglob("archivo_carpeta"):
        if a.exists():
            print("existe carperta")
            #"####"#"#"#"#"#"#"
            with open(uniendolo_ubicacion_archivo,"w",encoding="utf-8") as s:
                try:
                    print("guardando")
                    s.write(lista_de_tareas)
                    shutil.move("archivo.txt",)
                except Exception:
                    print("error al guardara")            
        else:
            os.mkdir(ubicacion_descargas / archivo)


##OPCIONES


lista_de_opciones=["añadir tarea","eleminar lista","json_import","json_export"]

while True:
    for z,y in enumerate(lista_de_opciones,start=1):
        print(z,"*",y)

    print("*"*64)    

    for a,b in enumerate(lista_de_tareas):
        print(a,"-.",b)
    pregunta=int(input("elige: "))
    
    match pregunta:
        case 1:
            agregar=input("tarea: ")
            añadir_tarea(agregar)
        case 2:
            eleminar=int(input("numero: "))
            eleminar_lista_numero(eleminar-1)
        case 3:
            confirmacion_archivo_confirmacion()
        case 4:
            exportar_txt()
##AUN NO TERMINADO