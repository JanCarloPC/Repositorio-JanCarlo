''' EJERCICIO RETADOR #4 '''

idProducto = [1, 2, 3]
tipoProducto = ["Maíz grano", "Pepino", "Tomate verde"]
costoPorCaja = [285.55, 334.72, 129.00]

numeroCajas = float(input ("Número de cajas a vender: "))
elegirIdProducto = int(input ("ID del producto: "))

if (numeroCajas <= 100):
    costoEnvio = 1500
else:
    costoEnvio = 0

if (elegirIdProducto == 1):
    print ("El producto es: " + tipoProducto[0])
    print ("El precio por caja es: " + str(costoPorCaja[0]))
    pagoTotal = (costoPorCaja[0]*numeroCajas) + costoEnvio
    print ("El costo total a pagar: ", round(pagoTotal))
  
elif (elegirIdProducto == 2):
    print ("El producto es: " + tipoProducto[1])
    print ("El precio por caja es: " + str(costoPorCaja[1]))
    pagoTotal = (costoPorCaja[1]*numeroCajas) + costoEnvio
    print ("El costo total a pagar: ", round(pagoTotal))
  
elif (elegirIdProducto == 3):
    print ("El producto es: " + tipoProducto[2])
    print ("El precio por caja es: " + str(costoPorCaja[2]))
    pagoTotal = (costoPorCaja[2]*numeroCajas) + costoEnvio
    print ("El costo total a pagar: ", round(pagoTotal))
  
else: 
    print("ID de producto no válido, Ingrese un ID Valido")