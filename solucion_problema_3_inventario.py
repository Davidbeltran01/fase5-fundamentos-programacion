"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación
Problema 3: Control de reabastecimiento de inventario

El programa revisa el stock de cada artículo y calcula cuántas unidades
se deben solicitar para alcanzar, como mínimo, el nivel requerido.
"""

def calcular_reabastecimiento(stock_actual, stock_minimo):
    """Devuelve las unidades necesarias para llegar al stock mínimo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def generar_informe(inventario):
    """Recorre la matriz y muestra el estado de cada artículo."""
    print("\n" + "=" * 72)
    print("INFORME DE REABASTECIMIENTO DE INVENTARIO")
    print("=" * 72)
    print(f"{'Código':<10}{'Artículo':<24}{'Stock':>9}{'Mínimo':>10}{'Pedir':>10}")
    print("-" * 72)

    articulos_por_pedir = 0
    unidades_totales = 0

    for articulo in inventario:
        codigo, nombre, stock_actual, stock_minimo = articulo
        cantidad_pedir = calcular_reabastecimiento(stock_actual, stock_minimo)

        print(
            f"{codigo:<10}{nombre:<24}{stock_actual:>9}"
            f"{stock_minimo:>10}{cantidad_pedir:>10}"
        )

        if cantidad_pedir > 0:
            articulos_por_pedir += 1
            unidades_totales += cantidad_pedir

    print("-" * 72)
    print(f"Artículos que necesitan reabastecimiento: {articulos_por_pedir}")
    print(f"Unidades necesarias en total: {unidades_totales}")
    print("=" * 72)


def main():
    # Datos de ejemplo creados para simular un pequeño almacén tecnológico.
    inventario = [
        ["TEC-101", "Teclado inalámbrico", 7, 12],
        ["TEC-102", "Mouse óptico", 18, 10],
        ["TEC-103", "Audífonos USB", 4, 9],
        ["TEC-104", "Cable HDMI", 6, 15],
        ["TEC-105", "Memoria USB 64 GB", 11, 11],
        ["TEC-106", "Base para portátil", 2, 6],
    ]

    generar_informe(inventario)


if __name__ == "__main__":
    main()
