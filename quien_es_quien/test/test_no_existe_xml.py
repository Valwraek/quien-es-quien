from ..service.cargar_personajes_desde_xml import cargar_personajes_desde_xml

def test_xml_vacio():
    assert cargar_personajes_desde_xml() is not []


if __name__ == '__main__':
    assert test_xml_vacio()    
