''' EJERCICIO RETADOR 3  '''

cementoPorKg = 40
yesoPorKg = 30
capacidadMaximaPorKg = 3254

cantCemento = int(input ("Número de costales de cemento (kg): "))
cantYeso = int(input ("Número de costales de yeso (kg): "))

totalCementoKg = cantCemento*cementoPorKg
totalYesoKg = cantYeso*yesoPorKg
pesoTotal = totalCementoKg + totalYesoKg

print ("El peso total en kg es: ", pesoTotal, " kg")
TrueFalse = pesoTotal>=(capacidadMaximaPorKg/2) and pesoTotal<=capacidadMaximaPorKg
print ("¿Se puede realizar el envío?: ", TrueFalse)