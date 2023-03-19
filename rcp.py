import machine
import utime

# Configuración de pines de entrada
pines_entrada = [machine.Pin(pin, machine.Pin.IN) for pin in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]


# Constante de conversión de bits a voltajes
CONVERSION_VOLTAJE = 3.3 / (2 ** 12 - 1)

# Captura de muestras
muestras = []
for i in range(100):
    # Esperar 10ms
    utime.sleep_ms(1)
    
    # Leer los valores de los pines de entrada y almacenarlos en una lista
    valores = [pin.value() for pin in pines_entrada]
    muestras.append(valores)

# Conversión de muestras a voltajes
voltajes = []
for muestra in muestras:
    # Convertir la lista de valores a un número entero
    n = sum([val * (1 << i) for i, val in enumerate(muestra)])
    # Calcular el voltaje correspondiente utilizando la constante de conversión
    V = n * CONVERSION_VOLTAJE
    # Almacenar el voltaje calculado en una lista
    voltajes.append(V)

# Imprimir la lista de voltajes
print(voltajes)
