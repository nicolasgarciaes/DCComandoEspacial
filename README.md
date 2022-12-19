# Tarea 2: DCComando espacial :school_satchel:

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Ventana de Inicio: 4 pts (4%)
#### Ventana de Ranking: 5 pts (5%)
#### Ventana principal: 7 pts (7%)
#### Ventana de juego: 14 pts (13%)
#### Ventana de post-nivel: 5 pts (5%)
#### Mecánicas de juego: 47 pts (45%)
##### ✅ Arma <El arma respesta los bordes de la ventana, al momento de disparar se produce el sonido solicitado y el centro cambia durante un segundo a color rojo, cabe destacar que se dispara con la tecla "k" no con el espacio.\>
##### ✅ Aliens y Escenario de Juego <Los aliens cambian dependiendo del nivel, aparecen de par en par y se ajustan a las velocidad de cada nivel y escenario.\>
##### ✅ Fin de Nivel <Al momento de terminar el nivel, ya sea, por falta de balas o por llegar el tiempo a 0, se pierde y se termina el nivel. En caso de matar a todos los aliens, se termina el nivel, aparece "nivel completado" y el perro realiza la animación correspondiente junto a su risa.\>
##### ✅ Fin del juego <Al momento de ponerle fin al juego, ya sea, mediante salir en la ventana juego o salir en la ventana de post-nivel, se escribe el puntaje en puntajes.txt y se muestra la ventana de inicio.\>
#### Cheatcodes: 8 pts (8%) 
##### ✅ Pausa <Al apretar el tecla "p" se lleva a pausa y en caso de estar en pausa y se vuelve a apretar, se saca la puasa, adicionalmente, hay dos botones en la interfaz, uno que sirve para pausar el juego y otro para despausar el juego, ambos cumplen la función de su asociada a su nombre.\>
##### ✅ O + V+ N + I <Al momento de apretar las teclas correspondientes en el orden correspondiente, se aplica el cheatcode y las balas suben a 10000\>
##### ✅  C + I + A <De igual manera que el cheatcode anterior, se aplica el cheatcode y se pasa al siguiente nivel con sus animaciones correspondientes.\>
#### General: 14 pts (13%)
##### ✅ Modularización <Se separa correctamente front-end del back-end, donde cada uno cumple sus respectivas funciones.\>
##### 🟠 Modelación <Considero que paso a paso, fui complicando más el codigo y por temas de tiempo no pude hacerlo más "corto".\>
##### ✅ Archivos  <Se abren y escriben corractamente los archivos.\>
##### ✅ Parametros.py <Posee todos los parametros minimos y algunos adicionales.\>
#### Bonus: 10 décimas máximo
##### ✅ Risa Dog <Se logra aplicar la risa al momento de superar el nivel.\>
##### ❌ Estrella
##### ❌ Disparos extra
##### ❌ Bomba
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```T2```
2. ```parametros.py``` en ```T2```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: ```QtCore```
2. ```PyQt5```: ```QtWidgets```
3. ```PyQt5```: ```QtGui```
4. ```PyQt5```: ```uic```
5. ```PyQt5```: ```QtMultimedia```
6. ```random```: ```randint```
7. ```attr```: ```Attribute```
8. ```sys```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```fronted```: Contiene a ```ventana_inico```, ```ventana_juego```, ```ventana_post_juego```, ```ventana_principal```, ```ventana_rankings```
2. ```backend```: Contiene a ```logica_aliens```, ```logica_inico```, ```logica_juego```, ```logica_mira```, ```logica_principio```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <En caso de querer usar los cheatscodes, sera necesario mover al menos una vez la mira, considero que es valido, ya que, el metodo KeyPressEvent considera en primera instancia el movimiento de la mira, posterior lee los posibles cheatscodes.> 
2. <Los disparos se realizán con la tecla "K"  y es valido, porque, en el enunciado admiten posibles modificaciones a la tecla con la cual se dispara.\>
3. <Al momento de disparar, cuando comienza el cambio de fase del disparo, si se apreta el botón pausa, la animación sigue de cambio de fase sigue corriendo, no lo logre modificar sin traer bugs al juego.>
4. <Los botones, salir de la ventana juego y de la ventana post juego, llevan a la ventana de inicio, esto se hizo asi, debido a la ambiguedad que lleva la rubrica con el enunciado, y adicionalmente, segui las instrucciones que un ayudante planteo en una issue elaborada por mi (```issue 202```).>\ 

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://pharos.sh/como-ordenar-un-diccionario-por-valor-en-python/#:~:text=Podemos%20ordenar%20un%20diccionario%20con,ordenado%20en%20un%20nuevo%20diccionario.>: este hace \<este codigo ordenada un diccionario por los valores de sus llaves.> y está implementado en el archivo <ventana_rankings.py> en las líneas <39 a 46> y hace <sirve para ordenar los valores de puntajes.txt en orden de mayor a menor, asociado al nombre del jugador.>


