# Scanner QR/Código de Barras 📷

Aplicación en Python para escanear códigos QR y códigos de barras en tiempo real utilizando la cámara web.

## 📋 Descripción

Este proyecto utiliza OpenCV y Pyzbar para detectar y decodificar códigos QR y códigos de barras a través de la cámara web en tiempo real. La aplicación muestra un rectángulo alrededor del código detectado y despliega la información decodificada directamente en la pantalla.

## 🚀 Características

- ✅ Lectura en tiempo real de códigos QR y códigos de barras
- ✅ Detección automática y resaltado visual del código
- ✅ Decodificación del contenido del código
- ✅ Visualización de datos en pantalla
- ✅ Soporte para múltiples formatos de códigos de barras

## 🛠️ Requisitos

- Python 3.12 o superior
- Cámara web funcional

## 📦 Dependencias

Las dependencias del proyecto están listadas en `requirements.txt`:

```
opencv-python==4.12.0.88
numpy==2.3.5
pyzbar==0.1.9
```

## 💻 Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone git@github.com:alexgrt5/Scanner-QR.git
   cd Scanner-QR
   ```

2. **Crear un entorno virtual (recomendado):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Instalar Zbar (requerido para pyzbar):**

   En Linux (Ubuntu/Debian):

   ```bash
   sudo apt-get install libzbar0
   ```

   En macOS:

   ```bash
   brew install zbar
   ```

   En Windows:

   - Descargar e instalar desde [ZBar para Windows](http://zbar.sourceforge.net/)

## 🎮 Uso

1. **Ejecutar la aplicación:**

   ```bash
   python3 scanner.py
   ```

2. **Usar el scanner:**

   - La aplicación abrirá una ventana mostrando la transmisión de la cámara web
   - Apunta la cámara hacia un código QR o código de barras
   - El código será detectado automáticamente y mostrado en pantalla
   - El contenido decodificado aparecerá tanto en la consola como en la ventana

3. **Salir:**
   - Presiona la tecla `q` para cerrar la aplicación

## 📝 Código de Ejemplo

```python
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

# Acceder a la camara web
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# Lectura de marcos
while True:
    ret,frame = cap.read()

    # Lectura de datos del código de barras
    for barcode in decode(frame):
        myData = barcode.data.decode('utf-8')
        print(myData)
```

## 🔧 Configuración

El código está configurado con una resolución de cámara de 640x480 píxeles. Puedes modificar estos valores en las líneas:

```python
cap.set(3,640)  # Ancho
cap.set(4,480)  # Alto
```

## 🐛 Solución de Problemas

### Error: "Could not find the Qt platform plugin"

Este es un warning que no afecta la funcionalidad. Si deseas suprimirlo, ejecuta:

```bash
export QT_QPA_PLATFORM=xcb
python3 scanner.py
```

### La cámara no se detecta

- Verifica que tu cámara web esté conectada y funcionando
- Prueba cambiar el índice de la cámara: `cv.VideoCapture(1)` o `cv.VideoCapture(2)`

### Error al decodificar el código

- Asegúrate de que el código QR/código de barras sea legible
- Mejora la iluminación
- Acerca o aleja la cámara para mejorar el enfoque

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 👤 Autor

**alexgrt5**

- GitHub: [@alexgrt5](https://github.com/alexgrt5)
- Email: alexgrt1703@gmail.com

## 🙏 Agradecimientos

- [OpenCV](https://opencv.org/) - Librería de visión por computadora
- [Pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) - Wrapper de Python para ZBar
- [NumPy](https://numpy.org/) - Librería de computación científica

---

**Creado por alexgrt5** 🚀
