# Monitor de Criptomoedas com Alertas via WhatsApp

## 📝 Descrição
Um bot em Python que monitora o preço de criptomoedas através da API do Mercado Bitcoin e envia atualizações automáticas via WhatsApp, incluindo informações sobre lucro/prejuízo baseado em uma posição específica. També é possivel mudar a moeda a ser monitorada trocando no campo MOEDA do começo pela singla da sua moeda.

## 🚀 Funcionalidades
- Monitoramento em tempo real do preço de criptomoedas
- Envio automático de mensagens via WhatsApp
- Cálculo de lucro/prejuízo baseado em posição definida
- Acompanhamento de máximas e mínimas diárias
- Atualização a cada 5 minutos

## 📋 Pré-requisitos
- Python 3.x
- Chrome WebDriver
- Bibliotecas Python:
  - selenium
  - requests

## 🔧 Instalação


```python
pip install selenium requests
```

## ⚙️ Configuração
1. Baixe o ChromeDriver compatível com sua versão do Chrome
2. Atualize o caminho do ChromeDriver no código
3. Configure as variáveis:
   - MOEDA
   - LIMITE_INFERIOR
   - LIMITE_SUPERIOR
   - PRECO_COMPRA
   - QUANTIDADE_COMPRADA

## 🎯 Uso

```python
python monitor_cripto.py
```


## 📱 Primeira Execução
1. Execute o script
2. Escaneie o QR Code do WhatsApp Web quando solicitado
3. O bot começará a enviar atualizações automaticamente

## 🛠️ Tecnologias Utilizadas
- Python
- Selenium WebDriver
- API do Mercado Bitcoin
- WhatsApp Web

## ⚠️ Observações
- Necessário manter uma sessão ativa do WhatsApp Web
- Requer conexão estável com a internet
- O intervalo de atualização pode ser ajustado modificando o valor de `time.sleep()`

## 📄 Licença
Este projeto está sob a licença MIT.