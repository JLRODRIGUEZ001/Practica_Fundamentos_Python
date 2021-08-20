#Libreria para generar datos aleatorios
import random
import matplotlib.pyplot as plt
            #⬆
# para instalar esto necesitas:
# py -m pip install -U pip
#py -m pip install -U pip matplotlib 
#----------------------------------------
#Generar un numero Aleatorio
print(random.randrange(10,100,2))

#Declara la lista

lista=[1,2,3,4,5,6,7,8,9,10]
#Imprime la lista
print("Lista original",lista)
#Mezcla los elementos de la lista al azar
random.shuffle(lista)

print("Lista mixeada",lista)
#Generar una grafica de campana de gasuss
campana=[random.gauss(0.5,0.10) for i in range (1000) ]
#Arma la grafica
plt.hist(campana,bins=15)

#Muestra la grafica
plt.show()