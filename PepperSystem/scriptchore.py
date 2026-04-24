import urllib2
import json
import threading

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
            # ===== ESTADO (HTML controla isso)
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

            # ===== GRUPOS (ESP32 manda isso)
            response2 = urllib2.urlopen(self.url_next)
            data2 = json.loads(response2.read())

            grupo = data2.get("grupo")

            if grupo is not None and grupo != self.ultimo_grupo:
                self.falar("Vou ajudar o grupo " + str(grupo))
                self.ultimo_grupo = grupo

        except Exception as e:
            print("Erro:", e)

        # repete a cada 5 segundos
        threading.Timer(5, self.monitorar).start()

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
    # RECONHECIMENTO DE VOZ
    # ------------------------

    def iniciar_reconhecimento(self):
        if self.ouvindo_ativo:
            return

        try:
            self.asr = self.session().service("ALSpeechRecognition")
            self.memory = self.session().service("ALMemory")

            self.asr.pause(True)
            self.asr.setLanguage("Portuguese")

            vocab = ["maker", "biologia", "ajuda", "laser"]
            self.asr.setVocabulary(vocab, False)

            self.asr.pause(False)
            self.asr.subscribe("Reconhecimento")

            self.subscriber = self.memory.subscriber("WordRecognized")
            self.subscriber.signal.connect(self.onPalavra)

            self.ouvindo_ativo = True

        except Exception as e:
            print("Erro ASR:", e)

    def parar_reconhecimento(self):
        if not self.ouvindo_ativo:
            return

        try:
            self.asr.unsubscribe("Reconhecimento")
            self.ouvindo_ativo = False
        except Exception as e:
            print("Erro ao parar ASR:", e)

    # ------------------------
    # QUANDO UMA PALAVRA É RECONHECIDA
    # ------------------------

    def onPalavra(self, valor):
        try:
            print("RAW:", valor)

            palavra = valor[0]
            confianca = valor[1]

            if confianca > 0.4:
                print("Reconhecido:", palavra)

                if palavra == "maker":
                    self.falar("Área maker selecionada")

                elif palavra == "Física":
                    self.falar("Vamos estudar física")

                elif palavra == "ajuda":
                    self.falar("Vou ajudar vocês agora")

                elif palavra == "laser":
                    self.falar("Para corte a laser, ajuste potência e velocidade.")

        except Exception as e:
            print("Erro palavra:", e)