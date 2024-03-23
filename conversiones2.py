"""Ejercicio desarrollado en grupo"""
import sys
#Se crea diccionario para guardar los valores
conversiones= {}
conversiones["sol_pe"]=float(sys.argv[1])
conversiones["peso_arg"]=float(sys.argv[2])
conversiones["dolar_usd"]=float(sys.argv[3])
conversiones["peso_cl"]=float(sys.argv[4])

#Cálculo de Conversiones
#print(conversiones)

print("Los",conversiones["peso_cl"],"pesos chilenos equivalen a: ")
print(f"{conversiones["sol_pe"] * conversiones["peso_cl"]} soles peruanos")
print(f"{conversiones["peso_arg"] * conversiones["peso_cl"]} peso argentino")
print(f"{conversiones["dolar_usd"] * conversiones["peso_cl"]} dolar americano")