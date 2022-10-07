#!/usr/bin/env python
# coding: utf-8

# # Método de Jacobi-Richardson
# 
# O método de Jacobi-Richardson (MJR) é um método iterativo que busca uma solução aproximada para sistemas lineares. Um método iterativo como tal é também conhecido como _aproximações sucessivas_, em que uma sequência convergente de vetores é desejada. O MJR é de especial interesse em sistemas cujas matrizes são _diagonalmente dominantes_.

# ## Instalações necessárias 
# 
# 
# Este notebook usa o módulo `plotly` para plotagem. Para instalá-lo via `conda` e habilitá-lo para uso como extensão do Jupyter Lab, execute os comandos abaixo em uma célula:

# ```
# import sys
# !conda install --yes --prefix {sys.prefix} nodejs plotly
# !jupyter labextension install jupyterlab-plotly@4.12.0
# ```

# ## Descrição do método
# 
# Suponha um sistema linear nas incógnitas $x_1, x_2, \dots, x_n$ da seguinte forma:
# 
# $$a_{11} x_{1} + a_{12} x_{2} + \dots + a_{1n} x_{n} = b_1 \\
# a_{21} x_{1} + a_{22} x_{2} + \dots + a_{2n} x_{n} = b_2 \\
# . \\
# . \\
# . \\
# a_{n1} x_{1} + a_{n2} x_{2} + \dots + a_{nn} x_{n} = b_n$$
# 
# Suponha também que todos os termos $a_{ii}$ sejam diferentes de zero $(i = 1, . . . , n)$. Se não for o caso, isso pode, geralmente, ser resolvido permutando equações. 
# 
# Inicialmente, o método sugere que as variáveis sejam isoladas em cada equação. Assim, escrevemos
# 
# $$
# x_1 = \dfrac{1}{a_{11}} [b_1 - a_{12} x_{2} - a_{13} x_{3} - \dots - a_{1n} x_{n}] \\
# x_2 = \dfrac{1}{a_{22}} [b_2 - a_{21} x_{1} - a_{23} x_{3} - \dots - a_{2n} x_{n}] \\
# . \\
# . \\
# . \\
# x_n = \dfrac{1}{a_{nn}} [b_n - a_{n1} x_{1} - a_{n2} x_{2} - \dots - a_{n \ n-1} x_{n-1}]
# $$
# 
# A partir dessas equações "isoladas" e de um vetor de estimativa inicial ("chute inicial") $[x^{(0)}_1 \ \ x^{(0)}_2 \ \ \dots \ \  x^{(0)}_n]^T$, criamos o processo iterativo inserindo, à direita, um contador. 
# 
# No primeiro passo, obtemos $[x^{(1)}_1 \ \ x^{(1)}_2 \ \ \dots \ \ x^{(1)}_n]^T$. Em seguida, estimamos $[x^{(2)}_1 \ \ x^{(2)}_2 \ \  \dots \ \  x^{(2)}_n]^T$. Repetindo o processo, a iterada $k$ é construída como segue:
# 
# $$
# x^{(k+1)}_1 = \dfrac{1}{a_{11}} [b_1 - a_{12} x^{(k)}_{2} - a_{13} x^{(k)}_{3} - \dots - a_{1n} x^{(k)}_{n}] \\
# x^{(k+1)}_2 = \dfrac{1}{a_{22}} [b_2 - a_{21} x^{(k)}_{1} - a_{23} x^{(k)}_{3} - \dots - a_{2n} x^{(k)}_{n}] \\
# . \\
# . \\
# . \\
# x^{(k+1)}_n = \dfrac{1}{a_{nn}} [b_n - a_{n1} x^{(k)}_{1} - a_{n2} x^{(k)}_{2} - \dots - a_{n \ n-1} x^{(k)}_{n-1}]
# $$
# 
# Logo, para todo $i = 1, 2, \dots , n$, esperamos que a sequência $\{ x^{(k+1)}_i \}_k$ convirja para o vetor solução ${\bf x}$ do sistema original, caracterizado por ${\bf A}{\bf x} = {\bf b}$.
# 
# Entretanto, a convergência é garantida apenas se houver dominância dos valores da diagonal principal sobre seus pares nas mesmas linhas. Podemos verificar a convergência do processo iterativo acima por meio do _critério das linhas_, embora exista uma maneira mais versátil de fazer esta verificação usando normas de matrizes. Por enquanto, entendamos o critério das linhas.

# ## Critério das linhas
# 
# O critério das linhas estabelece que 
# 
# $$\sum_{\substack{j = 1 \\ j \neq i}} ^n |a_{ij}| < |a_{ii}|, \forall i = 1, 2, \dots , n.$$
# 
# Em palavras: *“o valor absoluto do termo diagonal na linha $i$ é maior do que a soma dos valores absolutos de todos os outros termos na mesma linha”*. Se satisfeita, esta equação implica que a matriz ${\bf A}$ é (estritamente) diagonalmente dominante.
# 
# É importante observar que o critério das linhas pode deixar de ser satisfeito se houver troca na ordem das equações, e vice-versa. Todavia, uma troca cuidadosa pode fazer com que o sistema passe a satisfazer o critério. Por teorema, admite-se que se a matriz do sistema linear satisfaz o critério das linhas, então o algoritmo de Jacobi-Richardson converge para uma solução aproximada.

# ## Vantagens e desvantagens do método
# 
# O método tem a vantagem de ser de fácil implementação no computador do que o método de escalonamento e está menos propenso à propagação de erros de arredondamento. Por outro lado, sua desvantagem é não funcionar para todos os casos.

# ## Implementação do método de Jacobi

# In[4]:


"""
JACOBI: metodo de Jacobi para solução do sistema Ax=b.

x = jacobi(A,b,x0,N)

entrada:
   A: matriz n x n (tipo: lista de listas)
   b:  vetor n x 1 (tipo: lista)
  x0:  vetor n x 1, ponto de partida (tipo: lista)
   N:  numero de iterações do método
saidas:
x:  matriz n x N,
    contendo a sequencia de aproximações da solução
sp:  norma de B. O metodo converge se sp < 1.
""" 
import numpy as np
from matplotlib.pyplot import plot

"""
JACOBI: metodo de Jacobi para solução do sistema Ax=b.

x = jacobi(A,b,x0,N)

entrada:
   A: matriz n x n (tipo: lista de listas)
   b:  vetor n x 1 (tipo: lista)
  x0:  vetor n x 1, ponto de partida (tipo: lista)
   N:  numero de iterações do método
saidas:
x:  matriz n x N,
    contendo a sequencia de aproximações da solução
v:  norma de G. O metodo converge se v < 1.
""" 
def jacobi(A,b,x0,N):    
    
    f = lambda obj: isinstance(obj,list)     
    if not all([f(A),f(b),f(x0)]):
        raise TypeError('A, b e x0 devem ser do tipo list.')
    else:
        A = np.asarray(A)
        b = np.asarray(b)
        x0 = np.asarray(x0)
            
    n = np.size(b)
    x = np.zeros((n,N),dtype=float)
    x[:,0] = x0
        
    P = np.diag(np.diag(A))
    Q = P-A # elementos de fora da diagonal
    G = np.linalg.solve(P,Q) # matriz da função de iteração
    c = np.linalg.solve(P,b) # vetor da função de iteração
    v = np.linalg.norm(G)
    
    #processo iterativo
    X = x0[:]    
    j = 1
    for j in range(1,N):        
        X = G.dot(X) + c        
        x[:,j] = X                
        
    return x,v


# In[5]:


# Exemplo 15.2
A = [[10,2,1],[1,5,1],[2,3,10]]
b = [7,-8,6]
x = [1,1,1]
N = 10

sol,v = jacobi(A,b,x,N)
print(sol[:,-1])
print(v)


# ### Tarefa para turmas de computação: 
# 
# (Este código depende da biblioteca `plotly`, mas não *está otimizado*.)
# 
# Desenvolver código para plotagem 3D da convergência para o método de Jacobi.

# In[23]:


# plotagem 3D da convergência 
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode, plot
init_notebook_mode(connected=False)

xp = sol[0,:]
yp = sol[1,:]
zp = sol[2,:]

points = go.Scatter3d(x = xp, y = yp, z = zp, mode = 'markers', marker = dict(size = 0.1,color = "rgb(227,26,28)"))

vecs = []
for i in range(len(xp)):
    v = go.Scatter3d( x = [0,xp[i]], y = [0,yp[i]], z = [0,zp[i]], marker = dict(size = 0.1, color = "rgb(0,255,0)"),
                       line = dict( color = "rgb(0,255,0)", width = 4) )
    vecs.append(v)


cx = np.sum(xp)/np.size(xp)
cy = np.sum(yp)/np.size(yp)
cz = np.sum(zp)/np.size(zp)

vector = go.Scatter3d( x = [0,cx], y = [0,cy], z = [0,cz], marker = dict(size = 1, color = "rgb(100,100,100)"),
                       line = dict( color = "rgb(100,100,100)", width = 4) )

data = [points,vector] + vecs
layout = go.Layout(margin = dict( l = 0,r = 0, b = 0, t = 0))
fig = go.Figure(data=data,layout=layout)


# vector

fig.add_cone(x=[cx],y=[cy],z=[cz],u=[cx],v=[cy],w=[cz],sizeref=0.1,anchor='tip',colorscale='gray')

for i in range(len(xp)):
    fig.add_cone(x=[xp[i]],y=[yp[i]],z=[zp[i]],u=[xp[i]],v=[yp[i]],w=[zp[i]],sizeref=0.1,anchor='tip',colorscale='jet')
    fig.update_layout(showlegend=False)


plot(fig, show_link=True,filename='jacobi-3d-vectors.html')
from IPython.display import display, HTML
display(HTML('jacobi-3d-vectors.html'))


# In[ ]:




