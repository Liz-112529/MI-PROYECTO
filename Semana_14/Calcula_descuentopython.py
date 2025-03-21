def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el monto en función del porcentaje dado.
    :param monto_total: float - Monto total de la compra
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto es 10%)
    :return: float - Monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento  # Asegúrate de que el 'return' esté alineado con la línea anterior

# Llamada a la función
monto1 = 830.90
monto2 = 575.00
porcentaje_descuento2 = 25

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)

# Cálculo del monto final a cancelar
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# Mostrar en pantalla los resultados
print(f"Compra 1: Monto total: ${monto1:.2f}, descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")
print(f"Compra 2: Monto total: ${monto2:.2f}, descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")