# Code session 3

%matplotlib inline
import numpy as np 
import matplotlib.pyplot as plt 

## Determinação de raízes de polinômios

### `roots`

A função `roots` computa as raízes de uma função dentro de um intervalo dado usando o método de Hörner. 
O único argumento de entrada desta função é

1. o _array_ `p` com os coeficientes dos termos do polinômio.

$$P(x) = p_n x^n + p_{n-1} x^{n-1} + \ldots + p_1x + p_0$$


O argumento de saída é:

- `x`: _array_ com as raízes de $P(x)$.

Como importá-la? 

```python 
from numpy import roots
```

Porém, como já fizemos uma importação do `numpy` acima, basta utilizarmos 

```python 
np.roots(p)
```

### Problema 1 

Determine as raízes de $P(x) = 3x^3 +7x^2 - 36x + 20$.

#### Resolução

Para tornar claro, em primeiro lugar, vamos inserir os coeficientes de $P(x)$ em um _array_ chamado `p`. 

p = np.array([3,7,-36,20])

Em seguida, fazemos: 

x = np.roots(p)

Podemos imprimir as raízes da seguinte forma:

for i, v in enumerate(x):
    print(f'Raiz {i}: {v}')

### `polyval` 

Podemos usar a função `polyval` do `numpy` para avaliar $P(x)$ em $x = x_0$. Verifiquemos, analiticamente, se as raízes anteriores satisfazem realmente o polinômio dado.

for i in x:
    v = np.polyval(p,i)
    print(f'P(x) = {v}')

Note que as duas últimas raízes são "muito próximas" de zero, mas não exatamente zero. 

Podemos também fazer uma verificação geométrica plotando o polinômio e suas raízes. 

xx = np.linspace(np.min(x)-0.5,np.max(x)+0.5)
plt.plot(xx,np.polyval(p,xx));
for i in x:
    plt.plot(i,np.polyval(p,i),'or')

### Problema 2

Determine as raízes de $P(x) = x^4 - 3x^2 + 3x$.

#### Resolução

Resolvendo diretamente com `roots` e usando `polyval` para verificação, temos:

# coeficientes e raízes
p = np.array([1,0,-3,3,0])
x = np.roots(p)

# imprimindo as raizes
for i, v in enumerate(x):
    print(f'Raiz {i}: {v}')

Note que, neste caso, as raízes são complexas.

### Problema 3

Determine as raízes de $P(x) = x^5 - 30x^4 + 361x^3 - 2178x^2 + 6588x - 7992$.

#### Resolução

# coeficientes e raízes
p = np.array([1,-30,361,-2178,6588,-7992])
x = np.roots(p)

# imprimindo as raizes
for i, v in enumerate(x):
    print(f'Raiz {i}: {v}')