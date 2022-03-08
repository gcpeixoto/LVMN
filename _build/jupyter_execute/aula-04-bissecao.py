#!/usr/bin/env python
# coding: utf-8

# # Implementações do método da bisseção
# 
# Neste capítulo, apresentamos alternativas para a resolução de equações não-lineares através do Método da Bisseção. A primeira delas apresenta um algoritmo capaz de lidar com uma quantidade razoável de funções a uma variável, isto é.
# 
# Para ser executado, o método `bissecao` requer 5 parâmetros: 
# 
# - a função $f(x)$ propriamente dita;
# - o domínio de solução $[a,b]$;
# - o erro absoluto desejado $EA_d$, representado por `tol`;
# - o número máximo de iterações $N$ para tentativa de solução.

# In[1]:


"""MB - Metodo da Bisseção 1D

entrada: 
    f: string dependendo de uma variável, i.e., a função-alvo
        (e.g., 'x**2 - 1', 'x**2*cos(x)', etc.) 
    a: limite inferior do dominio
    b: limite superior do dominio
    tol: tolerancia    
    N: numero maximo de iteracoes do metodo

saida: 
    xm: raiz da funcao
    
nota:     
"""

import inspect, re
import numpy as np

def bissecao(f,a,b,tol,N):
        
    # adiciona as chamadas das funções do numpy
    f = re.sub('(sin|sinh|cos|cosh|tan|tanh|               exp|log|sqrt|log10|               arcsin|arccos|arctan|               arcsinh|arccosh|arctanh)', r'np.\1', f)
    
    # identifica a variavel
    var = re.search(r'([a-zA-Z][\w]*) ?([\+\-\/*]|$|\))', f).group(1)
    
    print('f('+ var +') = ' + f + '\n')

    # cria função anônima
    f = eval('lambda ' + var + ' :' + f)
    
    # Se função não for de uma variável, lança erro        
    if len(inspect.getfullargspec(f).args) - 1 > 0:    
        raise ValueError('O código é válido apenas para uma variável.')

    # calcula valor da função nos extremos
    fa = f(a) 
    fb = f(b)
    
    # verifica sinal da função para o intervalo passado     
    if fa*fb >= 0:
        raise ValueError('A função deve ter sinais opostos em a e b!')
    
    # flag usada para prevenir a obtenção da raiz 
    # antes de o intervalo ter sido 
    # suficientemente reduzido
    done = 0;

    # loop principal

    # bisecta o intervalo
    xm = (a+b)/2

    i = 1 # contador 

    while abs(a-b) > tol and ( not done or N != 0 ):
    # avalia a função no ponto médio
        fxm = f(xm)
        print("(i = {0:d}) f({4:s}m)={1:f} | f(a)={2:f} | f(b)={3:f}".format(i,fxm,fa,fb,var))
   
        if fa*fxm < 0:       # Raiz esta à esquerda de xm
            b = xm
            fb = fxm
            xm = (a+b)/2
        elif fxm*fb < 0:     # Raiz esta à direita de xm
            a = xm
            fa = fxm
            xm = (a+b)/2
        else:               # Achamos a raiz
            done = 1
    
        N -= 1              # Atualiza passo
        i += 1              # Atualiza contador
            
    print("Solução encontrada: {0}".format(xm))

    return xm


# **Exemplo:** Resolva o problema $f(x) = 0$, para $f(x) = -\text{arccos}(x) + 4\text{sen}(x) + 1.7$, no intervalo $-0.2 \le x \le 1.0$ e $\epsilon = 10^{-3}$.

# In[2]:


xm = bissecao('-arccos(x) + 4*sin(x) + 1.7',-0.2,1.0,1e-3,30)


# **Exemplo:** Resolva o problema $h(z) = 0$, para $h(z) = -z(1-2z)^{-1} - \text{tan}(z+1)$, no intervalo $[-10,10]$ e $\epsilon = 10^{-5}$.
# 
# _Nota:_ Neste exemplo, `N = 5` não afeta o processo iterativo de determinação da raiz, porque o algoritmo
# gera convergência para uma solução aproximada. Caso tivéssemos uma função mais "rígida", o valor de `N` impediria iterações _ad infinitum_.

# In[3]:


zm = bissecao('z/(1 - 2*z) - tan(z+1)',-10,10,1e-5,5)


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect, newton

# Dados de entrada

t = np.arange(0,520,1)   # tempo [s]
c = 1.46   # coeficiente de arrasto [kg/s]
m = 90     # massa [kg]
g = 9.81   # constante de gravidade [m/s2]

# Dados de saída

## velocidade terminal [m/s]
v_ms1 = (g*m/c)*(1 - np.exp((-c/m)*t))

# velocidade terminal [km/h]
v_kh1 = (1/3.6)*v_ms1;

# gráfico tempo x velocidade
plt.figure
plt.plot(t,v_ms1)
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.title('Velocidade terminal - paraquedista');


# In[6]:


import sympy as sp

time = 12     # tempo [s]
mass = 70     # massa [kg]
vel = 42     # velocidade [m/s]
grav = 9.81   # constante de gravidade [m/s2]

# defino variáveis simbólicas
g,m,t,v,c = sp.symbols('g,m,t,v,c')

# expressão geral
f_g = (g*m/c)*(1 - sp.exp((-c/m)*t)) - v

# expressão particular com valores substituídos 
# convertida para string
f_s = str(f_g.subs({'g':grav,'m':mass,'v':vel,'t':time}))

# TODO
# para esta função, teremos que substituir 'exp' por 'np.exp')
f_s = '-42 + 686.7*(1 - np.exp(-6*c/35))/c'

# resolve bisseção
xm = bissecao(f_s,12,16,1e-5,100)


# ## Tarefas
# 
# * Melhore o código Python tratando os TODOs: 
# 
# Tente generalizar o código da bisseção para que identifique automaticamente a variável de entrada utilizada pelo usuário (use expressões regulares e remova o argumento `var` da definição da função).
# 
# Note que o trecho simbólico abaixo foi necessário para substituir a função da chamada `exp`, não interpretada por `eval` por uma nova string que usasse `np.exp`.
# ```python
# # TODO
# # para esta função, teremos que substituir 'exp' por 'np.exp')
# print('f(c) = ' + f_s + '\n')
# f_s = '-42 + 686.7*(1 - np.exp(-6*c/35))/c'
# ```
# Tente fazer as correções necessárias no código. **Sugestão:** verifique a função `sympy.core.evalf` do módulo `sympy`)
# 
# * Adicione mecanismos de plotagem no código Python 
# 
# * Crie um código em Javascript para adicionarmos na página do projeto Numbiosis com o máximo possível de GUI (labels + input data).
# 
# * Teste a implementação com um problema realista.

# **Problema sugerido:**
# Uma reação química reversível
# 
# $$2A+B \iff C$$
# 
# pode ser caracterizada pela relação de equilíbrio
# 
# $$K = \dfrac{c_c}{c_a^2c_b},$$
# 
# onde a nomenclatura $c_i$ representa a concentração do constituinte $i$. Suponha que definamos uma variável $x$ como o número de moles de $C$ que são produzidos. A conservação da massa pode ser usada para reformular a relação de equilíbrio como
# 
# $$K = \dfrac{(c_{c,0} + x)}{(c_{a,0} - 2x)^2 (c_{b,0} - x),}$$
# 
# onde o subscrito $0$ designa a concentração inicial de cada constituinte. Se $K = 0,016$, $c_{a,0} = 42$, $c_{b,0} = 28$ e $c_{c,0} = 4$, determine o valor de $x$. 
# 
# (a) Obtenha a solução graficamente. 
# 
# (b) Com base em (a), resolva a raiz com suposições iniciais de $x_l = 0$ e $x_u = 20$, com critério de erro de $\epsilon_s = 0,5\%$. (Vide clipping _Definições de erro_ para entender $\epsilon_s$.)
# 
# (c) Use o método da bisseção.

# ## Tarefa: Falsa Posição
# Programe uma nova função para executar o método da falsa posição ou estenda o código anterior para uma nova função que contemple os dois casos (sugestão: use `switch... case...`).
# 
# 
