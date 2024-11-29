import random

from .cargar_personajes_desde_xml import cargar_personajes_desde_xml as lista_personajes

def elegir_personaje_random():
    return random.choice(lista_personajes())

def elegir_nombre_personaje_random():
    return random.choice(lista_personajes())['nombre']