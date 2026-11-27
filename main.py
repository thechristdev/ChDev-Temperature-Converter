#Christian Emanuel Wijaya (C) - 2026
#Python Temperature Converter

'''
╔╦╗┌─┐┌┬┐┌─┐┌─┐┬─┐┌─┐┌┬┐┬ ┬┬─┐┌─┐  ╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐┌─┐┬─┐
 ║ ├┤ │││├─┘├┤ ├┬┘├─┤ │ │ │├┬┘├┤   ║  │ ││││└┐┌┘├┤ ├┬┘ │ ├┤ ├┬┘
 ╩ └─┘┴ ┴┴  └─┘┴└─┴ ┴ ┴ └─┘┴└─└─┘  ╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴ └─┘┴└─'''
#=======Import Libraries=======#
import os
import sys
import time
import random
import string
import subprocess
import platform
import json
from modules import chcolor as chc
from modules import title as wt
from modules import chbox as chb


import datetime

platform = platform.system()
wt.Title.set("ChDev | Temperature Converter")
#=======Tools Version=======#
version = "1.0.0"
#=======Tittle=======#
def title_main():
    print(chc.Color.CYAN+"╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("  _______                                  _                     _____                          _             ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(255, 0, 0)  +"(0)"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient(" |__   __|                                | |                   / ____|                        | |            ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(255, 69, 0) +"|-|"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("    | | ___ _ __ ___  _ __   ___ _ __ __ _| |_ _   _ _ __ ___  | |     ___  _ ____   _____ _ __| |_ ___ _ _   ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(255, 165, 0)+"|-|"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("    | |/ _ \ '_ ` _ \| '_ \ / _ \ '__/ _` | __| | | | '__/ _ \ | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__| ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(255, 255, 0)+"|-|"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("    | |  __/ | | | | | |_) |  __/ | | (_| | |_| |_| | | |  __/ | |___| (_) | | | \ V /  __/ |  | ||  __/ |    ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(128, 255, 0)+"|-|"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("    |_|\___|_| |_| |_| .__/ \___|_|  \__,_|\__|\__,_|_|  \___|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|    ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(0, 255, 128)+"|-|"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("                     | |                                                                                      ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(0, 255, 255)+"|-|"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("                     |_|                                                                                      ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(0, 160, 255)+"|-|"+chc.Color.CYAN+"  ║")
    print(chc.Color.CYAN+"║"+chc.Color.gradient("                                                                                                              ",[(0, 255, 255),(160, 32, 240)])+chc.Color.rgb(0, 80, 255)+"|_|"+chc.Color.CYAN+"  ║")   
    print(chc.Color.CYAN+"╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
#=======Menu=======#
help_menu =chb.box("Help Menu ChTools", [
    ("HELP                  ","Show usefull commands"),
], width= 115)
tc_menu ='''Temperature Code List:
C                       Celsius
F                       Fahrenheit
R                       Reamur
K                       Kelvin
'''
TEMPERATURE_COLORS = [
    (0, 0, 180),       # 1. Biru tua
    (0, 80, 255),      # 2. Biru
    (0, 160, 255),     # 3. Biru muda
    (0, 255, 255),     # 4. Cyan
    (0, 200, 100),     # 5. Hijau
    (255, 255, 0),     # 6. Kuning
    (255, 165, 0),     # 7. Oranye
    (255, 69, 0),      # 8. Oranye kemerahan
    (255, 0, 0)        # 9. Merah
]

def main():
    os.system('cls||clear')
    print(chc.Color.BG_BRIGHT_MAGENTA+chc.Color.BRIGHT_WHITE+'''ChDev | Temperature Converter [Version '''+version+'''] - Platform '''+platform+'''                                                     '''+chc.Color.RESET)
    title_main()
    print(chc.Color.BOLD+"INFO: Gunakan help untuk bantuan")
    while True:
        int_term = input(":").lower()
        if int_term == "help":
            print(help_menu)
        elif int_term == "exit":
            exit()
        elif int_term == "tc":
            print(tc_menu)
        elif int_term == "clear":
            main()
        else:
            parts = int_term.split()
            if len(parts) == 2 and parts[1].lower() in ["c", "f", "r", "k"]:
                val = float(parts[0])
                unit = parts[1].lower()

                if unit == "c":
                    Celsius = val
                    Fahrenheit = (9 / 5) * Celsius + 32
                    Reamur = (4 / 5) * Celsius
                    Kelvin = Celsius + 273.15

                elif unit == "f":
                    Fahrenheit = val
                    Celsius = (Fahrenheit - 32) * (5 / 9)
                    Reamur = (4 / 5) * Celsius
                    Kelvin = Celsius + 273.15

                elif unit == "r":
                    Reamur = val
                    Celsius = Reamur * (5 / 4)
                    Fahrenheit = (9 / 5) * Celsius + 32
                    Kelvin = Celsius + 273.15

                elif unit == "k":
                    Kelvin = val
                    Celsius = Kelvin - 273.15
                    Fahrenheit = (9 / 5) * Celsius + 32
                    Reamur = (4 / 5) * Celsius
                else:
                    return
                output = chb.box("Temperature Converter", [
                    ("Celsius",    f"{Celsius:.2f} °C"),
                    ("Fahrenheit", f"{Fahrenheit:.2f} °F"),
                    ("Reamur",     f"{Reamur:.2f} °Ré"),
                    ("Kelvin",     f"{Kelvin:.2f} K"),
                ], width= 115)
            
                
                            
                if Celsius <= 0:
                    index = 0
                elif Celsius <= 10:
                    index = 1
                elif Celsius <= 15:
                    index = 2
                elif Celsius <= 20:
                    index = 3
                elif Celsius <= 25:
                    index = 4
                elif Celsius <= 30:
                    index = 5
                elif Celsius <= 35:
                    index = 6
                elif Celsius <= 40:
                    index = 7
                else:
                    index = 8
            
                print(output)
            else:
                print("sigma")
            
                

                    
                

    

if __name__ == "__main__":
    main()