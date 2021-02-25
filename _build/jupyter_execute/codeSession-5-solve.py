# Code session 5

import numpy as np

## `linalg.solve`

A função `solve` é o método mais simples disponibilizado pelos módulos `numpy` e `scipy` para resolver sistemas matriciais lineares. Como a função pertence ao escopo da Álgebra Linear, ela está localizada em submódulo chamado `linalg`. `solve` calculará a solução exata do sistema como um método direto se a matriz do sistema for determinada (quadrada e sem colunas linearmente dependentes). Se a matriz for singular, o método retorna um erro. Se for de posto deficiente, o método resolve o sistema linear usando um algoritmo de mínimos quadrados. 

Os argumentos de entrada obrigatórios desta função são: 

1. a matriz `A` dos coeficientes
2. o vetor independente `b`

O argumento de saída é:

- `x`: o vetor-solução do sistema.

Como importá-la? 

```python 
from numpy.linalg import solve
```

from numpy.linalg import solve

### Problema 1

Uma rede elétrica contém 3 _loops_. Ao aplicar a lei de Kirchoff a cada _loop_, o cientista Hely Johnson obteve as seguintes equações para as correntes $i_1$, $i_2$ e $i_3$ em cada _loop:_

$$\begin{eqnarray}
(50 + R)i_1 - Ri_2 - 30i_3 &=& 0 \\
- Ri_1 + (65 + R)i_2 - 15i_3 &=& 0 \\
-30i_1 - 15i_2 + 45i_3 &=& 120 
\end{eqnarray}$$

Ajude Hely Johnson em seus experimento e calcule as correntes para os valores de resistência $R = \{ 5 \Omega, 10 \Omega, 20 \Omega \}$.

### Resolução

Podemos começar definindo uma lista para armazenar os valores das resistências de teste:

R = [5.,10.,15.]

Em seguida, escreveremos a matriz dos coeficientes e o vetor independente (lado direito). Note que precisamos de uma "lista de listas", ou melhor, um _"array de arrays"_, onde cada _array_ está associado à uma linha da matriz.

Todavia, vamos definir uma função para montar o sistema em função do valor de $R$ e resolvê-lo. 

# montagem do sistema
def resolve_sistema(R):
    A = np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ])
    b = np.array([0,0,120])
    x = solve(A,b)
    return x

Além disso, usaremos um laço `for` para calcularmos todas as respostas necessárias de uma só vez e organizaremos os resultados em dicionário (objeto `dict`):

# salva soluções agrupadas em um dicionário
sols = {}
for r in R:
    sols[r] = resolve_sistema(r)
    print('Para o valor de resistência R = {0:g} ohms: i1 = {1:g} A, i2 = {2:g} A, i3 = {3:g} A'.format(r, sols[r][0], sols[r][1], sols[r][2]))

### Tarefa

Retorne ao notebook da [Aula 09](aula-09-eliminacao-gauss.ipynb) e use o conteúdo da aula para fazer uma verificação das soluções encontradas para este problema em cada caso. Use a função `linalg.cond` para calcular o _número de condicionamento_ da matriz do sistema em cada caso. (**Sugestão:** vide `numpy.allclose`)