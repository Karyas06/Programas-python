# -*- coding: utf-8 -*-
"""calculadora basica

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JUo8qzAIE2CSesebZHc8NdPyeK3Ybkjq
"""

n1=int(input("primer numero 3"))
n2=int(input("segundo numero "))
op=int(input("operacion a realizar "))

#1. suma
#2. resta
#3. multiplicacion
#4. division
t=0

if (op==1):
  t=n1+n2
elif (op==2):
  t=n1-n2
elif (op==3):
  t=n1*n2
elif (op==4):
  t=n1/n2

print(t)