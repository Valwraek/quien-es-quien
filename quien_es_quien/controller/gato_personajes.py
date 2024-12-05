import reflex as rx
from quien_es_quien.service.cargar_personajes_desde_xml import cargar_personajes_desde_xml as cargar_xml
from quien_es_quien.controller.pregunta_respuesta import Interaccion
class VivoOMuerto(rx.State):
    vivos = list = [personaje['nombre'] for personaje in cargar_xml()]
    muertos = set = set()
    
    @rx.event
    def estan_muriendo(self, key: str):
        if key == "Enter":
            print("muertos:", self.muertos)
            try:
                self.muertos.update(Interaccion.valor_question())
                self.vivos = [personaje for personaje in self.vivos if personaje not in self.muertos]
            except TypeError:
                print("Pudrete!")

    @rx.event  
    def todos_vivos(self):
        self.muertos = set
        self.vivos = [personaje['nombre'] for personaje in cargar_xml()]