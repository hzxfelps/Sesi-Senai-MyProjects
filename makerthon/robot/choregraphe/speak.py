from naoqi import ALProxy
from config import PEPPER_IP, PORT

def onInput_onStart(self):
    tts = ALProxy("ALTextToSpeech", PEPPER_IP, PORT)

    grupo = self.getInput("grupo")

    tts.say("Atendendo o grupo " + str(grupo))

    self.onStopped()