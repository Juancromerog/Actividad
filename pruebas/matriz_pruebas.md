# Matriz de Pruebas

## Proyecto: Sistema de Integración Hardware, Software y Firmware

| ID | Prueba / Condición | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|
| TP-01 | Recepción de datos normales | El sistema recibe y procesa correctamente la telemetría. | El sistema recibió y procesó datos correctamente. | APROBADA |
| TP-02 | Temperatura fuera del rango | El sistema identifica la temperatura como una anomalía. | Se detectaron temperaturas superiores a 50 °C y fueron clasificadas como anomalías. | APROBADA |
| TP-03 | Dato con formato incorrecto | El sistema rechaza el dato y continúa funcionando. | Se produjo un error controlado y la aplicación continuó ejecutándose. | APROBADA |
| TP-04 | Pérdida de comunicación | El sistema detecta la pérdida de comunicación y continúa funcionando. | El sistema controla la excepción de comunicación sin cerrarse. | APROBADA |
| TP-05 | Consulta de recursos del sistema operativo | La aplicación obtiene información del sistema operativo y procesos. | Se obtuvo información de Windows y cantidad de procesos. | APROBADA |
| TP-06 | Persistencia de datos | El sistema almacena las mediciones en un archivo CSV. | Se generó correctamente `telemetria.csv`. | APROBADA |
| TP-07 | Generación de reporte | El sistema genera un resumen de la ejecución en formato JSON. | Se generó correctamente `reporte.json`. | APROBADA |
| TP-08 | Registro de eventos | El sistema registra eventos, anomalías y errores. | Se generó correctamente `sistema.log`. | APROBADA |

## Resultados de la ejecución

La ejecución de prueba realizada produjo:

- Ciclos ejecutados: 15
- Datos válidos: 14
- Anomalías detectadas: 3
- Errores controlados: 1
- Porcentaje de datos válidos: 93,33 %

## Conclusión

Las pruebas realizadas evidencian que el prototipo puede recibir datos, validarlos,
clasificarlos, detectar condiciones anómalas, controlar errores y almacenar información
para su posterior análisis.