# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:59:41 2023

@author: Vinicius Campelo
"""

from control import*
import matplotlib.pyplot as plt
import numpy
from scipy import signal

def get_zeros(planta):
    
    zeros = input("informe os zeros separando por virgula:\n").split(",")
    if zeros == ['']:
        return planta
    for zero in zeros:
        planta = planta*(s-complex(zero))
    return planta

def get_poles(planta):
    poles = input("informe os polos separando por virgula:\n").split(",")
    for pole in poles:
        planta = planta/(s-complex(pole))
    return planta

def get_ideal_system():
    order = input("O sistema ideal é de ordem 1 ou ordem 2?\n")
    if order == "1":
        ts = float(input("Informe o tempo se assentamento\n"))
        return 1/(s*ts/5),ts
    if order == "2":
        second_order = input("Informe o tempo de assentamento e maximo percentual separado por virgula\n").split(",")
        ts = float(second_order[0])
        mp = float(second_order[1])
        
        z = (np.log(mp)**2/(np.pi**2+np.log(mp)**2))**0.5
        if z<0.78:
            wn = 3.716/(z*ts)
        else:
            wn = (9.274*z-3.394)/ts
        
        return wn**2/(s*(s+2*z*wn)), ts

def PI(entrada,saida):
            #PI por minimos quadrados
            int_entrada = [0]
            for j in range(len(u)):
                int_entrada.append(int_entrada[j]+entrada[j]*dt)    
            x = np.array([[entrada[i],int_entrada[i]] for i in range(len(SimuTime))])
            p = (np.linalg.inv(x.T @ x) @ x.T) @ saida
            #Obtendo parametros dos minimos
            k = p[0]
            a = p[1]/p[0]
            return k*(s+a)/s

def PID(entrada, saida):
    int_entrada = [0,0]
    int_saida = [0,0]
    d_entrada = [0]

    for j in range(1,len(u)):
        d_entrada.append((entrada[j]-entrada[j-1])/dt)
        int_entrada.append(int_entrada[j]+entrada[j]*dt)  
        int_saida.append(int_saida[j]+saida[j]*dt)
    x = np.array([[entrada[i],int_entrada[i],d_entrada[i]] for i in range(len(SimuTime))])
    p = (np.linalg.inv(x.T @ x) @ x.T) @ saida
    #Obtendo parametros dos minimos
    k = p[2]
    a = p[0]/p[2]
    b = p[1]/p[2]
    return k*(s**2+a*s+b)/s
        
s = tf([1,0], [0,1])

#Obter planta
planta = 1
planta = get_zeros(planta)
planta = get_poles(planta)
planta = float(input("Informe ganho da planta:\n"))*planta
print("A planta é dada por:\n")
print(planta)    

#Obter requisitos de projeto
ideal,tempo = get_ideal_system()
print("O systema ideal é")
print(ideal)

#Gerar respostas ao degrau
SimuTime = np.linspace(0,tempo*2,5000)
u = [1]*len(SimuTime)
dt = tempo*2/5000
#A entrada será a saida da planta
x , entrada = forced_response(planta, SimuTime, u, X0=0)
#A saida será o sistema ideal em malha fechada
x , saida = forced_response(ideal, SimuTime, u, X0=0)


Ctype = input("Para controlador PI responda 1, para PID responda 2\n")
if Ctype == "1":
    controler = PI(entrada,saida)
if Ctype == "2":
    controler = PID(entrada,saida)

print("Controlador Ideal:")
print(controler)

FTMA = planta*controler
FTMF = feedback(FTMA,1)
print("Confira margens do sistema projetado")
print(margin(FTMF))


x , xxx = forced_response(ideal/(ideal+1), SimuTime, u, X0=0)
plt.plot(x,entrada,label="planta")
plt.plot(x,xxx,label="ideal")
plt.legend()


x , yyy = forced_response(FTMF, SimuTime, u, X0=0)
plt.plot(x,yyy,label="Sistema projetado")
plt.legend()
plt.show()










