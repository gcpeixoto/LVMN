#!/usr/bin/env python
# coding: utf-8

# # Introdução à solução numérica de EDOs
# 
# Equações diferenciais ordinárias (EDOs) surgem em diversos problemas aplicados. Alguns exemplos: 
# 
# - _Química_: decréscimo radioativo de carbono 14;
# - _Engenharia_: queda da pressão atmosférica;
# - _Economia_: precificação de ativos financeiros.
# 
# Nem sempre é possível obter soluções analíticas (forma fechada) para EDOs. Então, precisamos obter soluções aproximadas por meio de métodos numéricos.
# 
# No passado, muito esforço era empregado para se desenvolver métodos computacionais ótimos, mas a insuficiência de poder computacional era um entrave. Hoje em dia, com a evolução tecnológica, a capacidade computacional de alto desempenho permite que soluções numéricas sejam obtidas com menor esforço de processamento e margem de erro satisfatória. A seguir, faremos uma breve introdução teórica sobre modelos clássicos descritos por EDOs e a resolubilidade das equações.
# 
# ## Modelos clássicos
# 
# ### EDOs de primeira ordem
# 
# - **Crescimento e decrescimento**: modelo (de Malthus) utilizado em crescimento populacional, mor- talidade de espécies biológicas.
# 
# $$y'(t)=ky\Rightarrow y(t)=ce^{kt}, c,k \in \mathbb{R}$$
# 
# **Interpretação:** taxa de mudança da quantidade $y$ é proporcional à própria quantidade ao longo do
# tempo. Se $k > 0$, temos uma lei de crescimento; se $k < 0$, temos uma lei de descrescimento (ou queda).
# 
# - **Lei do resfriamento de Newton:** modelo utilizado para determinar a troca de calor entre um corpo material e um meio externo.
# 
# $$T'(t) = k(T − T_{\infty}) \Rightarrow T(t) = T_0 + (T_{\infty} − T_0)e^{kt},$$
# 
# onde $T$ é a _temperatura do corpo_, $k > 0 \in \mathbb{R}$ a _condutividade térmica_ (dependente do material do corpo e nem sempre constante), $T_{\infty}$ a _temperatura do ambiente_ e $T_0$ a _temperatura inicial_. 
# 
# **Interpretação**: taxa de mudança da temperatura é proporcional a diferença entre a temperatura do objeto e do ambiente com o qual troca calor.
# 
# ### EDOs de segunda ordem
# 
# - **Variação da quantidade de movimento em um sistema (2a. lei de Newton)**: modelo utilizado para descrever a perda de equilíbrio de sistemas mecânicos (cordas vibrantes, molas amortecidas, escoamentos de fluidos viscosos).
# 
# $$my''(t) = −by'(t) − ky + f(t),$$
# 
# onde $m$ é a _massa_, $y$ é um _deslocamento_, $t$ o _tempo_, b > 0 uma _constante de amortecimento_ (absorvedor de choque), $k > 0$ um _parâmetro da mola/empuxo_ e $f(t)$ uma _força externa_. 
# 
# **Interpretação**: taxa de mudança da quantidade de movimento do corpo é igual às forças aplicadas sobre o mesmo. A solução geral desta equação não homogênea será omitida aqui (cf. Weiglholfer and Lindsay, p.32).
# 
# - **2a. lei de Kirchhoff**: modelo usado em circuitos elétricos e eletromagnetismo. 
# 
# $$LQ''(t) + RQ'(t) + \frac{1}{C}Q(t) = U(t),$$
# 
# onde $Q(t)$ é a _carga elétrica_, $L$ é a _indutância_, $R$ a _resistência_, $C$ a _capacitância_ e $U(t)$ a _força eletromotora_ (tensão elétrica). 
# 
# **Interpretação**: a força eletromotora (bateria, por exemplo) em qualquer circuito fechado equilibra todas as diferenças de potencial (d.d.p.) naquele circuito. Em outras palavras: em um circuito fechado, a soma de todas as d.d.p. é nula.
# 
# 
# ## Teoria geral de resolubilidade de EDOs
# 
# 
# ### Problema de Valor Inicial (PVI)  
# 
# Um _problema de valor inicial_ (PVI) é formado por uma EDO e uma _condição inicial_.
# 
# $$\begin{cases}
# y'(t) = f(t,y(t)) \\
# y(t_0) = y_0
# \end{cases},$$
# 
# Acima, $t$ é a _variável independente_, $y(t)$ é a _variável dependente_ (solução da EDO) e $t_0$ é a _condição inicial_.
# 
# **Exemplo:** A EDO $y'(t) = -[y(t)]^2 + y(t)$ possui a chamada solução trivial $y(t) \equiv 0$ e a solução geral: 
# 
# $$y(t) = \dfrac{1}{1+ce^{-t}}$$
# 
# Observemos que $y(t)$ é indefinida quando $1+ce^{-t}=0$, ou $t = \ln(-c)$. Se $y(0) = y_0 \neq 0$ for uma condição inicial geral, $c = \frac{1}{y_0} - 1$ e teremos os seguintes resultados adicionais: 
# 
# |condição inicial|valores de $c$|existência de solução
# |---|---|---|
# |$y_0 > 0$|$c > -1$|$0 \leq t < \infty$ |
# |$y_0 < 0$|$c < -1$|$0 < t < \ln(1 - y_0^{-1})$|
# 
# 
# Abaixo vemos os gráficos de $Y(t)$ quando $c = \{-0.8,-0.5,-0.4,0,0.5,1,0,2.5\}$ e para a solução trivial.

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 

# variavel independente
t = np.linspace(0,6,100)

# condicao inicial
C = [-0.8,-0.5,-0.4,0,0.5,1,0,2.5]

for c in C:    

    # solucoes não triviais
    if c != 0:
        plt.plot(t,1./(1 + c*np.exp(-t)))
    
    # solucao trivial
    else:
        plt.plot(t,0*t,'k--')    
            

