from app import app

def test_pagina_principal():
    with app.test_client() as client:
        respuesta = client.get("/")
        assert respuesta.status_code == 200 
