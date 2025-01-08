import reflex as rx
from ..service.personaje_a_adivinar import preguntar_atributos, adivinar_personaje, reiniciar_personaje_random
from quien_es_quien.service.cargar_personajes_desde_xml import todos_personajes as cargar_personajes
from quien_es_quien.service.comprobar_atributos_personaje import comprobar_atributos_personajes

class Interaccion(rx.State):

    question: str
    chat_history: list[tuple[str, str]]
    vivos = list = [personaje['nombre'] for personaje in cargar_personajes]
    muertos = set = set()
    adivinar = bool = False

    def flujo_trabajo(self, key: str):

        if key == "Enter":        

            if self.comprobar_input():
                self.question = ""
                return rx.window_alert("No puedes enviar mensajes vacios ni que contengan números!")              
            else:
                self.respuesta()
                self.estan_muriendo()
                self.question = ""
  

    def comprobar_input(self): 
        
        if not self.question.replace(" ", "").isalpha(): 
            return True
        return False
       
    def respuesta(self):
        
        self.chat_history.append((self.question, ""))

        if self.question == "reiniciar":
            self.adivinar = False
            self.todos_vivos()
            self.chat_history = []
            reiniciar_personaje_random()
            return

        if self.adivinar:
            answer = adivinar_personaje(self.question.strip())
            self.adivinar = False
        else:
            if self.question == "adivinar":
                answer = "Di el nombre del personaje"
                self.adivinar = True
            else:
                answer = preguntar_atributos(self.question.strip())

        self.chat_history[-1] = (self.question, answer)

    def todos_vivos(self):
        
        self.muertos = set()      
        self.vivos = [personaje['nombre'] for personaje in cargar_personajes]
    
    def estan_muriendo(self):
        
        if self.question.strip() == "nombre":
            return 
        self.muertos.update(comprobar_atributos_personajes(self.question.strip()))
        self.vivos = [personaje for personaje in self.vivos if personaje not in self.muertos]