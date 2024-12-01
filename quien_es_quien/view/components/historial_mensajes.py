import reflex as rx
from quien_es_quien.view.styles.tablero_personajes_estilos import estilos as cs

def historial(question:str, answer:str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=cs.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=cs.answer_style),
            text_align="left",
            
        ),
        margin_y="1em",
        width="100%",
    )