from collections import deque

fila_comentarios = deque()

def adicionar_item(comentario: str, sentimento: str):
    fila_comentarios.append({
         "comentario": comentario,
         "sentimento": sentimento,
    })

def listar_comentarios():
    coments = []
    for item in fila_comentarios: 
        if "comentario" in item and "sentimento" in item:
            coments.append(item)

        return(coments)
    
    
print("ok!")