import xml.etree.ElementTree as et
from ..service.cargar_personajes_desde_xml import cargar_personajes_desde_xml
from ..service.cargar_personajes_desde_xml import comprobar_ruta
import os

'''def test_ruta_xml():
    assert (comprobar_ruta() == "quien_es_quien\service\../model/personajes.xml") == True'''

def test_xml_vacio():
    assert cargar_personajes_desde_xml() is not []



if __name__ == '__main__':
    
    #assert (os.path.exists("../model/personajes.xml")) == True
    assert test_xml_vacio()    
