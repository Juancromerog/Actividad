class Procesamiento:

    def validar_datos(self, datos):
        """
        Valida estructura, tipos y rangos.
        """

        campos_requeridos = [
            "device_id",
            "timestamp",
            "temperature",
            "humidity",
            "voltage",
            "status"
        ]

        # Comprobar campos
        for campo in campos_requeridos:
            if campo not in datos:
                return False, f"Falta el campo: {campo}"

        # Comprobar tipos
        if not isinstance(datos["temperature"], (int, float)):
            return False, "La temperatura no es numérica."

        if not isinstance(datos["humidity"], (int, float)):
            return False, "La humedad no es numérica."

        if not isinstance(datos["voltage"], (int, float)):
            return False, "El voltaje no es numérico."

        # Comprobar rangos
        if not 0 <= datos["humidity"] <= 100:
            return False, "Humedad fuera de rango."

        if not 3.0 <= datos["voltage"] <= 5.5:
            return False, "Voltaje fuera de rango."

        return True, "Datos válidos."

    def clasificar(self, datos):
        """
        Determina si los datos representan
        una condición normal o anómala.
        """

        if datos["temperature"] > 50:
            return "ANOMALIA: temperatura fuera de rango"

        return "NORMAL"