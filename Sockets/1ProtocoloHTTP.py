"""Quizá la manera más sencilla de demostrar cómo funciona el protocolo HTTP
sea escribir un programa en Python muy sencillo, que realice una conexión a un
servidor web y siga las reglas del protocolo HTTP para solicitar un documento y
mostrar lo que el servidor envía de regreso."""

import socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)
while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(),end='')
misock.close()
"""En primer lugar, el programa realiza una conexión al puerto 80 del servidor
www.py4e.com. Puesto que nuestro programa está jugando el rol de “navegador
web”, el protocolo HTTP dice que debemos enviar el comando GET seguido de
una línea en blanco. \r\n representa un salto de línea (end of line, o EOL en
inglés), así que \r\n\r\n significa que no hay nada entre dos secuencias de salto
de línea. Ese es el equivalente de una línea en blanco.
Una vez que enviamos esa línea en blanco, escribimos un bucle que recibe los datos
desde el socket en bloques de 512 caracteres y los imprime en pantalla hasta queno quedan más datos por leer (es decir, la llamada a recv() devuelve una cadena
vacía).
El programa produce la salida siguiente:
HTTP/1.1 200 OK
Date: Wed, 11 Apr 2018 18:52:55 GMT
Server: Apache/2.4.7 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
La salida comienza con la cabecera que el servidor envía para describir el documento.
Por ejemplo, la cabecera Content-Type indica que el documento es un
documento de texto sin formato (text/plain).
Después de que el servidor nos envía la cabecera, añade una línea en blanco para
indicar el final de la cabecera, y después envía los datos reales del archivo romeo.txt.
Este ejemplo muestra cómo hacer una conexión de red de bajo nivel con sockets.
Los sockets pueden ser usados para comunicarse con un servidor web, con un
servidor de correo, o con muchos otros tipos de servidores. Todo lo que se necesita
es encontrar el documento que describe el protocolo correspondiente y escribir el
código para enviar y recibir los datos de acuerdo a ese protocolo.
Sin embargo, como el protocolo que se usa con más frecuencia es el protocolo web
HTTP, Python tiene una librería especial diseñada especialmente para trabajar
con éste para recibir documentos y datos a través de la web.

Uno de los requisitos para utilizar el protocolo HTTP es la necesidad de enviar y
recibir datos como objectos binarios, en vez de cadenas. En el ejemplo anterior, los
métodos encode() y decode() convierten cadenas en objectos binarios y viceversa.


"""