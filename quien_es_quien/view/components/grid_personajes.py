import reflex as rx
from ...service.cargar_personajes_desde_xml import cargar_personajes_desde_xml
from ...controller.elegir_personaje import Elegir_personaje


def grid_personajes():
    personajes = cargar_personajes_desde_xml()
    lista_nombres = [personaje['nombre'] for personaje in personajes]

    return rx.box( 
        rx.cond(
            ~Elegir_personaje.personaje_clicado,
            rx.center(
                rx.heading("Elije una tarjeta para empezar la partida" ,as_="h1"),
                
            ), 
        ),        
        rx.grid(
                rx.foreach(
                    lista_nombres,
                    lambda nombre: rx.cond(
                        Elegir_personaje.personaje_clicado,
                        # True
                        rx.container(
                            rx.card(
                                rx.inset(
                                    rx.image(
                                        src="https://reflex.dev/reflex_banner.png",
                                        width="100%",
                                        height="auto",
                                    ),
                                    side="top",
                                    pb="current",
                                ),
                                rx.text(
                                    nombre,
                                    text_align="center",
                                    font_weight="bold",
                                ),
                            ),
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
                            ),
                            on_click=Elegir_personaje.personaje_seleccionado,
                        ),
                    ),
                ),
                gap="1rem",
                grid_template_columns="repeat(6, 1fr)",
            )
    )
