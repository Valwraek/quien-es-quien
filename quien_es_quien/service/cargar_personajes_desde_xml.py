import xml.etree.ElementTree as et
import os

def cargar_personajes_desde_xml():
    
    try:
        archivo = os.path.join(os.path.dirname(__file__), "../model/personajes.xml")

        tree = et.parse(archivo)
        raiz = tree.getroot()


        personajes = []
        for nodo_personaje in raiz.findall("personaje"):
            personaje = {atributo: nodo_personaje.get(atributo) for atributo in nodo_personaje.keys()}

            if "gafas" in personaje:
                personaje["gafas"] = personaje["gafas"] == "True"
            if "sombrero" in personaje:
                personaje["sombrero"] = personaje["sombrero"] == "True"
            personajes.append(personaje)

        return personajes
    except FileNotFoundError:
        return "Archivo no encontrado"

personajes_cargados = cargar_personajes_desde_xml()
print(personajes_cargados)
