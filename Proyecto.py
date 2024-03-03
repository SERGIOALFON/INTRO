# import os #aqui importamos la libreria os
#
# def listar_archivos_y_directorios(ruta): #con la función enlistamos los archivos y directorios
#     try: #estas son las excepciones para llamar el requerimoento
#         contenido = os.listdir(ruta) #pedimos el contenido
#         for elemento in contenido: #aqui con el for decimos el elemanto y in dentro del contenido
#             print(elemento) #esto es requerimiento de imprimir
#     except OSError: #la excepcon que no marque el error
#         print(f"No se pudo acceder a la ruta: {ruta}") #imprimir
#
# # Ejemplo de uso
# ruta_auditoria = "C:\\Users\\Usuario\PycharmBasic\pythonProject" #cual es la ruta a buscar
# listar_archivos_y_directorios(ruta_auditoria) # por resultado no de el pedido en la ruta de auditoria


# import sys
#
# def mostrar_argumentos():
#     """
#     Muestra los argumentos pasados al script desde la línea de comandos.
#     """
#     print("Argumentos pasados al script:")
#     for arg in sys.argv:
#         print(arg)
#
# def main():
#     mostrar_argumentos()
#
# if __name__ == "__main__":
#     main()


# import socket
# import sys
#
#
# def checkPortsSocket(ip, portlist):
#     try:
#         for port in portlist:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             sock.settimeout(5)
#             result = sock.connect_ex((ip,port))
#             if result == 0:
#                 print("Puerto {}: \t Abierto".format(port))
#             else:
#                 print("Puerto {}: \t Cerrado".format(port))
#             sock.close()
#     except socket.error as error:
#         print(str(error))
#
# #if __name__ == '__main__':
# checkPortsSocket(ip='192.168.100.239', portlist=[22,25,80,443,])


# import shutil
#
# rutaorigen = 'D:/Descargas/vinculación'  # Ruta completa al archivo de origen
# rutadestino = 'D:/Descargas/glock doc'  # Ruta completa al archivo de destino
#
# try:
#     shutil.move(rutaorigen, rutadestino)
#     print("Archivo 'sergio.txt' movido correctamente.")
# except FileNotFoundError:
#     print(f"El archivo '{rutaorigen}' no se encontró.")

