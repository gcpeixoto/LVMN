#!/usr/bin/env python
# coding: utf-8

# # Implementação do método da bisseção
# 
# Neste capítulo, utilizamos uma implementação própria do método da bisseção para resolver equações não-lineares unidimensionais. O algoritmo é capaz de lidar com uma quantidade razoável de funções matemáticas.
# 
# Para ser executado, o método `bissecao` requer 5 parâmetros: 
# 
# - a função $f(x)$ propriamente dita, representada por `f`;
# - o domínio de busca da raiz $[a,b]$, representado pelas estimativas iniciais `a` e `b`;
# - o erro absoluto desejado $EA_d$, representado por `e`;
# - o número máximo de iterações $N$ para tentativa de solução, representado por `N`.

# In[1]:


import inspect, re
import numpy as np
from matplotlib.pyplot import plot
from warnings import warn
from prettytable import PrettyTable as pt


def bissecao(f,a,b,tol,N):
    """Algoritmo para determinação de raízes pelo método da bisseção.

    Parâmetros: 
        f: string dependendo de uma variável, i.e., a função-alvo
            (e.g., 'x**2 - 1', 'x**2*cos(x)', etc.) 
        a: estimativa inferior
        b: estimativa superior
        tol: erro desejado (tolerância)
        N: número máximo de iterações a repetir

    Retorno: 
        x: aproximação para a raiz da função   
    """
    
    # construtor de tabela
    table = pt()
    
    # substitui expressões da string pelas chamadas das funções do numpy
    f = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', f)
    
    # identifica a variável independente
    var = re.search(r'([a-zA-Z][\w]*) ?([\+\-\/*]|$|\))', f).group(1)
    
    # cria função anônima
    f = eval('lambda ' + var + ' :' + f)
    
    # checa se a função é de uma variável, senão lança erro        
    if len(inspect.getfullargspec(f).args) - 1 > 0:    
        raise ValueError('O código é válido apenas para uma variável.')

    # calcula valor da função nos extremos
    fa = f(a) 
    fb = f(b)
    
    # verifica sinal da função para o intervalo passado     
    if fa*fb >= 0:
        raise ValueError('A função deve ter sinais opostos em a e b!')
    
    # flag usada para marcar caso f(xm) = 0
    done = False;
        
    # no. iterações mínimo
    niter = int(np.ceil(np.log((b-a)/tol)/np.log(2)))
    if N < niter:
        print(f'! São necessárias pelo menos {niter} iterações, mas N = {N}.\n')

    
    # cabeçalho de tabela
    table.field_names = ['i','xm','f(xm)','a','b','f(a)','f(b)','EA']

    # bisecta o intervalo
    xm = (a+b)/2
    
    # contador 
    i = 1 
    
    # loop 
    while abs(a-b) > tol and (not done and N != 0):    
        
        # avalia a função no ponto médio
        fxm = f(xm) 
                        
        # adiciona linha de tabela de resultado
        table.add_row([i,np.round(xm,8),np.round(f(xm),8),
                   np.round(a,4),np.round(b,4),
                   np.round(f(a),4),np.round(f(b),4),
                   f'{abs(a-b):e}'])
   
        if fa*fxm < 0:      # Raiz esta à esquerda de xm
            b = xm
            fb = fxm
            xm = (a+b)/2
        elif fxm*fb < 0:    # Raiz esta à direita de xm
            a = xm
            fa = fxm
            xm = (a+b)/2
        else:               # Achamos a raiz
            done = True            
    
        N -= 1              # Atualiza passo
        i += 1              # Atualiza contador
    
    # impressão de tabela
    table.add_row([i,np.round(xm,8),np.round(f(xm),8),
                   np.round(a,4),np.round(b,4),
                   np.round(f(a),4),np.round(f(b),4),
                   f'{abs(a-b):e}'])
    table.align = 'c'; print(table)
    
    return xm


# ## Exemplo
# 
# Resolva o problema $f(x) = 0$, para $f(x) = -\text{arccos}(x) + 4\text{sen}(x) + 1.7$, no intervalo $-0.2 \le x \le 1.0$ e $\epsilon = 10^{-3}$.

# - Primeiramente, façamos uma análise gráfica para verificar o comportamento da função.

# In[2]:


x = np.linspace(-0.2,1,100)
plot(x,-np.arccos(x) + 4*np.sin(x) + 1.7,x,0*x);


# - Uma vez que a raiz é única, basta aplicar o método que construímos à função desejada.

# In[3]:


xm = bissecao('-arccos(x) + 4*sin(x) + 1.7',-0.2,1.0,1e-3,40)


# - A raiz aproximada $x^{*}$, tal que para $f(x^{*}) = 0$ no intervalo-alvo é mostrada na última linha da tabela. Isto é,

# In[4]:


# raiz aproximada
xm


# ## Exemplo
# 
# Resolva o problema $h(z) = 0$, para $h(z) = -z(1-2z)^{-1} - \text{tan}(z+1)$, no intervalo $[1,8]$ e $\epsilon = 10^{-5}$.

# - Primeiramente, façamos uma análise gráfica para verificar o comportamento da função.

# In[5]:


z = np.linspace(1,8.5,100)
plot(z,z/(1 - 2*z) - np.tan(z+1),z,0*z);


# - Neste caso, a função apresenta sensibilidades e mais de uma raiz no intervalo dado. Vamos buscar a raiz que está no subintervalo $[4,6]$. Para tanto, vamos deamplificar a plotagem.

# In[6]:


z = np.linspace(4,6,100)
plot(z,z/(1 - 2*z) - np.tan(z+1),z,0*z);


# - Uma vez que a raiz é única, basta aplicar o método que construímos à função desejada.

# In[7]:


zm = bissecao('z/(1 - 2*z) - tan(z+1)',4,6,1e-5,20)


# - A raiz aproximada $z^{*}$, tal que para $h(z^{*}) = 0$ é mostrada na última linha da tabela. Isto é,

# In[8]:


# raiz aproximada
zm


# ## Exemplo aplicado
# 
# Vamos aplicar nosso método da bisseção ao problema do paraquedista apresentado no capítulo introdutório para buscar o coeficiente de arrasto adequado para os parâmetros de projeto impostos. 

# - Primeiramente, vamos definir uma função para retornar a equação particular.

# In[11]:


def eq_paraq(tempo,massa,vel,grav):
    """ Define equação particular para cálculo de coeficiente de arrasto 
        em salto de paraquedista. (Ver introdução.)
        
        Parâmetros: 
        
            tempo: duração de salto até velocidade terminal [s]
            massa: massa do paraquedista [kg]
            vel: velocidade terminal desejada [m/s]
            grav: aceleração gravitacional ambiente [m/s**2]
        
        Retorno: 
        
            f: expressão numérica para equação particular
               do coeficiente de arrasto
                
    """
    
    # variáveis simbólicas    
    from sympy import symbols, exp, lambdify
    
    g,m,t,v,c = symbols('g,m,t,v,c')
    
    # expressão geral
    f = (g*m/c)*(1 - exp((-c/m)*t)) - v
    
    # expressão particular com valores substituídos convertidos para str
    fs = f.subs({'g':grav,'m':massa,'v':vel,'t':tempo})
    
    # expressão simbólica convertida para expessão numérica
    fn = lambdify(c,fs,"numpy")
    
    # imprime para 
    print(f'Equação particular: f(c) = {fs}')
    
    return (fs,fn)


# - Em seguida, inserimos os valores de entrada para teste. 

# In[12]:


# parâmetros de entrada
tempo, massa, vel, grav = 12, 70, 42, 9.81

# equação particular
fs,fn = eq_paraq(tempo,massa,vel,grav)


# - O próximo passo realiza a análise gráfica para localização do intervalo de aproximação da raiz.

# In[13]:


c = np.linspace(1,20)
plot(c,fn(c),c,0*c);


# - Por fim, aplicamos o método.

# In[14]:


cm = bissecao(str(fs),14,17.0,1e-4,20)


# O coeficiente de arrasto aproximado para este caso é dado por:

# In[15]:


cm


# ## Exercícios
# 
# 1. Repita a análise anterior alterando os parâmetros de projeto de salto para paraquedistas de diferentes massas e com duração de salto até a velocidade terminal variáveis. Faça a análise gráfica e busque aproximações.
# 
# 2. Programe uma nova função para executar o método da falsa posição ou estenda o código anterior para uma nova função que contemple os dois casos (sugestão: use `if`).

# ## Problema proposto 
# 
# Uma reação química reversível $2A+B \iff C$ pode ser caracterizada pela relação de equilíbrio $K = \dfrac{c_c}{c_a^2c_b}$, onde a nomenclatura $c_i$ representa a concentração do constituinte $i$. Suponha que $x$ é o número de moles de $C$ que são produzidos. A conservação da massa pode ser usada para reformular a relação de equilíbrio como
# 
# $$K = \dfrac{(c_{c,0} + x)}{(c_{a,0} - 2x)^2 (c_{b,0} - x)},$$
# 
# onde o subscrito $0$ designa a concentração inicial de cada constituinte. Considere $K = 0,016$, $c_{a,0} = 42$, $c_{b,0} = 28$ e $c_{c,0} = 4$ e faça o que se pede:
# 
# 
# 1. Faça a análise gráfica do problema.
# 2. Com base em no item anterior, escolha aproximações $x_l$ e $x_r$ adequadas e adote $\epsilon_s = 0,5\%$ como erro. (Vide clipping _Definições de erro_ para entender $\epsilon_s$.)
# 3. Aplique o método da bisseção para determinar uma aproximação para $x$.
