import reflex as rx
from quien_es_quien.view.components.menu_principal import menu_principal
from .view.tablero_personajes import tablero_personajes
from quien_es_quien.view.components.footer import footer


def index() -> rx.Component:
    return rx.fragment(
        menu_principal(),
        footer()

    )


app = rx.App(
    stylesheets=[
        "/estilos_menu_principal.css",
    ],
    theme=rx.theme(
        appearance="dark",
    )
)
app.add_page(index)
app.add_page(tablero_personajes, route="/un_jugador")