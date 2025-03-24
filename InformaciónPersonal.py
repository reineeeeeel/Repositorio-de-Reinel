# Nombres y Apellidos: Reine; Alejandro Jaramillo Aguirre

# Diccionario con información ficticia
información_personal = {
    "nombre": "Stiven Robalin",
    "edad": 27,
    "ciudad": "Esmeraldas",
    "profesión": "Auxiliar de ventas"
}

# Valor clave "ciudad" - modificación
información_personal["ciudad"] = "El Oro"

# Nueva clave-valor para "profesión"
información_personal["profesión"] = ("Supervisor de ventas")

# Ver si clave "teléfono" existe, caso contrario, agregar un ficticio
if"teléfono" not in información_personal:
    información_personal["teléfono"] = "0995867682"

# Eliminar clave "edad"
información_personal.pop("edad", None)

# Imprimir
print("Diccionario Final:", información_personal)