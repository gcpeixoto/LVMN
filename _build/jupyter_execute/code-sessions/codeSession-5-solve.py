#!/usr/bin/env python
# coding: utf-8

# # _Code Session_ 5: Sistemas Lineares

# ## `linalg.solve`
# 
# A função `solve` é o método mais simples disponibilizado pelos módulos `numpy` e `scipy` para resolver sistemas matriciais lineares. Como a função pertence ao escopo da Álgebra Linear, ela está localizada em submódulo chamado `linalg`. `solve` calculará a solução exata do sistema como um método direto se a matriz do sistema for determinada (quadrada e sem colunas linearmente dependentes). Se a matriz for singular, o método retorna um erro. Se for de posto deficiente, o método resolve o sistema linear usando um algoritmo de mínimos quadrados. 
# 
# Os argumentos de entrada obrigatórios desta função são: 
# 
# 1. a matriz `A` dos coeficientes
# 2. o vetor independente `b`
# 
# O argumento de saída é:
# 
# - `x`: o vetor-solução do sistema.

# In[7]:


from numpy.linalg import solve


# ### Problema 1
# 
# Uma rede elétrica contém 3 _loops_. Ao aplicar a lei de Kirchoff a cada _loop_, o cientista Hely Johnson obteve as seguintes equações para as correntes $i_1$, $i_2$ e $i_3$ em cada _loop:_
# 
# $$\begin{cases}
# (50 + R)i_1 - Ri_2 - 30i_3 &= 0 \\
# - Ri_1 + (65 + R)i_2 - 15i_3 &= 0 \\
# -30i_1 - 15i_2 + 45i_3 &= 120 
# \end{cases}$$
# 
# Ajude Hely Johnson em seus experimentos e calcule as correntes para os valores de resistência $R = \{ 5 \Omega, 10 \Omega, 20 \Omega \}$.

# ### Resolução

# Podemos começar definindo uma lista para armazenar os valores das resistências de teste:

# In[8]:


R = [5.,10.,15.]


# Em seguida, escreveremos a matriz dos coeficientes e o vetor independente (lado direito). Note que precisamos de uma "lista de listas", ou melhor, um _"array de arrays"_, onde cada _array_ está associado à uma linha da matriz.
# 
# Todavia, vamos definir uma função para montar o sistema em função do valor de $R$ e resolvê-lo. 

# In[9]:


# montagem do sistema
def resolve_sistema(R):
    A = np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ])
    b = np.array([0,0,120])
    x = solve(A,b)
    return x


# Além disso, usaremos um laço `for` para calcularmos todas as respostas necessárias de uma só vez e organizaremos os resultados em dicionário (objeto `dict`):

# In[10]:


# salva soluções agrupadas em um dicionário
sols = {}
for r in R:
    sols[r] = resolve_sistema(r)
    print('Para o valor de resistência R = {0:g} ohms: i1 = {1:g} A, i2 = {2:g} A, i3 = {3:g} A'.format(r, sols[r][0], sols[r][1], sols[r][2]))


# ### Tarefa

# Retorne ao notebook da [Aula 09](../aula-09-eliminacao-gauss.ipynb) e use o conteúdo da aula para fazer uma verificação das soluções encontradas para este problema em cada caso. Use a função `linalg.cond` para calcular o _número de condicionamento_ da matriz do sistema em cada caso. (**Sugestão:** vide `numpy.allclose`)

# ## `linalg.cholesky`
# 
# Assim como `solve`, a função `cholesky` está disponível tanto via `numpy` como `scipy` para determinar a decomposição de Cholesky de uma matriz simétrica e positiva definida.
# 
# Na prática, não é recomendável verificar se uma matriz é positiva definida através dos critérios teóricos. A função `cholesky` não realiza essa checagem. Portanto, é importante que, pelo menos, se saiba que a matriz é simétrica. Para testar se ela atende a propriedade de definição positiva, a abordagem mais direta é usar `cholesky` e verificar se ela retorna uma decomposição de Cholesky. Se não for o caso, um erro será lançado.
# 
# O argumento de entrada desta função é: 
# 
# - `A`: matriz dos coeficientes
# 
# O argumento de saída é:
# 
# - `L`: o fator de Cholesky
# 
# Como importá-la? 
# 
# ```python 
# from numpy.linalg import cholesky
# ```

# In[11]:


from numpy.linalg import cholesky


# ### Problema 2
# 
# Calcule o fator de Cholesky para a matriz $A$ do Problema 1 para $R = 5$.

# In[13]:


R = 5.
B = np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ])

L = cholesky(B)
L


# Podemos verificar a decomposição multiplicando a matriz triangular (fator de Cholesky) pela sua transposta.

# In[19]:


np.matmul(L,L.T)


# In[20]:


B


# Entretanto, não é verdade que

# In[21]:


# por que a igualdade falha 
# para algumas entradas?
B == np.matmul(L,L.T)


# ## Problema 3
# 
# Verificar se uma matriz simétrica é positiva definida.

# In[50]:


# cria matriz simétrica 
C = np.tril(B) - 60
C = np.tril(C) + np.tril(C,-1).T
C


# In[48]:


# erro! 
# matriz não é PD
#cholesky(C)


# In[51]:


# cria outra matriz simétrica
D = np.tril(B) + 1
D = np.tril(D) + np.tril(D,-1).T
D


# In[52]:


# matriz é PD
cholesky(D)


# ## Problema 4
# 
# Resolva o Problema 1 para $R = 10$ usando a fatoração de Cholesky.

# In[55]:


R = 10.
D = np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ])
b = np.array([0,0,120])

# fator 
L = cholesky(D)

# passo 1
# Ly = b
y = solve(L,b)

# passo 2
# L^T x = y
x = solve(L.T,y)

# solução
x


# Compare a solução via Cholesky com a do Problema 1:

# In[59]:


x, sols[10]


# Mais uma vez, note que:

# In[60]:


# A comparação falha.
# Por quê?
x == sols[10]

