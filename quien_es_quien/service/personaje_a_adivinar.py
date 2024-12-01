from quien_es_quien.service.personaje_random import elegir_personaje_random

PERSONAJE = elegir_personaje_random()

def preguntar_atributos(pregunta):
    try:
        return PERSONAJE[f'{pregunta}']
    except KeyError:
        return "Tienes que proporcionar un atributo válido!"