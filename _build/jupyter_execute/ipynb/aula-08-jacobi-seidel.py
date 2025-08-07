#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
plt.style.use('../styles/gcpeixoto-book.mplstyle')


# # Sistemas Lineares na Prática Computacional: Métodos Iterativos
# 
# <div class="chapter-thumb">
#     <div class="chapter-oa">
#         <h2>Objetivos de aprendizagem</h2>
#         <ul>
#         <li>Compreender os fundamentos dos métodos iterativos para a resolução de sistemas lineares; </li>
# 	    <li>Aplicar os métodos de Jacobi e Gauss-Seidel para resolver sistemas lineares;</li>	    
#         <li>Analisar critérios de convergência e recursos para condicionamento de sistemas;</li>
#         <li>Implementar algoritmos e resolver sistemas computacionalmente;</li>	    
#         </ul>
#     </div>        
#     <div class="quote-box">
#         <p><em>""
#         </p></em>
#     </div>        
# </div>

# # Processo iterativo multidimensional
# 
# Diferentemente da abordagem dos métodos diretos, a resolução de sistemas lineares por métodos iterativos dá-se por meio de aproximações sucessivas, nos mesmos moldes daquilo que estudamos para uma dimensão. A diferença, no caso do $\mathbb{R}^n$, é que os elementos da sequência são vetores que devem convergir para o vetor que soluciona o sistema dentro de uma margem de erro desejada. 
# 
# De forma similar ao caso unidimensional, um processo iterativo a várias variáveis pode ser descrito por:
# 
# $$\mathbf{x}^{({k})} = \mathbf{\phi}(\mathbf{x}^{(k-1)}), \ \ k = 1, \ldots, n < \infty$$
# $$\mathbf{x}^{(0)} = \mathbf{x}_0,$$
# 
# Acima, $\mathbf{\phi}$ é uma função de iteração vetorial e $\mathbf{x}_0$ o vetor de estimativa inicial. Nesta notação, $\mathbf{x}^{(k)}$ é a $k$-ésima _iterada_ de uma sequência numérica discreta de vetores.
# 
# No espaço de $n$ dimensões, como o objetivo é encontrar o vetor-solução $\mathbf{x}$ que soluciona a equação matricial
# 
# $$\mathbf{A}\mathbf{x} = \mathbf{b},$$
# 
# para $\mathbf{A}_{n \times n}$ (condições internas) e $\mathbf{b}_{n \times 1}$ (condições externas) previamente conhecidos, a estratégia a ser seguida é decompor a matriz $\mathbf{A}$ de forma a facilitar a solução. De uma maneira geral, este procedimento, chamado de _splitting_, pode ser realizado da seguinte forma: 
# 
# - devemos escolher duas matrizes $\mathbf{M}$ e $\mathbf{N}$, tais que $\mathbf{A} = \mathbf{M} - \mathbf{N}$;
# - $\mathbf{M}$ deve ser uma matriz facilmente inversível(p.ex. diagonal ou triangular).
# - $\mathbf{N}$, por sua vez, seja a parcela restante.
# 
# Por substituição direta da decomposição da matriz principal na equação, vemos que
# 
# $$\mathbf{A}\mathbf{x} = \mathbf{b} \Rightarrow
# (\mathbf{M} - \mathbf{N}) \mathbf{x} = \mathbf{b} \Rightarrow
# \mathbf{M} \mathbf{x} = \mathbf{N} \mathbf{x} + \mathbf{b} \Rightarrow 
# \mathbf{x} = \mathbf{M}^{-1}\mathbf{N} \mathbf{x} + \mathbf{M}^{-1}\mathbf{b}.$$ 
# 
# Uma vez que $\mathbf{M}^{-1}$ é supostamente fácil de ser calculada, a última equação descreve o processo iterativo
# 
# $$\mathbf{x}^{({k})} = \mathbf{M}^{-1}\mathbf{N} \mathbf{x}^{(k-1)} + \mathbf{M}^{-1}\mathbf{b} = 
# \mathbf{B} \mathbf{x}^{(k-1)} + \mathbf{c},$$
# 
# com $\mathbf{B} = \mathbf{M}^{-1}\mathbf{N}$ e $\mathbf{c} = \mathbf{M}^{-1}\mathbf{b}$. Em outras palavras, 
# 
# $$\mathbf{x}^{({k})} = \mathbf{\phi}(\mathbf{x}^{(k-1)}) = \mathbf{C} \mathbf{x}^{(k-1)} + \mathbf{g},$$
# 
# e a função de iteração estabelecida é, em síntese, uma sucessão de operações algébricas que resulta em um produto matriz-vetor seguido de uma adição. Geometricamente, este processo equivale a subsequentes modificações do vetor inicial no espaço de $n$ dimensões, acompanhadas de um deslocamento.  
# 
# Os diferentes métodos de solução para a equação original passam a existir, portanto, quando $\mathbf{C}$ e $\mathbf{g}$ assumem formas distintas em decorrência da escolha do $\mathbf{M}$ e $\mathbf{N}$. Neste capítulo, estudaremos dois procedimentos de _splitting_: o método de Jacobi-Richardson e o método de Gauss-Seidel, que é uma derivação do primeiro. Entretanto, o método de Gauss-Seidel é computacionalmente mais eficiente e deve ser priorizado para utilidade. A tabela abaixo resume essas escolhas.
# 
# | Método            | Escolha de $\mathbf{M}$                          | Escolha de $\mathbf{N}$                          | Resumo do Método                                                                 |
# |-------------------|---------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------|
# | Jacobi-Richardson        | $\mathbf{M} = \mathbf{D}$ (matriz diagonal de $\mathbf{A}$)    | $\mathbf{N} = \mathbf{L} + \mathbf{U}$ (triangular inferior + superior estrita) | Atualiza todas as variáveis simultaneamente usando apenas a diagonal de $\mathbf{A}$.     |
# | Gauss-Seidel  | $\mathbf{M} = \mathbf{D} - \mathbf{L}$ (diagonal + triangular inferior estrita) | $\mathbf{N} = \mathbf{U}$ (triangular superior estrita) | Atualiza as variáveis sequencialmente, usando valores mais recentes na mesma iteração. |
# 
#   

# # Método de Jacobi-Richardson
# 
# Suponha um sistema linear nas incógnitas $x_1, x_2, \dots, x_n$ da seguinte forma:
# 
# $$a_{11} x_{1} + a_{12} x_{2} + \dots + a_{1n} x_{n} = b_1 \\
# a_{21} x_{1} + a_{22} x_{2} + \dots + a_{2n} x_{n} = b_2 \\
# \vdots \\
# a_{n1} x_{1} + a_{n2} x_{2} + \dots + a_{nn} x_{n} = b_n$$
# 
# Suponha também que todos os termos $a_{ii}$ (diagonal) sejam diferentes de zero. Se não for o caso, isso pode, geralmente, ser resolvido permutando equações. 
# 
# Inicialmente, o método sugere que as variáveis sejam isoladas em cada equação (passagem de $\mathbf{M} = \mathbf{D}$ à esquerda seguida da aplicação da inversa). Assim, escrevemos
# 
# $$
# x_1 = \dfrac{1}{a_{11}} [b_1 - a_{12} x_{2} - a_{13} x_{3} - \dots - a_{1n} x_{n}] \\
# x_2 = \dfrac{1}{a_{22}} [b_2 - a_{21} x_{1} - a_{23} x_{3} - \dots - a_{2n} x_{n}] \\
# \vdots \\
# x_n = \dfrac{1}{a_{nn}} [b_n - a_{n1} x_{1} - a_{n2} x_{2} - \dots - a_{n \ n-1} x_{n-1}]
# $$
# 
# A partir dessas equações "isoladas" e do vetor de estimativa inicial $\mathbf{x}^{(0)} = [x^{(0)}_1 \ \ x^{(0)}_2 \ \ \dots \ \  x^{(0)}_n]^T$, criamos o processo iterativo inserindo o contador $k$:
# 
# $$
# x^{(k+1)}_1 = \dfrac{1}{a_{11}} [b_1 - a_{12} x^{(k)}_{2} - a_{13} x^{(k)}_{3} - \dots - a_{1n} x^{(k)}_{n}] \\
# x^{(k+1)}_2 = \dfrac{1}{a_{22}} [b_2 - a_{21} x^{(k)}_{1} - a_{23} x^{(k)}_{3} - \dots - a_{2n} x^{(k)}_{n}] \\
# \vdots \\
# x^{(k+1)}_n = \dfrac{1}{a_{nn}} [b_n - a_{n1} x^{(k)}_{1} - a_{n2} x^{(k)}_{2} - \dots - a_{n \ n-1} x^{(k)}_{n-1}]
# $$
# 
# Logo, para todo $i = 1, 2, \dots , n$, esperamos que a sequência de vetores $\{ \mathbf{x}^{(k)} \}_{k=1}^N$ convirja para o vetor solução ${\bf x}^{*}$ do sistema original. 
# 
# De outra forma, basta notar que o processo iterativo descrito acima por componente pode ser representado pela equação matricial:
# 
# $$\mathbf{x}^{(k+1)} = \mathbf{D}^{-1} (\mathbf{L} + \mathbf{U}) \mathbf{x}^{(k)} + \mathbf{D}^{-1} b,$$
# 
# pois 
# 
# $$
# D = \begin{bmatrix}
# a_{11} & 0 & \cdots & 0 \\
# 0 & a_{22} & \cdots & 0 \\
# \vdots & \vdots & \ddots & \vdots \\
# 0 & 0 & \cdots & a_{nn}
# \end{bmatrix}, \quad
# L = \begin{bmatrix}
# 0 & 0 & \cdots & 0 \\
# -a_{21} & 0 & \cdots & 0 \\
# \vdots & \vdots & \ddots & \vdots \\
# -a_{n1} & -a_{n2} & \cdots & 0
# \end{bmatrix}, \quad
# U = \begin{bmatrix}
# 0 & -a_{12} & \cdots & -a_{1n} \\
# 0 & 0 & \cdots & -a_{2n} \\
# \vdots & \vdots & \ddots & \vdots \\
# 0 & 0 & \cdots & 0
# \end{bmatrix}.
# $$
# 
# Ou, explícita e compactamente,
# 
# 
# $$
# \mathbf{x}^{(k)} = \begin{bmatrix}
# 0 & -\frac{a_{12}}{a_{11}} & \cdots & -\frac{a_{1n}}{a_{11}} \\
# -\frac{a_{21}}{a_{22}} & 0 & \cdots & -\frac{a_{2n}}{a_{22}} \\
# \vdots & \vdots & \ddots & \vdots \\
# -\frac{a_{n1}}{a_{nn}} & -\frac{a_{n2}}{a_{nn}} & \cdots & 0
# \end{bmatrix} \mathbf{x}^{(k-1)} + \begin{bmatrix}
# \frac{b_1}{a_{11}} \\
# \frac{b_2}{a_{22}} \\
# \vdots \\
# \frac{b_n}{a_{nn}}
# \end{bmatrix}.
# $$
# 
# No Método de Jacobi-Richardson (MJR), a matriz de iteração
# 
# $$\mathbf{C} =
# \begin{bmatrix}
# 0 & -\frac{a_{12}}{a_{11}} & \cdots & -\frac{a_{1n}}{a_{11}} \\
# -\frac{a_{21}}{a_{22}} & 0 & \cdots & -\frac{a_{2n}}{a_{22}} \\
# \vdots & \vdots & \ddots & \vdots \\
# -\frac{a_{n1}}{a_{nn}} & -\frac{a_{n2}}{a_{nn}} & \cdots & 0
# \end{bmatrix}$$
# 
# torna-se o "motor" responsável pela progressão do método. Ela transforma os vetores da sequência buscando uma trajetória "espiral" que deve estacionar em um ponto fixo do espaço $\mathbb{R}^n$, identificando-se com o vetor-solução. Como veremos adiante, existem condições a serem atendidas para que $\mathbf{B}$ produza uma sequência convergente. Mas, de maneira geral, se $\mathbf{A}$ for uma matriz _diagonalmente dominante_, as componentes de $\mathbf{B}$ terão valores menores do que 1 e o efeito geométrico de $\mathbf{B}$ sobre qualquer vetor será de uma _contração_.
# 
# 
# ## Matrizes diagonalmente dominantes
# 
# Matrizes _diagonalmente dominantes_ são aquelas em que o valor absoluto do termo diagonal de sua $i$-ésima linha é maior ou igual à soma dos valores absolutos de todos os outros termos na mesma linha. Esta condição é refletida no _critério das linhas_, que deve atender à sequinte desigualdade:
# 
# $$\sum_{\substack{j = 1 \\ j \neq i}} ^n |a_{ij}| < |a_{ii}|,$$
# 
# para cada linha $i = 1, 2, \dots, n$. Se satisfeitas as inequações acima, a matriz ${\bf A}$ é (estritamente) diagonalmente dominante (sinal $<$). É importante observar que o critério das linhas pode deixar de ser satisfeito se houver permutações na matriz. Todavia, uma permutação cuidadosa pode fazer com que o sistema passe a satisfazer o critério. Por teorema, admite-se que se a matriz do sistema linear satisfaz o critério das linhas, então o algoritmo de Jacobi-Richardson converge para uma solução aproximada.
# 
# Por exemplo, a matriz 
# 
# $$
# \mathbf{A} = \begin{bmatrix}
# 4 & 2 & 2 \\
# 1 & 3 & 1 \\
# -2 & -2 & 4
# \end{bmatrix}
# $$
# 
# é diagonalmente dominante (não estrita), pois
# 
# - na linha 1: $|2| + |2| = 4 = |4| = 4$,
# - na linha 2: $|1| + |1| = 2 < |3| = 3$ e
# - na linha 3: $|-2| + |-2| = 4 = |4| = 4$.
# 
# Por outro lado, a matriz 
# 
# $$
# \mathbf{B} = \begin{bmatrix}
# 5 & 1 & 1 \\
# 1 & 4 & 1 \\
# 0 & 1 & 6
# \end{bmatrix}
# $$
# 
# é estritamente diagonalmente dominante, porque
# 
# - na linha 1: $|1| + |1| = 2 < |5| = 5$,
# - na linha 2: $|1| + |1| = 2 < |4| = 4$ e
# - na linha 3: $|0| + |1| = 2 < |6| = 6$.
# 

# ## Implementação computacional
# 
# A função abaixo é uma implementação simples do método de Jacobi.

# In[42]:


def jacobi(A, b, x0, nit):    
    """ Método de Jacobi para solução do sistema Ax=b.

    x = jacobi(A, b, x0, nit)

    Entradas:
        - A: matriz n x n (tipo: lista de listas)
        - b: vetor n x 1 (tipo: lista)
        - x0: vetor n x 1, ponto de partida (tipo: lista)
        - nit: número de iterações
    
    Saídas:
        - x:  matriz n x nit, contendo a sequência de vetores
        - c:  norma da matriz de iteração
    """ 
    
    import numpy as np    
    
    f = lambda obj: isinstance(obj,list)     
    if not all([f(A),f(b),f(x0)]):
        raise TypeError('A, b e x0 devem ser do tipo list.')
    else:
        A = np.asarray(A)
        b = np.asarray(b)
        x0 = np.asarray(x0)
            
    n = np.size(b)
    x = np.zeros((n, nit),dtype=float)
    x[:,0] = x0
        
    P = np.diag(np.diag(A))
    Q = P - A # elementos de fora da diagonal
    C = np.linalg.solve(P,Q) # matriz da função de iteração
    g = np.linalg.solve(P,b) # vetor da função de iteração
    c = np.linalg.norm(C) 
    
    #processo iterativo
    X = x0[:]    
    j = 1
    for j in range(1,nit):        
        X = C.dot(X) + g        
        x[:,j] = X
        
    print(f"Vetor solução:{x[:,-1]}")                
    print(f"||C|| = {c:.4f}")                
        
    return x, c


# Este código simples aplicado ao sistema $\mathbf{B}\mathbf{x} = \mathbf{b}$, onde $\mathbf{B}$ é a matriz de exemplo acima e $\mathbf{b} = [ 7 \ \  -8 \ \ 6]^T$, converge para a solução aproximada em 15 passos com a norma do resíduo da ordem de $10^{-6}$. 

# In[104]:


import numpy as np

B = [[5,1,1],[1,4,1],[0,1,6]]
b = [7,-8,6]
x0 = [1,1,1]
nit = 15

_, c = jacobi(B, b, x0, N)

# vetor-solução
x = _[:,-1]

# norma do resíduo
r = np.sqrt(np.dot(B @ x - b, B @ x - b))
print(f"||r|| = {r:e}")


# ## Método de Gauss-Seidel
# 
# O método de Gauss-Seidel (MGS) é uma leve variação do MJR. A diferença é que para calcular a componente $x_j^{(k+1)}$, usamos os valores $x_1^{(k+1)}, x_2^{(k+1)}, \ldots, x_{j-1}^{(k+1)}$, já calculados e os valores restantes $x_{j+1}^{(k)}, \ldots, x_{n}^{(k)}$ da mesma forma. 
# 
# O mesmo esquema iterativo de Jacobi, alterado apenas nas componentes coloridas, produz o processo iterativo de Gauss-Seidel,
# 
# $$
# \begin{cases}
# {\color{red}x_1^{(k+1)}} = \frac{1}{a_{11}} \left[b_1 - a_{12} x_2^{(k)} + a_{13} x_3^{(k)} + \cdots + a_{1n} x_n^{(k)}\right] \\ 
# {\color{blue}x_2^{(k+1)}} = \frac{1}{a_{22}} \left[b_2 - a_{21} {\color{red}x_1^{(k+1)}} + a_{23} x_3^{(k)} + \cdots + a_{2n} x_n^{(k)}\right] \\
# {x_3^{(k+1)}} = \frac{1}{a_{33}} \left[b_3 - a_{31} {\color{red}x_1^{(k+1)}} + a_{32} {\color{blue} x_2^{(k+1)}} + \cdots + a_{3n} x_n^{(k)}\right] \\
# \vdots\\
# {x_n^{(k+1)}} = \frac{1}{a_{nn}} \left[b_n - a_{n1} {\color{red}x_1^{(k+1)}} + a_{n2} {\color{blue} x_2^{(k+1)}} + \cdots + a_{n(n-1)} {\color{magenta} x_{n-1}^{{(k+1)}} }\right],
# \end{cases} $$
# 
# cuja equação matricial é dada por $$\mathbf{x}^{(k+1)} = - ( \mathbf{D} + \mathbf{L})^{-1} \mathbf{U} \mathbf{x}^{(k)} + ( \mathbf{D} + \mathbf{L})^{-1}  b,$$
# 

# ### Implementação computacional
# 
# A função abaixo implementa o método de Gauss-Seidel como variação da função elaborada para o método de Jacobi, porém acrescentando o critério de parada baseado no erro relativo.

# In[105]:



def gauss_seidel(A, b, x0, nit, tol):
    """ Método de Gauss-Seidel de solucao do sistema Ax=b

    Entradas:
        - A: matriz n x n (tipo: lista de listas)
        - b: vetor n x 1 (tipo: lista)
        - x0: vetor n x 1, ponto de partida (tipo: lista)
        - nit: número de iterações
        - tol: tolerancia de erro relativo
   
    Saídas:
        - x: matriz n x N, contendo a sequência de vetores
        - c: norma da matriz de iteração       
        - err: erro relativo percentual por iteracao (norma 2)
    """

    import numpy as np
    n = len(b)
    x = np.zeros((n, nit))
    x[:,0] = x0
    xx = x0 # iterada atual
    P = np.tril(A)
    N = P - A
    C = np.linalg.solve(P, N)
    c = np.linalg.norm(C)
    g = np.linalg.solve(P, b)
    
    
    for j in range(1, nit):
        xx = C @ xx + g
        x[:,j] = xx
         
    key = True    
        
    for i in range(1, nit):   
             
        e = np.linalg.norm(x[:,i] - x[:,i-1])/np.linalg.norm(x[:,i])
            
        if (e < tol) and (key == True):                        
            key = False

    print(f'Vetor-solução: {x[:,-1]}')
    print(f"||C|| = {c:.4f}")
    
    return x, c


# Aplicando-a ao mesmo sistema anterior, chegamos a uma solução com poucos passos.

# In[ ]:


_, c = gauss_seidel(B, b, x0, nit, 1e-3)

# vetor-solução
x = _[:,-1]

# norma do resíduo
r = np.sqrt(np.dot(B @ x - b, B @ x - b))
print(f"||r|| = {r:e}")


# In[85]:


#(Este código depende da biblioteca `plotly`, mas não *está otimizado*.)
#Desenvolver código para plotagem 3D da convergência para o método de Jacobi.

# # plotagem 3D da convergência 
# import plotly.graph_objs as go
# from plotly.offline import iplot, init_notebook_mode, plot
# init_notebook_mode(connected=False)

# xp = sol[0,:]
# yp = sol[1,:]
# zp = sol[2,:]

# points = go.Scatter3d(x = xp, y = yp, z = zp, mode = 'markers', marker = dict(size = 0.1,color = "rgb(227,26,28)"))

# vecs = []
# for i in range(len(xp)):
#     v = go.Scatter3d( x = [0,xp[i]], y = [0,yp[i]], z = [0,zp[i]], marker = dict(size = 0.1, color = "rgb(0,255,0)"),
#                        line = dict( color = "rgb(0,255,0)", width = 4) )
#     vecs.append(v)


# cx = np.sum(xp)/np.size(xp)
# cy = np.sum(yp)/np.size(yp)
# cz = np.sum(zp)/np.size(zp)

# vector = go.Scatter3d( x = [0,cx], y = [0,cy], z = [0,cz], marker = dict(size = 1, color = "rgb(100,100,100)"),
#                        line = dict( color = "rgb(100,100,100)", width = 4) )

# data = [points,vector] + vecs
# layout = go.Layout(margin = dict( l = 0,r = 0, b = 0, t = 0))
# fig = go.Figure(data=data,layout=layout)


# # vector

# fig.add_cone(x=[cx],y=[cy],z=[cz],u=[cx],v=[cy],w=[cz],sizeref=0.1,anchor='tip',colorscale='gray')

# for i in range(len(xp)):
#     fig.add_cone(x=[xp[i]],y=[yp[i]],z=[zp[i]],u=[xp[i]],v=[yp[i]],w=[zp[i]],sizeref=0.1,anchor='tip',colorscale='jet')
#     fig.update_layout(showlegend=False)


# plot(fig, show_link=True,filename='jacobi-3d-vectors.html')
# from IPython.display import display, HTML
# display(HTML('jacobi-3d-vectors.html'))


# ## Critérios de parada
# 
# 
# Consideremos ${\bf x}^{(k)} = [x_1^{(k)} \ x_2^{(k)} \ \ldots \ x_n^{(k)}]^T$ o $k$-ésimo vetor de uma sequência de vetores do $\mathbb{R}^n$ e ${\bf x} = [x_1 \ x_2 \ \ldots \ x_n]^T$ um vetor de referência. A distância entre eles, em uma norma especificada define o erro (ou resíduo), ou seja:
# 
# $$r^{(k)} = || {\bf x}^{(k)} - {\bf x} ||_{\square}$$
# 
# A depender da escolha de ${\square}$, chegamos a diferentes formas de medir o erro. As mais comuns são por meio de normas clássicas:
# 
# - _norma do máximo_ ( $\square = \infty$ ) $\Rightarrow r^{(k)} = \max\limits_{1 \le i \le n} | x_i^{(k)} - x_i |$
# - _norma Euclidiana ( $\square = 2$ ) $\Rightarrow r^{(k)} = \{\sum_{i=1}^n (x_i^{(k+1)} - x_i)^2\}^{1/2}$
# 
# Dado $\epsilon > 0$ (tolerância) e para uma norma escolhida, temos duas maneiras usuais de encerrar o processo iterativo:
# 
# - _critério de parada do erro absoluto:_ $r^{(k)} < \epsilon$
# - _critério de parada do erro relativo:_ $\frac{ r^{(k)} }{ r } < \epsilon$, onde $r = \max\limits_{1 \le i \le n} | x_i^{(k)} |$

# ## Arcabouço teórico relevante
# 
# Esta seção traz alguns elementos teóricos importantes que ajudam a compreender os métodos iterativos e as situações de convergência.

# **Teorema:** Se ${\bf A}$ é uma matriz estritamente diagonalmente dominante, então, para qualquer escolha de ${\bf x}^{(0)}$, tanto o MJR quanto o MGS geram sequencias que convergem para a solução única de ${\bf A}{\bf x} = {\bf b}$.
# 
# **Teorema [Critério geral de convergência]:** O processo iterativo definido por  
# $${\bf x}^{(k+1)} = {\bf C} {\bf x}^{(k)} + {\bf g}, \ \ k = 0,1,2,\ldots,$$
# é convergente se, para qualquer norma de matrizes, $|| {\bf C} || < 1$.
# 
# > Definição [Raio espectral]: O raio espectral $\rho({\bf A})$ de uma matriz ${\bf A}$ é definido como $\rho({\bf A}) = \max | \lambda |$, onde $\lambda$ é um autovalor de ${\bf A}$. Se $\lambda = a + bi$, $| \lambda | = (a^2 + b^2)^{1/2}$.
# 
# > Teorema [Stein-Rosenberg]: Considere ${\bf J}$ e ${\bf G}$ as matrizes estacionárias que definem o processo iterativo de Jacobi-Richardson e Gauss-Seidel respectivamente, isto é, ${\bf C} = {\bf J}$, ou ${\bf C} = {\bf G}$. 
# > Se $a_{ij} \le 0$, para cada $i \ne j$ e $a_{ii} > 0$, para $i=1,2,\ldots,n$, então uma, e apenas uma, das seguintes sentenças vale: 
# >
# > - i) $ 0 \le \rho({\bf G}) < \rho({\bf J}) < 1$
# > - ii) $ 1 < \rho({\bf J}) < \rho({\bf G})$
# > - iii) $ \rho({\bf G}) = \rho({\bf J}) = 0$
# > - iv) $ \rho({\bf G}) = \rho({\bf J}) = 1$
# >
# > Em especial, o caso i) indica que, quando um método converge, então ambos convergem, e o MGS converge mais rápido do que o MJR; o caso ii) indica que, quando um método diverge, ambos divergem, com a divergência do MGS sendo mais pronunciada.
# 
