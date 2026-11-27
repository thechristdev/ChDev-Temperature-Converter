def thermometer(celsius):

    min_temp = -1000
    max_temp = 1000
    step = 100

    # Membatasi suhu indikator
    position = max(min_temp, min(max_temp, celsius))

    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                              ║")
    print("║   THERMOMETER          °C          °F         °Ré          K                 ║")

    for temp in range(max_temp, min_temp - 1, -step):

        fahrenheit = (temp * 9 / 5) + 32
        reamur = temp * 4 / 5
        kelvin = temp + 273.15

        if temp < position:
            indicator = "  |#|  "
        elif temp - step < position <= temp:
            indicator = "--|#|--"
        else:
            indicator = "  | |  "

        print(
            f"║     {indicator}"
            f"          {temp:>5}"
            f"       {fahrenheit:>5.0f}"
            f"       {reamur:>5.0f}"
            f"       {kelvin:>5.0f}               ║"
        )

    print("║      (===)                                                                   ║")
    print("║                                                                              ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")


# Contoh penggunaan
thermometer(-32032)