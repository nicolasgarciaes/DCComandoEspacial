import parametros as p
import sys
from PyQt5.QtCore import pyqtSignal, Qt, QRect, QUrl
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os
from PyQt5 import uic, QtMultimedia
sys.path.append("T2/..")


window_name, base_class = window_name, base_class = uic.loadUiType(
    p.RUTA_UI_VENTANA__POST_JUEGO)


class VentanaPostJuego(window_name, base_class):

    senal_comenzar_siguiente_nivel = pyqtSignal(tuple)
    senal_escribir_puntajes = pyqtSignal(tuple)
    senal_abrir_menu_principal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana Post Juego")
        self.boton_siguiente.clicked.connect(self.boton_siguiente_nivel)
        self.boton_salir.clicked.connect(self.boton_menu_principal)

    def inicar_post_juego(self):
        self.show()

    def info_post_juego(self, lista):
        self.nivel_actual = lista[0]
        balas_restantes = lista[1]
        estado_post_juego = lista[2]
        self.usuario = lista[3]
        self.nivel.setText(str(self.nivel_actual))
        self.balas.setText(str(balas_restantes))
        if not estado_post_juego:
            self.boton_siguiente.setEnabled(False)
            self.boton_siguiente.setText("No puedes pasar al siguiente nivel")
            self.label_estado_nivel.setText("No superaste el nivel!")
        if estado_post_juego:
            self.label_estado_nivel.setText("Superaste el nivel!")

    def setear_puntaje_total(self, puntaje_total):
        self.puntaje_total = puntaje_total
        self.label_valor_puntaje_total.setText(str(self.puntaje_total))

    def setear_puntaje_nivel(self, puntaje_nivel):
        self.puntaje_nivel = puntaje_nivel
        self.label_valor_puntaje_nivel.setText(str(self.puntaje_nivel))

    def setear_tiempo(self, tiempo):
        self.tiempo.setText(str(tiempo))

    def boton_siguiente_nivel(self):
        self.senal_comenzar_siguiente_nivel.emit(
            (self.puntaje_total, self.nivel_actual))
        self.hide()

    def boton_menu_principal(self):
        self.hide()
        self.senal_escribir_puntajes.emit((self.usuario, self.puntaje_total))
        self.senal_abrir_menu_principal.emit()
