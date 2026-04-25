from models import Usuario, Libro, Prestamo


def test_crear_usuario():
    usuario = Usuario(nombre="Jhean", tipo="estudiante")
    assert usuario.nombre == "Jhean"
    assert usuario.tipo == "estudiante"

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base


def test_guardar_y_recuperar_usuario_en_base_de_datos():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        usuario = Usuario(nombre="Jhean", tipo="estudiante")
        session.add(usuario)
        session.commit()

        recuperado = session.query(Usuario).filter_by(nombre="Jhean").first()
        assert recuperado is not None
        assert recuperado.tipo == "estudiante"