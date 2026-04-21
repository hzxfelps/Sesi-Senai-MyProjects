import requests
import time
from config import SERVER_URL

ultimo_grupo = None

def onInput_onStart(self):
    global ultimo_grupo

    while True:
        try:
            r = requests.get(SERVER_URL)
            data = r.json()

            grupo = data.get("grupo")
            nivel = data.get("nivel")

            if grupo is not None and grupo != ultimo_grupo:
                ultimo_grupo = grupo

                self.output("grupo", grupo)
                self.output("nivel", nivel)

        except Exception as e:
            print("Erro:", e)

        time.sleep(2)