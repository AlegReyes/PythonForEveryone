"""En el ejemplo anterior, recibimos un archivo de texto sin formato que tenía saltos
de línea en su interior, y lo único que hicimos cuando el programa se ejecutó fue
copiar los datos a la pantalla. Podemos utilizar un programa similar para recibir
una imagen utilizando HTTP. En vez de copiar los datos a la pantalla conforme
va funcionando el programa, vamos a guardar los datos en una cadena, remover
la cabecera, y después guardar los datos de la imagen en un archivo tal como se
muestra a continuación:"""
import socket
import time

SERVIDOR = 'data.pr4e.org'
PUERTO = 80
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect((SERVIDOR, PUERTO))
misock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
contador = 0
imagen = b""
while True:
    datos = misock.recv(5120)
    if len(datos) < 1: break
    #time.sleep(0.25)
    contador = contador + len(datos)
    print(len(datos), contador)
    imagen = imagen + datos
misock.close()

# Búsqueda del final de la cabecera (2 CRLF)
pos = imagen.find(b"\r\n\r\n")
print('Header length', pos)
print(imagen[:pos].decode())

# Ignorar la cabera y guardar los datos de la imagen
imagen = imagen[pos+4:]
fhand = open("cosa.jpg", "wb")
fhand.write(imagen)
fhand.close()
# Código: https://es.py4e.com/code3/urljpeg.py
"""Cuando el programa corre, produce la siguiente salida:
$ python urljpeg.py
5120 5120
5120 10240
4240 14480
5120 19600
...
5120 214000
3200 217200
5120 222320
5120 227440
3167 230607
Header length 394
HTTP/1.1 200 OK
Date: Fri, 21 Feb 2020 01:45:41 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Mon, 15 May 2017 12:27:40 GMT
ETag: "38342-54f8f2e5b6277"
Accept-Ranges: bytes
Content-Length: 230210
Vary: Accept-Encoding
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: image/jpeg
Puedes observar que para esta url, la cabecera Content-Type indica que el cuerpo
del documento es una imagen (image/jpeg). Una vez que el programa termina,
puedes ver los datos de la imagen abriendo el archivo cosa.jpg en un visor de
imágenes.
Al ejecutar el programa, se puede ver que no se obtienen 5120 caracteres cada vez
que llamamos el método recv(). Se obtienen tantos caracteres como hayan sido
transferidos por el servidor web hacia nosotros a través de la red en el momento de
la llamada a recv(). En este emeplo, se obtienen al menos 3200 caracteres cada
vez que solicitamos hasta 5120 caracteres de datos.
Los resultados pueden variar dependiendo de tu velocidad de internet. Además,
observa que en la última llamada a recv() obtenemos 3167 bytes, lo cual es el
final de la cadena, y en la siguiente llamada a recv() obtenemos una cadena de
longitud cero que indica que el servidor ya ha llamado close() en su lado del
socket, y por lo tanto no quedan más datos pendientes por recibir.
Podemos retardar las llamadas sucesivas a recv() al descomentar la llamada a
time.sleep(). De esta forma, esperamos un cuarto de segundo después de cada
llamada de modo que el servidor puede “adelantarse” a nosotros y enviarnos más
156 CHAPTER 12. PROGRAMAS EN RED
datos antes de que llamemos de nuevo a recv(). Con el retraso, esta vez el
programa se ejecuta así:
$ python urljpeg.py
5120 5120
5120 10240
5120 15360
...
5120 225280
5120 230400
208 230608
Header length 394
HTTP/1.1 200 OK
Date: Fri, 21 Feb 2020 01:57:31 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Mon, 15 May 2017 12:27:40 GMT
ETag: "38342-54f8f2e5b6277"
Accept-Ranges: bytes
Content-Length: 230210
Vary: Accept-Encoding
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: image/jpeg
Ahora todas las llamadas a recv(), excepto la primera y la última, nos dan 5120
caracteres cada vez que solicitamos más datos.
Existe un buffer entre el servidor que hace las peticiones send() y nuestra aplicación que hace las peticiones recv().
Cuando ejecutamos el programa con el
retraso activado, en algún momento el servidor podría llenar el buffer del socket y
verse forzado a detenerse hasta que nuestro programa empiece a vaciar ese buffer.
La detención de la aplicación que envía los datos o de la que los recibe se llama
“control de flujo”
"""
