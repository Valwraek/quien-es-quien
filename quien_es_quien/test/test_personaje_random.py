from ..service.personaje_random import elegir_personaje_random

def test_elegir_personaje_random():
    assert type(elegir_personaje_random()) == dict


if __name__ == "__main__":
    test_elegir_personaje_random()
    print("Todos los tests pasaron")