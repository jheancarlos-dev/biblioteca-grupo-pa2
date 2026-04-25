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