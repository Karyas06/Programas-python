# -*- coding: utf-8 -*-
"""fibonacci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u9LKaccPewCocCtyvMXkxULAvIXC3WZk
"""

f0=0
f1=1
ve=int(input("ingresa cuantos numeros: "))
if(ve==1):
  print(f0)
elif(ve==2):
  print(f0)
  print(f1)
elif(ve>2):
  print(f0)
  print(f1)
  for i in range (ve-2):
    fn=f0+f1
    f0=f1
    f1=fn
    
   
    print(fn)