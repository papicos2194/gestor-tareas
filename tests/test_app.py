import pytest

from app import tareas, crear_tarea, listar_tareas, completar_tarea, eliminar_tarea


def setup_function():
    tareas.clear()


def test_crear_tarea():
    tarea = crear_tarea("Subir proyecto a Git")

    assert tarea["id"] == 1
    assert tarea["titulo"] == "Subir proyecto a Git"
    assert tarea["prioridad"] == "media"
    assert tarea["fecha_limite"] is None
    assert tarea["completada"] is False


def test_crear_tarea_con_prioridad_y_fecha_limite():
    tarea = crear_tarea("Entregar práctica", prioridad="alta", fecha_limite="2026-05-01")

    assert tarea["prioridad"] == "alta"
    assert tarea["fecha_limite"] == "2026-05-01"


def test_no_permite_titulo_vacio():
    with pytest.raises(ValueError):
        crear_tarea("")


def test_listar_tareas():
    crear_tarea("Tarea 1")
    crear_tarea("Tarea 2")

    assert len(listar_tareas()) == 2


def test_completar_tarea():
    tarea = crear_tarea("Crear una rama")
    tarea_completada = completar_tarea(tarea["id"])

    assert tarea_completada["completada"] is True


def test_completar_tarea_inexistente():
    resultado = completar_tarea(999)

    assert resultado is None


def test_eliminar_tarea():
    tarea = crear_tarea("Eliminar esta tarea")

    resultado = eliminar_tarea(tarea["id"])

    assert resultado is True
    assert listar_tareas() == []


def test_eliminar_tarea_inexistente():
    resultado = eliminar_tarea(999)

    assert resultado is False
