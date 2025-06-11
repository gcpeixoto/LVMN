#!/usr/bin/env python
# coding: utf-8

# # Recorte 12: Condicionamento e normas de matrizes
# 
# ## Normas de matrizes e vetores
# 
# Uma norma é uma função de valor real que fornece uma medida do tamanho ou "comprimento" de entidades matemáticas de componentes múltiplos, tais como vetores e matrizes. Para um vetor de $n$ dimensões $\textbf{x}$, sabemos que uma norma Euclidiana seria calculada como
# 
# $$||\textbf{x}|| = \sqrt{\displaystyle \sum_{i=1}^n \textbf{x}_i^2}.$$
# 
# O conceito pode ser estendido para uma matriz $\textbf{A}$ da seguinte maneira:
# 
# $$||\textbf{A}|| = \sqrt{\displaystyle \sum_{i=1}^n \sum_{j=1}^n a_{i,j}^2},$$
# 
# cujo nome, em especial, é _norma de Frobenius_. Assim como qualquer outra norma de um vetor, ela fornece um valor único que quantifica o "tamanho" de $\textbf{A}$. 
# 
# Para vetores, existem alternativas, as chamadas normas-$p$. que podem ser representadas geralmente por
# 
# $$||\textbf{x}||_p = \left( \displaystyle \sum_{i=1}^n x_i^p \right)^{1/p}.$$
# 
# Vemos que a norma Euclidiana e a norma-$2$ são idênticas para vetores. 
# 
# Outros exemplos importantes são 
# 
# $$||\textbf{x}||_1 = \displaystyle \sum_{i=1}^n |x_i|,$$
# 
# que representa a norma como a soma dos valores absolutos dos elementos. Outra é a norma de _magnitude máxima_.
# 
# $$||\textbf{x}||_{\infty} = \max_{1 \le i \le n} |x_i|,$$
# 
# que define a norma como o elemento com o maior valor absoluto.
# 
# Usando uma abordagem similar, outras normas podem ser desenvolvidas por matrizes. Por exemplo, 
# 
# $$||\textbf{A}||_{1} = \max_{1 \le j \le n} \displaystyle \sum_{i=1}^n |a_{ij}|,$$
# 
# isto é, uma somatória dos valores absolutos dos coeficientes é feita para cada coluna, e a maior dessas somatórias é tomada como a norma. Esta é chamada _norma da soma das colunas_. 
# 
# Uma norma similar pode ser definida para as linhas, resultando na _norma da soma das linhas_
# 
# $$||\textbf{A}||_{\infty} = \max_{1 \le i \le n} \displaystyle \sum_{j=1}^n |a_{ij}|.$$
# 
# Deve-se notar que, em contraste com os vetores, a norma-2 e a norma Euclidiana para uma matriz não são as mesma. A norma-2 é calculada pela expressão 
# 
# $$||\textbf{A}|| = (\mu_{\max})^{1/2},$$ 
# 
# onde $\mu_{\max}$ é o maior autovalor da matriz $\textbf{B} = \textbf{A}^T \textbf{A}$. Esta norma é chamada de _norma espectral_.
# 
# ## Número de condição de uma matriz
# 
# O _número de condição de uma matriz_ é definido (pela forma mais comum) por 
# 
# $$\mathrm{cond}(\textbf{A}) = ||\textbf{A}|| \, || \textbf{A}^{-1} ||.$$
# 
# Se o valor de $\mathrm{cond}(\textbf{A})$ for muito maior do que 1, diz-se que o sistema é **mal-condicionado**. 
