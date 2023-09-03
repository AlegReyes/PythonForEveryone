"""12.7 Análisis de HTML mediante expresiones regulares
Una forma sencilla de analizar HTML consiste en utilizar expresiones regulares
para hacer búsquedas repetitivas que extraigan subcadenas coincidentes con un
patrón en particular.
Aquí tenemos una página web simple:
<h1>La Primera Página</h1>
<p>
Si quieres, puedes visitar la
<a href="http://www.dr-chuck.com/page2.htm">
Segunda Página</a>.
</p>
Podemos construir una expresión regular bien formada para buscar y extraer los
valores de los enlaces del texto anterior, de esta forma:
href="http[s]?://.+?"
Nuestra expresión regular busca cadenas que comiencen con “href="http://” o
“href="https://”, seguido de uno o más caracteres (.+?), seguidos por otra comilla
doble. El signo de interrogación después de [s]? indica que la coincidencia debe
ser hecha en modo “no-codicioso”, en vez de en modo “codicioso”. Una búsqueda
no-codiciosa intenta encontrar la cadena coincidente más pequeña posible, mientras
que una búsqueda codiciosa intentaría localizar la cadena coincidente más grande.
Añadimos paréntesis a nuestra expresión regular para indicar qué parte de la cadena 
localizada queremos extraer, y obtenemos el siguiente programa:
"""
# Búsqueda de valores de enlaces dentro de una URL ingresada
import urllib.request, urllib.parse, urllib.error
import re
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')
html = urllib.request.urlopen(url).read()
enlaces = re.findall(b'href="(http[s]?://.*?)"', html)
for enlace in enlaces:
    print(enlace.decode())
"""La librería ssl permite a nuestro programa acceder a los sitios web que estrictamente requieren HTTPS. El método read devuelve código fuente en HTML como
un objeto binario en vez de devolver un objeto HTTPResponse. El método de
expresiones regulares findall nos da una lista de todas las cadenas que coinciden con la expresión regular, devolviendo solamente el texto del enlace entre las
comillas dobles.
Cuando corremos el programa e ingresamos una URL, obtenemos lo siguiente:
Introduzca - https://docs.python.org
https://docs.python.org/3/index.html
https://www.python.org/
https://devguide.python.org/docquality/#helping-with-documentation
https://docs.python.org/3.9/
https://docs.python.org/3.8/
https://docs.python.org/3.7/
https://docs.python.org/3.6/
https://docs.python.org/3.5/
https://docs.python.org/2.7/
https://www.python.org/doc/versions/
https://www.python.org/dev/peps/
https://wiki.python.org/moin/BeginnersGuide
https://wiki.python.org/moin/PythonBooks
https://www.python.org/doc/av/
https://devguide.python.org/
https://www.python.org/
https://www.python.org/psf/donations/
https://docs.python.org/3/bugs.html
https://www.sphinx-doc.org/
Las expresiones regulares funcionan muy bien cuando el HTML está bien formateado y es predecible. Pero dado que ahí afuera hay muchas páginas con HTML
“defectuoso”, una solución que solo utilice expresiones regulares podría perder algunos enlaces válidos, o bien terminar obteniendo datos erróneos.
Esto se puede resolver utilizando una librería robusta de análisis de HTML.

12.8 Análisis de HTML mediante BeautifulSoup
A pesar de que HTML es parecido a XML1 y que algunas páginas son construidas
cuidadosamente para ser XML, la mayoría del HTML generalmente está incompleto, de modo que puede causar que un analizador de XML rechace una página
HTML completa por estar formada inadecuadamente.
Hay varias librerías en Python que pueden ayudarte a analizar HTML y extraer
datos de las páginas. Cada una tiene sus fortalezas y debilidades, por lo que puedes
elegir una basada en tus necesidades.
Por ejemplo, vamos a analizar una entrada HTML cualquiera y a extraer enlaces
utilizando la librería BeautifulSoup. BeautifulSoup tolera código HTML bastante
defectuoso y aún así te deja extraer los datos que necesitas. Puedes descargar e
instalar el código de BeautifulSoup desde:

https://pypi.python.org/pypi/beautifulsoup4

La información acerca de la instalación de BeautifulSoup utilizando la herramienta
de Python Package Index (Índice de Paquete de Python) pip, disponible en:

https://packaging.python.org/tutorials/installing-packages/

Vamos a utilizar urllib para leer la página y después utilizaremos BeautifulSoup
para extraer los atributos href de las etiquetas de anclaje (a).

# Para ejecutar este programa descarga BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# O descarga el archivo
# http://www.py4e.com/code3/bs4.zip
# y descomprimelo en el mismo directorio que este archivo

"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
# Recuperar todas las etiquetas de anclaje
etiquetas = sopa('a')
for etiqueta in etiquetas:
    print(etiqueta.get('href', None))
"""El programa solicita una dirección web, luego la abre, lee los datos y se los pasa al
analizador BeautifulSoup. Luego, recupera todas las etiquetas de anclaje e imprime
en pantalla el atributo href de cada una de ellas.
Cuando el programa se ejecuta, produce lo siguiente:
Introduzca - https://docs.python.org
genindex.html
py-modindex.html
https://www.python.org/
#
whatsnew/3.8.html
whatsnew/index.html
tutorial/index.html
library/index.html
reference/index.html
using/index.html
howto/index.html
installing/index.html
distributing/index.html
extending/index.html
c-api/index.html
faq/index.html
py-modindex.html
genindex.html
glossary.html
search.html
contents.html
bugs.html
https://devguide.python.org/docquality/#helping-with-documentation
about.html
license.html
copyright.html
download.html
https://docs.python.org/3.9/
https://docs.python.org/3.8/
https://docs.python.org/3.7/
https://docs.python.org/3.6/
https://docs.python.org/3.5/
https://docs.python.org/2.7/
https://www.python.org/doc/versions/
https://www.python.org/dev/peps/
https://wiki.python.org/moin/BeginnersGuide
https://wiki.python.org/moin/PythonBooks
https://www.python.org/doc/av/
https://devguide.python.org/
genindex.html
py-modindex.html
https://www.python.org/
#
copyright.html
https://www.python.org/psf/donations/
https://docs.python.org/3/bugs.html
https://www.sphinx-doc.org/

Esta lista es mucho más larga porque algunas de las etiquetas de anclaje son rutas
relativas (e.g., tutorial/index.html) o referencias dentro de la página (p. ej., ‘#’)
que no incluyen “http://” o “https://”, lo cual era un requerimiento en nuestra
expresión regular.
También puedes utilizar BeautifulSoup para extraer varias partes de cada etiqueta
de este modo:

# Para ejecutar este programa descarga BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# O descarga el archivo
# http://www.py4e.com/code3/bs4.zip
# y descomprimelo en el mismo directorio que este archivo

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')
html = urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, "html.parser")

# Obtener todas las etiquetas de anclaje
etiquetas = sopa('a')
for etiqueta in etiquetas:
    # Look at the parts of a tag
    print('ETIQUETA:', etiqueta)
    print('URL:', etiqueta.get('href', None))
    print('Contenido:', etiqueta.contents[0])
    print('Atributos:', etiqueta.attrs)

"""python urllink2.py
Introduzca - http://www.dr-chuck.com/page1.htm
ETIQUETA: <a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>
URL: http://www.dr-chuck.com/page2.htm
Contenido:
Second Page
Atributos: {'href': 'http://www.dr-chuck.com/page2.htm'}
html.parser es el analizador de HTML incluido en la librería estándar de Python
3. Para más información acerca de otros analizadores de HTML, lee:
http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
Estos ejemplo tan sólo muestran un poco de la potencia de BeautifulSoup cuando
se trata de analizar HTML.
"""