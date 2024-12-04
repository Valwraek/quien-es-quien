import reflex as rx
from ..service.personaje_a_adivinar import preguntar_atributos

class Interaccion(rx.State):

    question: str
    chat_history: list[tuple[str, str]]

    def flujo_trabajo(self, key: str):

        if key == "Enter":        

            if self.comprobar_input():
                self.question = ""
                return rx.window_alert("No puedes enviar mensajes vacios ni que contengan números!")              
            else:
                return self.respuesta()
                         

    def comprobar_input(self): 
        if not self.question or not self.question.isalpha() and self.question.isspace():
            return True
        return False
       
    def respuesta(self):

        self.chat_history.append((self.question, ""))
        answer = preguntar_atributos(self.question)
        self.question = ""
        
        for i in range(len(answer)):

            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )