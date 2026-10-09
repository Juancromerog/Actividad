import json
import random
import time
from datetime import datetime


DEVICE_ID = "SENSOR-001"


def generar_telemetria(numero):

    # Cada 5 lecturas generamos una temperatura anormal
    if numero % 5 == 0:
        temperatura = round(random.uniform(70, 90), 2)
    else:
        temperatura = round(random.uniform(20, 35), 2)

    humedad = round(random.uniform(40, 80), 2)
    voltaje = round(random.uniform(4.5, 5.2), 2)

    datos = {
        "device_id": DEVICE_ID,
        "timestamp": datetime.now().isoformat(),
        "temperature": temperatura,
        "humidity": humedad,
        "voltage": voltaje,
        "status": "ACTIVE"
    }

    return datos


def main():
    print("=" * 50)
    print("SIMULADOR DE FIRMWARE")
    print("=" * 50)
    print(f"Dispositivo: {DEVICE_ID}")
    print("Generando telemetría...")
    print("Presione CTRL+C para detener.\n")

    contador = 1

    try:
        while True:
            datos = generar_telemetria(contador)

            print(json.dumps(datos, indent=2))

            contador += 1
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nSimulador detenido.")


if __name__ == "__main__":
    main()