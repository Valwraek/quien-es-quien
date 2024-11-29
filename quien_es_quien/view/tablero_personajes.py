import reflex as rx
from .components.grid_personajes import grid_personajes

def tablero_personajes() -> rx.Component:
    return rx.container(
        grid_personajes()
        
    )
