import threading
from openai import OpenAI
import flet
import json

class Programa_interfaz():
    def __init__(self, pagina:flet.Page):


        ##API externo
        cliente_bot=OpenAI(base_url="",
        api_key="",)
        
        self.pag = pagina
        self.titulos_programa = self.pag.title
        
        ##FUNCIONES:
        def IA_chat_bot(INPUT : str):
            self.respuesta_texto.value = "pensando..."
            complementos=cliente_bot.responses.create(
                model="liquid/lfm-3-1.7b:free",
                instructions="Act with humanity.",
                input=INPUT,
            )
            self.respuesta_texto.value=complementos.output_text
            pagina.update()
            
        def al_hacer_enter(e):
           threading.Thread(target=IA_chat_bot,args=(self.Input_respuesta.value,)).start()



        ##estructura
        self.titulo = flet.Text(value="CHAT-BOT",text_align=flet.TextAlign.CENTER)
        self.Input_respuesta = flet.TextField(label="mensaje: ",on_submit=al_hacer_enter)
        self.respuesta_texto=flet.Text(value="respuesta_IA")

        

        #colocando
        self.pag.add(self.titulo, self.Input_respuesta,self.respuesta_texto)
def iniciando(z : flet.Page):
    clase=Programa_interfaz(z)
flet.run(iniciando)
print("Proceso  terminado..")