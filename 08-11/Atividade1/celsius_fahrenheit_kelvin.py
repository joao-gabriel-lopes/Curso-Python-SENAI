def celsiusParaFahrenheit(celsius):
    resultado = (celsius * 1.8) + 32
    return resultado

def celsiusParaKelvin(celsius):
    resultado = celsius + 273.15
    return resultado

def fahrenheitParaCelsius(fahrenheit):
    resultado = (fahrenheit - 32) * (5 / 9)
    return resultado

def fahrenheitParaKelvin(fahrenheit):
    resultado = (fahrenheit - 32) * (5 / 9) + 273.15
    return resultado

def kelvinParaCelsius(kelvin):
    resultado = kelvin - 273.15
    return resultado

def kelvinParaFahrenheit(kelvin):
    resultado = (kelvin - 273.15) * 1.8 + 32
    return resultado

celsius = float(input("Digite os graus em Celsius: "))
print(f"{celsius}°C são {celsiusParaFahrenheit(celsius)}°F e {celsiusParaKelvin(celsius)}K", end="\n\n")

fahrenheit = float(input("Digite os graus em Fahrenheit: "))
print(f"{fahrenheit}°F são {fahrenheitParaCelsius(fahrenheit)}°C e {fahrenheitParaKelvin(fahrenheit)}K", end="\n\n")

kelvin = float(input("Digite os graus em Kelvin: "))
print(f"{kelvin}K são {kelvinParaCelsius(kelvin)}°C e {kelvinParaFahrenheit(kelvin)}°F", end="\n\n")