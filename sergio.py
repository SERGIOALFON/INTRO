#sentencia if para condicionales
#a = input("ingrese un numero: ")
#b = input("ingrese un numero: ")
#if a < b:
#    print(f"{a} es mayor que {b}")
#elif a == b:
#    print(f"{a} es igual {b}")
#else:
#    print(f"{a} es menor que {b}")

#si un numero esta entre dos numeros

#def es_bisiesto(año):
#    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#        return True
#    else:
#        return False

# Verificar si el año 2024 es bisiesto
#año_a_verificar = 2028

#if es_bisiesto(año_a_verificar):
#    print(f"{año_a_verificar} es un año bisiesto.")
#else:
#    print(f"{año_a_verificar} no es un año bisiesto.")

import socket


#def extract_ip():
#    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    try:
#        st.connect(("10.255.255.255", 1))
#        IP = st.getsockname()[0]
#    except Exception:
#        IP = "127.0.0.1"
#    finally:
#        st.close()
#    return IP
#print(extract_ip())

#def determinar_clase_ipv4(ip):
    # Dividir la dirección IP en octetos
    #octetos = ip.split('.')
    # Convertir cada octeto a un número entero
    #primer_octeto = int(octetos[0])
    # Determinar la clase de la dirección IP
    #if 1 <= primer_octeto <= 126:
        #return 'Clase A'
    #elif 128 <= primer_octeto <= 191:
        #return 'Clase B'
    #elif 192 <= primer_octeto <= 223:
        #return 'Clase C'
    #else:
        #return 'No pertenece a las clases A, B o C'
    
# Ejemplo de uso
#direccion_ip = "192.168.100.239"
#clase = determinar_clase_ipv4(direccion_ip)
#print(f"La dirección IP {direccion_ip} pertenece a la {clase}.")

#from empleados import empleados
#for empleado in empleados:
#    print(empleado)

