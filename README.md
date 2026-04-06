# Deber: API de Login Sencilla con FastAPI

**Autor:** Juan Pablo Andino
**Semestre:** 3er Semestre - Ingeniería en Sistemas

## Descripción del Proyecto
Este repositorio contiene la implementación de una API REST mínima utilizando FastAPI. El objetivo principal de esta práctica es comprender la estructura básica de una API de autenticación, simulando un proceso de login contra una base de datos embebida (SQLite) a través de `sqlmodel`.

Para mantener la simplicidad requerida en la tarea, no se han implementado mecánicas complejas como JWT o manejo avanzado de sesiones; la API se encarga exclusivamente de validar las credenciales de usuario y contraseña y devolver el estado HTTP correspondiente.

## Requisitos
- Python 3.10+
- Dependencias listadas en `requirements.txt` (`fastapi`, `uvicorn`, `sqlmodel`).

## Instalación y Ejecución

1. Clonar este repositorio en tu máquina local.
2. Crear un entorno virtual para aislar las dependencias:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En macOS/Linux
   # En Windows usar: venv\Scripts\activate
