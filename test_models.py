 
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Usuario, Libro, Prestamo


def test_crear_usuario():
    usuario = Usuario(nombre="Jhean", tipo="estudiante")
    assert usuario.nombre == "Jhean"
    assert usuario.tipo == "estudiante"


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


def test_usuario_puede_tener_multiples_prestamos():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    libro1 = Libro(titulo="El Quijote")
    libro2 = Libro(titulo="Cien Años de Soledad")

    with Session(engine) as session:
        session.add_all([libro1, libro2])

        usuario = Usuario(nombre="Jhean", tipo="estudiante")
        session.add(usuario)

        prestamo1 = Prestamo(
            fecha_prestamo=date.today(),
            fecha_devolucion=date.today(),
            multa=0.0,
            usuario=usuario,
            libro=libro1
        )
        prestamo2 = Prestamo(
            fecha_prestamo=date.today(),
            fecha_devolucion=date.today(),
            multa=5.0,
            usuario=usuario,
            libro=libro2
        )
        session.add_all([prestamo1, prestamo2])
        session.commit()

        usuario_recuperado = session.query(Usuario).filter_by(nombre="Jhean").first()
        assert len(usuario_recuperado.prestamos) == 2
        assert usuario_recuperado.prestamos[0].libro.titulo == "El Quijote"
        assert usuario_recuperado.prestamos[1].multa == 5.0