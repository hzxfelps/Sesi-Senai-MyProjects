from naoqi import ALProxy
from config import PEPPER_IP, PORT

def onInput_onStart(self):
    motion = ALProxy("ALMotion", PEPPER_IP, PORT)

    nivel = self.getInput("nivel")

    motion.wakeUp()

    posicoes = [
        [0.2, 0, 0],
        [0.4, 0, 0],
        [0.6, 0, 0],
        [0.8, 0, 0],
        [1.0, 0, 0],
        [1.2, 0, 0],
        [1.4, 0, 0],
        [1.6, 0, 0],
        [1.8, 0, 0],
        [2.0, 0, 0]
    ]

    if nivel is not None and nivel < len(posicoes):
        x, y, theta = posicoes[nivel]
        motion.moveTo(x, y, theta)

    self.onStopped()