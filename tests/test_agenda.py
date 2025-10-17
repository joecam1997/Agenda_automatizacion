import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json
import pytest
from agenda import cargar_contactos, guardar_contactos, crear_contacto

ARCHIVO = "agenda.json"

@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Elimina el archivo antes y después de cada prueba."""
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)
    yield
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)

def test_guardar_y_cargar_contactos():
    contactos = [{"nombre": "Juan", "telefono": "123", "email": "juan@test.com"}]
    guardar_contactos(contactos)
    cargados = cargar_contactos()
    assert cargados == contactos

def test_crear_contacto_nuevo(monkeypatch):
    """Verifica que se pueda crear un contacto correctamente."""
    contactos = []
    inputs = iter(["Pedro", "999", "pedro@test.com"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    crear_contacto(contactos)
    assert len(contactos) == 1
    assert contactos[0]["nombre"] == "Pedro"

def test_no_crea_contacto_duplicado(monkeypatch):
    contactos = [{"nombre": "Ana", "telefono": "111", "email": "ana@test.com"}]
    inputs = iter(["Ana", "222", "ana2@test.com"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    crear_contacto(contactos)
    assert len(contactos) == 1  # No debe duplicar
