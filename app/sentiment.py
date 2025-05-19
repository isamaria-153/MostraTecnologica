from transformers import pipeline
import os

sentiment_pipeline = None

def get_pipeline():
    global sentiment_pipeline
    if sentiment_pipeline is None:
        print("Carregando modelo de análise de sentimento...")
        sentiment_pipeline = pipeline(
            "sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
        print("Modelo carregado com sucesso!")
    return sentiment_pipeline

def analisar_sentimento(texto):
    try:
        pipe = get_pipeline()
        resultado = pipe(texto)[0]
        estrelas = int(resultado['label'][0])
        
        if estrelas <= 2:
            return "negativo"
        elif estrelas == 3:
            return "neutro"
        else:
            return "positivo"
    except Exception as e:
        print(f"Erro na análise de sentimento: {e}")
        return "erro"

        
""" # Criar diretório para cache de modelos se não existir
os.makedirs("models", exist_ok=True)

# Configurar o cache do modelo para usar o diretório local
os.environ["TRANSFORMERS_CACHE"] = os.path.abspath("models")

# Inicializar o pipeline de análise de sentimento
# Isso baixará o modelo na primeira execução """