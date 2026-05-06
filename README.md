# Gestor de tareas

Proyecto sencillo en Python para practicar Git, GitHub, ramas, commits, merges y conflictos.

## Funcionalidades

- Crear tareas.
- Listar tareas.
- Marcar tareas como completadas.
- Eliminar tareas.
- Asignar prioridad.
- Añadir fecha límite opcional.

## Estructura

```text
gestor-tareas/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── tests/
    └── test_app.py
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uso

```bash
python app.py
```

## Ejecutar pruebas

```bash
pytest
```

## Iniciar Git desde cero

```bash
git init
git add .
git commit -m "Versión inicial del gestor de tareas"
git branch -M main
```

## Prueba recomendada con dos carpetas

Clona o copia este proyecto en dos carpetas:

```text
pruebas-git/
├── gestor-tareas-dev1/
└── gestor-tareas-dev2/
```

Haz cambios distintos en el mismo archivo desde cada carpeta para practicar conflictos de merge.

Ejemplo de conflicto:

- En `dev1`, cambia la función `crear_tarea` para añadir una nueva propiedad.
- En `dev2`, cambia la misma función de otra manera.
- Sube primero los cambios de `dev1`.
- Después intenta subir los de `dev2`.
- Haz `git pull`, resuelve el conflicto y vuelve a hacer `git push`.
