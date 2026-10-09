import json
import csv
import logging
import os
import time

from adquisicion import Adquisicion
from procesamiento import Procesamiento
from sistema import Sistema


# ==========================================
# CONFIGURACIÓN
# ==========================================

os.makedirs("../datos", exist_ok=True)
os.makedirs("../logs", exist_ok=True)

logging.basicConfig(
    filename="../logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# ==========================================
# OBJETOS
# ==========================================

adquisicion = Adquisicion()
procesamiento = Procesamiento()
sistema = Sistema()


# ==========================================
# ARCHIVO CSV
# ==========================================

archivo_csv = "../datos/telemetria.csv"

with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:

    escritor = csv.writer(archivo)

    escritor.writerow([
        "timestamp",
        "device_id",
        "temperature",
        "humidity",
        "voltage",
        "resultado"
    ])


# ==========================================
# EJECUCIÓN
# ==========================================

print("=" * 60)
print("SISTEMA DE INTEGRACIÓN HARDWARE - SOFTWARE - FIRMWARE")
print("=" * 60)

print("Sistema operativo:", sistema.obtener_informacion()["sistema_operativo"])
print("Procesos detectados:", sistema.obtener_informacion()["procesos"])
print()

logging.info("Aplicacion iniciada.")

total = 0
validos = 0
anomalias = 0
errores = 0


for ciclo in range(15):

    total += 1

    print(f"\n--- CICLO {ciclo + 1} ---")

    try:

        # --------------------------------------
        # ADQUISICIÓN
        # --------------------------------------

        trama = adquisicion.recibir_datos()

        # --------------------------------------
        # CONVERSIÓN JSON
        # --------------------------------------

        datos = json.loads(trama)

        # --------------------------------------
        # VALIDACIÓN
        # --------------------------------------

        valido, mensaje = procesamiento.validar_datos(datos)

        if not valido:

            errores += 1

            print("ERROR:", mensaje)

            logging.error(
                f"Dato rechazado: {mensaje}"
            )

            continue

        validos += 1

        # --------------------------------------
        # CLASIFICACIÓN
        # --------------------------------------

        resultado = procesamiento.clasificar(datos)

        if resultado != "NORMAL":
            anomalias += 1

            print("⚠", resultado)

            logging.warning(
                f"{datos['device_id']} - {resultado}"
            )

        else:

            print("Estado: NORMAL")

            logging.info(
                f"{datos['device_id']} - Datos normales"
            )

        # --------------------------------------
        # MOSTRAR DATOS
        # --------------------------------------

        print("Temperatura:", datos["temperature"], "°C")
        print("Humedad:", datos["humidity"], "%")
        print("Voltaje:", datos["voltage"], "V")

        # --------------------------------------
        # GUARDAR CSV
        # --------------------------------------

        with open(
                archivo_csv,
                "a",
                newline="",
                encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow([
                datos["timestamp"],
                datos["device_id"],
                datos["temperature"],
                datos["humidity"],
                datos["voltage"],
                resultado
            ])

    except ConnectionError as error:

        errores += 1

        print("⚠ FALLO DE COMUNICACIÓN")
        print("El sistema continuará ejecutándose.")

        logging.error(
            f"Fallo de comunicación: {error}"
        )

    except json.JSONDecodeError:

        errores += 1

        print("⚠ DATO CORRUPTO")
        print("El sistema rechazó el dato y continúa.")

        logging.error(
            "Se recibió una trama JSON inválida."
        )

    except Exception as error:

        errores += 1

        print("⚠ ERROR CONTROLADO:", error)

        logging.exception(
            "Error inesperado controlado."
        )

    time.sleep(1)


# ==========================================
# REPORTE
# ==========================================

reporte = {
    "total_ciclos": total,
    "datos_validos": validos,
    "anomalias": anomalias,
    "errores": errores,
    "porcentaje_datos_validos":
        round((validos / total) * 100, 2)
        if total > 0 else 0
}


with open(
        "../datos/reporte.json",
        "w",
        encoding="utf-8"
) as archivo:

    json.dump(
        reporte,
        archivo,
        indent=4,
        ensure_ascii=False
    )


logging.info("Aplicacion finalizada.")

print("\n" + "=" * 60)
print("REPORTE FINAL")
print("=" * 60)

print("Ciclos:", total)
print("Datos válidos:", validos)
print("Anomalías:", anomalias)
print("Errores:", errores)
print("Datos válidos (%):", reporte["porcentaje_datos_validos"])

print("\nArchivos generados:")
print("../datos/telemetria.csv")
print("../datos/reporte.json")
print("../logs/sistema.log")