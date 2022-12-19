from PyQt5.QtWidgets import QApplication
import sys
from frontend.ventana_inicio import VentanaInicio
from backend.logica_inicio import LogicaInicio
from frontend.ventana_juego import VentanaJuegos
from frontend.ventana_rankings import VentanaRankings
from frontend.ventana_principal import VentanaPrincipal
from backend.logica_principio import LogicaPrincipio
from frontend.ventana_juego import VentanaJuegos
from backend.logica_juego import Juego
from backend.logica_mira import Mira
from backend.logica_aliens import Aliens
from frontend.ventana_post_juego import VentanaPostJuego

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    ventana_inicio = VentanaInicio()
    logica_inicio = LogicaInicio()
    ventana_rankings = VentanaRankings()
    ventana_principal = VentanaPrincipal()
    logica_principio = LogicaPrincipio()
    ventana_juego = VentanaJuegos()
    mira = Mira()
    juego = Juego()
    aliens = Aliens()
    ventana_post_juego = VentanaPostJuego()

    ### señales ventana inicio ###
    ventana_inicio.mostrar_inicio()

    ventana_inicio.senal_rankings.connect(
        ventana_rankings.mostrar_rankings
    )
    ventana_rankings.senal_volver_inicio.connect(
        ventana_inicio.mostrar_inicio
    )
    ventana_inicio.senal_iniciar_juego.connect(
        ventana_principal.mostrar_principio
    )
    ventana_principal.senal_volver_inicio.connect(
        ventana_inicio.mostrar_inicio
    )

    ### señales ventana principal  ###
    logica_principio.senal_respuesta_validacion.connect(
        ventana_principal.recibir_validacion
    )

    ventana_principal.senal_enviar_nombre_y_mapa.connect(
        logica_principio.comprobar_nombre_y_mapa
    )

    # Envia el tipo de mapa, el nombre de usuario a la ventana del juego y luego comienza el juego
    logica_principio.senal_usuario_y_mapa.connect(
        ventana_juego.mapa_y_usuario
    )

    ventana_principal.senal_iniciar_juego.connect(
        ventana_juego.iniciar_juego_test
    )
    # Señales movimiento mira

    ventana_juego.senal_mover_mira.connect(
        juego.revisar_disparo
    )

    ventana_juego.senal_mover_mira.connect(
        mira.logica_mover_mira
    )

    mira.senal_cambio_mov.connect(
        ventana_juego.mover_mira
    )

    mira.senal_disparo.connect(
        ventana_juego.disparo
    )

    mira.senal_disparo_original.connect(
        ventana_juego.disparo
    )

    mira.senal_enviar_sonido.connect(
        ventana_juego.emitir_sonido
    )
    # Señales de generar aliens

    ventana_juego.senal_pos_aliens.connect(
        aliens.verificar_pos_inicial
    )

    aliens.senal_pos_inicial_logica.connect(
        ventana_juego.generar_aliens
    )

    # Señales movimiento aliens

    ventana_juego.senal_pos_aliens.connect(
        aliens.guardar_pos_inicial_1
    )

    ventana_juego.senal_comenzar_a_mover_aliens_1.connect(
        aliens.iniciar_timers_1
    )

    aliens.senal_cambio_pos_aliens_logica_1.connect(
        ventana_juego.mover_aliens_front_1
    )

    ventana_juego.senal_pos_aliens.connect(
        aliens.guardar_pos_inicial_2
    )

    ventana_juego.senal_comenzar_a_mover_aliens_2.connect(
        aliens.iniciar_timers_2
    )

    aliens.senal_cambio_pos_aliens_logica_2.connect(
        ventana_juego.mover_aliens_front_2
    )

    # Señales disparo mira a aliens

    ventana_juego.senal_enviar_alien_1.connect(
        juego.disparo_mira_alien_1
    )

    ventana_juego.senal_enviar_alien_2.connect(
        juego.disparo_mira_alien_2
    )

    ventana_juego.senal_enviar_mira.connect(
        juego.disparo_mira
    ) 

    # Señales disparo acertado

    juego.senal_disparo_acertado_f1_1.connect(
        ventana_juego.disparo_acertado_1
    )

    juego.senal_disparo_acertado_f2_1.connect(
        ventana_juego.disparo_acertado_1
    )

    juego.senal_disparo_acertado_f3_1.connect(
        ventana_juego.disparo_acertado_1
    )

    juego.senal_disparo_original_1.connect(
        ventana_juego.disparo_acertado_1
    )

    ventana_juego.senal_enviar_alien_muerto_1.connect(
        aliens.alien_muerto_1
    )

    juego.senal_pos_disparo_1.connect(
        ventana_juego.pos_disparo_1
    )
    # 2
    juego.senal_disparo_acertado_f1_2.connect(
        ventana_juego.disparo_acertado_2
    )

    juego.senal_disparo_acertado_f2_2.connect(
        ventana_juego.disparo_acertado_2
    )

    juego.senal_disparo_acertado_f3_2.connect(
        ventana_juego.disparo_acertado_2
    )

    juego.senal_disparo_original_2.connect(
        ventana_juego.disparo_acertado_2
    )

    ventana_juego.senal_enviar_alien_muerto_2.connect(
        aliens.alien_muerto_2
    )

    juego.senal_pos_disparo_2.connect(
        ventana_juego.pos_disparo_2
    )

    # Señal que envia que ambos aliens se murieron
    aliens.senal_resetear_aliens.connect(
        ventana_juego.nuevo_spawn_aliens
    )

    # Señal que envia que ambos aliens respawnearon
    ventana_juego.senal_aliens_vivos.connect(
        juego.check_estado_aliens
    )
    # Señales que envian el nivel y la balas correspondientes

    ventana_juego.senal_enviar_aliens_y_balas.connect(
        mira.recibir_balas
    )

    mira.senal_enviar_balas_usadas.connect(
        ventana_juego.ajustar_balas
    )

    mira.senal_sin_balas.connect(
        juego.check_balas
    )

    # Setea el nivel, las balas y el numero de aliens en la logica del juego 
    ventana_juego.senal_enviar_aliens_y_balas.connect(
        juego.setear_aliens_y_balas
    )

    # inicio post juego

    juego.senal_post_nivel.connect(
        ventana_post_juego.inicar_post_juego)

    # termino juego

    juego.senal_termino_juego.connect(
        ventana_juego.cierre_juego
    )

    # activar el perro al terminar el nivel 
    juego.senal_animacion_perro.connect(
        ventana_juego.activar_perro
    )

    # Muestra nivel superado en la ventana juego
    juego.senal_nivel_superado.connect(
        ventana_juego.mostrar_nivel_superado
    )

    # Entrega los aliens restantes y destruidos a la ventana de juego

    juego.senal_murio_alien.connect(
        ventana_juego.actualizar_aliens_faltantes_y_destruidos
    )

    # Entrega al post las nivel balas restantes

    mira.senal_enviar_balas_usadas.connect(
        juego.recibir_balas_restantes
    )

    juego.senal_info_post_nivel.connect(
        ventana_post_juego.info_post_juego
    )

    # Envia el nombre de usuario desde la ventana juego a la logica juego
    ventana_juego.senal_enviar_usuario.connect(
        juego.recibir_usuario
    )

    # Conexiones del tiempo entre logica y ventana juego
    ventana_juego.senal_contador_de_tiempo.connect(
        juego.tiempo_nivel
    )

    juego.senal_enviar_tiempo_inicial.connect(
        ventana_juego.setear_tiempo
    )

    ventana_juego.senal_comenzar_tiempo.connect(
        juego.instanciar_timers_tiempo
    )

    juego.senal_enviar_tiempo.connect(
        ventana_juego.actualizar_tiempo
    )

    # Actualiza el tiempo al cambiar de mapa o pasar al siguiente nivel

    ventana_juego.senal_tiempo_desde_0.connect(
        juego.tiempo_desde_el_comienzo
    )

    # Envia el tipo de mapa al backend de la logica juego

    ventana_juego.senal_enviar_ponderador.connect(
        juego.recibir_ponderador
    )

    # Envia el tipo de mapa a los aliens

    ventana_juego.senal_enviar_ponderador.connect(
        aliens.ponderador_aliens
    )

    # enviar puntaje y tiempo restante al post juego
    juego.senal_envio_puntaje.connect(
        ventana_post_juego.setear_puntaje_nivel
    )

    juego.senal_enviar_tiempo_post_juego.connect(
        ventana_post_juego.setear_tiempo
    )

    juego.senal_envio_puntaje_total.connect(
        ventana_post_juego.setear_puntaje_total
    )

    # Comenzar siguiente nivel desde post juego

    ventana_post_juego.senal_comenzar_siguiente_nivel.connect(
        ventana_juego.iniciar_juego_test_siguiente_nivel
    )

    # Resetea los contadores de las logicas 

    ventana_juego.senal_nuevo_nivel.connect(
        juego.resetar_nivel_nuevo
    )
    ventana_juego.senal_nuevo_nivel.connect(
        aliens.resetear_aliens
    )

    # Boton pausa

    ventana_juego.senal_pausa_logica.connect(
        juego.recibir_pausa
    )

    ventana_juego.senal_pausa_logica.connect(
        aliens.recibir_pausa_aliens
    )

    # Boton termino pausa

    ventana_juego.senal_termino_pausa.connect(
        juego.terminar_pausa
    )

    ventana_juego.senal_termino_pausa.connect(
        aliens.terminar_pausa_aliens
    )

    # Escribir puntajes

    ventana_post_juego.senal_escribir_puntajes.connect(
        ventana_rankings.escribir_puntajes
    )

    ventana_post_juego.senal_abrir_menu_principal.connect(
        ventana_inicio.mostrar_inicio
    )

    ventana_juego.senal_escribir_puntajes_desde_juego.connect(
        ventana_rankings.escribir_puntajes
    )

    ventana_juego.senal_abrir_menu_desde_juego.connect(
        ventana_inicio.mostrar_inicio
    )

    # Cheats codes

    ventana_juego.senal_cheat_code_ovni.connect(
        juego.cheat_code_ovni_logica
    )

    ventana_juego.senal_cheat_code_ovni.connect(
        mira.recibir_cheat_code_balas
    )

    ventana_juego.senal_cheat_code_cia.connect(
        juego.cheat_code_cia_logica
    )

    ventana_juego.senal_cheat_code_cia.connect(
        aliens.cheat_code_cia
    )

    app.exec()


