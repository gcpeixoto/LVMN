#!/usr/bin/env python
# coding: utf-8

# # Lista de Exercícios 1
# 
# Solucionário matemático e computacional de exercícios selecionados da Lista de Exercícios 1.

# ## Exercícios computacionais

# ### Q
# Considere a função quadrática $f(x) = x^2 - 100.0001 + 0.01$:
# 
# a) Implemente a fórmula de Bhaskara para calcular suas raízes
# 
# b) Racionalize a fórmula de Bhaskara para a solução $x_2$ (multiplique por $\frac{-b + \sqrt{\Delta}}{-b + \sqrt{\Delta}}$) e refaça o cálculo para $x_2$.
# 
# c) Compare os resultados para $x_2$.

# ### S

# In[1]:


from math import sqrt

# a)

# fórmula de Bhaskara 
a, b, c = 1, -100.0001, 0.01
Delta = b**2 - 4*a*c

# raízes
x1 = (- b + sqrt(Delta))/2*a
x2 = (- b - sqrt(Delta))/2*a

print('x1 = {0}'.format(x1))
print('x2 = {0}'.format(x2))

# b)

# Racionalizando, obtemos 

x2b = 2*c/(-b + sqrt(Delta))
print('x2b = {0}'.format(x2b))


# c) 

"""
Discussão: o valor calculado em b) possui um erro de arredondamento. 
           Como b < 0, o numerador envolve a subtração de
           dois números quase iguais (erro de cancelamento)
           e isto afeta o resultado. 
           
           Com a racionalização da expressão, obtemos uma fórmula
           menos propensa a erros. 
"""
b2 = sqrt(Delta)
print(b2)
print('Diferença no numerador: ' + str(-b - b2))
print('Erro absoluto na solução: ' + str(abs(x2 - x2b)))

