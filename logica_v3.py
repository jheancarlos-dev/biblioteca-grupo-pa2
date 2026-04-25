from abc import ABC, abstractmethod
from datetime import date, timedelta

DIAS_PRESTAMO_ESTUDIANTE: int = 7
DIAS_PRESTAMO_OTROS_USUARIOS: int = 15


class PoliticaPrestamo(ABC):
    @abstractmethod
    def obtener_dias_prestamo(self) -> int:
        ...


class PoliticaEstudiante(PoliticaPrestamo):
    def obtener_dias_prestamo(self) -> int:
        return DIAS_PRESTAMO_ESTUDIANTE


class PoliticaDocente(PoliticaPrestamo):
    def obtener_dias_prestamo(self) -> int:
        return DIAS_PRESTAMO_OTROS_USUARIOS


class BibliotecaService:
    MULTA_POR_DIA_POR_LIBRO: float = 0.50

    def __init__(self, politica: PoliticaPrestamo) -> None:
        if politica is None:
            raise TypeError("La política de préstamo no puede ser None")
        self._politica: PoliticaPrestamo = politica

    def calcular_prestamo(
        self, dias_retraso: int, cantidad_libros: int
    ) -> tuple[float, date]:
        if dias_retraso < 0:
            raise ValueError("dias_retraso no puede ser negativo")
        if cantidad_libros <= 0:
            raise ValueError("cantidad_libros debe ser mayor que cero")

        plazo_prestamo_en_dias: int = self._politica.obtener_dias_prestamo()

        monto_total_multa: float = (
            dias_retraso * cantidad_libros * self.MULTA_POR_DIA_POR_LIBRO
        )

        fecha_limite_devolucion: date = date.today() + timedelta(
            days=plazo_prestamo_en_dias
        )

        return monto_total_multa, fecha_limite_devolucion

class PoliticaInvitado(PoliticaPrestamo):
    def obtener_dias_prestamo(self) -> int:
        return 3