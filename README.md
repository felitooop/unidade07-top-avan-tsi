# Transcrição de Áudio com Whisper e Extração de Pontos-Chave com Ollama

## Descrição do Projeto

Este projeto é um script em Python projetado para processar arquivos de áudio de forma totalmente local.

O fluxo de funcionamento do script é simples e direto:
1. Carrega o modelo `large` do Whisper.
2. Lê um arquivo de áudio local (`hino.mp3`) e transcreve seu conteúdo.
3. Imprime o texto completo no terminal.
4. Envia o texto transcrito para um modelo LLM local (`llama3.2:latest` rodando no Ollama) com um prompt focado em extrair os pontos-chave em formato de tópicos.
5. Exibe o resumo final gerado pela IA.

---

## Pré-requisitos e Instalação

Para que o script funcione corretamente, você precisará de dependências tanto do sistema operacional quanto do Python.

### 1. Requisitos do Sistema

* **Python** instalado.
* **FFmpeg:** O Whisper requer a ferramenta de linha de comando `ffmpeg` para processar arquivos de áudio.
  * **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install ffmpeg`
  * **Windows:** Instale via [Winget]: `winget install ffmpeg`

### 2. Instalação do Ollama e do Modelo LLM

O script utiliza o Ollama para rodar o modelo de resumo localmente.
1. Baixe e instale o **Ollama** em [ollama.com](https://ollama.com/).
2. Abra o terminal e faça o download do modelo Llama 3.2:
```bash 
ollama pull llama3.2:latest
```
## 3. Dependências do Python
### Instalação das bibliotecas necessárias:
```bash
pip install openai-whisper langchain langchain-ollama 
```

## 4. Execução do Script
1. Coloque o arquivo de áudio que você deseja transcrever no mesmo diretório do script.
2. Certifique-se de que o nome do arquivo seja hino.mp3 (ou altere o nome diretamente no código do arquivo whisper.py na linha resultado = whisper.transcribe("hino.mp3")).
3. Execute o script Python:
```bash
python whisper.py
```