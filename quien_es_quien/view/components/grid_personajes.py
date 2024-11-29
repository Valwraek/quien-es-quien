import reflex as rx

from ...service.cargar_personajes_desde_xml import cargar_personajes_desde_xml





def grid_personajes():
    personajes = cargar_personajes_desde_xml()
    lista_nombres = [personaje['nombre'] for personaje in personajes]

    return rx.grid(
    rx.foreach(
        lista_nombres,
        lambda nombre: rx.card(
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
                nombre
            ),
        ),
    ),
    gap="1rem",
    grid_template_columns=[
        "1fr",
        "repeat(6, 1fr)"
    ]
    
)