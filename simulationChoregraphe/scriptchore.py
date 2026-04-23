import urllib2
import json
import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.url_estado = "http://192.168.1.11:5000/estado"
        self.url_next = "http://192.168.1.11:5000/next"
        self.ultimo_estado = None
        self.timer = None

    def onInput_onStart(self):
        self.monitorar()

    def monitorar(self):
        try:
            # ------------------------
            # ESTADO DO BOTÃO
            # ------------------------
            response = urllib2.urlopen(self.url_estado)
            data = json.loads(response.read())

            ouvindo = data.get("ouvindo", False)

            # Só fala se mudou
            if ouvindo != self.ultimo_estado:
                if ouvindo:
                    self.falar("Estou ouvindo vocês.")
                else:
                    self.falar("Estou aguardando.")

                self.ultimo_estado = ouvindo

            # ------------------------
            # PRÓXIMO GRUPO
            # ------------------------
            response2 = urllib2.urlopen(self.url_next)
            data2 = json.loads(response2.read())

            grupo = data2.get("grupo")

            if grupo is not None:
                self.falar("Vou ajudar o grupo " + str(grupo))

        except Exception as e:
            print("Erro:", e)

        # repete depois
        self.timer = self.qi.async(self.esperar)

    def esperar(self):
        time.sleep(5)
        self.monitorar()

    def falar(self, texto):
        try:
            tts = self.session.service("ALTextToSpeech")
            tts.say(texto)
        except Exception as e:
            print("Erro ao falar:", e)