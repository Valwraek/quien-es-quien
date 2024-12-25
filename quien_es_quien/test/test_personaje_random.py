from ..service.personaje_random import elegir_personaje_random
from ..service.personaje_random import elegir_nombre_personaje_random
from ..service.cargar_personajes_desde_xml import cargar_personajes_desde_xml as xml


def test_elegir_personaje_random():
    assert type(elegir_personaje_random()) == dict


if __name__ == "__main__":
    test_elegir_personaje_random()
    print("Todos los tests pasaron")