import requests
import time

while True:
    try:
        r = requests.get("http://127.0.0.1:5000/next")
        data = r.json()

        grupo = data.get("grupo")
        nivel = data.get("nivel")

        if grupo is not None:
            print(f"Indo atender grupo {grupo} (nivel {nivel})")

    except Exception as e:
        print("Erro:", e)

    time.sleep(2)