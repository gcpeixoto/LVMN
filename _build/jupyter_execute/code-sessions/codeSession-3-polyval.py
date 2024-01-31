#!/usr/bin/env python
# coding: utf-8

# # _Code Session_ 3: Raízes de Polinômios

# In[1]:


import numpy as np, matplotlib.pyplot as plt 


# ## Determinação de raízes de polinômios

# ### `roots`
# 
# A função `roots` computa as raízes de uma função dentro de um intervalo dado usando o método de Hörner. 
# O único argumento de entrada desta função é
# 
# 1. o _array_ `p` com os coeficientes dos termos do polinômio.
# 
# $$P(x) = p_n x^n + p_{n-1} x^{n-1} + \ldots + p_1x + p_0$$
# 
# 
# O argumento de saída é:
# 
# - `x`: _array_ com as raízes de $P(x)$.
# 

# ### Problema 1 
# 
# Determine as raízes de $P(x) = 3x^3 +7x^2 - 36x + 20$.

# #### Resolução

# Para tornar claro, em primeiro lugar, vamos inserir os coeficientes de $P(x)$ em um _array_ chamado `p`. 

# In[20]:


p = np.array([9,8,7,5,3,2,-1,-3.2,-4/5,])


# Em seguida, fazemos: 

# In[21]:


x = np.roots(p)


# Podemos imprimir as raízes da seguinte forma:

# In[22]:


for (i, v) in enumerate(x):
    print(f'Raiz {i}: {v}')


# In[ ]:





# ### `polyval` 
# 
# Podemos usar a função `polyval` do `numpy` para avaliar $P(x)$ em $x = x_0$. Verifiquemos, analiticamente, se as raízes anteriores satisfazem realmente o polinômio dado.

# In[23]:


for i in x: 
    v = np.polyval(p,i)
    print(f'P(x) = {v}')


# Note que as duas últimas raízes são "muito próximas" de zero, mas não exatamente zero. 

# Podemos também fazer uma verificação geométrica plotando o polinômio e suas raízes. 

# In[24]:


xx = np.linspace(np.min(x)-0.5,np.max(x)+0.5)
plt.plot(xx,np.polyval(p,xx));
for i in x:
    plt.plot(i,np.polyval(p,i),'or')


# ### Problema 2
# 
# Determine as raízes de $P(x) = x^4 - 3x^2 + 3x$.

# #### Resolução

# Resolvendo diretamente com `roots` e usando `polyval` para verificação, temos:

# In[7]:


# coeficientes e raízes
p = np.array([1,0,-3,3,0])
x = np.roots(p)


# In[8]:


# imprimindo as raizes
for i, v in enumerate(x):
    print(f'Raiz {i}: {v}')


# Note que, neste caso, as raízes são complexas.

# ### Problema 3
# 
# Determine as raízes de $P(x) = x^5 - 30x^4 + 361x^3 - 2178x^2 + 6588x - 7992$.

# #### Resolução

# In[9]:


# coeficientes e raízes
p = np.array([1,-30,361,-2178,6588,-7992])
x = np.roots(p)


# In[10]:


# imprimindo as raizes
for i, v in enumerate(x):
    print(f'Raiz {i}: {v}')

