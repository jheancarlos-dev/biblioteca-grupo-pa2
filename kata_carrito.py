class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self) -> None:
        self.total = 0.0
        self._productos = []

    def agregar(self, producto: Producto) -> None:
        if producto.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if not producto.nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío")
        self._productos.append(producto)
        self.total += producto.precio