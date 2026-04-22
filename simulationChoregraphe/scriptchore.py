import requests

def onStart():
    try:
        url = "http://10.121.235.55:5000/next"  # IP do seu notebook (ta o do marcelo)
        
        response = requests.get(url)
        data = response.json()

        grupo = data.get("grupo")
        nivel = data.get("nivel")

        if grupo is not None:
            frase = "Grupo {} precisa de ajuda. Nível {}".format(grupo, nivel)
            
            # Faz o Pepper falar
            tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
            tts.say(frase)

        else:
            tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559) #127.0.0.1 é server local robô
            tts.say("Nenhum grupo precisa de ajuda no momento.")

    except Exception as e:
        print("Erro:", e)