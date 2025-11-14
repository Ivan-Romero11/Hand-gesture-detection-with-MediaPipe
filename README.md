Actividad 5: Detección de Gestos con MediaPipe
Este proyecto es un script en Python que utiliza OpenCV y MediaPipe para detectar manos en tiempo real a través de una cámara web. El script no solo rastrea los 21 puntos de referencia de la mano, sino que también cuenta los dedos levantados y reconoce un conjunto de gestos específicos.

-Características
Detección de Manos: Detecta y rastrea hasta 2 manos simultáneamente.
Seguimiento de Puntos de Referencia: Visualiza en tiempo real los 21 puntos de referencia (landmarks) y el esqueleto de la mano.

-Identificación de Mano: Distingue entre la mano derecha y la izquierda.
-Conteo de Dedos: Cuenta cuántos dedos están levantados (incluyendo una lógica específica para el pulgar).
-Reconocimiento de Gestos: Identifica y muestra en pantalla gestos predefinidos.
-Información de Depuración: Muestra los índices numéricos (0-20) de cada punto de referencia para facilitar el desarrollo y la depuración.

-Gestos Reconocidos
El script está programado para identificar los siguientes gestos:
-LIKE (Pulgar arriba)
-DISLIKE (Pulgar abajo)
-O.K. (Punta del pulgar y punta del índice juntas)
-PAZ (Dedos índice y medio levantados)

-Tecnologías Utilizadas
Python 3
OpenCV (para la captura y visualización de la cámara)
MediaPipe (para el modelo de detección de manos)

-Instalación
Clona este repositorio o descarga el archivo hand.py.
(Recomendado) Crea un entorno virtual para instalar las dependencias:
Bash

python -m venv venv
# En Windows
.\venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
Instala las bibliotecas necesarias usando pip:

-Bash
pip install opencv-python mediapipe
▶️ Uso
Asegúrate de tener una cámara web conectada y funcional.

Ejecuta el script desde tu terminal:

-Bash
python hand.py
Se abrirá una ventana de OpenCV mostrando la imagen de tu cámara.
Muestra tus manos a la cámara para ver la detección y el reconocimiento de gestos.

-Controles
q: Presiona la tecla 'q' con la ventana de video seleccionada para cerrar la aplicación.
