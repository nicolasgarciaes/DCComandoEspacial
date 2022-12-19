import parametros as p
from random import randint
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, QRect
import sys
sys.path.append("T2/..")


class Aliens(QObject):

    senal_pos_inicial_logica = pyqtSignal(list)
    senal_cambio_pos_aliens_logica_1 = pyqtSignal(tuple)
    senal_cambio_pos_aliens_logica_2 = pyqtSignal(tuple)
    senal_resetear_aliens = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.pos_inicial_x_1 = ""
        self.pos_inicial_y_1 = ""
        self.pos_inicial_x_2 = ""
        self.pos_inicial_y_2 = ""
        self.direccion_1 = p.VELOCIDAD_ALIEN_1
        self.instanciar_timers_aliens_1()
        self.direccion_2 = p.VELOCIDAD_ALIEN_2
        self.instanciar_timers_aliens_2()
        self.permiso_1 = True
        self.permiso_2 = True
        self.contador_muertes = 0
        self.contador_alien_muerto_1 = 0
        self.contador_alien_muerto_2 = 0

    def verificar_pos_inicial(self, tupla):
        pos_1 = tupla[0]
        pos_2 = tupla[1]
        lista_enviar = []
        estado = False
        if pos_1 != pos_2:
            estado = True
            lista_enviar.append(estado)
            lista_enviar.append(pos_1)
            lista_enviar.append(pos_2)
            self.senal_pos_inicial_logica.emit(lista_enviar)
        else:
            self.senal_pos_inicial_logica.emit(False)

    def guardar_pos_inicial_1(self, tupla):
        self.pos_inicial_x_1 = tupla[0][0]
        self.pos_inicial_y_1 = tupla[0][1]
        self.permiso_1 = True
        try:
            self.direccion_1 = self.direccion_anterior_1
            if self.contador_alien_muerto_1 == 1:
                self.velocidad_mapa_1()
        except AttributeError:
            pass

    def guardar_pos_inicial_2(self, tupla):
        self.pos_inicial_x_2 = tupla[1][0]
        self.pos_inicial_y_2 = tupla[1][1]
        self.permiso_2 = True
        try:
            self.direccion_2 = self.direccion_anterior_2
            if self.contador_alien_muerto_2 == 1:
                self.velocidad_mapa_2()
        except AttributeError:
            pass

    def mover_aliens_1(self):
        nueva_direccion_x_1 = self.direccion_1[0]
        nueva_direccion_y_1 = self.direccion_1[1]
        self.pos_inicial_x_1 += nueva_direccion_x_1
        self.pos_inicial_y_1 += nueva_direccion_y_1
        if self.pos_inicial_x_1 < p.BORDE_VERTICAL_IZQUIERDO_ALIENS and self.permiso_1:
            nueva_direccion_x_1 *= -1
            self.direccion_1 = (nueva_direccion_x_1, nueva_direccion_y_1)
        if self.pos_inicial_x_1 > p.BORDE_VERTICAL_DERECHO_ALIENS and self.permiso_1:
            nueva_direccion_x_1 *= -1
            self.direccion_1 = (nueva_direccion_x_1, nueva_direccion_y_1)
        if self.pos_inicial_y_1 > p.BORDE_HORIZONTAL_INFERIOR_ALIENS and self.permiso_1:
            nueva_direccion_y_1 *= -1
            self.direccion_1 = (nueva_direccion_x_1, nueva_direccion_y_1)
        if self.pos_inicial_y_1 < p.BORDE_HORIZONTAL_SUPERIOR_ALIENS and self.permiso_1:
            nueva_direccion_y_1 *= -1
            self.direccion_1 = (nueva_direccion_x_1, nueva_direccion_y_1)
        self.senal_cambio_pos_aliens_logica_1.emit(
            (self.pos_inicial_x_1, self.pos_inicial_y_1))

    def mover_aliens_2(self):
        nueva_direccion_x_2 = self.direccion_2[0]
        nueva_direccion_y_2 = self.direccion_2[1]
        self.pos_inicial_x_2 += nueva_direccion_x_2
        self.pos_inicial_y_2 += nueva_direccion_y_2
        if self.pos_inicial_x_2 < p.BORDE_VERTICAL_IZQUIERDO_ALIENS and self.permiso_2:
            nueva_direccion_x_2 *= -1
            self.direccion_2 = (nueva_direccion_x_2, nueva_direccion_y_2)
        if self.pos_inicial_x_2 > p.BORDE_VERTICAL_DERECHO_ALIENS and self.permiso_2:
            nueva_direccion_x_2 *= -1
            self.direccion_2 = (nueva_direccion_x_2, nueva_direccion_y_2)
        if self.pos_inicial_y_2 > p.BORDE_HORIZONTAL_INFERIOR_ALIENS and self.permiso_2:
            nueva_direccion_y_2 *= -1
            self.direccion_2 = (nueva_direccion_x_2, nueva_direccion_y_2)
        if self.pos_inicial_y_2 < p.BORDE_HORIZONTAL_SUPERIOR_ALIENS and self.permiso_2:
            nueva_direccion_y_2 *= -1
            self.direccion_2 = (nueva_direccion_x_2, nueva_direccion_y_2)
        self.senal_cambio_pos_aliens_logica_2.emit(
            (self.pos_inicial_x_2, self.pos_inicial_y_2))

    def instanciar_timers_aliens_1(self):
        self.timer_aparecer_1 = QTimer()
        self.timer_aparecer_1.setInterval(100)
        self.timer_aparecer_1.timeout.connect(self.mover_aliens_1)

    def instanciar_timers_aliens_2(self):
        self.timer_aparecer_2 = QTimer()
        self.timer_aparecer_2.setInterval(100)
        self.timer_aparecer_2.timeout.connect(self.mover_aliens_2)

    def iniciar_timers_1(self, estado):
        if estado:
            self.timer_aparecer_1.start()

    def iniciar_timers_2(self, estado):
        if estado:
            self.timer_aparecer_2.start()

    def instanciar_timers_aliens_1_muerte(self):
        self.timer_muerte_1 = QTimer()
        self.timer_muerte_1.setSingleShot(True)
        self.timer_muerte_1.setInterval(1000)
        self.timer_muerte_1.timeout.connect(self.mov_alien_muerto_1)

    def instanciar_timers_aliens_2_muerte(self):
        self.timer_muerte_2 = QTimer()
        self.timer_muerte_2.setSingleShot(True)
        self.timer_muerte_2.setInterval(1000)
        self.timer_muerte_2.timeout.connect(self.mov_alien_muerto_2)

    def alien_muerto_1(self):
        self.instanciar_timers_aliens_1_muerte()
        self.timer_muerte_1.start()
        self.direccion_anterior_1 = self.direccion_1
        self.contador_alien_muerto_1 += 1
        self.direccion_1 = (0, 0)

    def mov_alien_muerto_1(self):
        self.direccion_1 = (0, 30)
        self.permiso_1 = False
        self.controlar_estado_aliens()

    def alien_muerto_2(self):
        self.instanciar_timers_aliens_2_muerte()
        self.timer_muerte_2.start()
        self.direccion_anterior_2 = self.direccion_2
        self.contador_alien_muerto_2 += 1
        self.direccion_2 = (0, 0)

    def mov_alien_muerto_2(self):
        self.direccion_2 = (0, 30)
        self.permiso_2 = False
        self.controlar_estado_aliens()

    def instanciar_timers_ambos_aliens_muertos(self):
        self.timer_muerte_general = QTimer()
        self.timer_muerte_general.setSingleShot(True)
        self.timer_muerte_general.setInterval(2000)
        self.timer_muerte_general.timeout.connect(
            self.envio_senales_front_reset_aliens)

    def controlar_estado_aliens(self):
        if (self.permiso_2 == False) and (self.permiso_1 == False):
            self.contador_muertes += 1
            self.instanciar_timers_ambos_aliens_muertos()
            self.timer_muerte_general.start()

    def envio_senales_front_reset_aliens(self):
        self.senal_resetear_aliens.emit(self.contador_muertes)

    def resetear_aliens(self):
        self.contador_muertes = 0
        self.contador_alien_muerto_1 = 1
        self.contador_alien_muerto_2 = 1

    def recibir_pausa_aliens(self):
        self.timer_aparecer_1.stop()
        self.timer_aparecer_2.stop()

    def terminar_pausa_aliens(self):
        self.timer_aparecer_1.start()
        self.timer_aparecer_2.start()

    def ponderador_aliens(self, mapa):
        self.mapa_actual = mapa
        if self.mapa_actual == "Lunar":
            self.ponderador = p.PONDERADOR_TUTORIAL
            self.velocidad_mapa_1()
            self.velocidad_mapa_2()
        if self.mapa_actual == "Jupiter":
            self.ponderador = p.PONDERADOR_ENTRENAMIENTO
            self.velocidad_mapa_1()
            self.velocidad_mapa_2()
        if self.mapa_actual == "Intergalactica":
            self.ponderador = p.PONDERADOR_INVASION
            self.velocidad_mapa_1()
            self.velocidad_mapa_2()

    def velocidad_mapa_1(self):
        direccion_1_x = self.direccion_1[0]
        direccion_1_y = self.direccion_1[1]
        direccion_1_x = float(direccion_1_x) / self.ponderador
        direccion_1_y = float(direccion_1_y) / self.ponderador
        self.direccion_1 = (direccion_1_x, direccion_1_y)

    def velocidad_mapa_2(self):
        direccion_2_x = self.direccion_2[0]
        direccion_2_y = self.direccion_2[1]
        direccion_2_x = float(direccion_2_x) / self.ponderador
        direccion_2_y = float(direccion_2_y) / self.ponderador
        self.direccion_2 = (direccion_2_x, direccion_2_y)

    def cheat_code_cia(self):
        self.direccion_anterior_1 = self.direccion_1
        self.direccion_anterior_2 = self.direccion_2
