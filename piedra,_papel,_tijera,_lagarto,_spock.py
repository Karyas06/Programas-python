# -*- coding: utf-8 -*-
"""piedra, papel, tijera, lagarto, spock

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jVJrlpmKLdYaqyeSIes7wYt1eMuPfWxw
"""

#1 piedra
#2 papel
#3 tijera
#4 lagarto
#5 spock

jugador1=float(input('Ingrese su opcion jugador 1 '))
jugador2=float(input('Ingrese su opcion jugador 2 '))
if((jugador1==1)and(jugador2==2)):
  print('Gano jugador 2')
elif((jugador1==1)and(jugador2==3)):
  print('Gano jugador 1')
elif((jugador1==1)and(jugador2==1)):
  print('Empate')
elif((jugador1==1)and(jugador2==4)):
  print('Gano jugador 1')
elif((jugador1==1)and(jugador2==5)):
  print('Gano jugador 2')
elif((jugador1==2)and(jugador2==3)):
  print('Gano jugador 2')
elif((jugador1==2)and(jugador2==1)):
  print('Gano jugador 1')
elif((jugador1==2)and(jugador2==2)):
  print('Empate')
elif((jugador1==2)and(jugador2==4)):
  print('Gano jugador 2')
elif((jugador1==2)and(jugador2==5)):
  print('Gano jugador 1')
elif((jugador1==3)and(jugador2==1)):
  print('Gano jugador 2')
elif((jugador1==3)and(jugador2==2)):
  print('Gano jugador 1')
elif((jugador1==3)and(jugador2==3)):
  print('Empate')
elif((jugador1==3)and(jugador2==4)):
  print('Gano jugador 1')
elif((jugador1==3)and(jugador2==5)):
  print('Gano jugador 2')
elif((jugador1==4)and(jugador2==1)):
  print('Gano jugador 1')
elif((jugador1==4)and(jugador2==2)):
  print('Gano jugador 1')
elif((jugador1==4)and(jugador2==3)):
  print('Gano jugador 2')
elif((jugador1==4)and(jugador2==4)):
  print('Empate')
elif((jugador1==4)and(jugador2==5)):
  print('Gano jugador 1')
elif((jugador1==5)and(jugador2==1)):
  print('Gano jugador 1')
elif((jugador1==5)and(jugador2==2)):
  print('Gano jugador 2')
elif((jugador1==5)and(jugador2==3)):
  print('Gano jugador 1')
elif((jugador1==5)and(jugador2==4)):
  print('Gano jugador 2')
elif((jugador1==5)and(jugador2==5)):
  print('Empate')