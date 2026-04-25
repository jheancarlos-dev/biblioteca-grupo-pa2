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