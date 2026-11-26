# Declaración de uso de IA

Durante el desarrollo de la práctica no se emplearon herramientas de IA, dado que el enunciado se encuentra muy guiado. Únicamente se recurrió a un modelo gratuito, Big Pickle, a través de opencode para dar formato al README y redactar esta declaración de uso de IA.

## Prompts utilizado

```text
Promt 1:

"Adaptame el readme existente (sin introducir grandes cambios, es más una cuestión de formato) a un estilo mas profesional, teniendo en cuenta el contexto de la práctica.
CONTEXTO DE LA PRÁCTICA (Ciclo DevOps con GitHub Actions - Universidad de León):
- Escenario: Módulo Python para un robot móvil (`robot.py`) con la función `can_move(distance: float) -> bool` que devuelve `True` si `distance > 0.5`, `False` si `<= 0.5`, y lanza `ValueError` si `distance < 0`. Incluye pruebas unitarias en `test_robot.py` con `pytest` (`requirements.txt` con `pytest>=8,<10`).
- Estructura del repo (`devops-robot-demo`): `robot.py`, `test_robot.py`, `requirements.txt`, `README.md`, `AI_USAGE.md`, `.github/workflows/ci.yml` y `.github/workflows/release.yml`.
- Flujo de trabajo (5 fases):
  1. Setup: Crear repo en rama `main`, implementar `robot.py`, `test_robot.py` (4 tests: seguro, inseguro, límite 0.5, negativo) y `README.md`.
  2. CI (`.github/workflows/ci.yml`): Ejecuta `pytest` en cada `push` o `pull_request` hacia `main` (Python 3.12).
  3. Simulación de fallo: Crear Issue ("Improve obstacle detection"), rama `feature/obstacle-detection`, cambiar umbral a `0.1` para forzar fallo en el PR, diagnosticar en Actions, corregir a `0.5` y hacer merge a `main` (opcional: proteger rama `main`)."

Promt 2:

Da formato al AI_usage. Puedes cambiar ligeramente el estilo del parrafo inicial (SIN CAMBIAR NADA DEL SIGNIFICADO) pero no puedes tocar ni una letra del promt.
```
