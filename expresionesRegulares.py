"""Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your 
testing and the other is the actual data you need to process for the assignment.
Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1852629.txt (There are 89 values and the sum ends with 849)
These links open in a new window. Make sure to save the file into the same folder as you will be 
writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
Data Format
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...

The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

#Uso de extend
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)

print(lista1)  # Salida: [1, 2, 3, 4, 5, 6]
"""

import re
suma=list()
count=0
iteraciones=0
#man = open('textoprueba.txt')
man = open('actualdata.txt')
#man = open('sampledata.txt')
for linea in man:
    linea = linea.rstrip()
    x = re.findall(r'\b\d+\b|\b\d+\.\d+\b|\b\.\d+\b', linea)
    if len(x) >= 0:
        suma.extend(x)
        #suma.append(x)
print(suma)
numeros_enteros=list(map(int,suma))
print(suma)
for numero in numeros_enteros:
    #count += numero esta es la forma abreviada
    count = numero + count
    iteraciones = iteraciones+1
print(count)
print(iteraciones)



        
