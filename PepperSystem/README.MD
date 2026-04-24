TESTE DE COMUNICACAO ENTRE APLICACOES
Segue fluxo do robo (esp32 -> server local notebook -> robo) 
utilizando o software choregraphe para simular o robo
Utilizamos algumas funcoes basicas como o get para atualizar a resposta do 
robo ao servidor / move para movimentacao / fala para fala

COMO TESTAR 
Rodar o server Flask
Rodar ESP32
Ver no terminal do Flask se está chegando dado
Rodar script Python (simulador robô)
Se OK → jogar no Choregraphe
    http://127.0.0.1:5000/update?grupo=2&nivel=5
http://127.0.0.1:5000/update?grupo=3&nivel=1


ERROS COMUNS
IP errado (esse é o principal)
Firewall bloqueando porta 5000
ESP32 e notebook não estão na mesma rede
esquecer host="0.0.0.0" no Flask

TROCA DA FUNÇÃO FALA
def falar(self, texto):
    try:
        print("FALANDO:", texto)
        tts = self.session().service("ALTextToSpeech")
        tts.say(texto)
    except Exception as e:
        print("Erro ao falar:", e)

Alteração de estado do robô
http://127.0.0.1:5000/estado?ouvindo=1

TODA VEZ que o botão de fala no html é pressionado ele envia ouvindo=1 para que o estado 
ouvindo seja =true

HTML → manda estado
Flask → guarda estado
Pepper → reage ao estado

IP DO NOTEBOOK EQUIPE: 192.168.1.2
RODAR HTML SEM LIVE SERVER: http://192.168.1.2:5000/ (ip do notebook)
