import reflex as rx
from quien_es_quien.service.personaje_random import elegir_personaje_random
from quien_es_quien.service.cargar_personajes_desde_xml import cargar_personajes_desde_xml as cargar_xml


todos_los_personajes = [persona['nombre'] for persona in cargar_xml()]
personaje = {}
def reiniciar_personaje_random():
    global personaje 
    personaje = elegir_personaje_random()

def adivinar_personaje(nombre_personaje):
        if nombre_personaje not in todos_los_personajes:
             return "Tienes que proporcionar un nombre del personaje!"
        
        nombre_personaje_oculto = personaje['nombre']
        if nombre_personaje == nombre_personaje_oculto:
             return "Correcto!!!"
        else:
             return nombre_personaje_oculto

def preguntar_atributos(pregunta):
    try:
        if pregunta == 'nombre':
            return "Buen intento pero no cuela."

        return personaje[f'{pregunta}']
    except KeyError:
        return "Tienes que proporcionar un atributo válido!"