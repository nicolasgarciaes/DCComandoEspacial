from random import randint
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
    p.RUTA_UI_VENTANA_JUEGOS)


class VentanaJuegos(window_name, base_class):

    senal_mover_mira = pyqtSignal(str)
    senal_pos_aliens = pyqtSignal(tuple)
    senal_pos_inicial_aliens = pyqtSignal(tuple)
    senal_cambio_pos_aliens = pyqtSignal(tuple)
    senal_comenzar_a_mover_aliens_1 = pyqtSignal(bool)
    senal_comenzar_a_mover_aliens_2 = pyqtSignal(bool)
    senal_enviar_alien_1 = pyqtSignal(tuple)
    senal_enviar_alien_2 = pyqtSignal(tuple)
    senal_enviar_mira = pyqtSignal(tuple)
    senal_enviar_nivel_actual = pyqtSignal(int)
    senal_enviar_aliens_y_balas = pyqtSignal(tuple)
    senal_enviar_alien_muerto_1 = pyqtSignal()
    senal_enviar_alien_muerto_2 = pyqtSignal()
    senal_aliens_vivos = pyqtSignal()
    senal_enviar_usuario = pyqtSignal(str)
    senal_comenzar_tiempo = pyqtSignal(int)
    senal_enviar_ponderador = pyqtSignal(str)
    senal_nuevo_nivel = pyqtSignal()
    senal_pausa_logica = pyqtSignal()
    senal_termino_pausa = pyqtSignal()
    senal_escribir_puntajes_desde_juego = pyqtSignal(tuple)
    senal_abrir_menu_desde_juego = pyqtSignal()
    senal_cheat_code_ovni = pyqtSignal()
    senal_cheat_code_cia = pyqtSignal()
    senal_contador_de_tiempo = pyqtSignal(int)
    senal_tiempo_desde_0 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.ruta_alien = ""
        self.mapa_elegido = ""
        self.nivel_actual = 1
        self.estado_pausa = False
        self.puntaje_total = 0
        self.teclas_apretadas = []
        self.contador_tiempo = 0

    def init_gui(self):
        self.setWindowTitle("Ventana Juego")
        self.boton_pausa.clicked.connect(self.comenzar_pausa)
        self.boton_despausar.clicked.connect(self.terminar_pausa)
        self.boton_salir.clicked.connect(self.salir)

    def generar_mira(self):
        self.mira_juego.setPixmap(QPixmap(p.RUTA_MIRA))
        self.mira_juego.setScaledContents(True)
        self.mira_juego.raise_()
        self.mira_juego_rect = QRect(*p.MEDIDAS_MIRA_QRECT)

    def posicion_inicial_aliens(self):
        pos_alien_1 = (randint(50, 900), randint(50, 450))
        pos_alien_2 = (randint(50, 900), randint(50, 450))
        tupla = ((pos_alien_1), (pos_alien_2))
        self.senal_pos_aliens.emit(tupla)
        self.senal_aliens_vivos.emit()

    def generar_aliens(self, pos_verificadas):
        if pos_verificadas[0]:
            self.label_alien_1.setPixmap(QPixmap(self.ruta_alien))
            self.label_alien_1.setGeometry(
                pos_verificadas[1][0], pos_verificadas[1][1], p.WIDTH_ALIEN, p.HEIGHT_ALIEN)
            self.label_alien_1.setScaledContents(True)
            self.senal_pos_inicial_aliens.emit(
                (pos_verificadas[1][0], pos_verificadas[1][1]))
            self.senal_comenzar_a_mover_aliens_1.emit(True)
            self.label_alien_1_rect = QRect(
                pos_verificadas[1][0], pos_verificadas[1][1],
                p.WIDTH_ALIEN_QRECT, p.HEIGHT_ALIEN_QRECT)
            self.label_alien_2.setPixmap(QPixmap(self.ruta_alien))
            self.label_alien_2.setGeometry(
                pos_verificadas[2][0], pos_verificadas[2][1], p.WIDTH_ALIEN, p.HEIGHT_ALIEN)
            self.label_alien_2.setScaledContents(True)
            self.senal_pos_inicial_aliens.emit(
                (pos_verificadas[2][0], pos_verificadas[2][1]))
            self.senal_comenzar_a_mover_aliens_2.emit(True)
            self.label_alien_2_rect = QRect(
                pos_verificadas[2][0], pos_verificadas[2][1],
                p.WIDTH_ALIEN_QRECT, p.HEIGHT_ALIEN_QRECT)

        else:
            self.posicion_inicial_aliens()

    def mover_aliens_front_1(self, movimiento):
        self.label_alien_1.move(movimiento[0], movimiento[1])
        self.label_alien_1_rect.moveTo(movimiento[0], movimiento[1])
        self.senal_enviar_alien_1.emit(self.label_alien_1_rect.getRect())

    def mover_aliens_front_2(self, movimiento):
        self.label_alien_2.move(movimiento[0], movimiento[1])
        self.label_alien_2_rect.moveTo(movimiento[0], movimiento[1])
        self.senal_enviar_alien_2.emit(self.label_alien_2_rect.getRect())

    def nivel_actual_aliens_balas(self):
        aliens_nivel = self.nivel_actual * 2
        balas_nivel = aliens_nivel * 2
        self.senal_enviar_aliens_y_balas.emit(
            (aliens_nivel, balas_nivel, self.nivel_actual))

    def mapa_y_usuario(self, tupla):
        self.usuario = tupla[0]
        self.mapa_elegido = tupla[1]
        if self.mapa_elegido == "Lunar":
            self.fondo_juego.setPixmap(QPixmap(p.RUTA_MAPA_LUNAR))
            self.fondo_juego.setScaledContents(True)
            self.ruta_alien = p.RUTA_ALIENS_1_VIVO
            self.senal_enviar_ponderador.emit("Lunar")
        elif self.mapa_elegido == "Jupiter":
            self.fondo_juego.setPixmap(QPixmap(p.RUTA_MAPA_JUPITER))
            self.fondo_juego.setScaledContents(True)
            self.ruta_alien = p.RUTA_ALIENS_2_VIVO
            self.senal_enviar_ponderador.emit("Jupiter")
        elif self.mapa_elegido == "Intergalactica":
            self.fondo_juego.setPixmap(QPixmap(p.RUTA_MAPA_GALAXIA))
            self.fondo_juego.setScaledContents(True)
            self.ruta_alien = p.RUTA_ALIENS_3_VIVO
            self.senal_enviar_ponderador.emit("Intergalactica")
        self.senal_enviar_usuario.emit(self.usuario)

    def iniciar_juego_test(self):
        self.resetear_tiempos_y_niveles()
        self.comenzar_nivel_nuevo()
        self.posicion_inicial_aliens()
        self.generar_mira()
        self.ajustar_balas(self.nivel_actual*4)
        self.setear_nivel()
        self.nivel_actual_aliens_balas()
        self.setear_icono_aliens()
        self.setear_aliens_faltantes_y_restantes()
        self.enviar_tiempo()
        self.desactivar_perro()
        self.estado_nivel.hide()
        self.show()

    def iniciar_juego_test_siguiente_nivel(self, info_nivel_anterior):
        self.puntaje_total = info_nivel_anterior[0]
        self.nivel_actual = info_nivel_anterior[1] + 1
        self.comenzar_nivel_nuevo()
        self.posicion_inicial_aliens()
        self.generar_mira()
        self.ajustar_balas(self.nivel_actual*4)
        self.setear_nivel()
        self.setear_puntaje()
        self.nivel_actual_aliens_balas()
        self.setear_icono_aliens()
        self.setear_aliens_faltantes_y_restantes()
        self.enviar_tiempo()
        self.desactivar_perro()
        self.estado_nivel.hide()
        self.show()

    def comenzar_nivel_nuevo(self):
        self.contador_aliens_muertos = 0
        self.tiempo = p.DURACION_NIVEL_INICIAL
        self.senal_nuevo_nivel.emit()

    def resetear_tiempos_y_niveles(self):
        self.contador_tiempo = 0
        self.nivel_actual = 1
        self.senal_tiempo_desde_0.emit()

    def setear_nivel(self):
        self.contador_nivel.setText(str(self.nivel_actual))

    def setear_puntaje(self):
        self.contador_puntos.setText(str(self.puntaje_total) + " puntos")

    def keyPressEvent(self, event):
        if not self.estado_pausa:
            if event.text().lower() == "w":
                self.senal_mover_mira.emit("up")
            elif event.text().lower() == "s":
                self.senal_mover_mira.emit("down")
            elif event.text().lower() == "d":
                self.senal_mover_mira.emit("right")
            elif event.text().lower() == "a":
                self.senal_mover_mira.emit("left")
            elif event.text().lower() == "k":
                self.senal_mover_mira.emit("k")
            elif event.text().lower() == "p":
                self.comenzar_pausa()
            try:
                if self.teclas_apretadas[-4] == Qt.Key_O and \
                        self.teclas_apretadas[-3] == Qt.Key_V and \
                        self.teclas_apretadas[-2] == Qt.Key_N and \
                        self.teclas_apretadas[-1] == Qt.Key_I:
                    self.cheat_code_ovni()
                if self.teclas_apretadas[-3] == Qt.Key_C and \
                        self.teclas_apretadas[-2] == Qt.Key_I and \
                        self.teclas_apretadas[-1] == Qt.Key_A:
                    self.cheat_code_cia()
            except IndexError:
                pass
            self.teclas_apretadas.append(event.key())
        else:
            if event.text().lower() == "p":
                self.terminar_pausa()

    def cheat_code_ovni(self):
        self.contador_balas.setText("10000")
        self.senal_cheat_code_ovni.emit()

    def cheat_code_cia(self):
        self.senal_cheat_code_cia.emit()

    def mover_mira(self, movimiento):
        x_mira = self.mira_juego.x()
        y_mira = self.mira_juego.y()
        self.mira_juego.move(movimiento[0], movimiento[1])
        self.mira_juego_rect.moveTo(movimiento[0] + 50, movimiento[1] + 30)
        self.senal_enviar_mira.emit(self.mira_juego_rect.getRect())

    def disparo(self, ruta):
        self.mira_juego.setPixmap(QPixmap(ruta))

    def ajustar_balas(self, cantidad):
        self.contador_balas.setText(str(cantidad))

    def emitir_sonido(self):
        self.label_sonido = QMediaPlayer()
        self.ruta_disparo = QUrl.fromLocalFile(p.RUTA_SONIDO_DISPARO)
        self.sonido_disparo = QMediaContent(self.ruta_disparo)
        self.label_sonido.setMedia(self.sonido_disparo)
        self.label_sonido.play()

    def pos_disparo_1(self, coords):
        self.label_disparo_1.setGeometry(
            coords[0], coords[1], p.WIDTH_ALIEN, p.HEIGHT_ALIEN)
        self.label_disparo_1.setScaledContents(True)

    def pos_disparo_2(self, coords):
        self.label_disparo_2.setGeometry(
            coords[0], coords[1], p.WIDTH_ALIEN, p.HEIGHT_ALIEN)
        self.label_disparo_2.setScaledContents(True)

    def disparo_acertado_1(self, ruta):
        self.label_disparo_1.setPixmap(QPixmap(ruta))
        if self.mapa_elegido == "Lunar":
            self.label_alien_1.setPixmap(QPixmap(p.RUTA_ALIENS_1_MUERTO))
        elif self.mapa_elegido == "Jupiter":
            self.label_alien_1.setPixmap(QPixmap(p.RUTA_ALIENS_2_MUERTO))
        elif self.mapa_elegido == "Intergalactica":
            self.label_alien_1.setPixmap(QPixmap(p.RUTA_ALIENS_3_MUERTO))
        if ruta == p.RUTA_DISPARO_FASE_1:
            self.senal_enviar_alien_muerto_1.emit()

    def disparo_acertado_2(self, ruta):
        self.label_disparo_2.setPixmap(QPixmap(ruta))
        if self.mapa_elegido == "Lunar":
            self.label_alien_2.setPixmap(QPixmap(p.RUTA_ALIENS_1_MUERTO))
        elif self.mapa_elegido == "Jupiter":
            self.label_alien_2.setPixmap(QPixmap(p.RUTA_ALIENS_2_MUERTO))
        elif self.mapa_elegido == "Intergalactica":
            self.label_alien_2.setPixmap(QPixmap(p.RUTA_ALIENS_3_MUERTO))
        if ruta == p.RUTA_DISPARO_FASE_1:
            self.senal_enviar_alien_muerto_2.emit()

    def nuevo_spawn_aliens(self, contador):
        self.contador_aliens_muertos = contador
        if self.contador_aliens_muertos*2 < self.nivel_actual*2:
            self.posicion_inicial_aliens()

    def mostrar_nivel_superado(self):
        self.estado_nivel.show()

    def cierre_juego(self):
        self.hide()

    def activar_perro(self):
        if self.mapa_elegido == "Lunar":
            self.perro_juego.setPixmap(QPixmap(p.RUTA_PERRO_1))
            self.emitir_sonido_perro()
        elif self.mapa_elegido == "Jupiter":
            self.perro_juego.setPixmap(QPixmap(p.RUTA_PERRO_2))
            self.emitir_sonido_perro()
        elif self.mapa_elegido == "Intergalactica":
            self.perro_juego.setPixmap(QPixmap(p.RUTA_PERRO_3))
            self.emitir_sonido_perro()

    def emitir_sonido_perro(self):
        self.label_sonido_perro = QMediaPlayer()
        self.ruta_sonido_perro = QUrl.fromLocalFile(p.RUTA_SONIDO_PERRO)
        self.sonido_perro = QMediaContent(self.ruta_sonido_perro)
        self.label_sonido_perro.setMedia(self.sonido_perro)
        self.label_sonido_perro.play()

    def desactivar_perro(self):
        self.perro_juego.setPixmap(QPixmap(p.RUTA_PERRO_ORIGINAL))

    def setear_icono_aliens(self):
        if self.mapa_elegido == "Lunar":
            self.icono_alien.setPixmap(QPixmap(p.RUTA_ALIENS_1_VIVO))
            self.icono_alien.setScaledContents(True)
            self.icono_alien_rip.setPixmap(QPixmap(p.RUTA_ALIENS_1_MUERTO))
            self.icono_alien_rip.setScaledContents(True)
        elif self.mapa_elegido == "Jupiter":
            self.icono_alien.setPixmap(QPixmap(p.RUTA_ALIENS_2_VIVO))
            self.icono_alien.setScaledContents(True)
            self.icono_alien_rip.setPixmap(QPixmap(p.RUTA_ALIENS_2_MUERTO))
            self.icono_alien_rip.setScaledContents(True)
        elif self.mapa_elegido == "Intergalactica":
            self.icono_alien.setPixmap(QPixmap(p.RUTA_ALIENS_3_VIVO))
            self.icono_alien.setScaledContents(True)
            self.icono_alien_rip.setPixmap(QPixmap(p.RUTA_ALIENS_3_MUERTO))
            self.icono_alien_rip.setScaledContents(True)

    def actualizar_aliens_faltantes_y_destruidos(self, valor):
        aliens_muertos = valor
        aliens_totales = self.nivel_actual*2 - aliens_muertos
        self.valor_restantes.setText(str(aliens_totales))
        self.valor_destriudos.setText(str(aliens_muertos))

    def setear_aliens_faltantes_y_restantes(self):
        self.valor_restantes.setText(str(self.nivel_actual*2))
        self.valor_destriudos.setText(str(0))

    def enviar_tiempo(self):
        self.senal_contador_de_tiempo.emit(self.contador_tiempo)
        self.contador_tiempo += 1

    def setear_tiempo(self, tiempo_inicial):
        self.label_tiempo.setText(str(tiempo_inicial))
        self.senal_comenzar_tiempo.emit(tiempo_inicial)

    def actualizar_tiempo(self, tiempo_nuevo):
        self.tiempo = tiempo_nuevo
        self.label_tiempo.setText(str(self.tiempo))

    def comenzar_pausa(self):
        self.estado_pausa = True
        self.senal_pausa_logica.emit()

    def terminar_pausa(self):
        self.estado_pausa = False
        self.senal_termino_pausa.emit()

    def salir(self):
        self.hide()
        self.senal_escribir_puntajes_desde_juego.emit(
            (self.usuario, self.puntaje_total))
        self.senal_abrir_menu_desde_juego.emit()
