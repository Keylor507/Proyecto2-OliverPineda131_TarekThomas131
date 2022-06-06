# Integrantes: Oliver Pineda y Tarek Thomas
# Cédulas: 8-978-694 y 8-970-510
# Grupo: 1SF131

import matplotlib.pyplot as plt
import numpy as np

#Función que resuelve la ecuación usando el valor brindado para x 
def func(eq,x):
    resp = eval(eq, {"x": x})
    return resp

#Función para obtener la raíz con el método númerico elegido
def bisection(a,b):
 
    if (func(eq, a) * func(eq, b) >= 0):
        print("No colocaste bien los valores de a y b\n")
        return
  
    c = a
    #for i in range (MAX_ITER):
    while ((b-a) >= 0.01):
 
        # Se encuentra el punto medio
        c = (a+b)/2
  
        # Se verifica si el punto medio es la raíz
        if (func(eq, c) == 0.0):
            break
  
        # Se decide qué lado se reemplaza en la siguiente iteración
        if (func(eq, c)*func(eq, a) < 0):
            b = c
        else:
            a = c
             
    print("El valor de la raíz es: ","%.4f"%c)

#Programa principal
#Se ingresa la ecuación a utilizar y se muestra al usuario
potencia = int(input("Ingresa el mayor exponente en la ecuación: "))
while potencia <= 0:
    print("La cantidad debe ser positiva")
    potencia = int(input("Ingresa el mayor exponente en la ecuación: "))
eq = ""
for i in reversed(range (potencia + 1)):
    num = float(input("Ingresa el coeficiente de x^" + str(i) + ": "))
    if i == 0:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ")"
    else:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ") + "
print("La ecuación a utilizar es: " + eq)
print("Observe la gráfica y elija 1 punto antes y otro después de la unión entre la gráfica y el eje x")

#Se diseña la gráfica para la ecuación ingresada
xlist = np.linspace(-10, 10,num=1000)
ylist = func(eq, xlist)
plt.figure(dpi=120)
plt.plot(xlist,ylist)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
plt.ylim(-10,10)
plt.show()

#Se solicitan los puntos iniciales para hacer los cálculos
a = float(input("Ingresa un punto por la izquierda de la gráfica: "))
b = float(input("Ingresa un punto por la derecha de la gráfica: "))

#Se ejecuta el método
bisection(a, b)