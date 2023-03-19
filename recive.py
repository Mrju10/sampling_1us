import machine
import time

# Configurar los pines de entrada
pines_entrada = [machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP),
                 machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP),
                 machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP),
                 machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)]

# Configurar el tiempo de espera entre cada muestra (en segundos)
tiempo_espera = 0.01

# Inicializar la lista de muestras
muestras = []

# Capturar las muestras
for i in range(100):
    # Leer los valores de los pines de entrada y almacenarlos en una lista
    valores = [pin.value() for pin in pines_entrada]
    muestras.append(valores)

    # Esperar el tiempo de espera antes de tomar la siguiente muestra
    time.sleep(tiempo_espera)

# Imprimir la lista de muestras capturadas
print(muestras)
