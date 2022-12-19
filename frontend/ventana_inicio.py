import parametros as p
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import os
from PyQt5 import uic

window_name, base_class = window_name, base_class = uic.loadUiType(
    p.RUTA_UI_VENTANA_INICIO)


class VentanaInicio(window_name, base_class):

    senal_iniciar_juego = pyqtSignal()
    senal_rankings = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana Inicio")
        self.boton_jugar.clicked.connect(self.ingresar_juego)
        self.boton_ranking.clicked.connect(self.ingresar_ranking)

    def ingresar_juego(self):
        self.senal_iniciar_juego.emit()
        self.hide()

    def ingresar_ranking(self):
        self.senal_rankings.emit()
        self.hide()

    def mostrar_inicio(self):
        self.show()

    def ocultar_inicio(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana. mostrar_inicio()
    sys.exit(app.exec_())
