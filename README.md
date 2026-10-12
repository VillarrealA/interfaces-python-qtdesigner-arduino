# Interfaces con Qt Designer y captura de Arduino

Práctica de Instrumentación Biomédica: un botón en Tkinter, un formulario creado con Qt Widgets Designer y una aplicación Python que recibe datos seriales con pyserial.

## Archivos y función

| Archivo | Función |
|---|---|
| `tkinter_boton.py` | Primer ejemplo: ventana y botón escritos en Python. |
| `captura.ui` | Diseño editable en Qt Designer. |
| `ui_captura.py` | Código generado desde el diseño; se incluye para ejecutar directamente. |
| `captura.py` | Aplicación completa: crea la ventana, captura y guarda. |
| `demo_sin_arduino.py` | Ejecuta esa misma interfaz con datos sintéticos y eco serial local. |
| `arduino_emisor/arduino_emisor.ino` | Programa de Arduino: tiempo en ms y lectura de A0. |
| `requirements.txt` | Dependencias Python. |
| `.gitignore` | Excluye entornos, archivos temporales y capturas del control de versiones. |
| `.gitattributes` | Normaliza finales de línea de los archivos de texto. |

Equivalencias con los archivos anteriores: `captura.py` corresponde a `03_captura_serial.py`; `demo_sin_arduino.py` corresponde a `04_demo_sin_arduino.py`. Se omite el ejemplo intermedio `02_qt_boton.py`. Cada programa se ejecuta por separado.

## Instalación en Windows (CMD)

Descomprimir el paquete y abrir una terminal dentro de la carpeta del proyecto. Usar Python compatible con PySide6 (por ejemplo, Python 3.12 o 3.13).

```bat
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

En PowerShell la activación es `.\.venv\Scripts\Activate.ps1`. Si el equipo restringe ese script, usar CMD. En macOS/Linux crear con `python3 -m venv .venv` y activar con `source .venv/bin/activate`. Tkinter puede necesitar un paquete del sistema en Linux.

## 1. Ejemplo de Tkinter

```bat
python tkinter_boton.py
```

Pulsar el botón y observar el cambio de texto.

## 2. Edición visual

```bat
pyside6-designer captura.ui
```

En Designer, conservar estos nombres para que el programa encuentre los controles:

| Elemento | objectName |
|---|---|
| Formulario Main Window | `MainWindow` |
| Botón | `btnCapturar` |
| Plain Text Edit | `txtDatos` |
| Label | `lblEstado` |

Los textos visibles, fuentes y tamaños se pueden modificar. El área de texto tiene `readOnly=true` para impedir que el usuario escriba durante la captura. Esta propiedad no bloquea la edición del diseño.

El formulario usa un layout vertical. Para mover libremente los controles, seleccionar `centralwidget` en Object Inspector y elegir **Form > Break Layout**. Al terminar, aplicar **Lay Out Vertically** para recuperar la distribución automática. Si está abierta una vista previa, cerrarla y volver al editor; F3 activa Edit Widgets.

Después de guardar cualquier cambio:

```bat
pyside6-uic captura.ui -o ui_captura.py
```

Editar el aspecto en `captura.ui` y el comportamiento en `captura.py`. La conversión sobrescribe `ui_captura.py`, por lo que no se escriben funciones de captura en ese archivo.

## 3. Captura de Arduino

1. Abrir `arduino_emisor/arduino_emisor.ino` en el IDE de Arduino y cargarlo a la placa.
2. Para un Uno de 5 V, conectar un potenciómetro entre 5 V y GND con cursor a A0. Para otra placa respetar su tensión admisible. A0 sin conectar produce valores flotantes.
3. Cerrar el Monitor y el Plotter Serial antes de abrir Python.
4. Consultar el puerto y ejecutar (sustituir COM3 por el puerto real):

```bat
python -m serial.tools.list_ports
python captura.py COM3
```

El botón **Capturar** abre el puerto. **Detener** cierra la conexión y guarda un archivo en `capturas/`. Cerrar la ventana también intenta guardar. El programa Arduino y Python usan 115200 baudios.

No hay que ejecutar Tkinter ni otro programa antes. `captura.py` importa `Ui_MainWindow` desde `ui_captura.py` y conecta el botón con la función `alternar`.

## 4. Demostración sin Arduino

```bat
python demo_sin_arduino.py
```

Pulsar Capturar y Detener. El ejemplo escribe datos sintéticos en `loop://`, un puerto de eco local de pyserial. No hace falta conectar una placa. Esta demostración no verifica el cable ni el puerto USB físico.

## Alcance

Se capturan los bytes que la aplicación consigue leer mientras el puerto está abierto. Arduino transmite continuamente: el botón inicia la recepción en la computadora, no envía una orden a la placa. No recupera datos históricos. Algunas placas se reinician al abrir la conexión.

Un QTimer consulta el puerto cada 50 ms con lectura no bloqueante. Este intervalo no determina la frecuencia de muestreo del Arduino. La vista interpreta ASCII y conserva hasta 1000 bloques de texto, pero el archivo guarda todos los bytes acumulados. Una lectura puede contener parte de una línea.

Ejemplo docente para sesiones cortas y bajo caudal: los datos permanecen en memoria hasta guardar. Para registros largos conviene guardar durante la adquisición; para garantizar detección de pérdidas se requiere un protocolo apropiado. Se verificó el flujo con eco local, no con Arduino físico.

## Crear el repositorio Git

En la carpeta descomprimida:

```sh
git init
git add .
git commit -m "Agrega practica de Qt Designer y captura serial"
git branch -M main
```

Si Git solicita nombre y correo, configurar los propios antes del commit. El paquete no contiene un historial `.git` ni está publicado en un servicio remoto.

Para subirlo a un repositorio remoto nuevo y vacío, reemplazar `URL_DEL_REPOSITORIO` por su dirección real (sin inicializarlo allí con otro README):

```sh
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

Para cambios posteriores:

```sh
git status
git add .
git commit -m "Actualiza interfaz de captura"
git push
```

Tras modificar el formulario, regenerar `ui_captura.py` y versionar tanto el `.ui` como el `.py` generado. La carpeta `capturas/` queda excluida; no contiene código necesario para ejecutar la práctica.

## Documentación

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Qt Designer](https://doc.qt.io/qt-6/es/qtdesigner-manual.html)
- [Conversión de .ui a Python](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/uifiles.html)
- [pyserial](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)
