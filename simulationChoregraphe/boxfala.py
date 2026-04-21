from naoqi import ALProxy

def onInput_onStart(self):
    tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)

    grupo = self.getInput("grupo")

    tts.say("Indo ajudar o grupo " + str(grupo))

    self.onStopped()