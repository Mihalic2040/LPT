from colorama import Fore
from datetime import datetime

def Log(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(Fore.GREEN + "[ " + Fore.WHITE + current_time + Fore.GREEN + " ]" + " < " + "[ Log ]" + " < " + message + Fore.RESET)

def Warning(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(Fore.YELLOW + "[ " + Fore.WHITE + current_time + Fore.YELLOW + " ]" + " < " + "[ WARN ]" + " < " + message + Fore.RESET)

def Error(message, error):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(Fore.RED + "[ " + Fore.WHITE + current_time + Fore.RED + " ]" + " < " + "[ WARN ]" + " < " + message + " <<< " + Fore.LIGHTRED_EX + str(error) + Fore.RESET)

def Progres_bar(progres, total):
    percent = 100 * (progres / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent)) 
    print(f"\r|{bar}| {percent:.2f}%", end="\r")



def TEST():

    Log("Starting sys initalization")
    Warning("Ping may not work properly")
    Error("System Error", "Err")


    Files = 1000000
    Files_worked = 0
    while True:
        Progres_bar(Files_worked, Files)
        Files_worked = Files_worked + 1
        if Files_worked == Files:
            break