#!/usr/bin/env python
# coding: utf-8

# # _Code Session_ 2: `bisect`

# O propósito desta _Code Session_ é resolver problemas aplicados de determinação de raízes de equações não lineares polinomiais e transcendentais utilizando a função `bisect` do módulo `scipy.optimize` em continuidade ao que foi discutido no {ref}`cap:bissecao`.

# In[22]:


# Importação de módulos (boilerplate)
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# ## A função `bisect`
# 
# A função `bisect` localiza a raiz de uma função dentro de um intervalo dado usando o método da bisseção, ressalvada a hipótese de que satisfaz o Teorema de Bolzano no intervalo. Os argumentos de entrada obrigatórios de `bisect` são: 
# 
# 1. a função-alvo `f` (contínua)
# 2. o limite esquerdo `a`
# 3. o limite direito `b`
# 
# Os parâmetros opcionais relevantes são: 
# 
# - `xtol`: tolerância (padrão: 2e-12)
# - `maxiter`: número máximo de iterações (padrão: 100)
# - `disp`: mostra erro se algoritmo não convergir (padrão: True)
# - `full_output`: mostra informações completas sobre a execução da função
# 
# O parâmetro de saída é:
# 
# - `x`: a estimativa para a raiz de `f`

# In[23]:


# Importação de bisect
from scipy.optimize import bisect


# ### Problema 1
# 
# Encontre a menor raiz positiva (real) de $f(x) = x^{3} - 3.23x^{2} - 5.54x + 9.84$.

# #### Resolução

# In[24]:


# Definição da função polinomial
def f(x): 
    return x**3 - 3.23*x**2 - 5.54*x + 9.84


# In[25]:


# Analise gráfica simples
x = np.linspace(-4,5)
plt.plot(x,f(x))
plt.axhline(y=0,color='r', linestyle=':');
plt.axvline(x=0,color='r', linestyle=':');


# Pelo gráfico, vemos que a menor raiz positiva está localizada no intervalo $(0,2]$. Vamos determiná-la utilizando este intervalo de confinamento. 

# In[26]:


# Resolução com bisect
x = bisect(f,2.5,4.5) # raiz
print(f'Raiz: x = {x:.6f}') # impressão de valor


# A mesma execução com `full_output=True` retornaria:

# In[27]:


x = bisect(f,1.2,1.4,xtol=1e-16,full_output=True, maxiter=50) # tupla 
x


# ### Problema 2
# 
# Determine a raiz de menor módulo de $\cosh(x) \cos(x) - 1 = 0$.

# #### Resolução
# 
# Sigamos o procedimento aprendido com `bisect`. 

# In[28]:


# Definição da função transcendental
def f(x): 
    return np.cosh(x)*np.cos(x) - 1 


# In[29]:


# Analise gráfica 
x = np.linspace(-5,-2)
plt.plot(x,f(x));
plt.axhline(y=0,color='r',linestyle=':');
plt.axvline(x=0,color='r',linestyle=':');


# In[30]:


# Resolução
x = bisect(f,-5,-2) # raiz de menor módulo 
print(f'Raiz: x = {x:.6f}') # impressão de valor


# ### Problema 3
# 
# Determine a raiz da equação $\tan(x) - \tanh(x) = 0$ que encontra-se em $(7.0,7.4)$. Determine esta raiz com três casas decimais de precisão pelo método da bisseção.

# #### Resolução

# In[31]:


# função
def f(x): 
    return np.tan(x) - np.tanh(x)


# Como o processo de análise gráfica é repetitivo, podemos criar outra função auxiliar dedicada à plotagem para refinamento.

# In[32]:


def aux_plot(a,b,fun):
    """Função auxiliar de plotagem
    
    Parâmetros: 
        a: limite inferior de plotagem (float)
        b: limite superior de plotagem (float)
        fun: função a ser plotada (function)

    Retorno: 
        None
    """
    x = np.linspace(a,b,100)
    plt.plot(x,f(x))
    plt.axhline(y=0,color='r',linestyle=':');
    


# In[33]:


# Analise gráfica 
aux_plot(6.5,7.5,f) # intervalo estendido


# Para obter as 3 casas decimas, vamos imprimir o valor final com 3 casas decimais. 

# In[34]:


# Resolução
x = bisect(f,7.0,7.4) # raiz de menor módulo 
print(f'Raiz: x = {x:.3f}') # impressão de valor


# ### Problema 4
# 
# Determine as raízes de $\text{sen}(x) + 3\cos(x) - 1 = 0$ no intervalo $(-2,2)$.

# #### Resolução

# In[35]:


# função
def f(x): 
    return np.sin(x) + np.cos(x) - 1


# In[36]:


# Analise gráfica 
aux_plot(-2,2,f)


# A análise gráfica mostra duas raízes. Vamos encontrar uma de cada vez.

# In[37]:


# Resolução

x1 = bisect(f,-2,1) # raiz 1  
x2 = bisect(f,1,2) # raiz 2 

print(f'Raízes: x1 = {x1:e}; x2 = {x2:e}')


# ### Problema 5
# 
# Determine todas as raízes reais de $f(x) = x^4 + 0.9x^3 - 2.3x^2 + 3.6x - 25.2$

# #### Resolução

# In[38]:


# função 
def f(x):
    return x**4 + 0.9*x**3 - 2.3*x**2 + 3.6*x - 25.2


# In[39]:


# Analise gráfica 
aux_plot(-100,100,f)


# In[40]:


# Refinamento
aux_plot(-20,20,f)


# In[41]:


# Refinamento
aux_plot(-5,5,f)


# In[42]:


# Resolução

x1 = bisect(f,-4,-2) # raiz 1  
x2 = bisect(f,1,3) # raiz 2 

print(f'Raízes: x1 = {x1:e}; x2 = {x2:e}')


# ### Problema 6
# 
# Um jogador de futebol americano está prestes a fazer um lançamento para outro jogador de seu time. O lançador tem uma altura de 1,82 m e o outro jogador está afastado de 18,2 m. A expressão que descreve o movimento da bola é a familiar equação da física que descreve o movimento de um projétil:
# 
# $$y = x\tan(\theta) - \dfrac{1}{2}\dfrac{x^2 g}{v_0^2}\dfrac{1}{\cos^2(\theta)} + h,$$
# 
# onde $x$ e $y$ são as distâncias horizontal e verical, respectivamente, $g=9,8 \, m/s^2$ é a aceleração da gravidade, $v_0$ é a velocidade inicial da bola quando deixa a mão do lançador e $\theta$ é o Ângulo que a bola faz com o eixo horizontal nesse mesmo instante. Para $v_0 = 15,2 \, m/s$, $x = 18,2 \, m$, $h = 1,82 \, m$ e $y = 2,1 \, m$, determine o ângulo $\theta$ no qual o jogador deve lançar a bola. 

# #### Resolução

# In[43]:


# parâmetros do problema
v0 = 15.2
x = 18.2
h = 1.82
y = 2.1
g = 9.8

# função f(theta) = 0
f = lambda theta: x*np.tan(theta) - 0.5*(x**2*g/v0**2)*(1/(np.cos(theta)**2)) + h - y


# In[44]:


# Análise gráfica
aux_plot(0,0.96*np.pi/2,f)


# In[45]:


# Refinamento
aux_plot(0,np.pi/4,f)


# In[46]:


# Resolução
xr = bisect(f,0.1,0.6)
print('Ângulo de lançamento: %.2f graus' % np.rad2deg(xr))


# In[47]:


xr


# ### Problema 7
# 
# A equação de Bernoulli para o escoamento de um fluido em um canal aberto com um pequeno ressalto é 
# 
# $$\dfrac{Q^2}{2gb^2h_0^2} + h_0 = \dfrac{Q^2}{2gb^2h^2} + h + H,$$
# 
# onde $Q = 1.2 \, m^3/s$ é a vazão volumétrica, $g = 9.81 \, m/s^2$ é a aceleração gravitacional, $b = 1.8 \, m$ a largura do canal, $h_0 = 0.6 \, m$ o nível da água à montante, $H = 0.075 \, m$ a altura do ressalto e $h$ o nível da água acima do ressalto. Determine $h$.

# #### Resolução
# 
# Para este problema, definiremos duas funções, uma auxiliar, que chamaremos `a`, e a função `f(h)` que reescreve a equação de Bernoulli acima em função de $h$. 

# In[48]:


# função para cálculo de parâmetros
def a(Q,g,b,H,h0):
    return Q,g,b,H,h0

# função do nível de água
def f(h):
    frate,grav,width,bHeight,ups = a(Q,g,b,H,h0)
    c = lambda arg: frate**2/(2*grav*width**2*arg**2)
    return c(h) - c(h0) + h - h0 + H 


# Note que a função `a` é apenas uma conveniência para o cálculo do termo comum envolvendo a vazão e para construírmos uma generalização para os dados de entrada. Em seguida, definiremos os parâmetros de entrada do problema. 

# In[49]:


# parâmetros de entrada
Q = 1.2 # m3/s 
g = 9.81 # m/s2
b = 1.8 # m
h0 = 0.6 # m
H = 0.075 # m


# A partir daí, podemos realizar a análise gráfica para verificar o comportamento de `f(h)`.

# In[50]:


# Análise gráfica
aux_plot(0.1,6,f)


# Ampliemos a localização.

# In[51]:


aux_plot(0.25,0.6,f)


# Verificamos que `f(h)` admite duas soluções. Vamos determinar cada uma delas. 

# In[52]:


# Resolução  
h1 = bisect(f,0.25,0.32)
print(f'Raiz: h1 = {h1:.8f}')

h2 = bisect(f,0.4,0.55)
print(f'Raiz: h2 = {h2:.8f}')


# **Nota:** as duas soluções viáveis dizem respeito ao regime de escoamento no canal aberto. Enquanto $h_1$ é um limite para escoamento supercrítico (rápido), $h_2$ é um limite para escoamento subcrítico (lento).

# ### Problema 8
# 
# A velocidade $v$ de um foguete Saturn V em voo vertical próximo à superfície da Terra pode ser aproximada por
# 
# $$v = u\textrm{ln}\left(\dfrac{M_0}{M_0 - \dot{m}t} \right) - gt,$$
# 
# onde $u = 2510 \, m/s$ é a velocidade de escape relativa ao foguete, $M_0 = 2.8 \times 10^6 \, kg$ é a massa do foguete no momento do lançamento, $\dot{m} = 13.3 \times 10^3 \, kg/s$ é a taxa de consumo de combustível, $g = 9.81 \, m/s^2$ a aceleração gravitacional e $t$ o tempo medido a partir do lançamento. 
# 
# Determine o instante de tempo $t^*$ quando o foguete atinge a velocidade do som ($335 \, m/s$).

# In[53]:


t = np.linspace(0,60*3)
u = 2510
M0 = 2.8e6
dmdt = 13.3e3
g = 9.81

v = u*np.log(M0/(M0 - dmdt*t)) - g*t
v1 = u*np.log(M0/(M0 - dmdt*t)) - g*t - 20000*t/(1.1 + g*t)
             
plt.plot(t,v,t,v1)


# #### Resolução
# 
# Seguiremos a mesma ideia utilizada no Problema 7. Primeiramente, construímos uma função auxiliar para calcular parâmetros e, em seguida, definimos uma função `f(t)`.  

# In[54]:


# função para cálculo de parâmetros
def a(u,M0,m,g,v):
    return u,M0,m,g,v

# função do tempo
def f(t):
    escape,mass,fuel,grav,vel = a(u,M0,m,g,v)    
    return escape*np.log(mass/(mass - fuel*t)) - g*t - vel


# Definimos os parâmetros do problema.

# In[55]:


# parâmetros de entrada
u = 2510.0 # m/s 
M0 = 2.8e6 # kg
m = 13.3e3 # kg/s
g = 9.81 # m/s2
v = 335.0 # m/s


# Utilizaremos a análise gráfica para determinar o intervalo de refinamento da raiz. 

# In[21]:


# Análise gráfica
aux_plot(0.5,100,f)


# Podemos verificar que a raiz está entre 60 e 80 segundos. Utilizaremos estes limitantes. 

# In[34]:


# solução  
tr = bisect(f,60,80)
print(f'Raiz: tr = {tr:.2f}s = {tr // 60:g}min {tr % 60:.2f}s')


# In[67]:


from scipy.optimize import newton
import sympy as sy

escape_s = sy.Symbol('es')
mass_s = sy.Symbol('ms')
fuel_s = sy.Symbol('fs')
t_s = sy.Symbol('ts')
g_s = sy.Symbol('gs')
vel_s = sy.Symbol('vels')

print(sy.diff(escape_s*sy.log(mass_s/(mass_s - fuel_s*t_s)) - g_s*t_s - vel_s, t_s))

def df(t):
    return escape*fuel/(-fuel*t + mass) - g

tr = newton(f,0)
tr


# O foguete rompe a barreira do som em pouco mais de 1 minuto!
