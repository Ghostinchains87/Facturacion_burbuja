import csv

def obtener_lista_facturacion():
  lista = []
  with open (r"C:\Users\bmiranda\Downloads\datos.csv", "r", newline="") as archivo:
    lector_csv = csv.reader(archivo, delimiter =";")
    pos = 0
    for linea in lector_csv:
      if pos != 0:
        año = int(linea[0])
        trimestre1 = float(linea[1])
        trimestre2 = float(linea[2])
        trimestre3 = float(linea[3])
        trimestre4 = float(linea[4])
        lista.append({
            "año": año,
            "trimestre1": trimestre1,
            "trimestre2": trimestre2,
            "trimestre3": trimestre3,
            "trimestre4": trimestre4,
        })
      else:
        pos = 1
  return lista

def imprimir_años_con_media():
  lista = obtener_lista_facturacion()
  burbuja(lista)
  for elemento in lista:
    año = elemento["año"]
    media = (elemento["trimestre1"]+elemento["trimestre2"]+elemento["trimestre3"]+elemento["trimestre4"]) /4
    print(f"año {año} facturacion media de {media} euros")
    
def burbuja(arreglo):
  longitud = len(arreglo)
  for i in range(longitud):
    for indice_actual in range(longitud - 1):
      indice_siguiente_elemento = indice_actual + 1
      if arreglo[indice_actual]["año"] < arreglo[indice_siguiente_elemento]["año"]:
        arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]

def guardar_años_cronologicamente():
  lista = obtener_lista_facturacion()
  burbuja(lista)
  with open("salida.csv", "w", newline="") as archivo:
    escritor_csv = csv.writer(archivo, delimiter = ";")
    escritor_csv.writerow(["Año", "Promedio"])
    for elemento in lista:
      año = elemento["año"]
      total = (elemento["trimestre1"]+elemento["trimestre2"]+elemento["trimestre3"]+elemento["trimestre4"]) /4
      salida = []
      salida.append(año)
      salida.append(total)
      escritor_csv.writerow(salida)
      

opciones = "1. Imprimir años con media\n2. Guardar años cronologicamente\n3. Salir\n"
eleccion = ""
while eleccion != "3":
  eleccion = input(opciones)
  if eleccion == "1":
    imprimir_años_con_media()
  elif eleccion == "2":
    guardar_años_cronologicamente()
    
