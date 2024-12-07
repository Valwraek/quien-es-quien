import reflex as rx
from quien_es_quien.service.personaje_a_adivinar import reiniciar_personaje_random
class Elegir_personaje(rx.State):
        
    personaje_clicado: bool = False

    @rx.event
    def personaje_seleccionado(self):
        
        if not self.personaje_clicado:
            self.personaje_clicado = True
            reiniciar_personaje_random()