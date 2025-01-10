# Proyecto de Visión por Ordenador - Análisis de Velocidad de Coches

Este proyecto utiliza técnicas de visión por ordenador para analizar la velocidad de los coches en un circuito. El sistema detecta el paso de un coche por dos líneas de barrera y calcula su velocidad en función del tiempo que tarda en recorrer la distancia entre ambas barreras.

## Ficheros Utilizados

A continuación, se describen los principales ficheros utilizados en este proyecto:

- **`radar.py`**: Este archivo contiene el código principal para procesar los frames de video, detectar los coches y calcular la velocidad en base a su desplazamiento a través de las barreras.
  
- **`rastreador.py`**: Implementa el algoritmo de seguimiento de objetos (coches) en los frames del video, permitiendo identificar cada coche y su trayectoria.

- **`radar.ipynb`**: El script en formato ipynb donde podemos ver el código realizado así como otras funciones que se han utilizado en el proyecto (creación de la imagen del primer frame para detectar las zonas)
- **`test.py`**: Ejemplo de código proporcionado de como extraer información de la cámara de la raspberry
## Instalación
- **`camara.py`**: Código que hemos utilizado previamente al fallo de la cámara para poder grabar con la raspberry camera y guardar el vídeo

## Requisitos del Sistema

- Python 3.8+
- OpenCV 4.5.0+
- NumPy
- Sistema operativo: Linux, macOS o Windows

## Arquitectura del Proyecto

El proyecto está compuesto por las siguientes partes:
- Calibración previa de la cámara
- Módulo de procesamiento de imágenes
- Algoritmo de seguimiento de objetos
- Cálculo de la velocidad y visualización de ella en tiempo real


Para ejecutar este proyecto localmente, sigue los siguientes pasos:

### Clonar el repositorio

```bash
git clone https://github.com/IgnacioViadero/ComputerVision
cd ProyectoFinal
