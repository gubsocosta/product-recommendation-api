import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Bem-vindo à API de Recomendação de Produtos"
    }


def test_criar_produto():
    payload = {"nome": "produto A", "categoria": "categoria 1", "tags": ["tag1", "tag2"]}

    response = client.post("/produtos", json=payload)

    assert response.status_code == 200
    assert response.json()["nome"] == payload["nome"]
    assert response.json()["categoria"] == payload["categoria"]


def test_listar_produtos():
    response = client.get("/produtos/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_criar_usuarios():
    nome_usuario = "User Test"
    response = client.post("/usuarios/", params={"nome": nome_usuario})

    assert response.status_code == 200

    dados_usuario = response.json()

    assert dados_usuario["id"] == 1
    assert dados_usuario["nome"] == nome_usuario


def test_listar_usuarios():
    response = client.get("/usuarios/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_criar_historico():
    response = client.post("/historico_compras/1", json={"produtos_ids": [1]})

    assert response.status_code == 200
    assert response.json() == {"mensagem": "Histórico de compras atualizado"}


def test_recomendar_produtos():
    response = client.post("/recomendacoes/1", json={
        "categorias": ["categoria 1"],
        "tags": ["tag1", "tag2"] 
    })

    assert response.status_code == 200
    assert len(response.json()) == 1

