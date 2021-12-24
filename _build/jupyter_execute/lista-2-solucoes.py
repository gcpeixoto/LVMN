#!/usr/bin/env python
# coding: utf-8

# # Lista de Exercícios 2 
# 
# Solucionário matemático e computacional de exercícios selecionados da Lista de Exercícios 2.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import metodosRaizes as rz
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt


# ## Q12 - L2
# 

# Primeiramente, recorramos à análise gráfica da função.

# In[3]:


from numpy import cos, exp

# funcao 
p = lambda x: 2*cos(x) - exp(x)

# plotagem
x = np.linspace(-1,1,30)
plt.plot(x,p(x),x,0*p(x));


# Vemos que a raiz está próxima de $x= 0.5$. Assim, qualquer valor próximo a este é razoável como aproximação inicial. 
# 
# Agora, antes de aplicar o método de Newton, vamos calcular a derivada da função simbolicamente. 

# In[4]:


# derivada simbolica 
xsym = sy.Symbol('x')
sy.diff(2*sy.cos(xsym) - sy.exp(xsym),xsym)


# Resolvamos com a nossa função programada.

# In[5]:


x0 = 0.2
tol = 1e-3
f = '2*cos(x) - exp(x)'
df = '-2*sin(x) - exp(x)'
xr = rz.newton(x0,f,df,tol,10,True)


# Verificação:

# In[6]:


2*cos(xr) - exp(xr)


# ## Q16 - L2

# In[7]:


p = lambda x: x**5 - 10/9*x**3 + 5/21*x
x = np.linspace(-1,1,50,endpoint=True)
plt.plot(x,p(x),x,0*p(x))

xr = np.roots([1,0,-10/9,0,5/21,0])
print(xr)

plt.scatter(xr,0*xr,c='r');
plt.grid(True);


# In[8]:


tol = 1e-3
nmax = 100


# ### item b.1)

# In[9]:


# Aproximacao de xi1 pelo MNR
x0 = -0.8
p = 'x**5 - 10/9*x**3 + 5/21*x'
dp = '5*x**4 -10/3*x**2 + 5/21'
plotar = True
rz.newton(x0,p,dp,tol,nmax,True)


# In[10]:


ff = lambda x: x**5 - 10/9*x**3 + 5/21*x
dff = lambda x: 5*x**4 - 30/9*x**2 + 5/21

xx = 0.857
ff(xx),dff(xx)


# ### item b.2)

# In[11]:


# Aproximacao de xi2 pelo MB

var = 'x'
a,b = -0.75, -0.25 
rz.bissecao(p,a,b,tol,100,var)


# ### item b.3)

# In[12]:


# Aproximacao de xi3 pelo MFP
a,b = -0.35, 0.25 
rz.falsa_posicao(p,a,b,tol,100,var)


# ### item b.4)

# In[13]:


# Aproximacao de xi4 pelo MPF

g = '( 0.9*(5/21 + x**5))**1./3.' 
#g = eval('lambda x:' + g)

#plt.plot(x,g(x))
rz.ponto_fixo(0.4,p,g,tol,nmax,True)


# ### item b.5)

# In[14]:


# Aproximacao de xi5 pelo MS

p = 'x**5 - 10/9*x**3 + 5/21*x'
x0,x1=0.8,1.
rz.secante(x0,x1,p,tol,nmax,True)


# ## Exemplos

# In[15]:


# exemplo bissecao
rz.bissecao('x**3-9*x+3',0,1,1e-3,100,var)


# In[16]:


rz.falsa_posicao('x**3-9*x+3',0,1,1e-3,100,var)


# ## Problemas aplicados

# A temperatura $T$ (em graus Kelvin) de um semicondutor pode ser calculada como uma função da resistência $R$ (em ohms) pela equação de Steinhart-Hart: 
# 
# $$T = \dfrac{1}{A + B\ln(R) + C\ln(R)^3},$$
# 
# para constantes $A$, $B$ e $C$ dependentes do material. Supondo que $A = 1.4056 \times 10^{-3}$, $B = 240.7620 \times 10^{-6} K^{-1}$ e $C = 7.48 \times 10^{-7}$, determine a resistência do semicondutor para uma temperatura de 135 graus Celsius.
# 
# **Sugestão:** use o método da bisseção e tolerância de $10^{-6}$.

# #### Solução computacional

# In[17]:


from scipy.optimize import bisect

# constantes
A = 1.4056e-3
B = 240.7620e-6
C = 7.48e-7
Tc = 135.0 # temperatura em Celsius
Tk = Tc + 273.15 # temperatura em Kelvin

# f(R) = 0
f = lambda R: 1/(A + B*np.log(R) + C*np.log(R)**3) - Tk

# localização 
R = np.linspace(1,100,50,True)
plt.plot(R,f(R))
plt.xlabel('$R$')
plt.ylabel('$T$')

# refinamento a=1; b=100
x = bisect(f,1,100,xtol=1e-6)
print("Para {0:.2f} graus Celsius, a resistência é de {1:.2f} ohms".format(Tc,x))


# <!-- Gilat/Subramanian 3.22-->
# ## Problema aplicado (revisar!)
# 
# Quando se calcula o pagamento de uma hipoteca, a relação entre o montante do empréstimo $E$, o pagamento mensal $P$, a duração do empréstimo em anos $a$, e a taxa de juros anual $t$ é dada pela equação: 
# 
# $$P = \dfrac{Et}{12\left( 1 - \dfrac{1}{\left(1 + \frac{t}{12}\right)^{12a}} \right)}.$$
# 
# Determine a taxa $t$ de um empréstimo de R<span>&#36;</span> 170.000 00 por 20 anos se o pagamento mensal for de R<span>&#36;</span> 1.250,00. 
# 
# **Sugestão:** usar método de Newton como função programada pelo estudante ou função residente.
# 
# #### Solução computacional:
# 
# Resolver o problema $f(t) = 0$ com método de Newton.

# In[18]:


from scipy.optimize import newton 
from sympy.utilities.lambdify import lambdastr

E = 170000 # montante do empréstimo
P = 1250 # pagamento mensal
a = 20 # duração do empréstimo em anos

# define função para computar 
# t: taxa de juros (incógnita)
def taxa_anuidade(E,P,a):

    Esym,t,asym,Psym = sy.symbols('Esym t asym Psym')

    fsym = Esym*t/( 12*(1 - 1/(1 + t/12)**(12*asym) ) ) - Psym 
    dfsym = sy.diff(fsym,t)

    f = fsym.subs({'Esym':E,'asym':a,'Psym':P})
    df = dfsym.subs({'Esym':E,'asym':a,'Psym':P})

    ft = eval(lambdastr(t,f))
    dft = eval(lambdastr(t,df))

    # Aplicação do método de Newton 

    # parâmetros 
    t0 = 1.0 # estimativa inicial
    tole=1e-3 # tolerância de erro
    nmax=50 # número máximo de iterações 

    # método de Newton 
    t = newton(ft,t0,dft,tol=tole,maxiter=nmax)    
    msg = "A taxa do empréstimo é de {0:.2f}% a.a.".format(t*100)
    
    return (t,msg)

# invoca função
taxa_anuidade(E,P,a)
# não sei se a equação do livro está correta: negativo até 12 
# aa = np.arange(1,50)
# tt = []
# for i in aa:
#     t=taxa_anuidade(E,P,i)
#     print(t[1])
#     tt.append(t[0])
# tt = np.asarray(tt)
# plt.plot(aa,tt)

