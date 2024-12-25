import random

from .cargar_personajes_desde_xml import todos_personajes

def elegir_personaje_random():
    return random.choice(todos_personajes)