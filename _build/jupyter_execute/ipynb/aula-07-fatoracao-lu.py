#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
plt.style.use('../styles/gcpeixoto-book.mplstyle')


# # Sistemas Lineares na Prática Computacional: Métodos Diretos e Fatoração LU
# 
# <div class="chapter-thumb">
#     <div class="chapter-oa">
#         <h2>Objetivos de aprendizagem</h2>
#         <ul>
#         <li>Compreender os fundamentos dos métodos diretos para a resolução de sistemas lineares e sua relação com a fatoração de matrizes.; </li>
# 	    <li>Aplicar a fatoração LU como estratégia eficiente para resolver sistemas lineares;</li>
# 	    <li>Implementar algoritmos de fatoração LU e resolver sistemas computacionalmente;</li>	    
#         <li>Analisar o condicionamento de matrizes e compreender seu impacto na estabilidade numérica das soluções computacionais;</li>
#         </ul>
#     </div>        
#     <div class="quote-box">
#         <p><em>""
#         </p></em>
#     </div>        
# </div>

# ## Métodos diretos
# 
# A resolução de sistemas lineares é uma das tarefas mais fundamentais da engenharia computacional, estando no cerne de aplicações que vão desde a análise estrutural até a simulação de escoamentos e processos térmicos. Um sistema linear é tipicamente representado na forma matricial $\mathbf{A} \mathbf{x} = \mathbf{b}$, onde $\mathbf{A}$ é uma matriz de coeficientes conhecida, $\mathbf{b}$ é um vetor de termos independentes conhecido, e $\mathbf{x}$ é o vetor de incógnitas a ser determinado. Para resolver esse tipo de problema, pode-se recorrer a métodos iterativos ou diretos. Os métodos diretos visam encontrar a solução exata (dentro dos limites da precisão numérica da máquina) por meio de um número finito de operações. Esses métodos são preferidos quando a matriz $\mathbf{A}$ é de tamanho moderado e bem condicionada, pois permitem resolver o sistema com robustez e sem necessidade de aproximações sucessivas. 
# 
# ### Fatoração de matrizes
# 
# O conceito de fatoração em álgebra linear tem forte analogia com a fatoração algébrica aprendida ainda no ensino médio, como quando escrevemos $x^2 - 9$ como $(x - 3)(x + 3)$, ou $x^2 + 5x + 6$ como $(x + 2)(x + 3)$. Nessas expressões, decompor um polinômio em fatores mais simples permite resolver equações com mais facilidade. Da mesma forma, na álgebra matricial, a fatoração de uma matriz busca expressar uma matriz $\mathbf{A}$ como o produto de duas ou mais matrizes com estrutura conhecida e propriedades computacionalmente vantajosas. Por exemplo, dada uma matriz
# 
# $$\mathbf{A} =\begin{bmatrix}2 & 4 \\4 & 10\end{bmatrix},$$
# 
# podemos reescrevê-la como o produto
# 
# $$\mathbf{A} = \mathbf{L} \mathbf{U} =\begin{bmatrix}1 & 0 \\2 & 1\end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 0 & 2 \end{bmatrix},$$
# 
# onde $\mathbf{L}$ é uma matriz triangular inferior com 1s na diagonal, e $\mathbf{U}$ é uma matriz triangular superior. Essa fatoração, em particular, é chamada de _fatoração LU_, que generaliza a ideia da eliminação Gaussiana, de transformar a matriz densa associada ao sistema em uma matriz triangular superior, para facilitar a resolução. Essa técnica é especialmente poderosa e serve como base para variações mais sofisticadas, como a fatoração com pivotamento e a decomposição de Cholesky para matrizes simétricas positivas definidas. O quadro abaixo resume os principais esquemas de fatoração conhecidos e as condições de funcionamento.
# 
# | Fatoração         | Forma da Decomposição                     | Condições / Observações                                                        |
# |-------------------|--------------------------------------------|---------------------------------------------------------------------------------|
# | LU (genérica)     | $\mathbf{A}$ = $\mathbf{LU}$                                 | A quadrada e não singular. Pode requerer pivotamento para estabilidade.         |
# | LU de Doolittle   | $\mathbf{A}$ = $\mathbf{LU}$, com $\textrm{diag}(L) = 1$            | A quadrada. $\mathbf{L}$ com 1s na diagonal; facilita implementação.                   |
# | LU de Crout       | $\mathbf{A}$ = $\mathbf{LU}$, com $\textrm{diag}(U) = 1$            | A quadrada. $\mathbf{U}$ com 1s na diagonal; alternativa ao Doolittle.                 |
# | LU com pivotamento| $\mathbf{P}\mathbf{A} = \mathbf{LU}$ ou $\mathbf{PAQ}$ = $\mathbf{LU}$                  | Usa permutação $\mathbf{P}$ e $\mathbf{Q}$ para melhorar estabilidade numérica.                     |
# | Cholesky          | $\mathbf{A}$ = $\mathbf{LL}^T$                                | A simétrica, definida positiva. Muito eficiente; reduz pela metade o custo.     |
# | LDL$^T$             | $\mathbf{A}$ = $\mathbf{LDL}^T$                               | A simétrica. $\mathbf{D}$ é diagonal; útil em substituição ao Cholesky quando $\mathbf{A}$ não é positiva definida. |
# | QR                | $\mathbf{A} = QR$                                 | $\mathbf{Q}$ ortogonal, $\mathbf{R}$ triangular superior. Muito usada em problemas de mínimos quadrados. |
# | Thomas            | $\mathbf{A}$ = $\mathbf{LU}$ otimizada                       | Para matrizes tridiagonais. Complexidade linear $\mathcal{O}(n)$.                       |
# | LU blocada          | $\mathbf{A}$ = $\mathbf{LU}$, por blocos                     | Usado para matrizes muito grandes ou estruturadas em blocos.                    |
# | SVD               | $\mathbf{A}$ = $\mathbf{U\Sigma V}^T$                               | Decomposição de valores singulares. Mais geral, usada em problemas mal-condicionados. 
# 
# Neste capítulo, exploraremos o processo de _fatoração LU de Doolittle_ cujo algoritmo busca resolver o sistema $\mathbf{A}\mathbf{x} = \mathbf{b}$, em duas etapas principais. Ambas as etapas envolvem apenas substituições diretas — progressiva e regressiva — que são muito mais eficientes do ponto de vista computacional do que operar diretamente com $\mathbf{A}$. Assim, a fatoração transforma o problema original em uma sequência de tarefas mais simples e rápidas de resolver, além de permitir reaproveitamento em casos com múltiplos vetores $\mathbf{b}$. 
# 

# ## Fatoração LU por substituição de recorrência
# 
# Consideraremos que as matrizes triangulares inferiores $\mathbf{L}$ sempre terão a sua diagonal principal formada por entradas iguais a 1.
# 
# $${\bf A} = \begin{bmatrix}
# 1 & 2 & 4\\
# 3 & 8 & 14\\
# 2 & 6 & 13
# \end{bmatrix} = \mathbf{L}\mathbf{U}$$
# onde
# 
# $${\bf L} = \begin{bmatrix}
# 1 & 0 & 0\\
# L_{21} & 1 & 0\\
# L_{31} & L_{32} & 1
# \end{bmatrix}
# \quad \text{e} \quad
# {\bf U} = \begin{bmatrix}
# U_{11} & U_{12} & U_{13}\\
# 0 & U_{22} & U_{23}\\
# 0 & 0 & U_{33}
# \end{bmatrix}
# $$
# 
# Multiplicando $\mathbf{L}\mathbf{U}$ e definindo a resposta igual a $\mathbf{A}$ temos:
# 
# $$\begin{bmatrix}
# U_{11} & U_{12} & U_{13}\\
# L_{21} U_{11} & L_{21} U_{12} + U_{22} & L_{21} U_{13} + U_{23}\\
# L_{31} U_{11} & L_{31} U_{12} + L_{32} U_{22} & L_{31} U_{13} + L_{32} U_{23} + U_{33}
# \end{bmatrix} = \begin{bmatrix}
# 1 & 2 & 4\\
# 3 & 8 & 14\\
# 2 & 6 & 13
# \end{bmatrix}
# $$
# 
# Agora, através de substituição de recorrência, facilmente encontramos $\mathbf{L}$ e $\mathbf{U}$.
# 
# $$
# {\bf A} = \begin{bmatrix}
# 1 & 2 & 4\\
# 3 & 8 & 14\\
# 2 & 6 & 13
# \end{bmatrix} = \begin{bmatrix}
# 1 & 0 & 0\\
# 3 & 1 & 0\\
# 2 & 1 & 1
# \end{bmatrix} \begin{bmatrix}
# 1 & 2 & 4\\
# 0 & 2 & 2\\
# 0 & 0 & 3
# \end{bmatrix}
# $$

# ## Algoritmo da fatoração LU
# 
# Uma vez decomposta a matriz $\mathbf{A}$ no produto $\mathbf{L}\mathbf{U}$, podemos obter a solução $\mathbf{x}$ de forma direta. O procedimento, equivalente à substituição de recorrência mencionada anteriormente, pode ser resumido como segue: dada $\mathbf{A}$, encontre $\mathbf{L}$ e $\mathbf{U}$ tal que $\mathbf{A} = \mathbf{L}\mathbf{U}$, ou seja, $(\mathbf{L}\mathbf{U})\mathbf{x} = \mathbf{b}$. Em outras palavras:
# 
# - Defina $\mathbf{y} = \mathbf{U}\mathbf{x}$.
# - Resolva o sistema triangular $\mathbf{L}\mathbf{y} = \mathbf{b}$ para $\mathbf{y}$.
# - Finalmente, resolva o sistema triangular $\mathbf{U}\mathbf{x} = \mathbf{y}$ para $\mathbf{x}$.
# 
# O benefício desta abordagem é a resolução de somente sistemas triangulares. Por outro lado, o custo empregado é termos de resolver dois sistemas.

# ### Exemplo
# 
# Encontre a solução $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ do sistema 
# 
# $$
# \begin{bmatrix} 
# 1 & 2 & 4\\ 
# 3 & 8 & 14\\ 
# 2 & 6 & 13 
# \end{bmatrix} 
# \begin{bmatrix} 
# x_1 \\ x_2 \\ x_3 
# \end{bmatrix} 
# = 
# \begin{bmatrix} 
# 3 \\ 13 \\ 4
# \end{bmatrix}.
# $$

# - As matrizes $\mathbf{L}$ e $\mathbf{U}$ já foram obtidas anteriormente.
# 
# $$\mathbf{L} = \begin{bmatrix}
# 1 & 0 & 0\\
# 3 & 1 & 0\\
# 2 & 1 & 1
# \end{bmatrix},
# \quad 
# \mathbf{U} = \begin{bmatrix}
# 1 & 2 & 4\\
# 0 & 2 & 2\\
# 0 & 0 & 3
# \end{bmatrix}$$
# 
# - A próxima etapa é resolver $\mathbf{L}\mathbf{y} = \mathbf{b}$, para o vetor $\mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix}$.
# 
# $$\mathbf{L}\mathbf{y} = \begin{bmatrix}
# 1 & 0 & 0\\
# 3 & 1 & 0\\
# 2 & 1 & 1
# \end{bmatrix}
# \begin{bmatrix}
# y_1 \\ y_2 \\ y_3
# \end{bmatrix} =
# \begin{bmatrix}
# 3 \\ 13 \\ 4
# \end{bmatrix} = \mathbf{b}$$
# 
# Este sistema pode ser resolvido por substituição direta, obtendo $\mathbf{y} = \begin{bmatrix} 3 \\ 4 \\ -6 \end{bmatrix}$.
# 
# - Agora que encontramos $\mathbf{y}$, concluímos o procedimento resolvendo $\mathbf{U}\mathbf{x} = \mathbf{y}$ para $\mathbf{x}$. Ou seja, resolvemos:
# 
# $$
# \mathbf{U}\mathbf{x} = \begin{bmatrix}
# 1 & 2 & 4\\
# 0 & 2 & 2\\
# 0 & 0 & 3
# \end{bmatrix}
# \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = 
# \begin{bmatrix} 3 \\ 4 \\ -6 \end{bmatrix}
# $$
# 
# Realizando a substituição regressiva (baixo para cima; direita para esquerda), obtemos a solução do problema.
# 
# $$\mathbf{x} = \begin{bmatrix} 3 \\ 4 \\ -2 \end{bmatrix}$$

# ### Implementação computacional
# 
# Em implementações computacionais, é comum armazenar as matrizes $\mathbf{L}$ e $\mathbf{U}$ sobre a própria estrutura da matriz original, economizando memória: os elementos abaixo da diagonal representam $\mathbf{L}$ (sem armazenar os 1s da diagonal), e os elementos da diagonal para cima representam $\mathbf{U}$. Além disso, o custo computacional da fatoração LU é da ordem de $\mathcal{O}(n^3)$ para matrizes densas, com $n$ sendo o número de variáveis, mas isso pode ser reduzido consideravelmente em matrizes esparsas ou com estrutura especial (como tridiagonais).
# 
# Abaixo, temos uma implementação de uma fatoração LU sem pivoteamento.

# In[88]:


import numpy as np 

def lu_nopivot(A):
    '''
    Realiza fatoração LU para a matriz A
    
    entrada: 
        A  -  matriz:  array (nxn) 
    
    saida: 
        L,U  - matriz triangular inferior, superior : array (nxn)         
    '''
        
    n = np.shape(A)[0] # dimensao
    L = np.eye(n) # auxiliar 
    
    for k in np.arange(n):
        L[k+1:n,k] = A[k+1:n,k]/A[k,k]        
        for l in np.arange(k+1,n):
            A[l,:] = A[l,:] - np.dot(L[l,k],A[k,:])
            
    U = A
    return (L,U)


# Vamos testar a implementação anterior para uma matriz de quarta ordem:
# 
# $${\bf A} =
# \begin{bmatrix}
# 4 & -2 & -3 &  6 \\  
# 1 &  4 &  2 &  3 \\
# 2 & -3 &  3 & -2 \\ 
# 1 &  5 &  3 &  4
# \end{bmatrix}$$

# In[3]:


A = np.array([[ 4., -2., -3.,  6.],[ 1.,  4.,  2.,  3.],[ 2.,  -3.,  3., -2.],[ 1.,  5.,  3.,  4.]])

L,U = lu_nopivot(A)


# In[4]:


L, U


# ## Resolução de sistemas com `scipy.linalg`

# Métodos adequados para a resolução de sistemas lineares e realizar operações no escopo da Álgebra Linear são encontrados no submódulo `linalg` do `scipy`. Importamos essas funcionalidades com: 
# 
# ```python
# from scipy import linalg
# ```
# 
# Vamos calcular a solução do sistema linear ${\bf A}{\bf x} = {\bf b}$ com
# 
# $${\bf A} = \begin{bmatrix}
# 4   & -2  & -3   & 6   &  \\
# -6  & 7   & 6.5  & -6  &  \\
# 1   & 7.5 & 6.25 & 5.5 &  \\
# -12 & 22  & 15.5 & -1 
# \end{bmatrix},
# \quad
# {\bf b} = \begin{bmatrix}
# 12   \\
# -6.5 \\
# 16   \\
# 17 
# \end{bmatrix}$$

# Vamos importar os módulos e escrever a matriz ${\bf A}$.

# In[5]:


import numpy as np
from scipy import linalg

A = np.array([[4,-2,-3,6],[-6,7,6.5,-6],[1,7.5,6.25,5.5],[-12,22,15.5,-1]])
print(A)


# Agora, vamos escrever o vetor ${\bf b}$.

# In[6]:


b = np.array([12,-6.5,16,17])
print(b)


# Podemos checar as dimensões com

# In[7]:


# dimensões de A
A.shape


# In[8]:


# dimensão de b
b.shape


# A solução do sistema pode ser obtida através do método `linalg.solve`.

# In[9]:


x = linalg.solve(A,b)
print(x)


# Matematicamente, a solução do sistema anterior é dada por ${\bf x} = {\bf A}^{-1}{\bf b}$. Podemos até invocar a matriz inversa aqui com `linalg.inv(A).dot(b)` e a solução é a mesma que no caso anterior.

# In[10]:


x2 = linalg.inv(A).dot(b)
print(x2)


#  Por outro lado, este método é ineficiente. Computacionalmente, a inversão de matrizes **não** é aconselhável. 

# ### Verificação da solução 
# 
# Podemos usar o fato de que ${\bf A}{\bf A}^{-1}{\bf b} - {\bf b} = {\bf 0}$.

# In[11]:


x3 = A.dot(linalg.inv(A).dot(b)) - b
print(x3)


# Note que o vetor é próximo do vetor nulo, mas não identicamente nulo.

# Podemos também computar a **norma do resíduo (erro)**: $||{\bf r}|| = ||{\bf b} - {\bf A}{\bf x}|| =  \langle {\bf b} - {\bf A}{\bf x}, {\bf b} - {\bf A}{\bf x} \rangle^{1/2}$

# In[12]:


r = b - A.dot(x) 
np.sqrt(r.dot(r))


# Como a norma do resíduo é próxima de zero, a solução do sistema linear é assumida como correta.

# ## Eliminação Gaussiana
# 
# A Eliminação Gaussiana (EG) é um algoritmo utilizado para resolver sistemas de equações lineares ao reduzir a matriz plena associada do sistema a uma matriz triangular. Este processo também é chamado de _escalonamento_. Abaixo, usaremos uma matriz genérica 3x3 para exemplificação.
# 
# Os passos para a EG são os seguintes:

# 1. Escrever o sistema linear na forma de _matriz estendida_ usando os coeficientes das variáveis como elementos da matriz e o vetor independente como sendo a última coluna;
# 
# $$\begin{array}{c}a_{11}x_1+a_{12}x_2+a_{13}x_3 = b_1 \quad(L_1)\\
# a_{21}x_1+a_{22}x_2+a_{23}x_3 = b_2 \quad(L_2)\\
# a_{31}x_1+a_{32}x_2+a_{33}x_3 = b_3 \quad(L_3)\\
# \downarrow\\
# \left[
# \begin{array}{ccc|c}
# 	a_{11}&a_{12}&a_{13}&b_{1}\\
# 	a_{21}&a_{22}&a_{23}&b_{2}\\
# 	a_{31}&a_{32}&a_{33}&b_{3}
# \end{array}
# \right]
# \end{array}$$

# 2. Realizar operações elementares de combinação linear e permutação entre linhas;
# 
# - Multiplicação por escalar:    
# $$
# \begin{array}{c}
# L_2 \leftarrow L_2 .w\ \Rightarrow\ 
# \begin{bmatrix}
# a_{11}&a_{12}\\
# a_{21}&a_{22}\\
# \end{bmatrix} \rightarrow
# \begin{bmatrix}
# a_{11}&a_{12}\\
# w.a_{21}&w.a_{22}\\
# \end{bmatrix}
# \end{array}
# $$
# 
# - Combinação linear:    
# $$
# \begin{array}{c}
# L_2 \leftarrow L_2 - L_1.w\ \Rightarrow\ 
# \begin{bmatrix}
# a_{11}&a_{12}\\
# a_{21}&a_{22}\\
# \end{bmatrix} \rightarrow
# \begin{bmatrix}
# a_{11}&a_{12}\\
# a_{21}-a_{11}.w&a_{22}-a_{12}.w\\
# \end{bmatrix}
# \end{array}
# $$
# 
# - Permutação:
#     
# $$
# \begin{array}{c}
# L_2 \leftarrow L_1\ e\ L_1\leftarrow L_2\ \Rightarrow\ 
# \begin{bmatrix}
# a_{11}&a_{12}\\
# a_{21}&a_{22}\\
# \end{bmatrix} \rightarrow
# \begin{bmatrix}
# a_{21}&a_{22}\\
# a_{11}&a_{12}\\
# \end{bmatrix}
# \end{array}
# $$

# 3. Anular todos os elementos na porção triangular inferior da matriz original, isto é, todas as entradas exatamente abaixo das entradas dispostas na diagonal principal;
# 
# $$\left[
# \begin{array}{ccc|c}
# 	a_{11}&a_{12}&a_{13}&b_{1}\\
# 	a_{21}&a_{22}&a_{23}&b_{2}\\
# 	a_{31}&a_{32}&a_{33}&b_{3}
# \end{array}
# \right]\ \rightarrow\ 
# \left[
# \begin{array}{ccc|c}
# 	a_{11}^{(k)}&a_{12}^{(k)}&a_{13}^{(k)}&b_{1}^{(k)}\\
# 	0&a_{22}^{(k)}&a_{23}^{(k)}&b_{2}^{(k)}\\
# 	0&0&a_{33}^{(k)}&b_{3}^{(k)}
# \end{array}
# \right]$$

# 4. A partir da forma triangular, realizar a substituição regressiva.
# 
# $$
# \left[
# \begin{array}{ccc|c}
# 	a_{11}^{(k)}&a_{12}^{(k)}&a_{13}^{(k)}&b_{1}^{(k)}\\
# 	0&a_{22}^{(k)}&a_{23}^{(k)}&b_{2}^{(k)}\\
# 	0&0&a_{33}^{(k)}&b_{3}^{(k)}
# \end{array}
# \right]\ \rightarrow\ 
# \left\{
# \begin{array}{c}
# x_3 = \frac{b_3^{(k)}}{a_{33}^{(k)}},\ a_{33}^{(k)} \neq 0\\\\
# x_2 = \frac{b_2^{(k)}-a_{23}^{(k)}.x_3}{a_{22}^{(k)}},\ a_{22}^{(k)} \neq 0\\\\
# x_1 = \frac{b_1^{(k)}-a_{12}^{(k)}.x_2-a_{13}^{(k)}.x_3}{a_{11}^{(k)}},\ a_{11}^{(k)} \neq 0\\\\
# \end{array}
# \right.
# $$

# Vejamos um exemplo numérico de como funciona a Eliminação Gaussiana.

# In[13]:


# matriz
M = np.array([[1.0,1.5,-2.0],[2.0,1.0,-1.0],[3.0,-1.0,2.0]])
print(M)


# In[14]:


# zeramento da segunda linha 
m1 = M[1,0]/M[0,0]
M[1,:] += - m1*M[0,:]
print(M)


# In[15]:


# zeramento da terceira linha
m2 = M[2,0]/M[0,0]
M[2,:] += - m2*M[0,:]
print(M)


# In[16]:


# eliminação
M = np.array([[1.0,1.5,-2.0],[2.0,1.0,-1.0],[3.0,-1.0,2.0]])
b = np.array([-2,3,1])

m,n = M.shape
for i in range(m):
    for j in range(i+1,n):
        pivo = M[j,i]/M[i,i]                        
        for k in range(m):
            M[j,k] += -pivo*M[i,k]

print(M)            


# In[17]:


# função simples para eliminação
def eliminacao(M):
    m,n = M.shape
    for i in range(m):
        for j in range(i+1,n):
            pivo = M[j,i]/M[i,i]                        
            for k in range(m):
                M[j,k] += -pivo*M[i,k]
    return M


# In[18]:


# matriz randômica 5x5
M2 = np.random.rand(5,5)
print(eliminacao(M2))


# ## Condicionamento de matrizes
# 
# O condicionamento de uma matriz está relacionado à sensibilidade da solução de um sistema linear $\mathbf{A}\mathbf{x} = \mathbf{b}$ a pequenas perturbações nos dados, sejam elas no vetor $\mathbf{b}$ ou nos coeficientes da própria matriz $\mathbf{A}$. Uma matriz é considerada *bem condicionada* quando pequenas variações em $\mathbf{b}$ produzem pequenas variações na solução $\mathbf{x}$; caso contrário, diz-se que a matriz é *mal condicionada*, o que compromete a estabilidade numérica e a confiabilidade da solução computacional. 
# 
# O número de condição da matriz, denotado por $\kappa(\mathbf{A})$, é uma medida quantitativa desse comportamento, sendo definido, por exemplo, como
# 
# $$\kappa(\mathbf{A}) = \|\mathbf{A}\| \cdot \|\mathbf{A}^{-1}\|$$
# 
# para uma dada norma. Quanto maior esse número, pior o condicionamento. Em problemas de engenharia e ciências aplicadas, identificar o condicionamento da matriz é fundamental para avaliar a precisão da solução e escolher algoritmos adequados, como métodos com pivotamento ou regularizações.

# Vejamos como pequenas "perturbações" em matrizes podem provocar mudanças drásticas nas soluções de sistemas. Isto ocorre quando temos um problema *mal condicionado*.

# In[19]:


A1 = np.array([[1,2],[1.1,2]])
b1 = np.array([10,10.4])
print('matriz')
print(A1)
print('vetor')
print(b1)


# In[20]:


# solução do sistema A1x1 = b1
x1 = linalg.solve(A1,b1)
print(x1)


# In[21]:


d = 0.045
A2 = np.array([[1,2],[1.1-d,2]])
b2 = np.array([10,10.4])
print('matriz')
print(A2)
print('vetor')
print(b2)


# In[22]:


# solução do sistema perturbado A2x1 = b2
x2 = linalg.solve(A2,b2)
print(x2)


# A solução muda drasticamente aqui! Isto se deve à quase dependência linear em que a matriz se encontra. Ou seja, $\det({\bf A}_2) \approx 0$.

# In[23]:


print(linalg.det(A1),linalg.det(A2))


# In[24]:


linalg.norm(A)*linalg.norm(linalg.inv(A))


# ## Método de Gauss-Jordan
# 
# O método de Gauss-Jordan é uma variação da EG, em que não apenas as entradas da porção inferior da matriz plena do sistema são anuladas, mas também as entradas da porção superior, resultando em uma matriz diagonal. 
# 
# Além disso, todas as linhas são normalizadas através da sua divisão pelo respectivo elemento pivô. Por exemplo, $a_{11}$ é o elemento pivô da primeira equação, $a_{22}$ da segunda, e assim por diante). A partir daí, a obtenção dos valores das variáveis é imediata. 
# 
# O método é melhor ilustrado no seguinte exemplo.

# In[25]:


# Matriz aumentada
AB = np.array([[3. , -0.1, -0.2, 7.85], [0.1, 7., -0.3, -19.3], [0.3, -0.2, 10., 71.4]])
print(AB)


# In[26]:


# Normalização da 1a. linha
AB[0,:] /= AB[0,0] # L1 <- L1/a11
print(AB)


# In[27]:


# Eliminação de x1 da 2a. e 3a. linhas
m1 = AB[1,0]
AB[1,:] -= m1*AB[0,:] # L2 <- L2 - m1*L1
m2 = AB[2,0]
AB[2,:] -= m2*AB[0,:] # L3 <- L3 - m2*L1
print(AB)


# In[28]:


# Normalização da 2a. linha
AB[1,:] /= AB[1,1] # L2 <- L2/a22
print(AB)


# In[29]:


# Eliminação de x2 da 1a. e 3a. linhas
m3 = AB[0,1]
AB[0,:] -= m3*AB[1,:] # L1 <- L1 - m3*L2  
m4 = AB[2,1]
AB[2,:] -= m4*AB[1,:] # L3 <- L3 - m4*L2 
print(AB)


# In[30]:


# Normalização da 3a. linha
AB[2,:] /= AB[2,2] # L3 <- L3/a33
print(AB)


# In[31]:


# Eliminação de x3 da 1a. e 2a. linhas
m5 = AB[0,2]
AB[0,:] -= m5*AB[2,:] # L1 <- L1 - m5*L3
m6 = AB[1,2]
AB[1,:] -= m6*AB[2,:] # L2 <- L2 - m5*L3
print(AB)


# Do último resultado, vemos que a matriz identidade é obtida, apontando para o vetor solução $[3 \ \ -2.5 \ \ 7]^T$.
