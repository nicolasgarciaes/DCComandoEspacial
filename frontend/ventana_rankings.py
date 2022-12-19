import parametros as p
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import os
from PyQt5 import uic
sys.path.append("T2/..")

window_name_main, base_class_main = uic.loadUiType(p.RUTA_UI_VENTANA_RANKINGS)


class VentanaRankings(window_name_main, base_class_main):

    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Rankings")
        self.boton_volver.clicked.connect(self.volver)

    def mostrar_rankings(self):
        self.top5()
        self.show()

    def volver(self):
        self.senal_volver_inicio.emit()
        self.hide()

    def crear_rankings(self):
        with open("puntajes.txt", "r") as lista_puntajes:
            jugadores_desordenados = {}
            lineas = lista_puntajes.readlines()
            for linea in lineas:
                jugadores_desordenados[linea.strip().split(
                    ",")[0]] = int(linea.strip().split(",")[1])
            jugadores_previo_orden = sorted(
                jugadores_desordenados, key=jugadores_desordenados.get)
            jugadores_listos = {}
            for puntaje in jugadores_previo_orden[::-1]:
                jugadores_listos[puntaje] = jugadores_desordenados[puntaje]
            if len(jugadores_listos) > 5:
                nombres = []
                puntajes = []
                contador_jugadores = 0
                contador_puntajes = 0
                for jugador in jugadores_listos:
                    if contador_jugadores < 5:
                        nombres.append(jugador)
                        contador_jugadores += 1
                for puntaje in jugadores_listos.values():
                    if contador_puntajes < 5:
                        puntajes.append(puntaje)
                        contador_puntajes += 1
            else:
                nombres = []
                puntajes = []
                for jugador in jugadores_listos:
                    nombres.append(jugador)

                for puntaje in jugadores_listos.values():
                    puntajes.append(puntaje)
        return nombres, puntajes
        # nombres me retorna los nombres ordenados de la lista de jugadores ordenada
        # puntajes me retorna la lista de puntajes ordenados de la lista de jugadores ordenada

    def top5(self):
        nombres_top5 = self.crear_rankings()[0]
        puntajes_top5 = self.crear_rankings()[1]
        try:
            self.label_top1.setText(
                f"1:  {nombres_top5[0]}   {str(puntajes_top5[0])}")
            self.label_top2.setText(
                f"2:  {nombres_top5[1]}   {str(puntajes_top5[1])}")
            self.label_top3.setText(
                f"3:  {nombres_top5[2]}   {str(puntajes_top5[2])}")
            self.label_top4.setText(
                f"4:  {nombres_top5[3]}   {str(puntajes_top5[3])}")
            self.label_top5.setText(
                f"5:  {nombres_top5[4]}   {str(puntajes_top5[4])}")
        except IndexError:
            pass

    def escribir_puntajes(self, info):
        nombre = info[0]
        puntaje = str(info[1])
        with open("puntajes.txt", "a", encoding="utf-8") as lista_puntajes:
            lista_puntajes.write("\n")
            lista_puntajes.write(nombre)
            lista_puntajes.write(",")
            lista_puntajes.write(puntaje)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaRankings()
    ventana.crear_rankings()
    ventana.top5()
    ventana.show()
    sys.exit(app.exec_())
