# 📚 Sistema de Gestión de Préstamos - Biblioteca Central "Mario Vargas Llosa"

Proyecto académico para el curso de **Construcción de Software**  
**PA2 & PA3** – Control de Versiones, TDD, Katas y ORM.

---

## 🚀 Descripción

Aplicación web desarrollada con **Python/Flask** que automatiza el cálculo de fechas de devolución y multas por retraso en el préstamo de libros.

El proyecto evolucionó en dos fases:
- **PA2**: Implementación de control de versiones con GitFlow, colaboración en equipo y CI/CD con GitHub Actions.
- **PA3**: Aplicación de Desarrollo Guiado por Pruebas (TDD), resolución de problemas mediante Katas TDD e integración de Mapeo Objeto-Relacional (ORM) con SQLAlchemy.

---

## 🛠️ Tecnologías utilizadas

| Área | Herramientas |
|------|--------------|
| **Backend** | Python 3.13, Flask 3.0 |
| **Base de Datos** | SQLite (desarrollo), SQLAlchemy ORM |
| **Pruebas** | Pytest, pytest-cov (cobertura) |
| **CI/CD** | GitHub Actions |
| **Control de Versiones** | Git, GitHub, GitFlow |
| **Calidad de Código** | Clean Code, Refactorización, TDD |

---

## 🧪 Pruebas y Cobertura

El proyecto incluye una suite de **19 pruebas unitarias y de integración**, con una cobertura superior al **89%**.

- `test_logica.py`: Validación de políticas de préstamo y casos borde.
- `test_kata_carrito.py`: Kata TDD "Carrito de Compras".
- `test_models.py`: Integración de modelos ORM con base de datos en memoria.
- `test_app.py`: Prueba de endpoint Flask.

El pipeline de CI/CD ejecuta automáticamente las pruebas en cada Pull Request.

---

## 👥 Equipo

| Integrante | Rol |
|------------|-----|
| Jhean Carlos | Líder / Arquitecto |
| Alejandro Valdivia | Desarrollador de pruebas |
| Higler Miki Mamani | Desarrollador de modelos |
| Jorge Junior Corrales | Desarrollador de integración |

---

## 📂 Estructura del proyecto

biblioteca-grupo-pa2/
├── .github/workflows/ci.yml   # Pipeline CI/CD
├── app.py                     # Aplicación Flask
├── logica_v3.py               # Lógica de préstamos (Strategy)
├── models.py                  # Modelos ORM (Usuario, Libro, Prestamo)
├── kata_carrito.py            # Kata TDD
├── test_logica.py             # Tests unitarios de lógica
├── test_kata_carrito.py       # Tests de la kata
├── test_models.py             # Tests de integración ORM
├── test_app.py                # Test de Flask
├── requirements.txt           # Dependencias
├── .coveragerc                # Configuración de cobertura
└── templates/                 # Plantillas HTML
