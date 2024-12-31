import reflex as rx
from ...controller.elegir_personaje import Elegir_personaje
from quien_es_quien.controller.pregunta_respuesta import Interaccion

def grid_personajes():

    return rx.box( 
        rx.cond(
            ~Elegir_personaje.personaje_clicado,
            rx.center(
                rx.heading("Elije una tarjeta para empezar la partida" ,as_="h1"),
                
            ), 
        ),        
        rx.grid(
                rx.foreach(
                    Interaccion.vivos,
                    lambda nombre: rx.cond(
                        Elegir_personaje.personaje_clicado,
                        # True
                        rx.container(
                            rx.card(
                                rx.inset(
                                    rx.image(
                                        src=f"/personajes/{nombre}.jpg",
                                        width="4.6rem",
                                        height="5.5rem",
                                    ),
                                    side="top",
                                    pb="current",
                                ),
                                rx.text(
                                    nombre,
                                    text_align="center",
                                    font_weight="bold",
                                    height="0.5rem",
                                    
                                ),
                                display="flex",
                                justify_content="center",
                                align_items="center",
                                flex_direction="column",
                                width="4.6rem",
                            ),
                            key=f"vivo-{nombre}"
                        ),

                        # Si False devolver Fallback
                        rx.card(
                            rx.inset(
                                rx.image(
                                    src="/quien-es-quien.jpg",
                                    width="100%",
                                    height="auto",
                                ),
                                side="top",
                                pb="current",
                            ),
                            rx.text(
                                "?",
                                text_align="center",
                                font_weight="bold",
                                height="0.5rem",
                            ),
                            on_click=Elegir_personaje.personaje_seleccionado,
                            key=f"oculto-{nombre}"
                        ),
                    ),
                ),
                rx.foreach(
                    Interaccion.muertos,
                    lambda nombre: 
                     rx.container(
                            rx.card(
                                rx.inset(
                                    rx.image(
                                        src=f"/skull.png",
                                        width="4.6rem",
                                        height="5.5rem",
                                    ),
                                    side="top",
                                    pb="current",
                                ),
                                rx.text(
                                    "Muerto",
                                    text_align="center",
                                    font_weight="bold",
                                    height="0.5rem",
                                ),
                                display="flex",
                                justify_content="center",
                                align_items="center",
                                flex_direction="column",
                                width="4.6rem",
                                
                            ),
                            key=f"muerto-{nombre}"
                        ),
                ),
                gap="0.5rem",
                grid_template_columns="repeat(8, 1fr)",
                grid_template_rows="repeat(3, 1fr)",
            )
    )
