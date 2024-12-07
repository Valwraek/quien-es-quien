from quien_es_quien.service.personaje_a_adivinar import reiniciar_personaje_random, adivinar_personaje

def test_personaje_no_nulo():
    
    reiniciar_personaje_random()

    from quien_es_quien.service.personaje_a_adivinar import personaje
    assert personaje

def test_adivinar_personaje_nombre_no_encontrado():
    
    reiniciar_personaje_random()

    assert adivinar_personaje("nombre no encontrado") == "Tienes que proporcionar un nombre del personaje!"

def test_adivinar_personaje_correcto():
    
    reiniciar_personaje_random()
    from quien_es_quien.service.personaje_a_adivinar import personaje

    assert adivinar_personaje(personaje['nombre']) == "Correcto!!!"


def test_adivinar_personaje_incorrecto():
    
    reiniciar_personaje_random()

    from quien_es_quien.service.personaje_a_adivinar import personaje
    from quien_es_quien.service.cargar_personajes_desde_xml import cargar_personajes_desde_xml as cargar_xml

    personajes_disponibles = [dict_personaje for dict_personaje in cargar_xml() if dict_personaje != personaje]
    personaje_incorrecto = personajes_disponibles[0]['nombre']

    assert adivinar_personaje(personaje_incorrecto) == personaje['nombre']