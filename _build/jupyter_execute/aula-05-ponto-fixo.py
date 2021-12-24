#!/usr/bin/env python
# coding: utf-8

# # Método da Iteração Linear (Ponto Fixo)

# Este notebook explora aspectos do método da _iteração linear_, ou também chamado de método do _ponto fixo_.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Exemplo
# 
# Estudamos a função $f(x) = x^2 + x - 6$.

# In[2]:


x = np.linspace(-4,4,50)
f = lambda x: x**2 + x - 6

xr = np.roots([1,1,-6])
print('Raízes: x1 = {:f}, x2 = {:f}'.format(xr[0], xr[1]))

# função de iteração
g1 = lambda x: 6 - x**2

plt.plot(x,f(x),label='$f(x)$');
plt.plot(x,x,'k--',label='$y=x$');
plt.plot(x,0*x,'c-.',label='$y=0$');
plt.plot(x,g1(x),'r--',label='$g_1(x)$');

plt.axvline(-3,-5,10,color='m');
plt.axvline(2,-5,10,color='m');
plt.legend(loc='best');


# ## Exemplo
# 
# Estudamos a função $f(x) = \exp(x) -x$

# In[3]:


x2 = np.linspace(-1,1,50)

f2 = lambda x: np.exp(-x) - x
g2 = lambda x:  np.exp(-x)

plt.plot(x2,f2(x2),x2,g2(x2),'r',x2,x2,'c')
plt.grid(True)


# ## Implementação do método do ponto fixo

# In[4]:


def ponto_fixo(x0,f,g,tol,N,vis):
    """ 
    Resolve problema de determinacao de raizes pelo 
    metodo do ponto fixo (iteracao linear).
    
    entrada: 
    
       x0  - aproximacao inicial        (float)
        f  - funcao a ser resolvida     (str)
        g  - funcao de iteracao         (str)
       tol - tolerancia                 (float)
        N  - numero maximo de iteracoes (int)
      vis  - flag para plotagem         (bool)
      
    saida:  
    
       x   - raiz aproximada para f     (float)      
    """
    from numpy import linspace
    from matplotlib.pyplot import plot,legend

    # funcoes
    f = eval('lambda x:' + f)
    g = eval('lambda x:' + g)
    
    # inicializacao
    it = 0 # contador 
    x, xn = x0, x0 + 1 # iteradas atual, anterior
    
    e = abs(x-xn)/abs(x) # erro    

    # tabela
    print('i\t x\t\t f(x)\t\t ER')
    print('{0:d}\t {1:f}\t {2:f}\t {3:e}'.format(it,x,f(x),e))       
    
    # laco
    while e >= tol and it <= N:
        it += 1    
        xn = x                             
        x = g(xn)               
        e = abs(x-xn)/abs(x)         
        print('{0:d}\t {1:f}\t {2:f}\t {3:e}'.format(it,x,f(x),e))      
        
        if it > N:
            print('Solução nao alcancada com N iteracoes.')
            break
       
    if vis == True:
        dx = 2*x
        dom = linspace(x - dx,x + dx,30)
        plot(dom,f(dom),label='$f(x)$')
        plot(dom,dom*0,label='$y=0$')
        plot(dom,g(dom),label='$g(x)$')
        plot(dom,dom,label='$y=x$')
        legend()
        
    return x


# ## Estudo de caso: $f(x) = x^2 + x - 6$
# 
# Função de iteração: $g(x) = \sqrt{6 - x}$

# In[5]:


f = 'x**2 + x - 6'
g = '(6 - x)**(1/2)'

x0 = 0.1
tol = 1e-5
N = 100

ponto_fixo(x0,f,g,tol,N,True)


# Função de iteração: $g(x) = -\sqrt{6 - x}$

# In[6]:


f = 'x**2 + x - 6'
g = '-(6 - x)**(1/2)'

x0 = 0.1
tol = 1e-5
N = 100

ponto_fixo(x0,f,g,tol,N,True)

