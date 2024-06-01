#!/usr/bin/env python
# coding: utf-8

# (clipping-decimal)=
# # Recorte 9: Aritmética exata e números racionais

# Em Python, os módulos `decimal` e `fractions` oferecem alternativas para manipulação numérica por meio de aritmética exata e números racionais. Aqui temos aplicações simples de cada um.

# ## `decimal`

# In[ ]:


from decimal import *


# - Módulo `decimal` baseado no modelo de ponto flutuante, mas focado na aritmética computacional que equivale à feita por humanos.

# - Exemplo de operação que destoa da prática. Deveríamos ter objetivamente 2.2

# In[8]:


0.3 + 1.9 


# - A aritmética de ponto flutuante é sensível

# In[9]:


0.1 + 0.1 + 0.1 - 0.3


# - O módulo `decimal` trabalha com exatidão, dentro 

# In[19]:


getcontext().prec = 16
Decimal(0.3) + Decimal(1.9)


# In[20]:


## ?
Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)


# In[15]:


getcontext().prec = 60
Decimal(1) / Decimal(7)


# In[16]:


getcontext()


# ## `fractions`
# 
# Módulo que fornece suporte à representação de números racionais (frações).

# In[21]:


from fractions import Fraction


# In[25]:


Fraction('0.1')


# In[24]:


Fraction(Decimal('0.1'))


# In[27]:


Fraction(32, 16), Fraction(16,32)


# In[28]:


Fraction('8/7')

