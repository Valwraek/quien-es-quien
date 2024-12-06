from quien_es_quien.service.cargar_personajes_desde_xml import cargar_personajes_desde_xml as cargar_xml
from quien_es_quien.service.personaje_a_adivinar import personaje as personaje_a_adivinar

def comprobar_atributos_personajes(atributo):
    try:
        return [personaje['nombre'] for personaje in cargar_xml() if personaje[f'{atributo}'] != personaje_a_adivinar[f'{atributo}'] ]
    except KeyError:
        return []
    