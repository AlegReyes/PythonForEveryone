"""12.4 Recepción de páginas web con urllib
Aunque podemos enviar y recibir datos manualmente mediante HTTP utilizando
la librería socket, existe una forma mucho más simple para realizar esta habitual
tarea en Python, utilizando la librería urllib.
Utilizando urllib, es posible tratar una página web de forma parecida a un archivo.
Se puede indicar simplemente qué página web se desea recuperar y urllib se encargará de manejar todos los detalles 
referentes al protocolo HTTP y a la cabecera.
El código equivalente para leer el archivo romeo.txt desde la web usando urllib
es el siguiente:
"""
import urllib.request
man_a = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for linea in man_a:
    print(linea.decode().strip())

"""Una vez que la página web ha sido abierta con urllib.urlopen, se puede tratar
como un archivo y leer a través de ella utilizando un bucle for.
Cuando el programa se ejecuta, en su salida sólo vemos el contenido del archivo.
Las cabeceras siguen enviándose, pero el código de urllib se encarga de manejarlas
y solamente nos devuelve los datos.

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief

Como ejemplo, podemos escribir un programa para obtener los datos de romeo.txt
y calcular la frecuencia de cada palabra en el archivo de la forma siguiente:
"""
man_a = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
contadores = dict()
for linea in man_a:
    palabras = linea.decode().split()
    for palabra in palabras:
        contadores[palabra] = contadores.get(palabra, 0) + 1
print(contadores)

"""De nuevo vemos que, una vez abierta la página web, se puede leer como si fuera
un archivo local.

12.5 Leyendo archivos binarios con urllib
A veces se desea obtener un archivo que no es de texto (o binario) tal como una
imagen o un archivo de video. Los datos en esos archivos generalmente no son
útiles para ser impresos en pantalla, pero se puede hacer fácilmente una copia de
una URL a un archivo local en el disco duro utilizando urllib.
El método consiste en abrir la dirección URL y utilizar read para descargar todo el
contenido del documento en una cadena (img) para después escribir esa información
a un archivo local, tal como se muestra a continuación:
"""
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
man_a = open('portada.jpg', 'wb')
man_a.write(img)
man_a.close()
"""Este programa lee todos los datos que recibe de la red y los almacena en la variable img en la memoria principal
 de la computadora. Después, abre el archivo
portada.jpg y escribe los datos en el disco. El argumento wb en la función open()
abre un archivo binario en modo de escritura solamente. Este programa funcionará
siempre y cuando el tamaño del archivo sea menor que el tamaño de la memoria
de la computadora.
Aún asi, si es un archivo grande de audio o video, este programa podría fallar o al
menos ejecutarse sumamente lento cuando la memoria de la computadora se haya
agotado. Para evitar que la memoria se termine, almacenamos los datos en bloques
(o buffers) y luego escribimos cada bloque en el disco antes de obtener el siguiente
bloque. De esta forma, el programa puede leer archivos de cualquier tamaño sin
utilizar toda la memoria disponible en la computadora."""
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
man_a = open('portada.jpg', 'wb')
tamano = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    tamano = tamano + len(info)
    man_a.write(info)
print(tamano, 'caracteres copiados.')
man_a.close()
"""En este ejemplo, leemos solamente 100,000 caracteres a la vez, y después los escribimos al archivo portada.jpg 
antes de obtener los siguientes 100,000 caracteres
de datos desde la web.
Este programa se ejecuta como se observa a continuación:
python curl2.py
230210 caracteres copiados.

12.6 Análisis the HTML y rascado de la web
Uno de los usos más comunes de las capacidades de urllib en Python es rascar
la web. El rascado de la web es cuando escribimos un programa que pretende ser
un navegador web y recupera páginas, examinando luego los datos de esas páginas
para encontrar ciertos patrones.
Por ejemplo, un motor de búsqueda como Google buscará el código de una página
web, extraerá los enlaces a otras paginas y las recuperará, extrayendo los enlaces
que haya en ellas y así sucesivamente. Utilizando esta técnica, las arañas de Google
alcanzan a casi todas las páginas de la web.
Google utiliza también la frecuencia con que las páginas que encuentra enlazan hacia una página concreta para calcular la “importancia” de esa página, y la posición
en la que debe aparecer dentro de sus resultados de búsqueda.
"""


