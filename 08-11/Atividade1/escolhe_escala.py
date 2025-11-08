def celsiusParaFahrenheit(celsius):
    resultado = (celsius * 1.8) + 32
    return resultado

def fahrenheitParaCelsius(fahrenheit):
    resultado = (fahrenheit - 32) * (5 / 9)
    return resultado

def paraQualEscalaConverter(escala):

    if(escala == "fahrenheit"):
        celsius = float(input("Digite os graus em Celsius: "))
        print(f"{celsius}°C são {celsiusParaFahrenheit(celsius)}°F")
    elif(escala == "celsius"):
        fahrenheit = float(input("Digite os graus em Fahrenheit: "))
        print(f"{fahrenheit}°F são {fahrenheitParaCelsius(fahrenheit)}°C")
    else:
        print("Digite uma escala válida!")

escalaDesejada = input("Digite a escala para qual deseja converter (celsius/fahrenheit): ")
paraQualEscalaConverter(escalaDesejada)