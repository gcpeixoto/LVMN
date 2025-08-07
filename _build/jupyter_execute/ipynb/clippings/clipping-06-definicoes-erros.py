#!/usr/bin/env python
# coding: utf-8

# # Recorte 6: Definições de erro
# 
# ## Erro absoluto
# 
# O _erro absoluto_ é computado pelo módulo do _erro real_ (ou verdadeiro) e dado por 
# 
# $$E_v = | \text{valor verdadeiro} - \text{valor aproximado}|,$$
# 
# onde o subscrito $v$ significa _verdadeiro_.  
# 
# No entanto, o grande defeito do erro absoluto é não levar em conta a **ordem de grandeza** dos valores envolvidos no seu cálculo. Então, para levarmos em conta a ordem de grandeza, devemos normalizá-lo.
# 
# ## Erro relativo
# 
# A normalização do erro absoluto produz o _erro relativo_, o qual pode ser relativo ao valor exato (verdadeiro) ou ao próprio valor aproximado. No primeiro caso, temos o _erro relativo verdadeiro_ $\epsilon_v$, dado por
# $$\epsilon_v = \dfrac{E_v}{\text{valor verdadeiro}}.$$ 
# 
# Em geral, os erros relativos são dados em porcentagem. Assim, podemos escrever 
# 
# $$\epsilon_v = \dfrac{E_v}{\text{valor verdadeiro}} \times 100\%.$$ 
# 
# ## Erro relativo aproximado
# 
# Todavia, em situações reais, nem sempre conhecemos o valor verdadeiro. Ele está disponível quando temos soluções analíticas ("fechadas") para alguns problemas simplificados. Este desconhecimento prévio do valor verdadeiro leva-nos à necessidade de se estabelecer o erro relativo normalizado pelo valor aproximado, isto é,
# 
# $$\epsilon_a = \dfrac{\text{erro aproximado}}{\text{valor aproximado}} \times 100\%,$$ 
# 
# sendo o erro aproximado não exatamente aquele dado por $E_v$. 
# 
# ## Erro relativo - abordagem iterativa
# 
# 
# Em métodos numéricos aplicados a problemas do mundo real, temos interesse em determinar estimativas de erro, já que não temos conhecimento prévio relativo ao valor verdadeiro. A abordagem _iterativa_, que veremos mais à frente, encontra a aproximação atual com base em uma aproximação prévia, que parte de uma estimativa inicial. Para essas situações, o erro relativo é estimado como 
# 
# $$\epsilon_a = \dfrac{\text{aproximação atual - aproximação prévia}}{\text{aproximação atual}} \times 100\%$$
# 
# Nos métodos iterativos, a prática comum é especificar uma tolerância porcentual $\epsilon_s$ para o erro relativo e esperar que os métodos obtenham um erro menor do que esta tolerância, isto é, 
# 
# $$|\epsilon_a | < \epsilon_s.$$ 
# 
# Caso esta desigualdade seja verificada, diremos que nosso o método possui uma margem de erro aceitável e pode ser considerado suficientemente preciso dentro do que estabelecemos.
# 
# 
# 
# 
# 
