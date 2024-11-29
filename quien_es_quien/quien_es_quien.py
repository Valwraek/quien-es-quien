import reflex as rx
from rxconfig import config
from quien_es_quien.view.components.menu_principal import menu_principal
from .view.tablero_personajes import tablero_personajes

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.container(
        menu_principal(),

    )


app = rx.App(
    stylesheets=[
        "/estilos_menu_principal.css",
    ]
)
app.add_page(index)
app.add_page(tablero_personajes, route="/un_jugador")