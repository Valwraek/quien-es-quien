import reflex as rx

class Elegir_personaje(rx.State):
        
    personaje_clicado: bool = False

    @rx.event
    def personaje_seleccionado(self):
        if not self.personaje_clicado:
            
            self.personaje_clicado = True