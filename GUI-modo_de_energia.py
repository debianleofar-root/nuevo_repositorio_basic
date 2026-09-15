import subprocess
import flet as ft
from time import sleep
from sys import exit



##INTERFAZ-FLET
def Main(page : ft.Page):

    ##FUNCIONES SUBPROCESOS
    estado = ft.Text(value="Modos de energía del sistema operativo", size=20)

    def atualizar(e):
        estado.value = "comun"
        page.update()

    def Apagar(e):
        estado.value="apagando"
        page.update()
        try:
            sleep(5)
            #subprocess.run(["shutdown","-h","now"])
        except Exception:
            print("consola: error apagar")
            exit(1)
        
        
    def Reiniciar(e):
        estado.value
        try:
            sleep(5)
            subprocess.run(["reboot"])
        except Exception:
            print("consola: error reinicio")
            exit(1)
        page.update
    def Suspender(e):
        estado.value
        try:
            sleep(5)
            subprocess.run(["systemctl suspend"])
        except Exception:
            print("consola: error Suspender")
            exit(1)
        page.update()
    page.window.width=800
    page.window.height=600

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.title = ("programa-energia")
    ft.Container(bgcolor="blue")


    
    page.add(
        ft.Row(
            controls=[ft.Button("apagar",color="red",bgcolor="white",on_click=Apagar)],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        ft.Row(
            controls=[ft.Button("reiniciar",color="green",bgcolor="white",on_click=Reiniciar)],
            alignment=ft.MainAxisAlignment.CENTER
               ),
        ft.Row(
        controls=[ft.Button("Suspender",color="blue",bgcolor="white",on_click=Suspender)],
        alignment=ft.MainAxisAlignment.CENTER
                )
        
             )
ft.run(Main)