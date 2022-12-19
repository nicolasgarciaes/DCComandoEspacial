from attr import Attribute
import parametros as p
from random import randint
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, QRect
import sys
sys.path.append("T2/..")


class Juego(QObject):

    senal_disparo_acertado_f1_1 = pyqtSignal(str)
    senal_disparo_acertado_f2_1 = pyqtSignal(str)
    senal_disparo_acertado_f3_1 = pyqtSignal(str)
    senal_disparo_acertado_f1_2 = pyqtSignal(str)
    senal_disparo_acertado_f2_2 = pyqtSignal(str)
    senal_disparo_acertado_f3_2 = pyqtSignal(str)
    senal_disparo_original_1 = pyqtSignal(str)
    senal_disparo_original_2 = pyqtSignal(str)
    senal_pos_disparo_1 = pyqtSignal(tuple)
    senal_pos_disparo_2 = pyqtSignal(tuple)
    senal_post_nivel = pyqtSignal()
    senal_termino_juego = pyqtSignal()
    senal_animacion_perro = pyqtSignal()
    senal_nivel_superado = pyqtSignal()
    senal_murio_alien = pyqtSignal(int)
    senal_info_post_nivel = pyqtSignal(tuple)
    senal_enviar_tiempo = pyqtSignal(int)
    senal_envio_puntaje = pyqtSignal(int)
    senal_enviar_tiempo_post_juego = pyqtSignal(int)
    senal_envio_puntaje_total = pyqtSignal(int)
    senal_enviar_tiempo_inicial = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.pos_alien_1 = ()
        self.pos_alien_2 = ()
        self.pos_mira = ()
        self.estado_alien_1 = True
        self.estado_alien_2 = True
        self.aliens_muertos = 0
        self.mira_rect_backend = QRect(475, 350, 25, 25)
        self.puntaje_total = 0

    def disparo_mira_alien_1(self, coords):
        self.alien_1_rect_backend = QRect(*coords)

    def disparo_mira_alien_2(self, coords):
        self.alien_2_rect_backend = QRect(*coords)

    def disparo_mira(self, coords):
        self.mira_rect_backend = QRect(*coords)

    def check_estado_aliens(self):
        self.estado_alien_1 = True
        self.estado_alien_2 = True

    def revisar_disparo(self, disparo):
        if disparo == "k":
            if self.mira_rect_backend.intersects(self.alien_1_rect_backend) and self.estado_alien_1:
                self.aliens_muertos += 1
                self.senal_pos_disparo_1.emit(
                    self.alien_1_rect_backend.getRect())
                self.disparo_acertado_f1_1()
                self.estado_alien_1 = False
                self.check_aliens_muertos()
                self.senal_murio_alien.emit(self.aliens_muertos)

            if self.mira_rect_backend.intersects(self.alien_2_rect_backend) and self.estado_alien_2:
                self.aliens_muertos += 1
                self.senal_pos_disparo_2.emit(
                    self.alien_2_rect_backend.getRect())
                self.disparo_acertado_f1_2()
                self.estado_alien_2 = False
                self.check_aliens_muertos()
                self.senal_murio_alien.emit(self.aliens_muertos)

    def disparo_acertado_f1_1(self):
        ruta_disparo = p.RUTA_DISPARO_FASE_1
        self.senal_disparo_acertado_f1_1.emit(ruta_disparo)
        self.instanciar_timers_disparos_1()
        self.timer_disparo_alien_f1_1.start()

    def disparo_acertado_f2_1(self):
        ruta_disparo = p.RUTA_DISPARO_FASE_2
        self.senal_disparo_acertado_f2_1.emit(ruta_disparo)
        self.timer_disparo_alien_f2_1.start()

    def disparo_acertado_f3_1(self):
        ruta_disparo = p.RUTA_DISPARO_FASE_3
        self.senal_disparo_acertado_f3_1.emit(ruta_disparo)
        self.timer_disparo_alien_f3_1.start()

    def disparo_original_1(self):
        ruta_disparo_original = ""
        self.senal_disparo_original_1.emit(ruta_disparo_original)

    def disparo_acertado_f1_2(self):
        ruta_disparo = p.RUTA_DISPARO_FASE_1
        self.senal_disparo_acertado_f1_2.emit(ruta_disparo)
        self.instanciar_timers_disparos_2()
        self.timer_disparo_alien_f1_2.start()

    def disparo_acertado_f2_2(self):
        ruta_disparo = p.RUTA_DISPARO_FASE_2
        self.senal_disparo_acertado_f2_2.emit(ruta_disparo)
        self.timer_disparo_alien_f2_2.start()

    def disparo_acertado_f3_2(self):
        ruta_disparo = p.RUTA_DISPARO_FASE_3
        self.senal_disparo_acertado_f3_2.emit(ruta_disparo)
        self.timer_disparo_alien_f3_2.start()

    def disparo_original_2(self):
        ruta_disparo_original = ""
        self.senal_disparo_original_2.emit(ruta_disparo_original)

    def instanciar_timers_disparos_1(self):
        self.timer_disparo_alien_f1_1 = QTimer()
        self.timer_disparo_alien_f1_1.setSingleShot(True)
        self.timer_disparo_alien_f1_1.setInterval(500)
        self.timer_disparo_alien_f1_1.timeout.connect(
            self.disparo_acertado_f2_1)
        self.timer_disparo_alien_f2_1 = QTimer()
        self.timer_disparo_alien_f2_1.setSingleShot(True)
        self.timer_disparo_alien_f2_1.setInterval(500)
        self.timer_disparo_alien_f2_1.timeout.connect(
            self.disparo_acertado_f3_1)
        self.timer_disparo_alien_f3_1 = QTimer()
        self.timer_disparo_alien_f3_1.setSingleShot(True)
        self.timer_disparo_alien_f3_1.setInterval(500)
        self.timer_disparo_alien_f3_1.timeout.connect(self.disparo_original_1)

    def instanciar_timers_disparos_2(self):
        self.timer_disparo_alien_f1_2 = QTimer()
        self.timer_disparo_alien_f1_2.setSingleShot(True)
        self.timer_disparo_alien_f1_2.setInterval(500)
        self.timer_disparo_alien_f1_2.timeout.connect(
            self.disparo_acertado_f2_2)
        self.timer_disparo_alien_f2_2 = QTimer()
        self.timer_disparo_alien_f2_2.setSingleShot(True)
        self.timer_disparo_alien_f2_2.setInterval(500)
        self.timer_disparo_alien_f2_2.timeout.connect(
            self.disparo_acertado_f3_2)
        self.timer_disparo_alien_f3_2 = QTimer()
        self.timer_disparo_alien_f3_2.setSingleShot(True)
        self.timer_disparo_alien_f3_2.setInterval(500)
        self.timer_disparo_alien_f3_2.timeout.connect(self.disparo_original_2)

    def setear_aliens_y_balas(self, tupla):
        self.aliens_nivel = tupla[0]
        self.balas_nivel = tupla[1]
        self.nivel_actual = tupla[2]

    def instanciar_timers_fin_nivel(self):
        self.timer_termino_nivel = QTimer()
        self.timer_termino_nivel.setSingleShot(True)
        self.timer_termino_nivel.setInterval(p.TIEMPO_TERMINATOR_DOG)
        self.timer_termino_nivel.timeout.connect(self.termino_juego_win)

    def termino_juego_win(self):
        try:
            self.estado_post_juego = True
            info_post_nivel = (self.nivel_actual,
                               self.balas_restantes, self.estado_post_juego, self.usuario_actual)
            self.senal_info_post_nivel.emit(info_post_nivel)
            self.enviar_info_post_juego(True)
            self.senal_post_nivel.emit()
            self.senal_termino_juego.emit()
        except AttributeError:
            self.estado_post_juego = True
            self.balas_restantes = self.nivel_actual * 4
            info_post_nivel = (self.nivel_actual,
                               self.balas_restantes, self.estado_post_juego, self.usuario_actual)
            self.senal_info_post_nivel.emit(info_post_nivel)
            self.enviar_info_post_juego(True)
            self.senal_post_nivel.emit()
            self.senal_termino_juego.emit()

    def check_aliens_muertos(self):
        if self.aliens_muertos == self.aliens_nivel:
            self.senal_animacion_perro.emit()
            self.senal_nivel_superado.emit()
            self.instanciar_timers_fin_nivel()
            self.timer_tiempo.stop()
            self.timer_termino_nivel.start()

    def check_balas(self):
        if self.aliens_muertos == self.aliens_nivel:
            self.check_aliens_muertos()
        elif self.aliens_muertos < self.aliens_nivel:
            self.estado_post_juego = False
            info_post_nivel = (self.nivel_actual,
                               self.balas_restantes, self.estado_post_juego, self.usuario_actual)
            self.senal_info_post_nivel.emit(info_post_nivel)
            self.enviar_info_post_juego(False)
            self.timer_tiempo.stop()
            self.senal_post_nivel.emit()
            self.senal_termino_juego.emit()

    def recibir_balas_restantes(self, balas):
        self.balas_restantes = balas

    def recibir_usuario(self, usuario):
        self.usuario_actual = usuario

    def recibir_ponderador(self, mapa):
        self.mapa_actual = mapa
        if self.mapa_actual == "Lunar":
            self.ponderador = p.PONDERADOR_TUTORIAL
        if self.mapa_actual == "Jupiter":
            self.ponderador = p.PONDERADOR_ENTRENAMIENTO
        if self.mapa_actual == "Intergalactica":
            self.ponderador = p.PONDERADOR_INVASION

    def enviar_info_post_juego(self, estado):
        try:
            if estado:
                puntaje_nivel = int(((self.aliens_muertos * 100) +
                                     (self.tiempo * 30 + self.balas_restantes * 70)
                                     * self.nivel_actual) / self.ponderador)
                self.puntaje_total += puntaje_nivel
                self.senal_envio_puntaje.emit(puntaje_nivel)
                self.senal_envio_puntaje_total.emit(self.puntaje_total)
            else:
                self.senal_envio_puntaje.emit(0)
                self.senal_envio_puntaje_total.emit(self.puntaje_total)
        except AttributeError:
            if estado:
                self.balas_restantes = self.nivel_actual * 4
                puntaje_nivel = int(((self.aliens_muertos * 100) +
                                     (self.tiempo * 30 + self.balas_restantes * 70)
                                     * self.nivel_actual) / self.ponderador)
                self.puntaje_total += puntaje_nivel
                self.senal_envio_puntaje.emit(puntaje_nivel)
                self.senal_envio_puntaje_total.emit(self.puntaje_total)
            else:
                self.senal_envio_puntaje.emit(0)
                self.senal_envio_puntaje_total.emit(self.puntaje_total)

        self.senal_enviar_tiempo_post_juego.emit(self.tiempo)

    def resetar_nivel_nuevo(self):
        self.aliens_muertos = 0

    def recibir_pausa(self):
        self.timer_tiempo.stop()
        try:
            self.timer_disparo_alien_f1_1.stop()
            self.timer_disparo_alien_f1_2.stop()
            self.timer_disparo_alien_f2_1.stop()
            self.timer_disparo_alien_f2_2.stop()
            self.timer_disparo_alien_f3_1.stop()
            self.timer_disparo_alien_f3_2.stop()
        except AttributeError:
            pass

    def terminar_pausa(self):
        self.timer_tiempo.start()
        try:
            self.timer_disparo_alien_f1_1.start()
            self.timer_disparo_alien_f1_2.start()
            self.timer_disparo_alien_f2_1.start()
            self.timer_disparo_alien_f2_2.start()
            self.timer_disparo_alien_f3_1.start()
            self.timer_disparo_alien_f3_2.start()
        except AttributeError:
            pass

    def cheat_code_ovni_logica(self):
        self.balas_nivel = 10000

    def cheat_code_cia_logica(self):
        self.senal_animacion_perro.emit()
        self.senal_nivel_superado.emit()
        self.instanciar_timers_fin_nivel()
        self.timer_tiempo.stop()
        self.timer_termino_nivel.start()

    def disminuir_tiempo(self):
        self.tiempo -= 1
        self.senal_enviar_tiempo.emit(self.tiempo)
        self.revisar_tiempo()

    def instanciar_timers_tiempo(self):
        self.timer_tiempo = QTimer()
        self.timer_tiempo.setInterval(1000)
        self.timer_tiempo.timeout.connect(self.disminuir_tiempo)
        self.timer_tiempo.start()

    def tiempo_nivel(self, contador_tiempo):
        if contador_tiempo == 0:
            self.tiempo = p.DURACION_NIVEL_INICIAL * self.ponderador
            self.tiempo_nivel_anterior = self.tiempo
            self.senal_enviar_tiempo_inicial.emit(self.tiempo)
        elif contador_tiempo >= 1:
            self.tiempo = self.tiempo_nivel_anterior * self.ponderador
            self.tiempo_nivel_anterior = self.tiempo
            self.senal_enviar_tiempo_inicial.emit(self.tiempo)

    def tiempo_desde_el_comienzo(self):
        self.tiempo_nivel_anterior = p.DURACION_NIVEL_INICIAL

    def revisar_tiempo(self):
        if self.tiempo == 0.0 and self.aliens_muertos < self.aliens_nivel:
            try:
                self.estado_post_juego = False
                info_post_nivel = (self.nivel_actual,
                                   self.balas_restantes, self.estado_post_juego,
                                   self.usuario_actual)
                self.senal_info_post_nivel.emit(info_post_nivel)
                self.enviar_info_post_juego(False)
                self.timer_tiempo.stop()
                self.senal_post_nivel.emit()
                self.senal_termino_juego.emit()
            except AttributeError:
                self.balas_restantes = self.nivel_actual * 4
                self.estado_post_juego = False
                info_post_nivel = (self.nivel_actual,
                                   self.balas_restantes, self.estado_post_juego,
                                   self.usuario_actual)
                self.senal_info_post_nivel.emit(info_post_nivel)
                self.enviar_info_post_juego(False)
                self.timer_tiempo.stop()
                self.senal_post_nivel.emit()
                self.senal_termino_juego.emit()
