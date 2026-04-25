import pytest

from kata_carrito import Carrito


def test_carrito_vacio_tiene_total_cero():
    carrito = Carrito()
    assert carrito.total == 0.0 

from kata_carrito import Carrito, Producto


def test_agregar_un_producto_suma_al_total():
    carrito = Carrito()
    producto = Producto("Libro", 25.0)
    carrito.agregar(producto)
    assert carrito.total == 25.0

def test_eliminar_producto_resta_del_total():
    carrito = Carrito()
    producto = Producto("Lápiz", 15.0)
    carrito.agregar(producto)
    carrito.eliminar(producto)
    assert carrito.total == 0.0

def test_carrito_con_dos_productos_tiene_cantidad_dos():
    carrito = Carrito()
    carrito.agregar(Producto("A", 10.0))
    carrito.agregar(Producto("B", 20.0))
    assert carrito.obtener_cantidad() == 2

def test_no_permitir_precio_negativo():
    carrito = Carrito()
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        carrito.agregar(Producto("X", -5.0))

def test_no_permitir_nombre_vacio():
    carrito = Carrito()
    with pytest.raises(ValueError, match="nombre del producto no puede estar vacío"):
        carrito.agregar(Producto("", 10.0))

def test_no_permitir_precio_negativo():
    carrito = Carrito()
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        carrito.agregar(Producto("X", -5.0))

def test_no_permitir_nombre_vacio():
    carrito = Carrito()
    with pytest.raises(ValueError, match="nombre del producto no puede estar vacío"):
        carrito.agregar(Producto("", 10.0))