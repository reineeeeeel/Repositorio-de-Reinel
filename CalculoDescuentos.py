# Nombres y Apellidos: Reinel Alejandro Jaramillo Aguirre

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el porcentaje dado.

    :param monto_total: Total de la compra en dólares
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%)
    :return: Monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

monto1 = 150
monto2 = 300

descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

descuento2 = calcular_descuento(monto2, 20)
monto_final2 = monto2 - descuento2

print(f"Compra de ${monto1}: Descuento de ${descuento1:.2f}, Total a pagar: ${monto_final1:.2f}")
print(f"Compra de ${monto2}: Descuento de ${descuento2:.2f}, Total a pagar: ${monto_final2:.2f}")