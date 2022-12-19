import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal
import sys
sys.path.append("T2/..")


class LogicaPrincipio(QObject):

    senal_respuesta_validacion = pyqtSignal(tuple)
    senal_usuario_y_mapa = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

    def comprobar_nombre_y_mapa(self, tupla):
        nombre = tupla[0]
        mapa = tupla[1]
        estado_nombre = False
        estado_mapa = False
        if mapa != None:
            if nombre == "":
                estado_nombre = False
                estado_mapa = True
                tupla_estados = (estado_nombre, estado_mapa)
                self.senal_respuesta_validacion.emit(tupla_estados)
            elif nombre.isalnum() == False:
                estado_nombre = False
                estado_mapa = True
                tupla_estados = (estado_nombre, estado_mapa)
                self.senal_respuesta_validacion.emit(tupla_estados)
            elif nombre != "" and nombre.isalnum():
                estado_nombre = True
                estado_mapa = True
                estado_juego = True
                tupla_estados = (estado_nombre, estado_mapa)

                tupla_nombre_y_juego = (nombre, mapa)
                self.senal_usuario_y_mapa.emit(tupla_nombre_y_juego)
                self.senal_respuesta_validacion.emit(tupla_estados)

        else:
            if nombre == "":
                estado_nombre = False
                estado_mapa = False
                tupla_estados = (estado_nombre, estado_mapa)
                self.senal_respuesta_validacion.emit(tupla_estados)
            elif nombre.isalnum() == False:
                estado_nombre = False
                estado_mapa = False
                tupla_estados = (estado_nombre, estado_mapa)
                self.senal_respuesta_validacion.emit(tupla_estados)
            elif nombre != "" and nombre.isalnum():
                estado_nombre = True
                estado_mapa = False
                tupla_estados = (estado_nombre, estado_mapa)
                self.senal_respuesta_validacion.emit(tupla_estados)
