from typing import Dict

from fastapi import FastAPI

from app.routers import routers_products, routers_users

app = FastAPI()
app.include_router(routers_users.router)
app.include_router(routers_products.router)

MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"


@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}
