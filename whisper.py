import whisper
from langchain_ollama.llms import OllamaLLM

print("1. Carregando o modelo Whisper (large)...")

whisper = whisper.load_model("large") 

print("Transcrevendo o arquivo de áudio... (hino.mp3)")
resultado = whisper.transcribe("hino.mp3")

print("--- Texto Transcrito ---")
print(resultado["text"])
print("------------------------")

prompt = (
    "Você é um assistente especialista em resumos."
    " Leia o texto transcrito abaixo e gere um resumo destacando os principais pontos-chave"
    "em formato de tópicos.\n"
    f"Texto: {resultado['text']}"
)

print(f"2. Enviando transcrição para o Ollama (modelo: llama 3.2:latest)...")

resumo = OllamaLLM(model="llama3.2:latest").invoke(prompt)

print("--- Pontos-Chave Extraídos pelo Ollama ---")
print(resumo)
print("------------------------------------------")