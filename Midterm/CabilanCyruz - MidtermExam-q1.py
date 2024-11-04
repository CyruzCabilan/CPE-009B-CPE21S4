def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class FahrenheitToCelsius(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 - 32
 class KelvinToCelsius(TemperatureConversion):
  def conversion(self):
   return self._temp - 273.15

 tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
 convert = KelvinToCelsius(tempInFahrenheit)
 print(str(convert.conversion()) + " Celsius")
 tempInkelvin = float(input("Enter the temperature in Kelvin: "))
 convert = KelvinToCelsius(tempInkelvin)
 print(str(convert.conversion()) + " Celsius")

main()