#!/usr/bin/env python
# coding: utf-8

# #  Recorte 14: Projeção ortogonal e equações normais
# 
# ## Projeção ortogonal de um vetor sobre um subespaço
# 
# Seja $E$ um espaço Euclidiano e seja $E'$, de dimensão finita $n$, um subespaço de $E$. Seja $v$ um vetor de $E$ não pertencente a $E'$.
# 
# **Problema**: obter um vetor $v_0 \in E'$ tal que $v − v_0$ seja ortogonal a todo vetor de $E'$. Na figura abaixo, $E = \mathbb{R}^3$ e $E' = \mathbb{R}^2$.
# 
# **Solução**: seja $\{ e_1, e_2, \ldots, e_n \}$ uma uma base de $E'$. Como $v_0 \in E'$, podemos escrevê-lo pela combinação linear:
# 
# $$v_0 = \gamma_1e_1 + \gamma_2e_2 + \ldots + \gamma_ne_n.$$
# 
# Devemos determinar, caso possível, as coordenadas $\gamma_1, \gamma_2, \ldots \gamma_n$.
# 
# Para $v - v_0$ ser ortogonal a $E'$, ele deve ser ortogonal a todo vetor de $E'$. Logo, basta que seja ortogonal a todo vetor de uma base de $E'$. Então, 
# 
# $$\langle v - v_0, e_j \rangle = \langle v - (\gamma_1e_1 + \gamma_2e_2 + \ldots + \gamma_ne_n), e_j \rangle = 0 \qquad \text{para} \ \ j = 1,2,\ldots,n$$ 
# 
# Expandindo o produto vetorial, observamos que a seguinte equação deve ser satisfeita
# 
# $$\gamma_1 \langle e_1, e_j \rangle + \gamma_2 \langle e_2, e_j \rangle + \ldots + \gamma_n \langle e_n, e_j \rangle = \langle v, e_j \rangle, \ \ j = 1,2,\ldots,n.$$
# 
# Equações desse tipo são conhecidas como **equações normais**.
# 
# Assim, para obtermos as coordenadas de $V_0$ na base$ \{ e_1, e_2, \ldots, e_n \}$, devemos resolver o sistema de equações lineares:
# 
# $$\begin{bmatrix}
# \langle e_1,e_1 \rangle & \langle e_2,e_1 \rangle & \ldots & \langle e_n,e_1 \rangle \\
# \langle e_1,e_2 \rangle & \langle e_2,e_2 \rangle & \ldots & \langle e_n,e_2 \rangle \\
# \vdots & \vdots & \ddots & \vdots \\
# \langle e_1,e_n \rangle & \langle e_2,e_n \rangle & \ldots & \langle e_n,e_n \rangle
# \end{bmatrix}
# \begin{bmatrix}
# \gamma_1 \\
# \gamma_2 \\
# \vdots \\
# \gamma_n \\
# \end{bmatrix}
# \,
#  =
# \,
# \begin{bmatrix}
# \langle v,e_1 \rangle \\
# \langle v,e_2 \rangle \\
# \vdots \\
# \langle v,e_n \rangle
# \end{bmatrix},$$
# 
# cuja matriz é simétrica. Pode-se mostrar que o sistema acima possui solução **única**, implicando que $v_0$ é a **projeção ortogonal** de $v$ sobre o subespaço $E'$.
