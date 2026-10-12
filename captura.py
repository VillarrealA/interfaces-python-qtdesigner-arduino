import sys
from datetime import datetime
from pathlib import Path

import serial
from PySide6.QtCore import QTimer
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_captura import Ui_MainWindow

PUERTO = "COM3"  # Cambiar por el puerto de Arduino.
BAUDIOS = 115200
CARPETA = Path(__file__).resolve().parent / "capturas"


class Ventana(QMainWindow):
    def __init__(self, puerto=PUERTO):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.puerto = puerto
        self.ser = None
        self.datos = bytearray()
        self.ui.txtDatos.setMaximumBlockCount(1000)
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.leer_serial)
        self.ui.btnCapturar.clicked.connect(self.alternar)

    def alternar(self):
        if self.ser is None:
            self.iniciar()
        else:
            self.detener()

    def iniciar(self):
        # Un fallo previo al guardar no debe borrar la captura.
        if self.datos and not self.guardar():
            return
        try:
            self.ser = serial.serial_for_url(
                self.puerto, baudrate=BAUDIOS, timeout=0)
        except (serial.SerialException, OSError, ValueError) as error:
            QMessageBox.warning(self, "Puerto serial", str(error))
            return
        self.datos.clear()
        self.ui.txtDatos.clear()
        self.ui.btnCapturar.setText("Detener")
        self.ui.lblEstado.setText(f"Capturando en {self.puerto}")
        self.timer.start()

    def recibir(self):
        # Una lectura breve de los bytes disponibles, sin esperar una línea.
        n = self.ser.in_waiting
        if n:
            bloque = self.ser.read(n)
            self.datos.extend(bloque)
            self.ui.txtDatos.moveCursor(QTextCursor.MoveOperation.End)
            self.ui.txtDatos.insertPlainText(
                bloque.decode("ascii", errors="replace"))
            self.ui.txtDatos.ensureCursorVisible()
            self.ui.lblEstado.setText(f"Recibidos: {len(self.datos)} bytes")

    def leer_serial(self):
        if self.ser is None:
            return
        try:
            self.recibir()
        except (serial.SerialException, OSError) as error:
            self.detener(lectura_final=False)
            QMessageBox.warning(self, "Conexión interrumpida", str(error))

    def detener(self, lectura_final=True):
        self.timer.stop()
        if self.ser is not None:
            try:
                if lectura_final:
                    self.recibir()
            except (serial.SerialException, OSError):
                pass  # Conservamos lo recibido antes de la desconexión.
            finally:
                self.ser.close()
                self.ser = None
        self.ui.btnCapturar.setText("Capturar")
        return self.guardar()

    def guardar(self):
        if not self.datos:
            self.ui.lblEstado.setText("Sin datos pendientes de guardar")
            return True
        nombre = datetime.now().strftime("captura_%Y%m%d_%H%M%S_%f.txt")
        try:
            CARPETA.mkdir(exist_ok=True)
            ruta = CARPETA / nombre
            ruta.write_bytes(self.datos)
        except OSError as error:
            QMessageBox.warning(self, "No se pudo guardar", str(error))
            return False  # Los bytes permanecen en memoria para reintentar.
        self.ui.lblEstado.setText(f"Guardado: {ruta.name}")
        self.datos.clear()
        return True

    def closeEvent(self, event):
        if self.detener():
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    puerto = sys.argv[1] if len(sys.argv) > 1 else PUERTO
    ventana = Ventana(puerto)
    ventana.show()
    sys.exit(app.exec())
