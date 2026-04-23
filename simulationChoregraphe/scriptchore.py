import urllib2
import json
import time
import threading

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.url_estado = "http://127.0.0.1:5000/estado"
        self.url_next = "http://127.0.0.1:5000/next"
        self.ultimo_estado = None
        self.ultimo_grupo = None

    def onInput_onStart(self):
        self.monitorar()

    def monitorar(self):
        try:
            # ------------------------
            # ESTADO
            # ------------------------
            response = urllib2.urlopen(self.url_estado)
            data = json.loads(response.read())

            ouvindo = data.get("ouvindo", False)

            if ouvindo != self.ultimo_estado:
                if ouvindo:
                    self.falar("Estou ouvindo vocês.")
                else:
                    self.falar("Estou aguardando.")

                self.ultimo_estado = ouvindo

            # ------------------------
            # GRUPO
            # ------------------------
            response2 = urllib2.urlopen(self.url_next)
            data2 = json.loads(response2.read())

            grupo = data2.get("grupo")

            if grupo is not None and grupo != self.ultimo_grupo:
                self.falar("Vou ajudar o grupo " + str(grupo))
                self.ultimo_grupo = grupo

        except Exception as e:
            print("Erro:", e)

        # LOOP FUNCIONAL
        threading.Timer(5, self.monitorar).start()

    #def falar(self, texto):
        #try:
            #tts = self.session.service("ALTextToSpeech")
            #tts.say(texto)
        #except Exception as e:
            #print("Erro ao falar:", e)
            
    def falar(self, texto):
        try:
            print("FALANDO:", texto)
            tts = self.session().service("ALTextToSpeech")
            tts.say(texto)
        except Exception as e:
            print("Erro ao falar:", e)