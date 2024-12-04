import reflex as rx
from .components.grid_personajes import grid_personajes
from .components.area_texto import area_texto
from .components.historial_mensajes import historial
from quien_es_quien.controller.pregunta_respuesta import Interaccion 
from quien_es_quien.view.styles.tablero_personajes_estilos import estilos as cs
from ..controller.elegir_personaje import Elegir_personaje

def tablero_personajes() -> rx.Component:
    return rx.container(
        grid_personajes(),

        rx.cond(
            Elegir_personaje.personaje_clicado,
            rx.box(
                rx.box(
                    rx.foreach (
                        Interaccion.chat_history,
                        lambda messages: historial(messages[0], messages[1]),
                    ),
                    style=cs.caja_pregunta_respuesta,
                ),
                area_texto()
            )
        ),
        
        background_color="#111113"
    )
