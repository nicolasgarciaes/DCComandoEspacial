import parametros as p
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import os
from PyQt5 import uic
sys.path.append("T2/..")

window_name, base_class = window_name, base_class = uic.loadUiType(
    p.RUTA_UI_VENTANA_PRINCIPAL)


class VentanaPrincipal(window_name, base_class):

    senal_cazar_aqui = pyqtSignal(str)
    senal_volver_inicio = pyqtSignal()
    senal_enviar_nombre_y_mapa = pyqtSignal(tuple)
    senal_iniciar_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.mapa_actual = None

    def init_gui(self):
        self.setWindowTitle("Ventana Principal")
        self.boton_volver.clicked.connect(self.volver)
        self.lunar.clicked.connect(self.registrar_mapa)
        self.jupiter.clicked.connect(self.registrar_mapa)
        self.intergalactica.clicked.connect(self.registrar_mapa)
        self.boton_cazar.clicked.connect(self.enviar_nombre_y_mapa)

    def mostrar_principio(self):
        self.show()
        self.bool_mapa.hide()

    def volver(self):
        self.senal_volver_inicio.emit()
        self.hide()

    def registrar_mapa(self):
        if self.lunar.isChecked():
            self.mapa_actual = "Lunar"
        elif self.jupiter.isChecked():
            self.mapa_actual = "Jupiter"
        elif self.intergalactica.isChecked():
            self.mapa_actual = "Intergalactica"

    def enviar_nombre_y_mapa(self):
        nombre = self.nombre_astronauta.text()
        mapa = self.mapa_actual
        tupla = (nombre, mapa)
        self.senal_enviar_nombre_y_mapa.emit(tupla)

    def recibir_validacion(self, tupla):
        validacion_nombre = tupla[0]
        validacion_mapa = tupla[1]
        if validacion_nombre == False:
            self.nombre_astronauta.setText("")
            self.nombre_astronauta.setPlaceholderText("Usuario inválido")
        if validacion_mapa == False:
            self.bool_mapa.show()
        if validacion_mapa == True:
            self.bool_mapa.hide()
        if validacion_mapa == True and validacion_nombre == True:
            self.senal_iniciar_juego.emit()
            self.hide()
            self.nombre_astronauta.setText("")
