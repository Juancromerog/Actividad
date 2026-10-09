# Sistema de Integración Hardware, Software y Firmware

## 1. Descripción

Este proyecto implementa un prototipo de integración entre hardware simulado,
firmware, sistema operativo y una aplicación desarrollada en Python.

El sistema simula un dispositivo de monitoreo denominado SENSOR-001,
que genera información de temperatura, humedad y voltaje.

Los datos son recibidos, validados y procesados por la aplicación Python.
Posteriormente son almacenados en archivos CSV y JSON y se registran eventos
en un archivo de logs.

## 2. Arquitectura

El flujo general del sistema es:

Hardware simulado
↓
Firmware / simulador
↓
Comunicación
↓
Sistema operativo
↓
Aplicación Python
↓
Persistencia
↓
Reporte

## 3. Variables monitoreadas

- Temperatura
- Humedad
- Voltaje
- Estado del dispositivo

## 4. Condiciones anómalas

El sistema identifica como anomalía una temperatura superior a 50 °C.

También controla errores de comunicación y datos inválidos.

## 5. Recursos del sistema operativo

La aplicación consulta:

- Sistema operativo.
- Versión del sistema.
- Procesos activos.

## 6. Archivos generados

### telemetria.csv

Contiene las mediciones obtenidas durante la ejecución.

### reporte.json

Contiene un resumen de la ejecución:

- Total de ciclos.
- Datos válidos.
- Anomalías.
- Errores.
- Porcentaje de datos válidos.

### sistema.log

Registra eventos normales, anomalías y errores.

## 7. Ejecución

Para ejecutar el simulador:

python firmware/simulador.py

## Para ejecutar la aplicación:

python app/main.py

## 8. Pruebas

Las pruebas realizadas se encuentran en:
pruebas/matriz_pruebas.md

## 9. Tecnologías
Python

Windows

JSON

CSV

Git

GitHub