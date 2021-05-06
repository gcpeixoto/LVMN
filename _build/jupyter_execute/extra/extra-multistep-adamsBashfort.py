## Métodos de Adams-Bashfort

%matplotlib inline 
from numpy import *
from matplotlib.pyplot import *

# Metodo de Adams-Bashfort de 2a. ordem

def adams_bashfort_2nd_order(t0,tf,y0,h,fun):
    '''
    Resolve o PVI y' = f(t,y), t0 <= t <= b, y(t0)=y0
    usando a formula de Adams-Bashfort de ordem 2 
    com passo h. O metodo de Euler eh usado para 
    obter y1. A funcao f(t,y) deve ser definida 
    pelo usuario. 
  
    Saida: 
  
    A rotina AB2 retorna dois vetores, t e y,  
    contendo, nesta orde, os pontos nodais e 
    a solucao numerica. 
    '''

    # malha numerica  
    n = round((tf - t0)/h) + 1
    t = linspace(t0,t0+(n-1)*h,n)
    y = np.zeros(n)

    y[0] = y0 # condicao inicial 

    f1 = fun(t[0],y[0]) # f(t_i,y_i)
    y[1] = y[0] + h*f1 # Euler 

    for i in range(2,n):
        f2 = fun(t[i-1],y[i-1]) # f(t_i-1,y_i-1)
        y[i] = y[i-1] + h*(3*f2 - f1)/2 # esquema AB2
        f1 = f2 # atualiza 
        
    return t,y


def tab_erro_rel(t,y_n,y_e):

    # erro relativo
    e_r = abs(y_n - y_e)/abs(y_e)

    print('i \t t \t y_ex \t y_num \t e_r')
    for i in range(len(e_r)): 
        
        if i % 10 == 0:
            print('{0:d} \t {1:f} \t {2:f} \t {3:f} \t {4:e} \n'.format(i,t[i],y_e[i],y_n[i],e_r[i]))
            
def plot_fig(t,y_n,y_e,h):    
    plot(t,y_e,'r-')
    plot(t,y_n,'bo')
    title('Adams-Bashfort, 2a. ordem: $h=' + str(h) + '$')
    legend(['$y_{exata}$','$y_{num}$'])


**Exemplo:** Use o esquema de Adams-Bashfort de 2a. ordem para resolver o PVI. 

$$\begin{cases}
y'(t) = -y(t) + 2 \cos(t) \\
y(0) = 1 \\
0 \le t \le 18 \\ 
\end{cases}$$

_Solução exata_: $y(t) = {\rm sen}(t) + \cos(t)$

# define funcao
f = lambda t,y: -y + 2*cos(t)

# parametros
t0 = 0.0
tf = 18.0
y0 = 1.0
h = 0.5

# solucao numerica 
t,y_num = adams_bashfort_2nd_order(t0,tf,y0,h,f)
    
# solucao exata 
y_ex = sin(t) + cos(t)

plot_fig(t,y_num,y_ex,h)

tab_erro_rel(t,y_num,y_ex)

h = 0.1

# solucao numerica 
t,y_num = adams_bashfort_2nd_order(t0,tf,y0,h,f)
    
# solucao exata 
y_ex = sin(t) + cos(t)

plot(t,y_ex,'r-')
plot(t,y_num,'bo')
title('Adams-Bashfort, 2a. ordem: $h=0.5$')
legend(['$y_{exata}$','$y_{num}$'])

tab_erro_rel(t,y_num,y_ex)

plot_fig(t,y_num,y_ex,h)

h = 0.01

# solucao numerica 
t,y_num = adams_bashfort_2nd_order(t0,tf,y0,h,f)
    
# solucao exata 
y_ex = sin(t) + cos(t)

plot(t,y_ex,'r-')
plot(t,y_num,'bo')
title('Adams-Bashfort, 2a. ordem: $h=0.1$')
legend(['$y_{exata}$','$y_{num}$'])

#tab_erro_rel(t,y_num,y_ex)

plot_fig(t,y_num,y_ex,h)