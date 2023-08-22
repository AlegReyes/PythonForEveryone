
 #Create a function with two arguments that will return an array of the first n multiples of x.
    #Assume both the given number and the number of times to count will be positive numbers greater than 0.
    #count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
    #count_by(2,5) #should return [2,4,6,8,10]
def count_by(a,b):
    array=[]
    for i in range(b):
        array.append(a*(i+1))
    return array
result=count_by(3,10)
print(result)

""" Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. 
It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical 
structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

For example:
"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. 
All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'. """

""" def dna_to_rna(dna):
    input = dna
    chars = list(input)         # ['A', 'B', 'C']
    return chars

result=dna_to_rna("PEDRO")
print(result) """
""" 
hrs = input("Enter Hours:")
rate= input("Enter Rate:")
r=float(rate)
h = float(hrs)
pay=r*h
if h <= 40:
    print('Pay: ',+ pay )
if h > 40:
    h2=h-40
    h2=h2*1.5
    ra=h2*r
    ra2=(40*r)+ra
    print('Pay: ', + ra2) """

""" def computepay(h, r):
    if h>40:
        extra=h-40
        extra=extra*1.5*r
        h=(40*r)+extra
        return h
    else:
        pay=h*r
        return pay
hrs= input("Enter Hours:")
rate=input("Enter Rate:")
hrs=float(hrs)
rate=float(rate)
p=computepay(hrs,rate)
print("Pay",p) """
""" Escriba un programa que solicite repetidamente al usuario números enteros hasta que el usuario ingrese 'hecho'. 
Una vez que haya ingresado 'hecho', imprima el mayor y el menor de los números. 
Si el usuario ingresa algo que no sea un número válido, atrápelo con un intento/excepto y emita un mensaje 
apropiado e ignore el número. Ingrese 7, 2, bob, 10 y 4 y haga coincidir el resultado a continuación.
 """

largest=None
smallest=None
aray=[]

def infinito():
    while True:
        num=input("Enter a number: ")
        if num == "done":
            break
        else:
            try:
                num=float(num)
                aray.append(num)
            except:
                print("Invalid input")
                continue
            
loop=infinito()
print(loop) 
if aray:
    largest = max(aray)
    smallest = min(aray)

#print("Array:", aray)
print("Largest:", largest)
print("Smallest:", smallest)
