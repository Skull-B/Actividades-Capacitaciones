edad = int(input("edad: "))

if edad >= 18:
  licencia = input( "tienes licnecias? (s/n)") == "S"
  if licencia =="s":
    print ("Usted es mayor de edad si puede conducir")
  else:
     print("Uste es mayor dedad no tiene licecia")
else: 
    print ("Usted es menor de edad no puede conduncir")