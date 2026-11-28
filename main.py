#Christian Emanuel Wijaya (C) - 2026
#Python Temperature Converter
#ChTools

#=====================================#
#IMPORT MODULE
#=====================================#
import os
import sys
import time
import random
import string
import subprocess
import platform
import json
from modules import chcolor as chc
from modules import chtitle as wt
from modules import chbox as chb
from modules import chmessage as msg
import datetime
platform = platform.system()
#=====================================#
#CONFIGURATION
#=====================================#
wt.Title.set("ChDev | Temperature Converter")
version = "1.1.7"

#=====================================#
#TITTLE
#=====================================#
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
#=====================================#
#MENU
#=====================================#
help_menu = chb.box("Help Menu — ChTools", [
    ("ABOUT", "Display information about ChTools, including author, version, license, and donation links."),
    ("CLEAR", "Clear the terminal screen. Removes all previous output and resets the display."),
    ("EXIT",  "Exit the application. Closes ChTools and returns to the command prompt."),
    ("HELP",  "Display this help menu. Shows all available commands with their descriptions."),
    ("TC",    "Temperature Converter. Convert between Celsius, Fahrenheit, Reamur, and Kelvin."),
    ("USAGE", "Type <number> <unit> to convert. Example: 23 C"),
], width=115)

tc_menu = chb.table(
    ["Code", "Unit"],
    [
        ["C", "Celsius"],
        ["F", "Fahrenheit"],
        ["R", "Reamur"],
        ["K", "Kelvin"],
    ],
    aligns=["center", "left"],)

show_about = chb.box("About ChTools", [
    ("Name", "ChTools - Temperature Converter"),
    ("Version",  version),
    ("Author",  "thechrisdev AKA Christian Emanuel Wijaya"),
    ("Copyright",    "(C) 2026 Christian Emanuel Wijaya "),
    ("License",   "Apache License 2.0"),
    ("Github","https://github.com/thechristdev"),
], width=115)

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
#=====================================#
#MAIN
#=====================================#
def main():
    os.system('cls||clear')
    print(chc.Color.BG_BRIGHT_MAGENTA+chc.Color.BRIGHT_WHITE+'''ChDev | Temperature Converter [Version '''+version+'''] - Platform '''+platform+'''                                                     '''+chc.Color.RESET)
    title_main()
    msg.info("Type 'Help' to see the available commands.")
    while True:
        int_term = input("ChTools | >").lower()
        parts = int_term.split()
        if int_term == "help":
            print(help_menu)
        elif int_term == "exit":
            exit()
        elif int_term == "tc":
            print(tc_menu)
        elif int_term == "clear":
            main()
        elif int_term == "about":
            print(show_about)
        elif int_term == "usage":
            msg.info("Type <number> <unit> to convert. Example: 23 C")
        
            
        elif len(parts) == 2:
            
            if len(parts) == 2 and parts[1].lower() in ["c", "f", "r", "k"]:
                try:
                    val = float(parts[0])
                except ValueError:
                    msg.error(f"'{parts[0]}' is not a valid number. Please enter a numeric value.")
                    msg.info("Type <number> <unit> to convert. Example: 23 C")
                    continue                         
                unit = parts[1].lower()
                #=====================================#
                #UNIT
                #=====================================#
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
                
                output = chb.box("Temperature Converter", [
                    ("Celsius",    f"{Celsius:.2f} °C"),
                    ("Fahrenheit", f"{Fahrenheit:.2f} °F"),
                    ("Reamur",     f"{Reamur:.2f} °Ré"),
                    ("Kelvin",     f"{Kelvin:.2f} K"),
                ], width= 115)
                print(output)
            else:
                units = parts[1]
                msg.error(f"Temperature unit '{units}' not found. Please use one of the following valid codes!")
                print(tc_menu)
                continue
        else:
            msg.error(f"Command '{int_term}' not found!")
            msg.info("Type 'Help' to see the available commands.")
            continue

if __name__ == "__main__":
    main()