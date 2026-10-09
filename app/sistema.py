import os
import platform


class Sistema:

    def obtener_informacion(self):

        informacion = {
            "sistema_operativo": platform.system(),
            "version": platform.version(),
            "procesos": len(os.popen("tasklist").readlines())
        }

        return informacion