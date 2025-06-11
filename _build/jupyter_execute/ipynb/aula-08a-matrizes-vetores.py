#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
plt.style.use('styles/gcpeixoto-book.mplstyle')


# # Álgebra Linear Computacional básica

# ## Objetivos
# 
# - Associar conceitos abstratos de Álgebra Linear a estruturas computacionais; 
# - Realizar operações básicas com vetores e matrizes;
# - Saber como resolver sistemas lineares de pequeno porte;
# - Calcular autovalores e autovetores em matrizes reais;

# ## Introdução
# 
# Neste capítulo, mostraremos como realizar operações básicas entre matrizes e vetores usando o computador. A manipulação de matrizes e vetores é essencial em muitas ciências, principalmente para resolver sistemas lineares. 
# 
# As matrizes são utilizadas na computação para armazenar informações bidimensionais. Em particular, podem representar translação, rotação, escalonamento e sistemas de equações. O estudo da relação entre algoritmos e métodos computacionais para trabalhar eficientemente com matrizes e vetores é realizado no âmbito da _Álgebra Linear Computacional_.

# ## Matrizes e vetores
# 
# Uma matriz ${\bf A}$ de ordem $m \times n$ pode ser escrita como:
# 
# $${\bf A} = 
# \begin{bmatrix}
# a_{11} & a_{12} & \ldots & a_{1n} \\
# a_{21} & a_{22} & \ldots & a_{2n} \\
# \vdots & \vdots & \ddots & \vdots \\
# a_{m1} & a_{m2} & \ldots & a_{mn}
# \end{bmatrix}$$
# 

# As colunas de uma matriz com $m$ linhas correspondem a $n$ vetores $\vec{v}_1, \vec{v}_2, \ldots,\vec{v}_n$, de maneira que
# 
# $${\bf A} = 
# \begin{bmatrix}
# \vec{v}_1 & \vec{v}_2 & \ldots & \vec{v}_n \\
# \end{bmatrix}$$
# 
# é uma representação equivalente para a matriz anterior.

# Em Python, usamos o módulo _numpy_ para trabalhar com matrizes e vetores. Vetores são _arrays_ 1D, ao passo que matrizes são _arrays_ 2D, ou seja, um "_array_ de _arrays_".

# **Exemplo.** Represente computacionalmente os vetores do $\mathbb{R}^3$ a seguir:
# 
# - $\vec{u} = 3\vec{i} - 2\vec{j} + 9\vec{k}$
# - $\vec{v} = -2\vec{i} + 4\vec{j}$
# - $\vec{w} = \vec{i}$

# ```{note}
# O _NumPy_ possui uma classe especial para se trabalhar com matrizes e vetores em uma ou duas dimensões, a saber o tipo `matrix`, ou `mat`. Com objetos `matrix`, as  operações particulares de multiplicação matriz-matriz ou matriz-vetor comportam-se diferentemente daquelas na classe `ndarray`. Neste texto, abordaremos apenas os tipos `ndarray` porque são aplicáveis também a matrizes multidimensionais.
# ```

# In[41]:


import numpy as np

u = np.array([3,-2,9])
v = np.array([-2,4,0])
w = np.array([1,0,0])
print(u), print(v), print(w);


# **Exemplo.** Represente computacionalmente a matriz 3 x 3 dada por
# 
# $${\bf A} = 
# \begin{bmatrix}
# \vec{u} & \vec{v} & \vec{w} \\
# \end{bmatrix}$$

# Observe que os vetores devem ser escritos como "coluna".

# In[49]:


A = np.array([u,v,w]).T


# **Exemplo.** Represente computacionalmente a matriz 
# 
# $$ 
# \begin{bmatrix}
# 2 & -2 \\
# 4 & 1 \\
# 2 & 1 
# \end{bmatrix}$$
# 

# Vamos escrever linha por linha.

# In[43]:


L1 = np.array([2,-2]) # linha 1
L2 = np.array([4,1]) # linha 2
L3 = np.array([2,1]) # linha 3

A2 = np.array([L1,L2,L3]) # lista de listas
print(A2)


# Diretamente, poderíamos também definir: 

# In[44]:


A3 = np.array([[2,-2],[4,1],[2,1]])
print(A3)


# Note que cada lista representa uma linha. 

# ### Transposição 
# 
# Matrizes e vetores podem ser transpostos com `.T`:

# In[45]:


A2T = A2.T
print(A2T)


# In[46]:


uu0 = [1,2,3]
uu1 = np.array(uu0)
type(uu0), type(uu1)


# Assim, com as variáveis antes definidas, poderíamos, equivalentemente, fazer para ${\bf A}$:

# In[47]:


# modo 2: matriz transposta
At = np.array([u,v,w]).T 
print(At)


# ### Teste de igualdade 
# 
# Podemos verificar a igualdade entre matrizes como

# In[62]:


np.array([np.array([1,2,3]), np.array([-4,2,1]), np.array([3,3,1])])


# No caso de vetores:

# In[11]:


# vetor "linha" não difere
# do vetor "coluna"
u == u.T 


# ## Operações fundamentais

# ### Adição e subtração
# 
# A adição (subtração) de matrizes e vetores pode ser realizada de modo usual com computação vetorizada.

# **Exemplo:** $\vec{u} \pm \vec{v}$

# In[63]:


# adição 
ad = u + v
print(ad)

# subtração
sub = u - v
print(sub)


# **Exemplo:** $\bf{A} \pm \bf{B}$, com 
#     
# $${\bf B} = 
# \begin{bmatrix}
# \vec{u} & 2\vec{u} & 3\vec{v} \\
# \end{bmatrix}$$    

# In[64]:


# adição

B = np.array([u,2*u,3*v]).T

ad2 = A + B
print(ad2)

sub2 = A - B
print(sub2)


# ### Produto interno
# 
# O produto interno $\langle \vec{u}, \vec{v}\rangle$ é computado com `.dot`:

# In[65]:


pi = np.dot(u,v)
print(pi)

pi2 = np.dot(np.array([3,1]),np.array([-1,-1]))
print(pi2)


# Uma segunda forma, mais imediata, emprega o operador infixo `@`:

# In[66]:


pii = u @ v
print(pii)

pii2 = np.array([3,1]) @ np.array([-1,-1])
print(pii2)


# ### Norma de vetor
# 
# A norma $||\vec{u}||$ de um vetor $\vec{u}$ é calculada como:

# In[17]:


np.sqrt(np.dot(u,u))


# ### Produto de matrizes
# 
# O produto $\bf{A}\bf{B}$ entre matrizes bidimensionais pode ser calculado com `np.dot`, mas recomenda-se usar `np.matmul`.

# In[18]:


# não tem o mesmo efeito para 
# matrizes A e B de tamanhos arbitrários
np.dot(A,B)


# In[19]:


# uso recomendado para a operação tradicional
np.matmul(A,B)


# ### Produto entre matriz e vetor
# 
# Neste caso, sendo ${\vec{\vec A}}$ (dois símbolos indicam que a matriz é uma grandeza de ordem 2, ao passo que o vetor é de ordem 1 e aqui usamos para consistência de notação) uma matriz $m \times n$ e ${\vec{b}}$ e um vetor $n \times 1$, respectivamente, o produto $\vec{\vec{A}}\vec{b}$ é dado por:

# In[107]:


b = np.array([3,4,1])

np.dot(A,b)


# ## Demais operações com `numpy.linalg`
# 
# Para outras operações, devemos utilizar o submódulo `numpy.linalg`. Para importá-lo com o _alias_ `lin`, fazemos:

# In[108]:


import numpy.linalg as lin


# ### Determinante
# 
# O determinante de ${\bf A}$ é dado por $\det({\bf A})$ e pode ser computado pela função `det`.

# In[109]:


# calculando o determinante da matriz
det = lin.det(A)
print(det)


# ### Inversa de uma matriz
# 
# A inversa de uma matriz é dada por ${\bf A}^{-1}$, onde ${\bf A}{\bf A}^{-1}={\bf I}$, e ${\bf I}$ é a matriz identidade.
# Para usar esta função, devemos fazer:

# In[111]:


B2 = np.array([[1,2,3],
              [2,3,4],
              [1,2,0]]) 

B3 = lin.inv(B2)
np.matmul(B3,B2) == np.eye(3)


# ### Soluções de sistemas lineares
# 
# Para resolver sistemas lineares, devemos escrever as equações em forma de matriz, ou seja, ${\vec{\vec A}}\vec{x} = \vec{b}$ e utilizar `solve`.

# **Exemplo:** Resolva o sistema linear abaixo:
# 
# $$\begin{cases}
# ax + by = c \\ 
# dx + ey = f
# \end{cases}$$
# 
# para $a = -4$, $b = 1$, $c = 1/2$, $d = 3$, $e = 5$ e $f = 10$,  

# In[122]:


A = np.array([ [20,20,60], [40,35,25], [5,5,90] ])
b = np.array([80,65,72])

# solução
x = lin.solve(A, b)
print(x)

np.sqrt( np.dot(np.dot(A,x) - b, np.dot(A,x) - b) )


# In[123]:


Ainv = lin.inv(A)

xx = np.dot(Ainv,b)
xx


# ### Inversa de matriz
# 
# A inversa de uma matriz (faça esta operação apenas para matrizes quadradas de pequena dimensão) pode ser encontrada como:

# In[25]:


Ainv = lin.inv(A)
print(Ainv)


# Para realizar uma "prova real" da solução do sistema anterior, poderíamos fazer:

# In[26]:


x2 = np.dot(lin.inv(A), b)
print(x2)


# Note, entretanto que:

# In[27]:


x == x2


# Isto ocorre devido a erros numéricos. Um teste mais adequado deve computar a norma do vetor "erro", dado por ${\bf e} = \bf{b} - \bf{A}\bf{x}$. A norma pode ser calculada diretamente com:

# In[28]:


e = b - np.dot(A,x)
lin.norm(e)


# Isto é, esperamos que $||{\bf e}|| \approx 0$ quando a solução do sistema for exata, a menos de erros numéricos.

# ```{warning}
# Nunca compare dois números reais (`float`) usando igualdade. Ou seja, `x == y`, não é, em geral, um bom teste lógico para verificar se `x` e `y` possuem o mesmo valor numérico.
# ```

# ## Algumas matrizes especiais

# ### Nula
# 
# Para criar uma matriz nula de ordem _m x n_, usamos `zeros`.

# In[124]:


m,n = 2,6
np.zeros((m,n))


# ### Identidade
# 
# Uma matriz identidade (quadrada) de ordem _p_ é criada com `eye`.

# In[30]:


p = 4
np.eye(p)


# ### Matriz de "uns"
# 
# Uma matriz composta apenas de valores 1 de ordem _m x n_ pode ser criada com `ones`:

# In[31]:


np.ones((3,5))


# ### Triangular inferior
# 
# A matriz triangular inferior de uma dada matriz pode ser criada com `tril`. Note que podemos também defini-la explicitamente, linha a linha.

# In[32]:


# os valores correspondentes
# são zerados
np.tril(B)


# ### Triangular superior
# 
# A matriz triangular superior de uma dada matriz pode ser criada com `triu`. Note que podemos também defini-la explicitamente, linha a linha.

# In[33]:


np.triu(B)


# **Exercício.** Por que há dois valores `False` no teste a seguir? 

# In[34]:


B == np.tril(B) + np.triu(B)


# ## Autovalores e autovetores
# 
# Um vetor ${\bf v} \in V$, ${\bf v} \neq {\bf 0}$ é vetor próprio de ${\bf A}$ se existir $\lambda \in \mathbb{R}$ tal que 
# 
# $${\bf Av}=\lambda {\bf v}.$$
# 
# O número real $\lambda$ é denominado valor próprio (autovalor) de ${\bf A}$ associado ao vetor próprio (autovetor) ${\bf v}$.

# In[35]:


A = np.array([[2,1],
              [1,-5]])

w, v = lin.eig(A)
a,b = w

# autovalores
print(a,b)

# autovetor 1
print(v[:,0])

# autovetor 2
print(v[:,1])


# ## Somas e valores extremos 
# 
# Podemos calcular somas de elementos de matrizes e vetores de maneiras diferentes. Para matrizes, em particular, há soma total, por linha, ou por coluna. 

# In[36]:


a = np.array([1,-2,-3,10])

# soma de todos os elementos 
np.sum(a)


# In[37]:


# modo alternativo
a.sum() 


# In[38]:


# soma total de matriz
O = np.ones((5,3))

np.sum(O)


# In[39]:


# modo alternativo
O.sum()


# In[127]:


# soma por linha 

M = np.array( [ [ [ [-1,0],[1,0] ], [ [-1,0],[1,0] ]] ])

np.sum(M,axis=3)


# In[128]:


# soma por coluna 
np.sum(O,axis=1)


# Valores máximos e mínimos, absolutos ou não, também podem ser computados com funções simples.

# In[42]:


# min
np.min(a)


# In[43]:


# max
np.max(a)


# In[44]:


# modo alternativo
a.min()


# In[45]:


a.max()


# In[46]:


# mínimo absoluto 
np.abs(a).min()


# In[47]:


# máximo absoluto
np.abs(a).max()


# In[48]:


O2 = np.array([[-4,5],[2,7]])

# min
np.min(O2)


# In[49]:


# max 
np.max(O2)


# In[50]:


O2.min()


# In[51]:


O2.max()


# In[52]:


np.abs(O2).min()


# In[53]:


np.abs(O2).max()


# In[54]:


plt.rcdefaults()


# In[139]:


np.min( np.array([[1,-2,-3], [0,0,4]]), axis=0)


# In[ ]:




