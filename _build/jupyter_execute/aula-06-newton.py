#!/usr/bin/env python
# coding: utf-8

# # Implementação do método de Newton

# Neste capítulo, utilizamos uma implementação própria do método de Newton para resolver equações não-lineares unidimensionais. O algoritmo é limitado para a entrada de funções matemáticas.
# 
# Para ser executado, o método `newton` requer 5 parâmetros: 
# 
# - a estimativa inicial, representada pela variável `x0`;
# - a função $f(x)$ propriamente dita, representada por `f`;
# - a derivada $f'(x)$, representada por `df`;
# - o erro relativo assumido, representado por `tol`;
# - o número máximo de iterações $N$ para tentativa de solução, representado por `nmax`.

# In[19]:


import inspect, re, numpy as np
from matplotlib.pyplot import plot
from prettytable import PrettyTable as pt

def newton(x0,f,df,tol,N):
    """Algoritmo para determinação de raízes pelo método de Newton.

    Parâmetros: 
        x0: estimativa inicial
        f: string dependendo de uma variável, i.e., a função-alvo
            (e.g., 'x**2 - 1', 'x**2*cos(x)', etc.) 
        df: string dependendo de uma variável, i.e., a derivada da função-alvo
        tol: erro desejado (tolerância)
        N: número máximo de iterações a repetir

    Retorno: 
        x: aproximação para a raiz da função    
    """

    # construtor de tabela
    table = pt()
    
    # substitui expressões da string pelas chamadas das funções do numpy
    f = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', f)
    df = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', df)
    
    # identifica a variável independente em f
    var = re.search(r'([a-zA-Z][\w]*) ?([\+\-\/*]|$|\))', f).group(1)
    
    # cria função
    f = eval('lambda ' + var + ' :' + f)
    
    # checa se a função é de uma variável, senão lança erro        
    try: 
        len(inspect.getfullargspec(f).args) - 1 > 0
    except:
        raise ValueError('O código é válido apenas para uma variável.')
    finally:
        # cria função derivada
        df = eval('lambda ' + var + ' :' + df)
    
    it = 0 # contador de iteracoes
    
    # cabeçalho de tabela
    table.field_names = ['i','x','f(x)','f\'(x)','ER']

    # imprime estimativa inicial
    print(f'Estimativa inicial: x0 = {x0:.6f}\n')  

    # Loop 
    for i in range(0,N):
        
        x = x0 - f(x0)/df(x0) # funcao de iteracao 
        
        e = abs(x-x0)/abs(x) # erro
        
        # tabela
        # impressão de tabela
        table.add_row([i,np.round(x,8),np.round(f(x),8),np.round(df(x),4),f'{e:e}'])
        table.align = 'c';      
        
        if e < tol:
            break
        x0 = x                
        
    print(table)
       
    if i == N:
        print(f'Solução não obtida em {N:d} iterações')
    else:
        print(f'Solução obtida: x = {x:.6f}')


    return x


# ## Exemplo
# 
# Resolva o problema $f(x) = 0$, para $f(x) = -\text{arccos}(x) + 4\text{sen}(x) + 1.7$, no intervalo $-0.2 \le x \le 1.0$ e $\epsilon = 10^{-3}$.

# In[16]:


# Chamada da função
xm = newton(-0.1,
            '-arccos(x) + 4*sin(x) + 1.7',
            '4*cos(x) - 1/(1 - x**2)**1/2',
            1e-3,
            30)


# ## Exemplo
# 
# Resolva o problema $h(z) = 0$, para $h(z) = -z(1-2z)^{-1} - \text{tan}(z+1)$, no intervalo $[1,8]$ e $\epsilon = 10^{-5}$.

# Como no exemplo anterior, para utilizarmos o método de Newton é preciso saber a derivada da função $h(z)$. Vamos encontrá-la utilizando o módulo de computação simbólica `sympy`.

# In[46]:


# Importa variável z como símbolo
from sympy.abc import z 
import sympy as sym

# Derivada
dh = sym.diff(-z/(1 - 2*z) - sym.tan(z+1))

# Impressão
print(dh)


# A partir daí, utilizamos a expressão normalmente na função.

# In[47]:


zm = newton(5,
            'z/(1 - 2*z) - tan(z+1)',
            '-2*z/(1 - 2*z)**2 - tan(z + 1)**2 - 1 - 1/(1 - 2*z)',
            1e-5,30)


# Compare a quantidade de iterações obtidas com o mesmo exemplo resolvido com o algoritmo da bisseção.

# ## Tarefa
# 
# - Generalize o código acima para que a expressão da derivada seja calculada diretamenta por computação simbólica sem intervenção manual.
