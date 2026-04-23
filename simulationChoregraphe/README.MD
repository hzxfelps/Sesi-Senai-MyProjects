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


ERROS COMUNS
IP errado (esse é o principal)
Firewall bloqueando porta 5000
ESP32 e notebook não estão na mesma rede
esquecer host="0.0.0.0" no Flask