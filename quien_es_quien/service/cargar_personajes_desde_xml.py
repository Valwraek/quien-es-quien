import xml.etree.ElementTree as et
import os


def comprobar_ruta():
    
        archivo = os.path.join(os.path.dirname(__file__), "../model/personajes.xml")
        return archivo
    

def cargar_personajes_desde_xml():
    
    try:
        archivo = comprobar_ruta()
        arbol = et.parse(archivo)
        raiz = arbol.getroot()

        personajes = []
        for nodo_personaje in raiz.findall("personaje"):
            personaje = {atributo: nodo_personaje.get(atributo) for atributo in nodo_personaje.keys()}
            personajes.append(personaje)
        return personajes
    except FileNotFoundError:
        return "Archivo no encontrado"

