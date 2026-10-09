import json
import random
import time


class Adquisicion:
    """
    Se encarga de obtener los datos provenientes
    del dispositivo simulado.
    """

    def __init__(self):
        self.device_id = "SENSOR-001"

    def recibir_datos(self):
        """
        Simula la recepción de una trama enviada
        por el firmware.
        """

        # Simulación de pérdida de comunicación
        if random.random() < 0.05:
            raise ConnectionError("No se pudo establecer comunicación con el dispositivo.")

        # Simulación de dato corrupto
        if random.random() < 0.05:
            return '{"device_id": "SENSOR-001", "temperature": "ERROR"}'

        # Datos normales
        temperatura = round(random.uniform(20, 35), 2)
        humedad = round(random.uniform(40, 80), 2)
        voltaje = round(random.uniform(4.5, 5.2), 2)

        # Algunas veces generamos una temperatura anormal
        if random.random() < 0.20:
            temperatura = round(random.uniform(70, 90), 2)

        datos = {
            "device_id": self.device_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": temperatura,
            "humidity": humedad,
            "voltage": voltaje,
            "status": "ACTIVE"
        }

        return json.dumps(datos)