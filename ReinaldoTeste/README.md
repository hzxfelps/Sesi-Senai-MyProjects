## Visão geral

O sistema conecta:

* Notebook → servidor Flask (HTML + lógica)
* Robô Pepper → acessa o servidor e executa voz + navegação no tablet

Fluxo:

1. Tablet do Pepper abre interface web
2. Usuário aperta botão → ativa escuta
3. Pepper detecta palavra
4. Pepper responde com fala + abre página específica no tablet

---

## 1. Rodar o servidor (Notebook)

Instalar dependências:

```bash
pip install flask
```

Rodar:

```bash
python app.py
```

Importante:

* Substituir `IPSEUNOTEBOOK` pelo IP real do notebook
* Exemplo: `192.168.1.11`
* Porta usada: `5000`

Testar no navegador:

```
http://IPSEUNOTEBOOK:5000/
```

---

## 2. Estrutura das páginas

Rotas esperadas:

* `/` → tela inicial
* `/laser` → conteúdo corte a laser
* `/biologia` → conteúdo biologia

Arquivos HTML devem estar na pasta `templates/` do Flask.

---

## 3. Configuração no Choregraphe

### Blocos necessários

* 1x **Python Script** (código principal)
* (NÃO precisa de Speech Recognition box se estiver usando ALSpeechRecognition via código)

### Fluxo

```
onStart → Python Script
```

---

## 4. Código no Python do Choregraphe

Antes de rodar:

Substituir:

```python
"http://IPSEUNOTEBOOK:5000/"
```

pelo IP real do notebook.

---

## 5. Configuração do robô

* Robô e notebook devem estar no mesmo Wi-Fi
* Descobrir IP do robô pelo tablet
* Porta padrão NAOqi: `9559`
* Firewall do notebook deve liberar porta `5000`

---

## 6. Funcionamento esperado

1. Inicia behavior
2. Tablet abre automaticamente a interface
3. Clique em "ATIVAR VOZ"
4. Pepper fala: "Estou ouvindo vocês"
5. Usuário fala uma palavra:

   * "laser" → abre página de laser
   * "biologia" → abre página de biologia
   * "maker" → volta para início

---

## 7. Possíveis erros (debug rápido)

### Tablet não abre página

* IP errado no código
* Servidor Flask não rodando
* Testar URL no navegador do notebook

---

### Robô não fala

* Problema no `ALTextToSpeech`
* Testar:

```python
tts.say("teste")
```

---

### Voz não reconhece

* Verificar idioma:

```python
self.asr.setLanguage("Portuguese")
```

* Tentar aumentar confiança:

```python
if confianca < 0.6:
```

* Falar palavras EXATAS do vocabulário

---

### Nada acontece ao clicar no botão

* Verificar endpoint:

```
/estado?ouvindo=1
```

* Testar manualmente no navegador

---

### Robô abre páginas sozinho

* Bug de evento duplicado
* Verificar se `self.ouvindo_ativo` está sendo respeitado

---

### Delay ou travamento

* Loop usando `threading.Timer`
* Evitar chamadas muito rápidas (<1s)

---

## 8. Observações finais

* Melhor usar IP fixo no notebook
* Testar tudo no navegador antes de usar no robô
* Evitar mudar rotas sem atualizar o código do Pepper