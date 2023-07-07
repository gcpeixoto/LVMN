#!/usr/bin/env python
# coding: utf-8

# # Erros numéricos e seus efeitos

# ## Motivação

# **Exemplo**: Avaliar o polinômio $P(x) = x^3 - 6x^2 + 4x - 0.1$
# no ponto $x=5.24$ e comparar com o resultado exato.
# 
# Vamos fazer o seguinte:
# 
# 1. Com uma calculadora, computar o valor de $P(5.24)$ e assuma que este é seu valor exato.
# 
# 2. Calcular $P(5.24)$ usando arredondamento com dois dígitos de precisão.
# 
# **Passo 1**
# 
# Faça as suas contas! Suponhamos que seja -0.007776.
# 
# **Passo 2**
# 
# Vamos "imitar" as contas feitas na mão... 

# In[2]:


# parcelas 

p1 = 5.24**3
print('p1: {0:.20g}'.format(p1)) # 20 dígitos significativos
print('p1 (com arredondamento): {0:.2f}'.format(p1)) 

print('\n')

p2 = - 6*5.24**2
print('p2: {0:.20g}'.format(p2))
print('p2 (com arredondamento): {0:.2f}'.format(p2))

print('\n')

p3 = 4*5.24
print('p3: {0:.20g}'.format(p3))
print('p3 (com arredondamento): {0:.2f}'.format(p3))

print('\n')

p4 = - 0.1
print('p4: {0:.20g}'.format(p4))
print('p4 (com arredondamento): {0:.2f}'.format(p4))

print('\n')

Px = p1 + p2 + p3 + p4
print('Px: {0:.20g}'.format(Px))
print('Px: (com arredondamento): {0:.2f}'.format(Px))


# **Conclusão:** o cálculo com dois dígitos afeta o resultado drasticamente!

# Agora, vamos comparar o resultado de se avaliar $P(5.24)$ com as duas formas do polinômio e 16 dígitos de precisão:

# In[4]:


# ponto de análise
x = 5.24

# P1(x) 
P1x = x**3 - 6*x**2 + 4*x - 0.1 
print('{0:.16f}'.format(P1x))

# P2(x) 
P2x = x*(x*(x - 6) + 4) - 0.1 # forma estruturada (forma de Hörner)
print('{0:.16f}'.format(P2x))


# O que temos acima? Dois valores levemente distintos. Se computarmos os erros absoluto e relativo entre esses valores e nosso valor supostamente assumido como exato, teríamos: 
# 
# **Erros absolutos**

# In[4]:


x_exato = -0.007776
EA1 = abs(P1x - x_exato)
print(EA1)

EA2 = abs(P2x - x_exato)
print(EA2)


# Claro que $EA_1 > EA_2$. Entretanto, podemos verificar pelo seguinte teste lógico:

# In[5]:


# teste é verdadeiro
EA1 > EA2


# **Erros relativos**
# 
# Os erros relativos também podem ser computados como:

# In[6]:


ER1 = EA1/abs(x_exato)
print(ER1)

ER2 = EA2/abs(x_exato)
print(ER2)


# **Gráfico de $P(x)$**

# In[7]:


import numpy as np
import matplotlib.pyplot as plt

# eixo x com 20 pontos
x = np.linspace(-3,3,num=20,endpoint=True)

# plotagem de P1(x) e P2(x)
P1x = lambda x: x**3 - 6*x**2 + 4*x - 0.1
P2x = lambda x: x*(x*(x - 6) + 4) - 0.1
plt.plot(x,P1x(x),'r',x,P2x(x),'bo');


# ### Função de Airy
# 
# A função de Airy é solução da equação de Schrödinger da mecânica quântica. Muda o comportamento de oscilatório para exponencial.
# 
# Abaixo, vamos criar uma função aproximada (perturbada) para a função de Airy (assumindo-a como uma aproximação daquela que é exata) e outra para calcular diretamente o erro relativo para valores dessas funções.
# 

# In[8]:


from scipy import special
import matplotlib.pyplot as plt 

# eixo x 
x = np.linspace(-10, -2, 100)

# funções de Airy e derivadas (solução exata)
ai, aip, bi, bip = special.airy(x)

# função de Airy (fazendo papel de solução aproximada)
ai2 = 1.1*ai + 0.05*np.cos(x) 


# Podemos usar o conceito de _função anônima_ para calcular diretamente o **erro relativo percentual** para cada ponto $x$:
# 
# $$ER_p(x) = \frac{\mid \ f_{aprox}(x) - f_{ex}(x) \ \mid}{\mid \ f_{ex}(x) \ \mid},$$
# 
# onde $f_{aprox}(x)$ é o valor da função aproximada (de Airy) e 
# onde $f_{ex}(x)$ é o valor da função exata (de Airy).

# In[9]:


# define função anônima para erro relativo
r = lambda fex,faprox: (np.abs(fex-faprox)/np.abs(fex))/100

# calcula erro relativo para função de Airy e sua aproximação
rel = r(ai,ai2)


# A seguir, mostramos a plotagem das funções exatas e aproximadas, bem como do erro relativo pontual.

# In[10]:


# plotagens 
plt.plot(x, ai, 'r', label='sol exata')
plt.plot(x, ai2, 'b', label='sol aprox')
plt.grid()
plt.legend(loc='upper right')
plt.show()

plt.plot(x,rel,'-', label='err rel %')
plt.grid()
plt.legend(loc='upper right');


# ## Erro de cancelamento
# 
# Ocorre quando números de grandezas próximas são subtraídos. No exemplo, a seguir, induzimos uma divisão por zero usando o valor do épsilon de máquina $\epsilon_m$ ao fazer 
# 
# $$\dfrac{1}{(1 + 0.25\epsilon_m) - 1}$$
# 
# Isto ocorre porque o denominador sofre um _cancelamento subtrativo_, quando, para a matemática precisa, deveria valer $0.25\epsilon_m$.

# ## Propagação de erros
# 
# Vamos comparar duas situações. Calcular 
# 
# $$e^{-v} = \sum_{i=0}^{\infty} (-1)^i \frac{v^i}{i!}$$
# 
# e comparar com a identidade $$e^{-v} = \dfrac{1}{e^v}.$$

# In[11]:


# somatória (primeiros 20 termos)
v = 5.25
s = 0
for i in range(20):    
    print('{0:5g}'.format(s))    
    s += ((-1)**i*v**i)/np.math.factorial(i)

print('\ncaso 1: {0:5g}'.format(s))    

print('caso 2: {0:5g}'.format(1/np.exp(v)))


# ## Exemplos
# 
# ### Erro relativo percentual
# 
# Dois estudantes medem a altura h da sala de aula com dois instrumentos de medida diferentes e encontram, respectivamente $h_1 = 2.965 \pm 0.001 \, m$ e $h_2 = 2.964 \pm 0.002\, m$. Qual o erro relativo percentual cometido por cada um? 
# 
# #### Solução 
# 
# O valor exato $h$ não é conhecido. O primeiro estudante tem um instrumento cujo erro máximo cometido é $EA_1 = 0.001 \, m$; o segundo, $EA_2 = 0.002 \, m$. Notemos que pelas expressões $EA_1 = | h - h_1 |$ e $EA_2 = | h - h_2 |$, os erros absolutos não são diretamente computáveis. Logo, temos que usar limitantes de erro. 
# 
# Assim, os erros relativos são computados com base nos limitantes e nos valores medidos (aproximados). Portanto,  
# 
# $$ER_1 = (EA_1/2.965) \times 100\% = (0.001/2.965) \times 100\% = 0.0337\%$$
# 
# $$ER_2 = (EA_2/2.964) \times 100\% = (0.002/2.964) \times 100\% = 0.0675\%$$

# ### Erro máximo
# 
# Uma sala de formato retangular foi medida e foram obtidos 8 m e 12 m como sendo sua largura e seu comprimento, respectivamente. Sabendo que o erro cometido em cada uma dessas medições foi de no máximo 2 cm, determine o erro máximo cometido no cálculo de sua área. 
# 
# #### Solução
# 
# Sejam:
# 
# - $a'$: largura aproximada (obtida pela medição)
# - $b'$: comprimento aproximado (obtido pela medição) 
# - $a$:  largura exata da sala; 
# - $b$:  comprimento exato da sala
# - $A'$: área aproximada da sala; 
# - $A$:  área exata 
# 
# São dados $a' = 8m$ e $b' = 12 \, m$. Portanto, $A' = a'b' = 8.12 = 96 \, m^2$. 
# 
# Por hipótese, $EA_a = |a-a'| \leq 2 \, cm$ e $EA_b = |b−b'| \leq 2 \, cm$. 
# 
# Ou seja, $|a−8| \leq 0.02 \, m$ e $|b−12| \leq 0.02 \, m$, que equivalem a 
# $$−0.02 \leq a−8 \leq 0.02 \Rightarrow$$ 
# $$8−0.02 \leq a \leq 8+0.02 \Rightarrow$$
# $$7.98 \leq a \leq 8.02 \quad(i)$$
# $$\text{e}$$
# $$−0.02 \leq b−12 \leq 0.02 \Rightarrow$$
# $$12−0.02 \leq b \leq 12+0.02 \Rightarrow$$
# $$11.98 \leq b \leq 12.02 \quad (ii).$$ 
# 
# Multiplicando (i) e (ii), obtemos: 
# $$95.6004 \leq ab \leq 96.4004 \Rightarrow \\
#   95.6004 \leq A \leq 96.4004 \Rightarrow \\
#   A \in [95.6004, 96.4004].$$ 
#   
# Como $A'$ também pertence ao intervalo, a maior distância entre $A$ e $A'$ ocorre quando $A$ for uma das extremidades do intervalo. Portanto, como 
# $$|96.0000 − 95.6004| = 0.3960 \, m^2,$$ 
# 
# o erro máximo no cálculo da área é de 
# $$|96.0000 − 96.4004| = 0.4004 \, m^2.$$ 

# ### Truncamento e arredondamento
# 
# Considere o sistema $\mathbb{F}(10,4,−3,3)$. Isto é, a representação exata de um númeor real deve ter a forma: $\pm 0.d_1d_2d_3d_4 \times 10^e$, com $d_1 \neq 0$ e $e \in \{−3,−2,−1,0,1,2,3\}$. Sejam $x = 0.2345 \times 10^3$ e $y = 0.7000 \times 10^{−1}$.
# 
# Sabemos que $x + y = 234.5 + 0.07 = 234.57$. No entanto, este resultado não pode ser representado neste sistema, pois para isto precisaríamos de cinco dígitos! No caso, seria $x + y = 0.2345{7} \times 10^3.$
# 
# Como aproximar a soma $s = x + y$, de tal forma que seja possível representá-la nesse sistema de ponto flutuante?
# 
# #### Solução 
# 
# Determine os erros.
# 
# Temos $d_1 = 2, d_2 = 3,d_3 = 4,d_4 = 5$ e $d_5 = 7$. 
# 
# ##### Aproximação por Truncamento 
# 
# Despreze o quinto dígito ($d_5 = 7$) para obter $\bar{s} = 0.2345 \times 10^3 = 234.5$. 
# 
# Neste caso, o Erro Absoluto é:$|EA_s|=|s−\bar{s}|=
# |234.57−234.5|=0.07$. 
# 
# O valor absoluto do Erro Relativo é: $|ER_s| = \frac{0.07}{234.5} \approx 0.2985 \times 10^{−3}.$
# 
# ##### Aproximação por Arredondamento 
# 
# O quinto dígito ($d_5 = 7$) é levado em conta, assim provocando uma modificação no quarto dígito ($d_4 = 5$). Como $7 \geq 5$, soma-se $0.5 \times 10^{−4} = 0.00005$ a $s$, obtendo-se: 
# $$\bar{s} = 0.23462\times 10^3.$$
# 
# Daí, trunca-se $\bar{s}$ no quarto novo dígito. 
# 
# A aproximação de $s$ por arredondamento é $\bar{s} = 0.2346\times 10^3$.
# 
# Neste caso o Erro Absoluto é: $|EA_s|=|s−\bar{s}|=|234.57−234.6|=0.03.$
# 
# O Erro Relativo é: $|ER_s| = \frac{0.03}{234.6} \approx 0.1278\times 10^{−3}.$

# 
