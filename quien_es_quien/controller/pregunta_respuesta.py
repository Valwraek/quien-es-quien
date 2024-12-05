import reflex as rx
from ..service.personaje_a_adivinar import preguntar_atributos
from quien_es_quien.service.cargar_personajes_desde_xml import cargar_personajes_desde_xml as cargar_xml
from quien_es_quien.service.personaje_a_adivinar import personaje as personaje_a_adivinar

class Interaccion(rx.State):

    question: str
    chat_history: list[tuple[str, str]]

    def flujo_trabajo(self, key: str):

        if key == "Enter":        

            if self.comprobar_input():
                self.question = ""
                return rx.window_alert("No puedes enviar mensajes vacios ni que contengan números!")              
            else:
                self.respuesta()

    @rx.var
    def valor_question(self):
        try:
            atributo = self.question
            print(self.question)
            print("comprobar:", [personaje['nombre'] for personaje in cargar_xml() if personaje[f'{atributo}'] != personaje_a_adivinar[f'{atributo}'] ])
            return [personaje['nombre'] for personaje in cargar_xml() if personaje[f'{atributo}'] != personaje_a_adivinar[f'{atributo}'] ]
        except KeyError:
            print("NO FURRULA!")
            return []
    

    def comprobar_input(self): 
        if not self.question: 
            return True
        elif not self.question.replace(" ", "").isalpha():
            return True 
        return False
       
    def respuesta(self):

        self.chat_history.append((self.question, ""))
        answer = preguntar_atributos(self.question)

        self.chat_history[-1] = (
            self.chat_history[-1][0],
            answer,
        )
        