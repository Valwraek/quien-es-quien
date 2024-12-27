import xml.etree.ElementTree as et
import os


def comprobar_ruta():
    
        archivo = os.path.join(os.path.dirname(__file__), "../model/personajes.xml")
        return archivo

def respuestas_lenguaje_natural(clave):

    claves_no_es = ["nombre", "mujer", "hombre", "calvo", "blanco", "rubio", "negro", "castaño", "naranja", "pelirrojo"]
    if clave in claves_no_es:
         return f'No es {clave}'
    
    claves_no_tiene = ["ojos", "gafa", "pendiente", "sombrero", "coleta", "barba", "bigote", "narizGrande"]
    if clave in claves_no_tiene:
         return f'No tiene {clave}'
    
    claves_no_esta = ["sonrojado"]
    if clave in claves_no_esta:
         return f'No está {clave}'
    
    return f'{clave}'

def leer_claves_desde_xml(raiz):
     nodo_claves = raiz.find("claves")
     return {clave.text: respuestas_lenguaje_natural(clave.text) for clave in nodo_claves.findall("clave")}

def cargar_personajes_desde_xml():
    
    try:
        arbol = et.parse(comprobar_ruta())
        raiz = arbol.getroot()

        claves_predeterminadas = leer_claves_desde_xml(raiz)
        personajes = []
        for nodo_personaje in raiz.findall("personajes/personaje"):
            personaje = claves_predeterminadas.copy()
            for atributo in nodo_personaje:
                if atributo.tag in personaje:
                    personaje[atributo.tag] = atributo.text
            
            personajes.append(personaje)
        return personajes
    except FileNotFoundError:
        return "Archivo no encontrado"

todos_personajes = cargar_personajes_desde_xml()