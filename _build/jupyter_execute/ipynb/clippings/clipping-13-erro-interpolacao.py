#!/usr/bin/env python
# coding: utf-8

# # Recorte 13: Análise de erros em interpolação polinomial
# 
# ## Erro na interpolação
# 
# - O problema da interpolação garante que 
# 
# $$P_n(x_k) = f(x_k), \ \ k = 0,1,\ldots,n,$$
# 
# para um polinômio $P_n(x)$ interpolador de $f(x)$ sobre um conjunto distinto de pontos $x_0,x_1,\ldots,x_n$.
# 
# - O mesmo não é garantido para pontos $\overline{x} \neq x_k$, isto é, nem sempre teremos $P_n(\overline{x}) = f(\overline{x})$
# 
# -  Uma vez que $P_n(x)$ aproxima $f(x)$, um erro existe
# 
# -  Perguntas: quão boa é a aproximação feita por $P_n(x)$? Como ter ideia do erro cometido? 
# 
# 
# Ao se aproximar $f(x)$ por $P_n(x)$ (grau $\leq n$), comete-se um erro – Notemos que $E_n(\overline{x}) = 0, \forall \overline{x} \neq x_k$.
# 
# $$E_n(x) = f(x) - P_n(x), \qquad \forall x \in [x_0,x_n]$$
# 
# **Teorema 1:** Seja $f(x)$ contínua em $[a,b]$ e suponhamos que $f^{(n+1)}(x)$ exista para todo $x \in (a,b)$. Se $a \leq x_0 < x_1 < x_2 < \ldots < x_n \leq b$, então:
# $$E_n(x) = f(x) - P_n(x) = (x-x_0)(x-x_1)(x-x_2) \ldots (x-x_n) \dfrac{ f^{(n+1)}(\xi_x) }{ (n+1)! },$$
# onde $x_0 < \xi_x < x_n$. O ponto $\xi_x$ depende de $x$.
# 
# ### Majorante para o erro
# 
# - A fórmula para o erro dada anteriormente tem uso prático limitado, pois $f^{(n+1)}(x)$ nem sempre sera conhecida, assim como a determinação de $\xi_x$.
# 
# - A fórmula exata tem relevância teórica, já que é usada na obtenção de estimativas de erro para as fórmulas de interpolação, diferenciação e integração numérica
# 
# - Dois corolários do teorema anterior são importantes para se trabalhar com um **majorante para o erro**
# 
# 
# **Corolário 1:** Sob as hipóteses do Teorema 1, se $f^{(n+1)}(x)$ for contínua em $I = [x_0, x_n]$, podemos escrever a seguinte relação
# $$| E_n(x) | = | f(x) - P_n(x) | \leq | (x-x_0)(x-x_1) \ldots (x-x_n) | \dfrac{ M_{n+1} }{(n+1)!}$$
# 
# com 
# 
# $$M_{n+1} = \max_{x  \in I}| f^{(n+1)}(x) |.$$
# 
# 
# **Corolário:** Se além das hipóteses do Corolário 1, os pontos forem igualmente espaçados, isto é, 
# $x_1 - x_0 = x_2 - x_1 = \ldots = x_n - x_{n-1} = h$, então
# 
# $$| f(x) - P_n(x) | < \dfrac{ h^{(n+1)}M_{n+1} }{ 4(n+1) }$$
# 
# O majorante independe de $x$.
# 
# 
# ### Estimativa para o erro
# 
# Se $f(x)$ for dada na forma de tabela, o valor absoluto $| E_n(x) |$ pode ser apenas estimado, pois, neste caso, não é possível calcular $M_{n+1}$; mas, se continuarmos a tabela de DDs até a ordem $n+1$, poderemos usar o maior valor (em módulo) das DDs como uma aproximação para
# 
# $$\dfrac{M_{n+1}}{(n+1)!}, \qquad [x_0,x_n].$$
# 
# Neste caso, dizemos que
# 
# $$| E_n(x) | \approx | (x-x_0)(x-x_1) \ldots (x-x_n) | | M |,$$
# 
# para $M$ o valor máximo das DDs de ordem $n+1$.
