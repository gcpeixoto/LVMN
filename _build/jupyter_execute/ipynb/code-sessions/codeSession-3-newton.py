#!/usr/bin/env python
# coding: utf-8

# # _Code Session_ 3: `newton`

# O propósito desta _Code Session_ é resolver problemas de determinação de raízes de equações não lineares polinomiais e transcendentais utilizando a função `newton` do módulo `scipy.optimize`. Replicaremos alguns problemas da _Code Session_ 1 e faremos algumas adições.

# In[2]:


# Importação de módulos
import numpy as np, matplotlib.pyplot as plt, sympy as sy


# ## Determinação de raízes

# ## `newton`
# 
# A função `newton` localiza a raiz de uma função dentro de um intervalo dado usando o método de Newton, sob especificação da primeira derivada. Os argumentos de entrada obrigatórios desta função são: 
# 
# 1. a função-alvo `f` (contínua)
# 2. a estimativa inicial `x0`
# 
# Os parâmetros opcionais relevantes são: 
# 
# - `fprime`: a derivada da função, quando disponível. Caso ela não seja especificada, o _método da secante_ é usado. 
# - `fprime2`: a segunda derivada da função, quando disponível. Se ela for especificada, o _método de Halley_ é usado. 
# - `tol`: tolerância (padrão: 1.48e-08)
# - `maxiter`: número máximo de iterações (padrão: 50)
# - `disp`: mostra erro se algoritmo não convergir (padrão: True) 
# 
# O argumento de saída é:
# 
# - `x`: a estimativa para a raiz de `f`

# In[3]:


# Importação de 'newton'
from scipy.optimize import newton


# ### Problema 1
# 
# Encontre a menor raiz positiva (real) de $x^{3} - 3.23x^{2} - 5.54x + 9.84 = 0$ pelo método de Newton.

# #### Resolução

# Definimos a função e sua primeira derivada.

# In[14]:


# Função primitiva
def f(x): 
    return x**3 - 3.23*x**2 - 5.54*x + 9.84

# 1a. derivada
def df(x):
    return 3*x**2 - 2*3.23*x - 5.54


# Realizamos a análise gráfica.

# In[25]:


# Análise gráfica 
x = np.linspace(-3,5)
plt.plot(x,f(x))
plt.plot(x,df(x))
plt.axhline(y=0,color='k',ls='--')
plt.legend(['$f(x)$','$f\'(x)$','$y=0$'],
           loc='lower right');
plt.grid()


# Vamos realizar um estudo de diferentes estimativas iniciais e ver o que acontece.

# ##### Estimativa inicial: $x_0 = -1$

# In[18]:


x0 = -1.
x = newton(f,x0,df) # raiz 
print('Raiz: x = %f' % x)


# ##### Estimativa inicial: $x_0 = 0$

# In[19]:


x0 = 0.
x = newton(f,x0,df) # raiz 
print('Raiz: x = %f' % x)


# ##### Estimativa inicial: $x_0 = 3$

# In[23]:


x0 = -300000.
x = newton(f,x0,df) # raiz 
print('Raiz: x = %f' % x)


# ### Problema 2
# 
# Determine a menor raiz não nula positiva de $\cosh(x) \cos(x) - 1 = 0$ dentro do intervalo $(4,5)$.

# #### Resolução:

# Primeiramente, vamos escrever a função `f(x)`.

# In[ ]:


# Função (anônima)
f = lambda x: np.cosh(x)*np.cos(x) - 1 


# Para computar a primeira derivada, utilizaremos computação simbólica. Veja no início deste notebook que inserimos a instrução
# a seguir para chamar objetos do módulo `sympy`.
# 
# ```python
# import sympy as sy
# ```
# 
# Em primeiro lugar, devemos estabelecer uma variável simbólica `xs`.

# In[62]:


# Variável simbólica
xs = sy.Symbol('x')


# Em seguida, devemos utilizar as funções `cosh` e `cos` **simbólicas** para derivar `f`. Elas serão **chamadas de dentro do módulo sympy**.
# 
# Escrevemos a expressão simbólica para a derivada.

# In[63]:


d = sy.diff(sy.cosh(xs)*sy.cos(xs) - 1)
d


# Note que `d` é um objeto do módulo `sympy`

# In[64]:


type(d)


# Podemos agora aproveitar a expressão de `d` para criar nossa derivada. Se imprimirmos `d`, teremos:

# In[65]:


print(d)


# Porém, precisamos indicar que as funções serão objetos numpy. Logo, adicionamos `np`, de modo que:

# In[66]:


df = lambda x: - np.sin(x)*np.cosh(x) + np.cos(x)*np.sinh(x)


# Agora, realizamos a análise gráfica. 

# In[68]:


# analise gráfica 
x = np.linspace(4,5)
plt.plot(x,f(x));
plt.plot(x,df(x));
plt.axhline(y=0,color='r',ls='--');
plt.legend(['$f(x)$','$f\'(x)$','$y=0$']);


# Agora, vamos resolver optando pela estimativa inicial $x_0 = 4.9$.

# In[69]:


# resolução com newton 
x0 = 4.9
x = newton(f,x0,df) # raiz 
print('Raiz: x = %f' % x)


# ## Tarefas 
# 
# 1. Reproduza os Problemas de 3 a 8 da _Code Session 1_ resolvendo com o método `newton`.
# 2. Para os casos possíveis, determine a derivada. Caso contrário, utilize como método da Secante. 
# 3. Pesquise sobre o método de Halley e aplique-o aos problemas usando a função `newton`, mas avaliando-a também com a segunda derivada. 
