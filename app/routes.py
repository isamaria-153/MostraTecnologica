from fastapi import Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app import app, templates
from app.sentiment import analisar_sentimento
from app.fila import adicionar_item, listar_comentarios


class Comentario(BaseModel):
    texto: str

@app.get("/sent", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/sentimento")
async def analisar(comentario: Comentario):
    sentimento = analisar_sentimento(comentario.texto)
    adicionar_item(comentario.texto, sentimento)
    return {"sentimento": sentimento}

@app.get("/fila")
async def fila():
    return listar_comentarios()