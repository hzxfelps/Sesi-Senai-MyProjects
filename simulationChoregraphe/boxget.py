import requests
import time

def onInput_onStart(self):
    while True:
        try:
            r = requests.get("http://192.168.0.100:5000/next")
            data = r.json()

            grupo = data.get("grupo")
            nivel = data.get("nivel")

            if grupo is not None:
                self.output("grupo", grupo)
                self.output("nivel", nivel)

        except:
            pass

        time.sleep(2)