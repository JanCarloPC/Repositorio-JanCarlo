''' EJERCICIO RETADOR 2  '''

municipios = []
habitantes = []

municipios.append(input("Ingresar  municipio: "))
habitantes.append(input("Ingrese el numero de habitantes de " + municipios[0] + ": "))

municipios.append(input("Ingresar  municipio: "))
habitantes.append(input("Ingrese el numero de habitantes de " + municipios[1] + ": "))

municipios.append(input("Ingresar  municipio: "))
habitantes.append(input("Ingrese el numero de habitantes de " + municipios[2] + ": "))

totalHabitantes = int(habitantes[0]) + int(habitantes[1]) + int(habitantes[2])
promedioHabitantes = totalHabitantes/3

print ("El total de habitantes es: ", totalHabitantes)
print ("El promedio de habitantes es: ", promedioHabitantes)