import datetime, sys, signal, time, os
from pip import main
from playsound import playsound
from prettytable import from_csv



def sig_handler(sig, frame):
    print(f"\n\n[*] {bcolors.OKGREEN}Saliendo...{bcolors.ENDC} [*]\n")
    time.sleep(2)
    os.system('cls')
    sys.exit(0)

def salir():
    print(f"\n\n[*] {bcolors.OKGREEN}Saliendo...{bcolors.ENDC} [*]\n")
    time.sleep(2)
    os.system('cls')
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
    os.system('cls')
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
    os.system('cls')
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
    os.system('cls')
    print(f"[+] {bcolors.CYAN}Temporizador finalizado{bcolors.ENDC} [+]")
    time.sleep(1)

def main():
    signal.signal(signal.SIGINT, sig_handler)

    print("\n           " + bcolors.WARNING + "[" + bcolors.ENDC + bcolors.OKBLUE + "MENU" + bcolors.ENDC + bcolors.WARNING + "]" + bcolors.ENDC)
    print("------<<<<-------->>>>------")
    print("        1. Horario")
    print("        2. Temporizador Normal")
    print("        0. Salir")
    print("------<<<<-------->>>>------\n")

    opcionMenuGeneral = input("Selecciona la opción: ")

    if opcionMenuGeneral == "1":
        generarHorario()
    elif opcionMenuGeneral == "2":
        temporizadorNormal()
    elif opcionMenuGeneral == "0":
        salir()
    else:
        print("\nOpción invalida\n")



if __name__ == "__main__":
    main()