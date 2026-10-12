"""Demostración de la interfaz con eco serial local, sin placa Arduino."""
import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from captura import Ventana

app = QApplication(sys.argv)
ventana = Ventana("loop://")
ventana.setWindowTitle("DEMO SIN ARDUINO: eco serial local")
contador = 0


def emitir():
    global contador
    if ventana.ser is not None:
        valor = 400 + (contador % 100)
        ventana.ser.write(f"{contador * 100},{valor}\r\n".encode("ascii"))
        contador += 1


emisor = QTimer()
emisor.timeout.connect(emitir)
emisor.start(100)
ventana.show()
sys.exit(app.exec())
