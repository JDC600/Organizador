import datetime, sys, signal, time, os
from pip import main
from playsound import playsound
from prettytable import from_csv



def sig_handler(sig, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\n[*] {bcolors.OKGREEN}Saliendo...{bcolors.ENDC} [*]\n")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit(0)

def salir():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\n[*] {bcolors.OKGREEN}Saliendo...{bcolors.ENDC} [*]\n")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit(0)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    CYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def generarHorario():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("archivos/horario.csv", "r") as fp: 
        x = from_csv(fp)

    horarioTitulo = """
    
                                                 _    _                      _       
                                                | |  | |                    (_)      
                                                | |__| | ___  _ __ __ _ _ __ _  ___  
                                                |  __  |/ _ \| '__/ _` | '__| |/ _ \ 
                                                | |  | | (_) | | | (_| | |  | | (_) |
                                                |_|  |_|\___/|_|  \__,_|_|  |_|\___/ 
                                                \n\n
    """
    print(horarioTitulo, '\n\r', x)

def temporizadorNormal():
    os.system('cls' if os.name == 'nt' else 'clear')
    horaEnSegs = 3600
    while horaEnSegs > 0:
        tiempo = datetime.datetime.now()  
        hora = tiempo.hour
        minutos = tiempo.minute
        segundos = tiempo.second
        contador = datetime.timedelta(seconds=horaEnSegs)
        print(f"{bcolors.FAIL}Hora:{bcolors.ENDC} {hora}h {minutos}m {segundos}s {bcolors.OKBLUE}Contador:{bcolors.ENDC} {contador}s", end='\r')
        time.sleep(1)
        horaEnSegs -= 1

    playsound('audios/alarma.wav')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"[+] {bcolors.CYAN}Temporizador finalizado{bcolors.ENDC} [+]")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def temporizadorPomodoro():
    os.system('cls' if os.name == 'nt' else 'clear')
    minutosTrabajo = 1500
    while minutosTrabajo > 0:
        tiempo = datetime.datetime.now()  
        hora = tiempo.hour
        minutos = tiempo.minute
        segundos = tiempo.second
        contador = datetime.timedelta(seconds=minutosTrabajo)
        print(f"{bcolors.FAIL}Hora:{bcolors.ENDC} {hora}h {minutos}m {segundos}s {bcolors.OKBLUE}Contador:{bcolors.ENDC} {contador}s", end='\r')
        time.sleep(1)
        minutosTrabajo -= 1
    playsound('audios/alarma.wav')
    os.system('cls' if os.name == 'nt' else 'clear')

    def descanso():
        print("\n         " + bcolors.WARNING + "[" + bcolors.ENDC + bcolors.OKBLUE + "DESCANSO" + bcolors.ENDC + bcolors.WARNING + "]" + bcolors.ENDC)
        print("------<<<<-------->>>>------")
        print("        1. 5 minutos")
        print("        2. 15 minutos")
        print("        3. Tiempo personalizado")
        print("        0. Salir")
        print("------<<<<-------->>>>------\n")

        opcionMenuPomodoro = input("Selecciona la opción: ")
        os.system('cls' if os.name == 'nt' else 'clear')
 
        if opcionMenuPomodoro == "1":
            minutosDescanso = 300
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcionMenuPomodoro == "2":
            minutosDescanso = 900
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcionMenuPomodoro == "3":
            while True:
                try:
                    minutosDescansoInput = int(input("Selecciona un número en minutos: "))
                    minutosDescanso = minutosDescansoInput * 60
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                except ValueError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"[+] {bcolors.FAIL}Debe poner un número válido.{bcolors.ENDC} [+]")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        elif opcionMenuPomodoro == "0":
            salir()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"[+] {bcolors.FAIL}Opción invalida.{bcolors.ENDC} [+]")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            descanso()
        if 'minutosDescanso' in locals():
            while minutosDescanso > 0:
                tiempo = datetime.datetime.now()  
                hora = tiempo.hour
                minutos = tiempo.minute
                segundos = tiempo.second
                contador = datetime.timedelta(seconds=minutosDescanso)
                print(f"{bcolors.FAIL}Hora:{bcolors.ENDC} {hora}h {minutos}m {segundos}s {bcolors.OKGREEN}Descanso:{bcolors.ENDC} {contador}s", end='\r')
                time.sleep(1)
                minutosDescanso -= 1
            playsound('audios/alarma.wav')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"[+] {bcolors.CYAN}Temporizador finalizado{bcolors.ENDC} [+]")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
    descanso()
def temporizadorPersonalizado():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            horasDescansoInput = int(input("Selecciona un número para las horas: "))
            minutosDescansoInput = int(input("Selecciona un número para los minutos: "))
            segundosDescansoInput = int(input("Selecciona un número para los segundos: "))
            tiempoTotal = horasDescansoInput*3600 + minutosDescansoInput*60 + segundosDescansoInput
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"[+] {bcolors.FAIL}Debe poner un número válido.{bcolors.ENDC} [+]")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
    if 'tiempoTotal' in locals():
        while tiempoTotal > 0:
            tiempo = datetime.datetime.now()  
            hora = tiempo.hour
            minutos = tiempo.minute
            segundos = tiempo.second
            contador = datetime.timedelta(seconds=tiempoTotal)
            print(f"{bcolors.FAIL}Hora:{bcolors.ENDC} {hora}h {minutos}m {segundos}s {bcolors.CYAN}Contador:{bcolors.ENDC} {contador}s", end='\r')
            time.sleep(1)
            tiempoTotal -= 1
        playsound('audios/alarma.wav')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"[+] {bcolors.CYAN}Temporizador finalizado{bcolors.ENDC} [+]")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
def main():
    signal.signal(signal.SIGINT, sig_handler)

    print("\n           " + bcolors.WARNING + "[" + bcolors.ENDC + bcolors.OKBLUE + "MENU" + bcolors.ENDC + bcolors.WARNING + "]" + bcolors.ENDC)
    print("------<<<<-------->>>>------")
    print("        1. Horario")
    print("        2. Temporizador Normal (1 hora)")
    print("        3. Temporizador Pomodoro")
    print("        4. Temporizador Personalizado")
    print("        0. Salir")
    print("------<<<<-------->>>>------\n")

    
    opcionMenuGeneral = input("Selecciona la opción: ")
    
    if opcionMenuGeneral == "1":
        generarHorario()
    elif opcionMenuGeneral == "2":
        temporizadorNormal()
    elif opcionMenuGeneral == "3":
        temporizadorPomodoro()
    elif opcionMenuGeneral == "4":
        temporizadorPersonalizado()
    elif opcionMenuGeneral == "0":
        salir()
    else:        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"[+] {bcolors.FAIL}Opción invalida.{bcolors.ENDC} [+]")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()