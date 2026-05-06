"""Aplicación sencilla de gestión de tareas para practicar Git y GitHub."""


tareas = []


def crear_tarea(titulo, prioridad="media", fecha_limite=None):
    """Crea una tarea y la añade a la lista global de tareas."""
    if not titulo.strip():
        raise ValueError("El título de la tarea no puede estar vacío")

    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "prioridad": prioridad,
        "fecha_limite": fecha_limite,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea


def listar_tareas():
    """Devuelve todas las tareas."""
    return tareas


def completar_tarea(id_tarea):
    """Marca una tarea como completada por su ID."""
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            return tarea
    return None


def eliminar_tarea(id_tarea):
    """Elimina una tarea por su ID."""
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tareas.remove(tarea)
            return True
    return False


if __name__ == "__main__":
    crear_tarea("Aprender Git")
    crear_tarea("Practicar conflictos de merge", prioridad="alta", fecha_limite="2026-05-01")

    for tarea in listar_tareas():
        print(tarea)
