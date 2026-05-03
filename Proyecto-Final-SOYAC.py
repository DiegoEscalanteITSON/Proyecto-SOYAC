# Proyecto Final SOYAC

import random
import time

class Proceso:
    def __init__(self, nombre, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_restante = tiempo_ejecucion
        self.estado = "Listo"

    def __str__(self):
        return f"Proceso: {self.nombre}, Tiempo restante: {self.tiempo_restante} segundos, Estado: {self.estado}"
    
class Planificador:
    @staticmethod
    def fcfs(procesos):
        print("Planificación FCFS (First-Come, First-Served):")
        for proceso in procesos:
            proceso.estado = "En Ejecución"
            print(proceso)
            time.sleep(1) 
            proceso.tiempo_restante = 0
            proceso.estado = "Terminado"
            print("\nFinalizado FCFS\n")
        
    @staticmethod
    def round_robin(procesos, quantum):
        print("\n--- Round Robin ---\n")
        cola = procesos.copy()
        while cola:
            p = cola.pop(0)
            if p.estado == "Terminado":
                continue
            p.estado = "Ejecutando"
            if p.tiempo_restante > quantum:
                print(f"{p.nombre} ejecuta {quantum}")
                p.tiempo_restante -= quantum
                time.sleep(1)
                p.estado = "Listo"
                cola.append(p)
            else:
                print(f"{p.nombre} termina")
                time.sleep(1)
                p.tiempo_restante = 0
                p.estado = "Terminado"
        print("\nFinalizado Round Robin\n")

class SistemaOperativo:
    def __init__(self):
            self.procesos = []
                
    def crear_proceso(self):
        nombre = input("Ingrese el nombre del proceso: ")
        tiempo_ = int(input("Tiempo:"))
        proceso = Proceso(nombre, tiempo_)
        proceso.estado = "Listo"
        self.procesos.append(proceso)

    def mostrar_procesos(self):
        print("\n--- Procesos ---")
        for proceso in self.procesos:
            print(proceso)

    import random
    def simluar_io(self):
         for proceso in self.procesos:
              if proceso.estado == "Ejecutando" and random.choice([True, False]):
                proceso.estado = "Bloqueado"
                print(f"{proceso.nombre} se bloqueó por I/O")

    def ejecutar_fcfs(self):
        Planificador.fcfs(self.procesos)

    def ejecutar_round_robin(self):
        quantum = int(input("Quantum: "))
        Planificador.round_robin(self.procesos, quantum)

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Crear Proceso")
            print("2. Mostrar Procesos")
            print("3. Ejecutar FCFS")
            print("4. Ejecutar Round Robin")
            print("5. Simular I/O")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.crear_proceso()
            elif opcion == "2":
                self.mostrar_procesos()
            elif opcion == "3":
                self.ejecutar_fcfs()
            elif opcion == "4":
                self.ejecutar_round_robin()
            elif opcion == "5":
                self.simluar_io()
            elif opcion == "6":
                break
            else:
                print("Opción no válida")

if __name__ == "__main__":
    sistema = SistemaOperativo()
    sistema.menu()