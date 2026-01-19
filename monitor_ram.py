import subprocess
import time

def check_ram():
    while True:
        # Ejecuta el comando de sistema 'free -m' para ver la RAM en Megabytes
        output = subprocess.check_output(['free', '-m']).decode('utf-8')
        lines = output.split('\n')
        
        # La segunda línea contiene la información de la memoria
        ram_info = lines[1].split()
        total = ram_info[1]
        used = ram_info[2]
        free = ram_info[6] # Memoria disponible (la más real)
        
        print(f"\r[ESTADO RAM] Total: {total}MB | Usada: {used}MB | Disponible: {free}MB", end="")
        time.sleep(2) # Se actualiza cada 2 segundos

if __name__ == "__main__":
    print("--- Monitoreo de RAM iniciado (Presiona Ctrl+C para salir) ---")
    try:
        check_ram()
    except KeyboardInterrupt:
        print("\nMonitoreo finalizado.")
