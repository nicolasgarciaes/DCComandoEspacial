import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal
import sys
sys.path.append("T2/..")


class LogicaInicio(QObject):

    senal_abrir_rankig = pyqtSignal(str)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()
