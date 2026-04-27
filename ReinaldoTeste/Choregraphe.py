import urllib2
import json
import threading

class MyClass(GeneratedClass):

    def __init__(self):
        GeneratedClass.__init__(self)

        self.url_estado = "http://IPSEUNOTEBOOK:5000/estado"

        self.ultimo_estado = None
        self.ouvindo_ativo = False

        self.asr = None
        self.memory = None
        self.subscriber = None

    def onInput_onStart(self):

        # TABLET
        try:
            tablet = self.session().service("ALTabletService")
            tablet.enableWifi()
            tablet.showWebview("http://IPSEUNOTEBOOK:5000/")
        except Exception as e:
            print("Erro tablet:", e)

        # INICIA LOOP
        self.monitorar()

    # ------------------------
    # LOOP PRINCIPAL
    # ------------------------

    def monitorar(self):
        try:
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

        except Exception as e:
            print("Erro monitorar:", e)

        threading.Timer(2, self.monitorar).start()

    # ------------------------
    # FALA
    # ------------------------

    def falar(self, texto):
        try:
            tts = self.session().service("ALTextToSpeech")
            tts.say(texto)
        except Exception as e:
            print("Erro fala:", e)

    # ------------------------
    # TABLET
    # ------------------------

    def abrir_pagina(self, pagina):
        try:
            tablet = self.session().service("ALTabletService")
            tablet.showWebview("http://IPSEUNOTEBOOK:5000/" + pagina)
        except Exception as e:
            print("Erro tablet:", e)

    # ------------------------
    # VOZ (REAL)
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
            self.asr.subscribe("MeuASR")

            # 🔥 evita duplicação
            if self.subscriber is None:
                self.subscriber = self.memory.subscriber("WordRecognized")
                self.subscriber.signal.connect(self.onPalavra)

            self.ouvindo_ativo = True
            print("ASR ATIVADO")

        except Exception as e:
            print("Erro iniciar ASR:", e)

    def parar_reconhecimento(self):

        if not self.ouvindo_ativo:
            return

        try:
            if self.asr:
                self.asr.unsubscribe("MeuASR")

            self.ouvindo_ativo = False
            print("ASR DESATIVADO")

        except Exception as e:
            print("Erro parar ASR:", e)

    # ------------------------
    # EVENTO DE VOZ
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
            print("Reconhecido:", palavra)

            # ------------------------
            # AÇÕES
            # ------------------------

            if palavra == "laser":
                self.falar("Abrindo conteúdo de corte a laser")
                self.abrir_pagina("laser")

            elif palavra == "biologia":
                self.falar("Abrindo conteúdo de biologia")
                self.abrir_pagina("biologia")

            elif palavra == "maker":
                self.falar("Voltando para a tela inicial")
                self.abrir_pagina("")

            elif palavra == "ajuda":
                self.falar("Vou ajudar vocês agora")

        except Exception as e:
            print("Erro voz:", e)