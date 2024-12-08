<div align="center">

# Tabla de contenido

</div>

<div style="font-size: 20px;">

- [**Introducción**](#introducción)
- [**Manual**](#manual)
    - [**Instalación**](#instalación)
    - [**Uso**](#uso)
- [**Metodología**](#metodología)
- [**Descripción técnica**](#descripción-técnica)
    - [**Requisitos funcionales/no funcionales, NOT LIST**](#not-list)
    - [**Historias de usuario**](#historias-de-usuario)
    - [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
-  [**Diseño**](#diseño)
    - [**Diagrama de Componentes**](#diagrama_de_componentes)
- [**Implementación**](#implementación)
    - [**Tecnologías y Herramientas utilizadas**](#tecnologías-y-herramientas-utilizadas)
    - [**Backend**](#backend)
    - [**Frontend**](#frontend)
- [**Pruebas**](#pruebas)
    - [**Coverage**](#coverage)
    - [**Test de unidad**](#test-de-unidad)
    - [**Test de integración**](#test-de-integracion)
- [**Análisis del tiempo invertido**](#analisis-del-tiempo)
    - [**Clockify + Wakatime**](#clockify-+-wakatime)
    - [**Justificación temporal**](#justificacion-temporal)
- [**Conlusión**](#conclusion)
    - [**Posibles mejoras**](#posibles-mejoras)
    - [**Dificultades**](#dificultades)

</div>

# Introducción
Bardia Rajab Rajabi - [@Valwraek](https://github.com/Valwraek)  
Gabriel Suárez Domínguez - [@GabrielgsdCIUwU](https://github.com/GabrielgsdCIUwU)

Somos alumnos de Desarrollo de Aplicaciones Multiplataforma en el IES de Teis.  
Este proyecto se ha realizado como una muestra de nuestro aprendizaje de dos meses y medio de python, markdown y git.


# Manual

## Instalación


### Entorno Virtual - Windows

1. El primer paso es descargar el proyecto.  

    - ![Imagen de como descargar el proyecto](assets/img-readme/descargar-proyecto.png)  

    - El siguiente paso es descomprimir y abrir la carpeta en nuestro editor de código o cmd.  
    - ![Imagen de abrir el proyecto](assets/img-readme/abrir-proyecto.png)

2. Abrimos una terminal y en ella escribiremos lo siguiente:  
    - **``py -m venv venv``** con esto se ha creado un entorno virtual llamado **``venv``**.  

    <img src="assets/img-readme/comando-crear-entorno-virtual.png" alt="Comando para crear entorno virtual llamado venv" width="500px" height="350px"><br>

3. Ahora toca activar el entorno virtual y para ello hacemos lo siguiente:
    - En la terminal escribimos lo siguiente **``cmd``**.
    - Luego se escribirá **``.\venv\Scripts\activate.bat``**.  

    <img src="assets/img-readme/activar-entorno-virtual.png" alt="Comando para activar el entorno virtual"><br>

La razón por la que se crea un entorno virtual es para que al instalar Reflex solo se haga en este entorno y no en todo nuestro equipo.

4. Ahora instalaremos todas las dependencias necesarias para nuestro proyecto.  
    - **``pip install -r requirements.txt``** con este comando se instalará reflex.  

    <img src="assets/img-readme/instalacion-requirements.png" alt="Comando para instalar requirements"><br>

5. Ya tenemos instalado Reflex. Esto lo podemos saber, ya que donde antes teniamos la carpeta venv ahora existen más archivos y carpetas.

    <img src="assets/img-readme/inicializado-reflex.png" alt="Imagen de prueba de la inicialización de reflex"><br>

### Entorno virtual - Linux

El paso 2 y el paso 3 difieren en Linux. Los comandos para crear un entorno virtual y activarlo son:  

- **``python3 -m venv .venv``** con este comando se crea el entorno virtual.  
- **``source .venv/bin/activate``** con este se activará el entorno virtual.  

<img src="assets/img-readme/linux-entorno-virtual-y-activacion.png" alt="Comando para crear y activar entorno virtual en Linux">

---

## Uso
### Ejecutar la aplicación

Para los dos sistemas operativos es igual. 

- **``reflex run``** es el comando a utilizar para esta tarea.

<img src="assets/img-readme/reflex-run.png" alt="Ejecutar la aplicación">   
<br><br>
<img src="assets/img-readme/web-activo.png" alt="Servidor Web activo">


## Descripción técnica

### Not List

| In Scope | Out of Scope | Unresolved |
| -------- | ------------ | ---------- |
| Menú principal| El jugador pueda elegir su nombre | Menú de reglas |
| El jugador elige al azar al personaje a adivinar | Tabla de puntuación con los mejores jugadores | - |
| Proteger el input de entradas vacias, números y carácteristicas fallidas | Diferentes tableros | - |
| Ocultar personajes que no tienen la característica de manera automática| Modo jugador vs jugador | - |
| Opción para jugar de nuevo al terminar o perder | Chat para interaccionar en el modo jugador vs jugador | Indicar que pierde la partida

---

### Historias de usuario
![Historia de usuario](assets/img-readme/usuario1.png)  

![Historia de usuario](assets/img-readme/usuario2.png)

### Arquitectura de la aplicación

La arquitectura que se ha utilizado para este proyecto es el de MVC más servicios.  
 - En el **modelo** nos encontramos con nuestro sistema de almacenamiento de personajes.
 - En la **vista** nos encontramos con lo que el jugador ve en su navegador.
 - En el **controlador** coordina las acciones entre la vista y el modelo.
 - En el **servicio** contiene funciones o clases que encapsulan lógica de negocio.


## Diseño

### Diagrama de Componentes

[![Diagrama de dependencias](assets/diagrama_dependencias.svg)](assets/diagrama_dependencias.svg)
