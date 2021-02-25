# Otimização de código 

Python possui diversas bibliotecas para computação numérica que são eficientes e de alto desempenho, tais como _numpy_ e _scipy_. A computação de alta performance é atingida não por Python puro, mas pelo aproveitamento de bibliotecas que são compiladas externamente. 

Às vezes, temos necessidade de desenvolver código do zero usando puramente Python. Entretanto, essa escolha pode levar a códigos lentos. A solução é escrever rotinas em linguages externas, tais como C, C++ ou Fortran que façam os cálculos que consomem mais tempo e criar interfaces entre elas e o código Puython.

Existem métodos que permitem criar módulos de extensão para Python, tais como: 

- módulo _ctypes_
- API Python para C 
- CFFI (C foreign function interface)

Embora úteis, todas elas exigem conhecimento aprofundado de outras linguagens e são mais úteis para códigos-fonte já escritos nessas linguagens. Algumas alternativas de desenvolvimento que se aproximam de Python que valem a pena ser consideradas antes de partirmos para uma implementação direta em linguagem complicada existem. Duas delas são: _numba_ e _cython_.

## _numba_

[[Numba]](https://numba.pydata.org) é um compilador *just-in-time* (JIT) para código Python usando _numpy_ que produz código de máquina executável de forma mais eficiente do que o código Python original. Para conseguir isso, _numba_ aproveita o conjunto de compiladores [[LLVM]](http://llvm.org), que se tornou muito popular nos últimos anos por seu design e interface modular e reutilizável. 

## _cython_

[[Cython]](http://cython.org) é um superconjunto da linguagem Python que pode ser traduzido automaticamente para C ou C++ e compilado em um código de máquina executável de modo muito mais rápido do que o código Python. Cython é amplamente utilizado em projetos Python orientados computacionalmente para acelerar partes críticas de tempo de um código que é escrita em Python. Várias bibliotecas dependem muito do Cython. Isso inclui NumPy, SciPy, Pandas e scikit-learn, apenas para mencionar algumas.

Veremos como usar _numba_ e _cython_ para acelerar códigos originalmente escritos em Python. É recomendado que se faça um perfilamento de código com o módulo `cProfile` ou outras ferramentas para identificar gargalos de cálculo antes de tentarmos otimizar algo.

## Exemplos com numba

import numba
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

Não precisamos alterar o código-alvo a ser acelerado. Basta usar o JIT do Numba como "decorador" `@numba.jit` para uma função.

### Soma de elementos em um array

Consideramos o seguinte código simples.

def py_sum(val):
    s = 0
    for v in val:
        s += v
    return s

val = np.random.rand(50000) # 50000 aleatórios
%timeit py_sum(val) 

A versão vetorizada da somatória é mais rápida.

%timeit np.sum(val)

Teste da função. Se assert não lança erro, temos a condição válida.

assert abs(py_sum(val) - np.sum(val)) < 1e-9

Tratando com numba.

@numba.jit
def jit_sum(val):
    s = 0
    for v in val:
        s += v
    return s

assert abs(jit_sum(val) - np.sum(val)) < 1e-9 # função numba produz mesmo valor

%timeit jit_sum(val)

Comparando isto com a implementação pura, temos uma grande diferença.

### Soma cumulativa

def py_cumsum(val):
    o = np.zeros_like(val)
    s= 0
    for n in range(len(val)):
        s += val[n]
        o[n] = s
    return o

%timeit py_cumsum(val)

%timeit np.cumsum(val)

Utilizando numba:

@numba.jit
def jit_cumsum(val):
    o = np.zeros_like(val)
    s= 0
    for n in range(len(val)):
        s += val[n]
        o[n] = s
    return o

%timeit jit_cumsum(val)

### Fractal de Julia

O fractal de Julia exige um número variável de iterações para cada elemento de uma matriz com coordenadas no plano complexo:

- Um ponto $z$ no plano complexo pertence ao conjunto de Julia se a fórmula de iteração $z \leftarrow z^2 + c$ não diverge após um número grande de iterações.

def py_julia_fractal(z_re, z_im, j):
    for m in range(len(z_re)):
        for n in range(len(z_im)):
            z = z_re[m] + 1j * z_im[n] 
            for t in range(256):
                z = z ** 2 - 0.05 + 0.68j 
                if np.abs(z) > 2.0:
                    j[m, n] = t 
                    break

Decorador:

jit_julia_fractal = numba.jit(nopython=True)(py_julia_fractal) # nopython : 

Chamada da função:

N = 1024
j = np.zeros((N, N), np.int64)
z_real = np.linspace(-1.5, 1.5, N) 
z_imag = np.linspace(-1.5, 1.5, N) 
jit_julia_fractal(z_real, z_imag, j)

Visualização do fractal gerado por Numba:

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(j, cmap=plt.cm.RdBu_r, extent=[-1.5, 1.5, -1.5, 1.5])
ax.set_xlabel("$\mathrm{Re}(z)$", fontsize=18)
ax.set_ylabel("$\mathrm{Im}(z)$", fontsize=18);

Comparação do tempo em cada chamada:

%timeit py_julia_fractal(z_real, z_imag, j)

%timeit jit_julia_fractal(z_real, z_imag, j)

### `numba.vectorize`

Aqui, vamos construir a função de Heaviside:

def py_Heaviside(x):
    if x == 0.0: 
        return 0.5
    if x < 0.0: 
        return 0.0    
    else:
        return 1.0

x = np.linspace(-2, 2, 50001)
%timeit [py_Heaviside(xx) for xx in x]

Para ter a função aplicada elemento a elemento em um array, fazemos:

np_vec_Heaviside = np.vectorize(py_Heaviside)
np_vec_Heaviside(x)

A função `vectorize` não resolve o problema com a performance.

%timeit np_vec_Heaviside(x)

Melhor performance é atingida com:

def np_Heaviside(x):
    return (x > 0.0) + (x == 0.0)/2.0

%timeit np_Heaviside(x)

Um desempenho ainda melhor pode ser alcançado usando Numba e o decorador `vectorize`, que obtém uma lista de assinaturas de função para a qual gerar o código compilado por JIT. 

Aqui, escolhemos gerar funções vetorizadas para duas assinaturas - uma que recebe matrizes de números de ponto flutuante de 32 bits como entrada e saída, definidos como `numba.float32`, e um que recebe matrizes de números de ponto flutuante de 64 bits como entrada e saída, definido como `numba.float64`:

@numba.vectorize([numba.float32(numba.float32), numba.float64(numba.float64)])
def jit_Heaviside(x):
    if x == 0.0: 
        return 0.5
    if x < 0.0: 
        return 0.0    
    else:
        return 1.0

%timeit jit_Heaviside(x)