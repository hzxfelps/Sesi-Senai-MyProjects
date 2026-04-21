# Projeto Makerthon – Sistema Inteligente com Robô Pepper (Léia)

## Visão Geral

Este projeto propõe um sistema educacional interativo no qual um robô humanoide (Pepper, chamado de Léia) auxilia grupos de alunos durante atividades em sala de aula.

Cada grupo possui um painel físico com um potenciômetro e LEDs. Esse painel permite que os alunos indiquem, em tempo real, o nível de entendimento da atividade.

Com base nesses dados, o sistema identifica automaticamente quais grupos precisam de mais apoio. O robô, então, se desloca até esses grupos e realiza intervenções pedagógicas de forma orientadora.

---

## Como o sistema funciona

O funcionamento segue uma sequência simples:

1. O grupo interage com o painel girando o potenciômetro  
2. O ESP32 lê esse valor e transforma em um nível de 0 a 10  
3. O ESP32 envia esse dado para o notebook via HTTP  
4. O servidor no notebook armazena e organiza essas informações  
5. O robô consulta o servidor periodicamente  
6. O sistema retorna qual grupo precisa de ajuda  
7. O robô se desloca até o grupo  
8. O robô inicia a interação com os alunos  

---

## Arquitetura do sistema

[ Painel (potenciômetro + LEDs) ]  
                ↓  
             ESP32  
                ↓ (HTTP)  
      Servidor no Notebook  
                ↓ (GET /next)  
          Robô Pepper  

---

## Estrutura do projeto

/project  
│  
├── esp32/  
│   ├── main.ino  
│   └── wifi_config.h  
│  
├── server/  
│   ├── app.py  
│   ├── routes.py  
│   └── data_store.py  
│  
├── robot/  
│   ├── get_next.py  
│   ├── movement.py  
│   └── speech.py  
│  
└── README.md  

---

## Parte 1 – ESP32 (coleta de dados)

### main.ino

Esse arquivo é responsável por:

- Conectar o ESP32 ao Wi-Fi  
- Ler o valor do potenciômetro  
- Converter esse valor em um nível de 0 a 10  
- Enviar esses dados para o servidor via requisição HTTP  

Exemplo de envio:  
/update?grupo=1&nivel=3  

Isso indica que o grupo 1 está com nível 3 de compreensão.

---

### wifi_config.h

Esse arquivo contém:

- Nome da rede Wi-Fi  
- Senha  
- IP do servidor (notebook)  

A ideia é facilitar alterações sem precisar modificar o código principal.

---

## Parte 2 – Servidor (Notebook)

O servidor é o núcleo do sistema. Ele recebe, organiza e distribui os dados.

### app.py

Arquivo principal que inicializa o servidor Flask.

Ele permite que o ESP32 envie dados e que o robô consulte essas informações.

---

### routes.py

Define as rotas do sistema.

#### /update

Recebe dados do ESP32.

Exemplo:  
/update?grupo=2&nivel=1  

Função:
- Armazena o nível de cada grupo  
- Atualiza os dados em tempo real  

---

#### /next

Utilizado pelo robô.

Função:
- Analisa todos os grupos  
- Retorna aquele com maior necessidade de ajuda (menor nível)  

Exemplo de resposta:

{
  "grupo": 2,
  "nivel": 1
}

---

### data_store.py

Responsável por armazenar os dados dos grupos.

Estrutura simples, como:

grupos = {
  1: 5,
  2: 1,
  3: 7
}

---

## Parte 3 – Robô Pepper (Léia)

O robô funciona de forma ativa. Ele não recebe comandos diretamente, mas consulta o servidor constantemente para saber o que fazer.

---

### get_next.py

Responsável por:

- Fazer requisições para o servidor (/next)  
- Receber o grupo prioritário  
- Enviar esses dados para os outros módulos do robô  

---

### movement.py

Responsável pelo movimento do robô.

Utiliza a API ALMotion para:

- Ativar o robô  
- Movimentá-lo até o grupo correspondente  

As posições dos grupos são definidas previamente e podem ser ajustadas conforme o ambiente.

---

### speech.py

Responsável pela fala do robô.

Utiliza o sistema de Text-to-Speech para interagir com os alunos.

Exemplo de fala:
"Indo ajudar o grupo 2"

---

## Lógica de priorização

A regra utilizada é simples:

Quanto menor o nível informado pelo grupo, maior a prioridade de atendimento.

Exemplo:

Grupo 1 → nível 8  
Grupo 2 → nível 2  
Grupo 3 → nível 5  

Nesse caso, o robô irá primeiro ao grupo 2.

---

## Estratégia pedagógica

O robô não entrega respostas prontas. Ele atua como mediador do aprendizado, seguindo três níveis de intervenção:

1. Reflexiva  
   Perguntas abertas para estimular o pensamento  

2. Guiada  
   Direciona o raciocínio com mais foco  

3. Orientadora  
   Sugere caminhos possíveis, sem entregar a solução  

Essa abordagem incentiva autonomia, pensamento crítico e participação ativa dos alunos.

---

## Tecnologias utilizadas

- ESP32 para coleta de dados  
- Flask para o servidor  
- HTTP para comunicação  
- Python para lógica do sistema  
- Choregraphe para programação do robô  
- NAOqi para controle de movimento e fala  
