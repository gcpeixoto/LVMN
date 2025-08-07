#!/usr/bin/env python
# coding: utf-8

# # Recorte 11: Método de Newton-Raphson para raízes múltiplas
# 
# 
# Para mais detalhes, veja o artigo _Newton's method for multiple roots_, autorado por William Gilbert e publicado na revista Computers & Graphics 18(2):227-229, em 1994. DOI: 10.1016/0097-8493(94)90097-3.
# 
# ## Método modificado
# 
# Uma _raiz múltipla_ corresponde a um ponto no qual a função é tangente ao eixo _x_. Por exemplo, 
# 
# $$f(x) = (x-0.5)(x+2)(x+2)$$ 
# 
# possui uma _raiz dupla_ $x = -2$, ao passo que 
# 
# $$f(x) = (x + \pi)^4(x-1)$$ 
# 
# possui uma _raiz quádrupla_ em $x = - \pi$.
# 
# Raízes múltiplas causam dificuldades para muitos dos métodos numéricos iterativos. Ralston e Rabinowitz (1978) propuseram um método de Newton-Raphson modificado para computar raízes múltiplas de uma função $f(x)$. Eles definiram uma nova função 
# 
# $$u(x) = \frac{f(x)}{f'(x)},$$
# 
# cujas raízes são as mesmas de $f(x)$ 
# 
# O MNR padrão aplicado à função $u(x)$ é dado por
# 
# $$x_{i+1} = x_i - \frac{u(x_i)}{u'(x_i)}, \quad i = 0,1,2,\ldots$$
# 
# Tendo em vista que a derivada de $u(x)$ é dada por
# 
# $$u'(x) = \frac{f'(x)f'(x) - f(x)f''(x)}{[f(x)]^2},$$
# 
# podemos substituir $u(x)$ e $u'(x)$ no método padrão para obter o **método de Newton-Raphson modificado**:
# 
# $$x_{i+1} = x_i - \frac{f(x_i)f'(x_i)}{[f'(x_i)]^2 - f(x_i)f'(x_i)}, \quad i = 0,1,2,\ldots$$
