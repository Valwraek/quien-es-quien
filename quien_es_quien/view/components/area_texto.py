import reflex as rx
from quien_es_quien.controller.pregunta_respuesta import Interaccion
from quien_es_quien.view.styles.tablero_personajes_estilos import estilos as cs
from quien_es_quien.controller.gato_personajes import VivoOMuerto
def area_texto() -> rx.Component:
    return (
        rx.input(
            placeholder="Haz tu pregunta",
            value=Interaccion.question,
            on_change=Interaccion.set_question,
            on_key_down=Interaccion.flujo_trabajo,
            on_key_up=VivoOMuerto.estan_muriendo,
            autofocus=True,
            style=cs.input_style,
            is_required=True
        )
    )