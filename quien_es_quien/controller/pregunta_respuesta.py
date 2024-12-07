import reflex as rx
from ..service.personaje_a_adivinar import preguntar_atributos, adivinar_personaje, reiniciar_personaje_random
from quien_es_quien.service.cargar_personajes_desde_xml import cargar_personajes_desde_xml as cargar_xml
from quien_es_quien.service.comprobar_atributos_personaje import comprobar_atributos_personajes
from quien_es_quien.controller.elegir_personaje import Elegir_personaje
class Interaccion(rx.State):

    question: str
    chat_history: list[tuple[str, str]]
    vivos = list = [personaje['nombre'] for personaje in cargar_xml()]
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
    
    def valor_question(self):
        try:
            from quien_es_quien.service.personaje_a_adivinar import personaje as personaje_a_adivinar
            atributo = self.question
            return [personaje['nombre'] for personaje in cargar_xml() if personaje[f'{atributo}'] != personaje_a_adivinar[f'{atributo}'] ]
        except KeyError:
            return []
    

    def comprobar_input(self): 
        if not self.question: 
            return True
        elif not self.question.replace(" ", "").isalpha():
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
            answer = adivinar_personaje(self.question)
            self.adivinar = False
        else:
            if self.question == "adivinar":
                answer = "Di el nombre del personaje"
                self.adivinar = True
            else:
                answer = preguntar_atributos(self.question)

        self.chat_history[-1] = (
            self.chat_history[-1][0],
            answer,
        )

    def todos_vivos(self):
        
        self.muertos = set()      
        self.vivos = [personaje['nombre'] for personaje in cargar_xml()]
    
    def estan_muriendo(self):
        
        self.muertos.update(comprobar_atributos_personajes(self.question))
        self.vivos = [personaje for personaje in self.vivos if personaje not in self.muertos]