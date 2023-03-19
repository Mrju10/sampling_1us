from machine import DMA
import utime

# Configuración de pines de entrada
pines_entrada = [machine.Pin(pin, machine.Pin.IN) for pin in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
pin_dma = machine.Pin(14, machine.Pin.IN) # Pin de control del DMA

# Constante de conversión de bits a voltajes
CONVERSION_VOLTAJE = 3.3 / (2 ** 12 - 1)

# Configuración de DMA
dma_channel = 0
dma_buffer = bytearray(2 * len(pines_entrada))
dma = machine.DMA(channel=dma_channel, source=pin_dma, destination=dma_buffer, transfer_size=2, transfer_width=2, repeat_count=len(pines_entrada), dreq=machine.Pin(15))

# Captura de muestras
muestras = []
dma.start()
for i in range(100):
    # Esperar a que el DMA termine la transferencia
    while dma.busy():
        pass
    
    # Leer los valores de los pines de entrada y almacenarlos en una lista
    valores = [dma_buffer[j] | (dma_buffer[j + 1] << 8) for j in range(0, len(dma_buffer), 2)]
    muestras.append(valores)
    
    # Reiniciar el DMA para la siguiente transferencia
    dma.start()

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
