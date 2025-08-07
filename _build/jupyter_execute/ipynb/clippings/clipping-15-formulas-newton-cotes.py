#!/usr/bin/env python
# coding: utf-8

# # Recorte 15: Fórmulas de Newton-Cotes
# 
# ## Introdução
# 
# No texto a seguir, vamos construir uma fórmula geral de Newton-Cotes para integração numérica _fechada_. Assumimos que os nós de integração são igualmente espaçados e que os pontos extremos também são incluídos na fórmula de quadratura. Isto significa que para $n+1$ nós, temos
# 
# $$a = x_0 < x_1 < x_2 < \ldots < x_{n-1} < x_n = b, \ \ \text{com} \ \ h = x_{k+1} - x_k, \, k = 0,1,\ldots,n-1.$$
# 
# Integrar $f(x)$ no domínio $[a,b]$ equivale a buscar o valor de $\int_a^b f(x) \, dx$. De maneira geral, podemos ter $\int_a^b \omega(x) f(x) \, dx$, onde $\omega(x) \geq 0$ é uma _função-peso_ que pode anular-se em um número finito de pontos. Entretanto, usaremos $\omega(x) \equiv 1$.
# 
# Para cada nó $x_k$, os valores $f_k = f(x_k)$ são conhecidos. Numericamente, podemos aproximar o valor exato da integral por um polinômio de Lagrange de ordem $n$ da seguinte forma: 
# 
# $$\int_a^b f(x) \, dx \approx \displaystyle \sum_{k=0}^n f_k A_k = \displaystyle \sum_{k=0}^n f_k \int_{x_0}^{x_n} \mathcal{L}_{n,k}(x) \, dx,$$
# 
# em que, evidentemente, $A_k = \int_{x_0}^{x_n} \mathcal{L}_{n,k}(x) \, dx$, para a função de base de Lagrange $\mathcal{L}_{n,k}(x)$.

# ## Forma de Lagrange para pontos igualmente espaçados
# 
# Antes de prosseguirmos, vale a pena escrever as funções de base de Lagrange e, consequentemente, o próprio polinômio de Lagrange em uma forma especial. Para isso, vamos utilizar a seguinte mudança de variável 
# 
# $$u = \dfrac{x-x_0}{h}.$$
# 
# Esta mudança está embasada em dois resultados (teoremas que podem ser provados por indução): 
# 
# 1. Para $r \in \mathbb{Z}_{+}$, $x - x_r = (u-r)h$
# 2. Para $r,s \in \mathbb{Z}_{+}$, $x_r - x_s = (r-s)h$
# 
# Uma vez que o polinômio de Lagrange é dado por $P_n(x) = \sum_{k=0}^n \, f_k \mathcal{L}_{n,k}(x)$ com funções de base
# 
# $$\mathcal{L}_{n,k}(x) = \dfrac{ (x-x_0)(x-x_1) \ldots (x-x_{k-1})(x-x_{k+1}) \ldots (x-x_n) }{ (x_k-x_0)(x-x_1) \ldots (x_k-x_{k-1})(x_k-x_{k+1}) \ldots (x_k-x_n)  },$$
# 
# a mudança de variável anterior permite-nos escrevê-lo como
# 
# $$P_n(x_0 + uh) = \sum_{k=0}^n \, f_k \lambda_{n,k}(u),$$ 
# 
# para
# 
# $$\lambda_{n,k}(u) = \dfrac{ u(u-1) \ldots (u-(k-1))(u-(k+1)) \ldots (u-n) }{ k(k-1) \ldots (k-(k-1))(k-(k+1)) \ldots (k-n)  }.$$
# 
# Logo, $P_n(x_0 + uh)$ é a **forma de Lagrange para pontos igualmente espaçados**.

# ## Fórmulas gerais
# 
# A mudança de variável nos permite ter $dx = hdu$, de onde segue que: 
# 
# $$\begin{cases}
# x=x_0,& \rightarrow u = 0 \\
# x=x_n,& \rightarrow u = n \\
# \end{cases}$$
# 
# Assim, a aproximação de nossa integral converte-se em:
# 
# $$\int_{x_0}^{x_n} f(x) \, dx \approx \displaystyle \sum_{k=0}^n f_k h C_k^n \approx \displaystyle \sum_{k=0}^n f_k h \int_{0}^{n} \lambda_{n,k}(u) \, du,$$
# 
# para $C_k^n = \int_{0}^{n} \lambda_{n,k}(u) \, du$.
# 
# A fórmula anterior, totalmente independente dos limites de integração fornece-nos as mais diversas (e conhecidas) fórmulas de Newton-Cotes. 
# 
# ### Regra do Trapézio Simples
# 
# Quando $n=1$, obtemos uma fórmula de quadratura a dois pontos com polinômio de grau 1. Isto é, 
# 
# $$\int_{x_0}^{x_1} f(x) \, dx \approx f_0 h C_0^1 + f_1 h C_1^1.$$
# 
# Porém, notemos que: 
# 
# $$\begin{aligned}
# C_0^1 &= \int_{0}^{1} \lambda_{1,0}(u) \, du = \int_{0}^{1} \dfrac{u-1}{0-1} \, du = \int_{0}^{1} (1-u) \, du = \dfrac{1}{2} \\
# C_1^1 &= \int_{0}^{1} \lambda_{1,1}(u) \, du = \int_{0}^{1} \dfrac{u-0}{1-0} \, du = \int_{0}^{1} u \, du = \dfrac{1}{2} \end{aligned}$$
# 
# Logo,
# 
# $$\int_{x_0}^{x_1} f(x) \, dx \approx f_0 h \dfrac{1}{2} + f_1 h \dfrac{1}{2} = \dfrac{h}{2}(f_0 + f_1) = \dfrac{h}{2}[f(x_0) + f(x_1)],$$
# 
# que é a tradicional **regra do trapézio simples**.
# 
# ### Regra do Trapézio Composta
# 
# A **regra do trapézio composta** equivale a aplicar a regra simples para cada subintervalo de $[a,b]$: 
# 
# $$\int_{x_0}^{x_n} f(x) \, dx \approx \dfrac{h}{2}[f(x_0) + 2( f(x_1) + f(x_2) + \ldots + f(x_{n-1})) + f(x_n)],$$
# 
# 
# ### Regra 1/3 de Simpson
# 
# Quando $n=2$, obtemos uma fórmula de quadratura a três pontos com polinômio de grau 2. Isto é, 
# 
# $$\int_{x_0}^{x_2} f(x) \, dx \approx f_0 h C_0^2 + f_1 h C_1^2 + f_2 h C_2^2.$$
# 
# Porém, notemos que: 
# 
# $$\begin{aligned}
# C_0^2 &= \int_{0}^{2} \lambda_{2,0}(u) \, du = \int_{0}^{2} \dfrac{(u-1)(u-2)}{(0-1)(0-2)} \, du = \dfrac{1}{2}\int_{0}^{2} u^2 - 3u + 2 \, du = \dfrac{1}{3} \\
# C_1^2 &= \int_{0}^{2} \lambda_{2,1}(u) \, du = \int_{0}^{2} \dfrac{(u-0)(u-2)}{(1-0)(1-2)} \, du = -\int_{0}^{2} u^2 - 2u \, du = \dfrac{4}{3} \\ 
# C_2^2 &= \dfrac{1}{3} \end{aligned}$$
# 
# Logo,
# 
# $$\int_{x_0}^{x_2} f(x) \, dx \approx \dfrac{h}{3}(f_0 + 4f_1 + f_2) = \dfrac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)],$$
# 
# que é a tradicional **regra 1/3 de Simpson simples**.
# 
# 
# ### Regra 1/3 de Simpson composta
# 
# A **regra 1/3 de Simpson composta** é obtida de forma similar. Dividimos o intervalo de integração em subintervalos de comprimento $h = (b-a)/2n$ (múltiplo de 2 para que a regra simples valha a cada 3 pontos), de modo que 
# 
# 
# $$\int_{x_0}^{x_{2n}} f(x) \, dx \approx \dfrac{h}{3}[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + 2f(x_4) + \ldots + 2f(x_{2n-2}) + 4f(x_{2n-1}) + f(x_{2n})],$$
# 
# 
# ### Regra 3/8 de Simpson
# 
# Quando $n=3$, obtemos uma fórmula de quadratura a quatro pontos com polinômio de grau 3. Isto é, 
# 
# $$\int_{x_0}^{x_3} f(x) \, dx \approx f_0 h C_0^3 + f_1 h C_1^3 + f_2 h C_2^3 + f_2 h C_3^3.$$
# 
# Porém, notemos que: 
# 
# $$\begin{aligned}
# C_0^3 &= \int_{0}^{3} \lambda_{3,0}(u) \, du = \int_{0}^{3} \dfrac{(u-1)(u-2)(u-3)}{(0-1)(0-2)(0-3)} \, du = -\dfrac{1}{6}\int_{0}^{3} u^3 - 6u^2 + 11u - 6 \, du = \dfrac{3}{8} \\
# C_1^3 &= \int_{0}^{3} \lambda_{3,1}(u) \, du = \int_{0}^{3} \dfrac{u(u-2)(u-3)}{(1-0)(1-2)(1-3)} \, du = \dfrac{1}{2}\int_{0}^{3} u^3 - 5u^2 + 6u \, du = \dfrac{9}{8} \\ 
# C_2^3 &= \dfrac{9}{8}  \\ 
# C_3^3 &= \dfrac{3}{8}\end{aligned}$$
# 
# Logo,
# 
# $$\int_{x_0}^{x_3} f(x) \, dx \approx \dfrac{3h}{8}(f_0 + 3f_1 + 3f_2 + f_3) = \dfrac{3h}{8}[f(x_0) + 3(f(x_1) + f(x_2)) + f(x_3)],$$
# 
# que é **regra 3/8 de Simpson simples**.
# 
# ### Regra 3/8 de Simpson composta
# 
# A **regra 3/8 de Simpson composta** é obtida de forma similar. Dividimos o intervalo de integração em subintervalos de comprimento $h = (b-a)/3n$ (múltiplo de 3 para que a regra simples valha a cada 4 pontos), de modo que 
# 
# 
# $$\int_{x_0}^{x_{3n}} f(x) \, dx \approx \dfrac{3h}{8}[f(x_0) + 3(f(x_1) + f(x_2)) + 2f(x_3) + \ldots + \\ 
# + \ \ 2f(x_{3n-3}) + 3(f(x_{3n-2}) + f(x_{3n-1})) + f(x_{3n})],$$
