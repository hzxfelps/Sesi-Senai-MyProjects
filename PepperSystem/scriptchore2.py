import urllib2
import json
import threading
#CÓDIGO NOVOOOOOOOOOOOOOOOOOOOOOOOO
class MyClass(GeneratedClass):

    def __init__(self):
        GeneratedClass.__init__(self)

        self.url_estado = "http://127.0.0.1:5000/estado"
        self.url_next = "http://127.0.0.1:5000/next"

        self.ultimo_estado = None
        self.ultimo_grupo = None
        self.ouvindo_ativo = False

    def onInput_onStart(self):
        self.monitorar()

    # ------------------------
    # LOOP PRINCIPAL
    # ------------------------

    def monitorar(self):
        try:
            print("MONITORANDO...")

            response = urllib2.urlopen(self.url_estado)
            data = json.loads(response.read())

            ouvindo = data.get("ouvindo", False)

            if ouvindo != self.ultimo_estado:

                if ouvindo:
                    self.falar("Estou ouvindo vocês.")
                    self.iniciar_reconhecimento()
                else:
                    self.falar("Estou aguardando.")
                    self.parar_reconhecimento()

                self.ultimo_estado = ouvindo

            response2 = urllib2.urlopen(self.url_next)
            data2 = json.loads(response2.read())

            grupo = data2.get("grupo")

            if grupo is not None and grupo != self.ultimo_grupo:
                self.falar("Vou ajudar o grupo " + str(grupo))
                self.ultimo_grupo = grupo

        except Exception as e:
            print("Erro:", e)

        import time
        time.sleep(2)
        self.monitorar()

    # ------------------------
    # FALA
    # ------------------------

    def falar(self, texto):
        try:
            print("FALANDO:", texto)
            tts = self.session().service("ALTextToSpeech")
            tts.say(texto)
        except Exception as e:
            print("Erro ao falar:", e)

    # ------------------------
    # RECONHECIMENTO SIMULADO
    # ------------------------

    def iniciar_reconhecimento(self):
        print(">>> ASR SIMULADO <<<")

        if self.ouvindo_ativo:
            return

        self.ouvindo_ativo = True

        def simular():
            print(">>> SIMULANDO PALAVRA <<<")
            self.onPalavra(["maker", 0.9])

        threading.Timer(2, simular).start()

    def parar_reconhecimento(self):
        if not self.ouvindo_ativo:
            return

        self.ouvindo_ativo = False

    # ------------------------
    # QUANDO RECONHECE PALAVRA
    # ------------------------

    def onPalavra(self, valor):
        try:
            print("RAW:", valor)

            palavra = valor[0]
            confianca = valor[1]

            if confianca > 0.4:
                palavra = palavra.lower()

                if palavra == "maker":
                    self.falar("Área maker selecionada")

                elif palavra == "física":
                    self.falar("Vamos estudar física")

                elif palavra == "ajuda":
                    self.falar("Vou ajudar vocês agora")

                elif palavra == "laser":
                    self.falar("Para corte a laser, ajuste potência e velocidade.")

        except Exception as e:
            print("Erro palavra:", e)