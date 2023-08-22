
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
    print('Pay: ', + ra2) 

def computepay(h, r):
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
print("Pay",p) 

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
