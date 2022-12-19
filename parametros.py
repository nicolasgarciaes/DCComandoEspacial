import os

#### rutas ventanas y mapas

RUTA_UI_VENTANA_INICIO = os.path.join("frontend", "assets",
                                         "ventana_inicio.ui")

RUTA_UI_VENTANA_RANKINGS = os.path.join("frontend", "assets",
                                         "ventana_rankings.ui")

RUTA_UI_VENTANA_PRINCIPAL = os.path.join("frontend", "assets",
                                         "ventana_principal.ui")

RUTA_UI_VENTANA_JUEGOS = os.path.join("frontend", "assets",
                                         "ventana_juegos.ui")

RUTA_UI_VENTANA__POST_JUEGO = os.path.join("frontend", "assets",
                                         "ventana_post_nivel.ui")

RUTA_MAPA_LUNAR = os.path.join("Sprites", "fondos",
                                         "Luna.png")

RUTA_MAPA_JUPITER = os.path.join("Sprites", "fondos",
                                         "Jupiter.png")             

RUTA_MAPA_GALAXIA = os.path.join("Sprites", "fondos",
                                         "Galaxia.png")      

#### rutas miras

RUTA_MIRA = os.path.join("Sprites", "Elementos juego",
                                         "Disparador_negro.png")  

MEDIDAS_MIRA = (475, 350, 150, 100)

MEDIDAS_MIRA_QRECT = (475, 350, 25, 25)

RUTA_MIRA_DISPARO = os.path.join("Sprites", "Elementos juego",
                                         "Disparador_rojo.png")  

RUTA_SONIDO_DISPARO = os.path.join("Sonidos", "disparo.wav")

#### rutas aliens

RUTA_ALIENS_1_VIVO = os.path.join("Sprites", "Aliens",
                                         "Alien1.png")
RUTA_ALIENS_1_MUERTO = os.path.join("Sprites", "Aliens",
                                         "Alien1_dead.png")
RUTA_ALIENS_2_VIVO = os.path.join("Sprites", "Aliens",
                                         "Alien2.png")                                        
RUTA_ALIENS_2_MUERTO = os.path.join("Sprites", "Aliens",
                                         "Alien2_dead.png")
RUTA_ALIENS_3_VIVO = os.path.join("Sprites", "Aliens",
                                         "Alien3.png")                                        
RUTA_ALIENS_3_MUERTO = os.path.join("Sprites", "Aliens",
                                         "Alien3_dead.png")

WIDTH_ALIEN = 50
HEIGHT_ALIEN = 60
WIDTH_ALIEN_QRECT = 30
HEIGHT_ALIEN_QRECT = 45

#### Bordes ventana de juegos

BORDE_VERTICAL_IZQUIERDO = -30
BORDE_VERTICAL_DERECHO = 978
BORDE_HORIZONTAL_SUPERIOR = -3
BORDE_HORIZONTAL_INFERIOR = 574     

BORDE_VERTICAL_IZQUIERDO_ALIENS = 5
BORDE_VERTICAL_DERECHO_ALIENS = 1040
BORDE_HORIZONTAL_SUPERIOR_ALIENS = -3
BORDE_HORIZONTAL_INFERIOR_ALIENS = 595     

#### ruta fases disparos

RUTA_DISPARO_FASE_1 = os.path.join("Sprites", "Elementos juego",
                                         "Disparo_f1")
RUTA_DISPARO_FASE_2 = os.path.join("Sprites", "Elementos juego",
                                         "Disparo_f2")
RUTA_DISPARO_FASE_3 = os.path.join("Sprites", "Elementos juego",
                                         "Disparo_f3")                    
                                         


#### PERRO

RUTA_PERRO_1 = os.path.join("Sprites", "Terminator-Dog",
                                         "Perro_y_alien1.png")
                                         
RUTA_PERRO_2 = os.path.join("Sprites", "Terminator-Dog",
                                         "Perro_y_alien2.png")

RUTA_PERRO_3 = os.path.join("Sprites", "Terminator-Dog",
                                         "Perro_y_alien3.png") 

RUTA_PERRO_ORIGINAL = os.path.join("Sprites", "Terminator-Dog",
                                         "Dog1.png")

TIEMPO_TERMINATOR_DOG = 5000

RUTA_SONIDO_PERRO = os.path.join("Sonidos", "risa_robotica.wav")

#### PARAMETROS ESCENARIOS

DURACION_NIVEL_INICIAL = 60 #segundos

VELOCIDAD_ALIEN_1 = (2, 2)

VELOCIDAD_ALIEN_2 = (-2, -2)

PONDERADOR_TUTORIAL = 0.95

PONDERADOR_ENTRENAMIENTO = 0.85

PONDERADOR_INVASION = 0.75

CANTIDAD_DE_ALIENS_NIVEL_1 = 2

