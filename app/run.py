import uvicorn

if __name__ == "__main__":
    print("Iniciando servidor de análise de sentimento...")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)