import parametros as p
from random import randint
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, QRect
import sys
sys.path.append("T2/..")


class Mira(QObject):

    senal_cambio_mov = pyqtSignal(tuple)
    senal_disparo = pyqtSignal(str)
    senal_disparo_original = pyqtSignal(str)
    senal_enviar_balas_usadas = pyqtSignal(int)
    senal_sin_balas = pyqtSignal(bool)
    senal_enviar_sonido = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.pos_x = 475
        self.pos_y = 350
        self.velocidad = 15
        self.disparo = False
        self.cantidad_balas = 0

    def recibir_balas(self, nivel):
        self.cantidad_balas = nivel[1]

    def logica_mover_mira(self, event):
        if event == "left":  # Apreto la A
            self.pos_x -= self.velocidad
        elif event == "up":  # Apreto la W
            self.pos_y -= self.velocidad
        elif event == "right":  # Apreto la D
            self.pos_x += self.velocidad
        elif event == "down":  # Apreto la S
            self.pos_y += self.velocidad
        if self.pos_x < p.BORDE_VERTICAL_IZQUIERDO:
            self.pos_x = p.BORDE_VERTICAL_IZQUIERDO
        if self.pos_x > p.BORDE_VERTICAL_DERECHO:
            self.pos_x = p.BORDE_VERTICAL_DERECHO
        if self.pos_y > p.BORDE_HORIZONTAL_INFERIOR:
            self.pos_y = p.BORDE_HORIZONTAL_INFERIOR
        if self.pos_y < p.BORDE_HORIZONTAL_SUPERIOR:
            self.pos_y = p.BORDE_HORIZONTAL_SUPERIOR
        elif event == "k":
            self.disparar()
        self.senal_cambio_mov.emit((self.pos_x, self.pos_y))

    def disparar(self):
        ruta_disparo = p.RUTA_MIRA_DISPARO
        self.senal_disparo.emit(ruta_disparo)
        self.instanciar_timers_mira()
        self.timer_mira.start()
        self.cantidad_balas -= 1
        self.senal_enviar_balas_usadas.emit(self.cantidad_balas)
        self.senal_enviar_sonido.emit()
        if self.cantidad_balas == 0:
            self.senal_sin_balas.emit(True)

    def mira_original(self):
        ruta_mira_orignal = p.RUTA_MIRA
        self.senal_disparo_original.emit(ruta_mira_orignal)

    def instanciar_timers_mira(self):
        self.timer_mira = QTimer()
        self.timer_mira.setInterval(1000)
        self.timer_mira.timeout.connect(self.mira_original)

    def recibir_cheat_code_balas(self):
        self.cantidad_balas = 10000
