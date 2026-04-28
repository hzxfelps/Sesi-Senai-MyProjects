import urllib2
import json
import threading

class MyClass(GeneratedClass):

    def __init__(self):
        GeneratedClass.__init__(self)

        self.url_estado = "http://IPSEUNOTEBOOK:5000/estado"
        self.url_next = "http://IPSEUNOTEBOOK:5000/next"

        self.ultimo_estado = None
        self.ultimo_grupo = None
        self.ouvindo_ativo = False

    def onInput_onStart(self):

        tablet = self.session().service("ALTabletService")
        tablet.enableWifi()
        tablet.showWebview("http://IPSEUNOTEBOOK:5000/")

        self.monitorar()

    # ------------------------
    # LOOP PRINCIPAL
    # ------------------------

    def monitorar(self):
        try:
            # ESTADO (botão)
            response = urllib2.urlopen(self.url_estado)
            data = json.loads(response.read())

            ouvindo = data.get("ouvindo", False)

            if self.ultimo_estado is None:
                self.ultimo_estado = ouvindo

            if ouvindo != self.ultimo_estado:

                if ouvindo:
                    self.falar("Estou ouvindo vocês.")
                    self.iniciar_reconhecimento()
                else:
                    self.falar("Estou aguardando.")
                    self.parar_reconhecimento()

                self.ultimo_estado = ouvindo

            # GRUPOS (ESP32)
            response2 = urllib2.urlopen(self.url_next)
            data2 = json.loads(response2.read())

            grupo = data2.get("grupo")

            if grupo is not None and grupo != self.ultimo_grupo:
                self.falar("Grupo " + str(grupo) + ", vou ajudar vocês.")
                self.ultimo_grupo = grupo

                # simula movimento
                self.ir_para_grupo(grupo)

        except Exception as e:
            print("Erro:", e)

        threading.Timer(2, self.monitorar).start()

    # ------------------------
    # FALA
    # ------------------------

    def falar(self, texto):
        tts = self.session().service("ALTextToSpeech")
        tts.say(texto)

    # ------------------------
    # SIMULA MOVIMENTO
    # ------------------------

    def ir_para_grupo(self, grupo):
        import time
        self.falar("Indo até o grupo " + str(grupo))
        time.sleep(3)
        self.falar("Cheguei no grupo " + str(grupo))

    # ------------------------
    # VOZ
    # ------------------------

    def iniciar_reconhecimento(self):

        if self.ouvindo_ativo:
            return

        self.ouvindo_ativo = True

        self.asr = self.session().service("ALSpeechRecognition")
        self.memory = self.session().service("ALMemory")

        self.asr.pause(True)
        self.asr.setLanguage("Portuguese")

        vocab = ["maker", "biologia", "laser"]
        self.asr.setVocabulary(vocab, False)

        self.asr.pause(False)
        self.asr.subscribe("MeuASR")

        self.subscriber = self.memory.subscriber("WordRecognized")
        self.subscriber.signal.connect(self.onPalavra)

    def parar_reconhecimento(self):
        if not self.ouvindo_ativo:
            return

        self.asr.unsubscribe("MeuASR")
        self.ouvindo_ativo = False

    # ------------------------
    # QUANDO FALA
    # ------------------------

    def onPalavra(self, valor):
        try:
            if not self.ouvindo_ativo:
                return

            if len(valor) < 2:
                return

            palavra = valor[0]
            confianca = valor[1]

            if confianca < 0.5:
                return

            palavra = palavra.lower()

            if palavra == "laser":
                self.falar("Abrindo conteúdo de corte a laser")
                self.abrir_pagina("laser")

            elif palavra == "biologia":
                self.falar("Abrindo conteúdo de biologia")
                self.abrir_pagina("biologia")

            elif palavra == "maker":
                self.falar("Voltando ao início")
                self.abrir_pagina("")

        except Exception as e:
            print("Erro voz:", e)

    # ------------------------
    # TABLET
    # ------------------------

    def abrir_pagina(self, pagina):
        tablet = self.session().service("ALTabletService")
        tablet.showWebview("http://IPSEUNOTEBOOK:5000/" + pagina)