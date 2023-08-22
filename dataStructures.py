import string
##########   STRINGS
s="Hola"
s2='Perro'
bob=s + s2
print(bob)
############
x='40'
y=int(x)+2
print(y)
#########
x='From marqua@uct.ac.za'
print(x[8])
############String slicing
s='From marquard@uct.ac.za'
print(s[14:17])
###########
print(s.upper())
print(s.lower())
print(s.lstrip())
#print(s.startswith())
#print(s.wsrem())
#print(s.strtrunc())
#print(s.rltrim())
print(s.strip())
###########
#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

""" text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0.8475')
float(pos)
number=text[pos:pos+6]
print(number) """

#############FILES
#Write a program that prompts for a file name, then opens that file and reads through the file, 
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# Use words.txt as the file name
# Use words.txt as the file name

""" fname = input("Enter file name: ")
fh = open(fname)
print(fh.read().rstrip().lstrip().upper()) """

""" Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines 
 of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and 
compute the average of those values and produce an output as shown below. Do not use the sum() 
function or a variable named sum in your solution. 
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
total=0.0
count=0
try:
    fh= open(fname)
except:
    print('Archivo no encontrado',fname)
    exit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    colon_pos=line.find(":")
    value_str=line[colon_pos + 1:].strip()

    try:
        value=float(value_str)
        total += value
        count += 1
    except ValueError:
        print("Dato no valido")

if count > 0:
    average=total/count
    print(average)
else:
    print("N")
"""



#print("Done")
#print(coincidences)
"""solucion chida
fname = input("Enter file name: ")

try:
    with open(fname, 'r') as fh:
        total = 0.0  # Variable to store the sum of floating point values
        count = 0  # Variable to count the number of lines with floating point values

        for line in fh:
            if line.startswith("X-DSPAM-Confidence:"):
                # Extract the floating point value from the line
                colon_pos = line.find(":")
                value_str = line[colon_pos + 1:].strip()
                print(value_str)
                
                try:
                    value = float(value_str)
                    total += value
                    count += 1
                except ValueError:
                    print(f"Invalid floating point value: {value_str}")

    if count > 0:
        average = total / count
        print(f"Average spam confidence: {average:.4f}")
    else:
        print("No lines with 'X-DSPAM-Confidence:' found in the file.")
except FileNotFoundError:
    print("File not found.")
"""
###############LISTAS
numeros = [17, 123]
numeros[1] = 5
print(numeros)
#################
quesos = ['Cheddar', 'Edam', 'Gouda']

for queso in quesos:
    print(queso)

"""Esto funciona bien si solamente necesitas leer los elementos de la lista. Pero si
quieres escribir o actualizar los elementos, necesitas los índices. Una forma común
de hacer eso es combinando las funciones range y len """
for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2
print(numeros)
"""Este bucle recorre la lista y actualiza cada elemento. len regresa el número de
elementos en una lista. range regresa una lista de índices desde 0 hasta n − 1,
donde n es la longitud de la lista. Cada vez que pasa a través del recorrido, i
obtiene el índice del siguiente elemento. La sentencia de asignación dentro del
bucle utiliza i para leer el valor original del elemento y asignar un nuevo valor.
 """
 #El operador + concatena listas:

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
#De igual forma, el operador * repite una lista un determinado número de veces:
l=[0] * 4
print(l)
l2=[1, 2, 3] * 3
print(l2)
# Rebanado de listas
#El operador de rebanado también funciona en listas:
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
"""Si omites el primer índice, el rebanado comienza desde el inicio de la lista. Si
omites el segundo, el rebanado se va hasta el final. Así que si omites ambos, el
rebanado es una copia de la lista completa.
"""
print(t[:])
"""Como las listas son mutables, a veces es útil hacer una copia antes de hacer operaciones que doblan, pegan, o cortan listas.
Un operador de rebanado al lado izquierdo de una asignación puede actualizar
múltiples elementos:"""
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
"""Python provee métodos que operan en listas. Por ejemplo, append agrega un nuevo
elemento al final de una lista:"""
t = ['a', 'b', 'c']
t.append('d')
print(t)
"""extend toma una lista como argumento y agrega todos los elementos:"""
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
"""sort ordena los elementos de la lista de menor a mayor:"""
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
"""Hay varias formas de eliminar elementos de una lista. Si sabes el índice del elemento
que quieres, puedes usar pop:"""
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)
"""pop modifica la lista y regresa el elemento que fue removido. Si no provees un
índice, la función elimina y retorna el último elemento.
Si no necesitas el valor removido, puedes usar el operador del:"""
t = ['a', 'b', 'c']
del t[1]
print(t)
"""Si sabes qué elemento quieres remover (pero no sabes el índice), puedes usar
remove:
"""
t = ['a', 'b', 'c']
t.remove('b')
print(t)
"""El valor de retorno de remove es None.
Para remover más de un elemento, puedes usar del con un índice de rebanado:
"""
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
"""Listas y funciones
Hay un cierto número funciones internas que pueden ser utilizadas en las listas que
te permiten mirar rápidamente a través de una lista sin escribir tus propios bucles:
"""
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
"""La función sum() solamente funciona cuando los elementos de la lista son números.
Las otras funciones (max(), len(), etc.) funcionan con listas de cadenas y otros
tipos que pueden ser comparados entre sí.
Podríamos reescribir un programa anterior que calculaba el promedio de una lista
de números ingresados por el usuario utilizando una lista.
Primero, el programa para calcular un promedio sin una lista:
total = 0
contador = 0
while (True):
    inp = input('Ingresa un número: ')
    if inp == 'fin': break
    valor = float(inp)
    total = total + valor
    contador = contador + 1

promedio = total / contador
print('Promedio:', promedio)
"""
"""Una cadena es una secuencia de caracteres y una lista es una secuencia de valores,
pero una lista de caracteres no es lo mismo que una cadena. Para convertir una
cadena en una lista de caracteres, puedes usar list:"""
s = 'spam'
t = list(s)
print(t)
"""La función list divide una cadena en letras individuales. Si quieres dividir una
cadena en palabras, puedes utilizar el método split:
"""
s = 'suspirando por los fiordos'
t = s.split()
print(t)
print(t[2])
"""Una vez que hayas utilizado split para dividir una cadena en una lista de palabras,
puedes utilizar el operador índice (corchetes) para ver una palabra en particular
en la lista.
Puedes llamar split con un argumento opcional llamado delimitador que especifica
qué caracteres usar para delimitar las palabras. El siguiente ejemplo utiliza un
guión medio como delimitador:"""
s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter))
"""join es el inverso de split. Este toma una lista de cadenas y concatena los
elementos. join es un método de cadenas, así que tienes que invocarlo en el
delimitador y pasar la lista como un parámetro:
"""
t = ['suspirando', 'por', 'los', 'fiordos']
delimiter = ' '
print(delimiter.join(t))

""" Analizando líneas
Normalmente cuando estamos leyendo un archivo queremos hacer algo con las
líneas que no sea solamente imprimir las líneas como son. Frecuentemente queremos encontrar 
las “líneas interesantes” y después analizar la línea para encontrar
alguna “parte interesante” en la línea. ¿Qué tal si quisiéramos imprimir el día de
la semana de las líneas que comienzan con “From”?

El método split es muy efectivo cuando nos encontramos este tipo de problemas.
Podemos escribir un pequeño programa que busca líneas donde la línea comienza
con “From”, split (dividir) esas líneas, y finalmente imprimir la tercer palabra de
la línea:

"""
man_a = open('mbox-short.txt')
for linea in man_a:
    linea = linea.rstrip()
    if not linea.startswith('From '): continue
    palabras = linea.split()
    print(palabras[2])
"""Es importante distinguir entre operaciones que modifican listas y operaciones que
crean nuevas listas. Por ejemplo, el método append modifica una lista, pero el
operador + crea una nueva lista:"""

"""Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using 
the split() method. The program should build a list of words. For each word on each line check to see if the word 
is already in the list and if not append it to the list. When the program completes, sort and print the resulting 
words in python sort() order as shown in the desired output."""
#Solucion usando "set"
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #print(line.rstrip())
    lst=line.split() + lst
print(lst)
norepeats=list(set(lst))
norepeats.sort()
print(norepeats)
"""
#Solucion usando for y append
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #print(line.rstrip())
    lst=line.split() + lst
print(lst)
norepeats=[]
for element in lst:
    if element  not in norepeats:
        norepeats.append(element)
norepeats.sort()
print(norepeats) 
"""

"""8.5 Open the file mbox-short.txt and read it line by line. When you find 
a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in 
the line (i.e. the entire address of the person who sent the message). Then 
print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0

for line in fh:
    line=line.rstrip()
    if not line.startswith('From '): continue
    word=line.split()
    count = count + 1
    print(word[1])

print("There were", count, "lines in the file with From as the first word")
""" 
#####################Diccionarios
stuff=dict()
print(stuff.get('candy',-1))

"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
number of mail messages. The program looks for 'From ' lines and takes the second word of those lines 
as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail 
address to a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer."""
"""
fname = input("Enter file:")
try:
    fhand=open(fname)
except:
    print('El archivo no se puede abrir: ')
    exit()

counts=dict()
for line in fhand:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        if len(words)>1:#Verificamos si hay al menos dos palabras
            remitente=words[1]
            counts[remitente]=counts.get(remitente,0) + 1
max_llave=max(counts, key=counts.get)
max_valor=max(counts.values())
print(max_llave + ' '+ str(max_valor))
"""

####################TUPLAS
x={'chck':1,'fred':42}
y=x.items()
print(y)
"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the 
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""
#fname = input("Enter file:")

try:
    fhand=open('mbox-short.txt')
except:
    print('El archivo no se puede abrir: ')
    exit()

counts=dict()
for line in fhand:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        #print(words)
        if len(words)>=6:#Verificamos si hay al menos dos palabras
            remitente=words[5]
            horario=remitente.split(':')[0]
            #hora = int(horario)  # Convertir la cadena a un número entero
            #for hora in horario:
                #print(horario)
            if horario not in counts:
                counts[horario]=1
            else:
                counts[horario]+=1
            #counts[horario]=counts.get(horario,0) + 1 tambien se puede usar este modo en vez del if anterior
#Ordenamos el diccionario por valor
sorted_hours=sorted(counts.items())

for hour ,count in sorted_hours:
    print(f"{hour} {count}")
#max_llave=max(counts, key=counts.get)
#max_valor=max(counts.values())
#print(max_llave + ' '+ str(max_valor))


