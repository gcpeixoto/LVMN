# Álgebra linear com Python: Eliminação Gaussiana e Condicionamento

%matplotlib inline

## Solução de sistemas lineares

Métodos adequados para a resolução de sistemas lineares e realizar operações no escopo da Álgebra Linear são encontrados no submódulo `linalg` do `scipy`. Importamos essas funcionalidades com: 

```python
from scipy import linalg
```

Vamos calcular a solução do sistema linear ${\bf A}{\bf x} = {\bf b}$ com

$${\bf A} = \begin{bmatrix}
4   & -2  & -3   & 6   &  \\
-6  & 7   & 6.5  & -6  &  \\
1   & 7.5 & 6.25 & 5.5 &  \\
-12 & 22  & 15.5 & -1 
\end{bmatrix},
\quad
{\bf b} = \begin{bmatrix}
12   \\
-6.5 \\
16   \\
17 
\end{bmatrix}$$

Vamos importar os módulos e escrever a matriz ${\bf A}$.

import numpy as np
from scipy import linalg

A = np.array([[4,-2,-3,6],[-6,7,6.5,-6],[1,7.5,6.25,5.5],[-12,22,15.5,-1]])
print(A)

Agora, vamos escrever o vetor ${\bf b}$.

b = np.array([12,-6.5,16,17])
print(b)

Podemos checar as dimensões com

# dimensões de A
A.shape

# dimensão de b
b.shape

A solução do sistema pode ser obtida através do método `linalg.solve`.

x = linalg.solve(A,b)
print(x)

## Inversão de matrizes



Matematicamente, a solução do sistema anterior é dada por ${\bf x} = {\bf A}^{-1}{\bf b}$. Podemos até invocar a matriz inversa aqui com `linalg.inv(A).dot(b)` e a solução é a mesma que no caso anterior.

x2 = linalg.inv(A).dot(b)
print(x2)

 Por outro lado, este método é ineficiente. Computacionalmente, a inversão de matrizes **não** é aconselhável. 

## Verificação da solução 

Podemos usar o fato de que ${\bf A}{\bf A}^{-1}{\bf b} - {\bf b} = {\bf 0}$.

x3 = A.dot(linalg.inv(A).dot(b)) - b
print(x3)

Note que o vetor é próximo do vetor nulo, mas não identicamente nulo.

Podemos também computar a **norma do resíduo (erro)**: $||{\bf r}|| = ||{\bf b} - {\bf A}{\bf x}|| =  \langle {\bf b} - {\bf A}{\bf x}, {\bf b} - {\bf A}{\bf x} \rangle^{1/2}$

r = b - A.dot(x) 
np.sqrt(r.dot(r))

Como a norma do resíduo é próxima de zero, a solução do sistema linear é assumida como correta.

# Eliminação Gaussiana

A Eliminação Gaussiana (EG) é um algoritmo utilizado para resolver sistemas de equações lineares ao reduzir a matriz plena associada do sistema a uma matriz triangular. Este processo também é chamado de _escalonamento_. Abaixo, usaremos uma matriz genérica 3x3 para exemplificação.

## Passos

* Escrever o sistema linear na forma de _matriz estendida_ usando os coeficientes das variáveis como elementos da matriz e o vetor independente como sendo a última coluna;

$$\begin{array}{c}a_{11}x_1+a_{12}x_2+a_{13}x_3 = b_1 \quad(L_1)\\
a_{21}x_1+a_{22}x_2+a_{23}x_3 = b_2 \quad(L_2)\\
a_{31}x_1+a_{32}x_2+a_{33}x_3 = b_3 \quad(L_3)\\
\downarrow\\
\left[
\begin{array}{ccc|c}
	a_{11}&a_{12}&a_{13}&b_{1}\\
	a_{21}&a_{22}&a_{23}&b_{2}\\
	a_{31}&a_{32}&a_{33}&b_{3}
\end{array}
\right]
\end{array}$$

* Realizar operações elementares de combinação linear e permutação entre linhas;
    - Multiplicação por escalar:    
$$
\begin{array}{c}
L_2 \leftarrow L_2 .w\ \Rightarrow\ 
\begin{bmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}\\
\end{bmatrix} \rightarrow
\begin{bmatrix}
a_{11}&a_{12}\\
w.a_{21}&w.a_{22}\\
\end{bmatrix}
\end{array}
$$

    - Combinação linear:    
$$
\begin{array}{c}
L_2 \leftarrow L_2 - L_1.w\ \Rightarrow\ 
\begin{bmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}\\
\end{bmatrix} \rightarrow
\begin{bmatrix}
a_{11}&a_{12}\\
a_{21}-a_{11}.w&a_{22}-a_{12}.w\\
\end{bmatrix}
\end{array}
$$

    - Permutação:
    
$$
\begin{array}{c}
L_2 \leftarrow L_1\ e\ L_1\leftarrow L_2\ \Rightarrow\ 
\begin{bmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}\\
\end{bmatrix} \rightarrow
\begin{bmatrix}
a_{21}&a_{22}\\
a_{11}&a_{12}\\
\end{bmatrix}
\end{array}
$$

* Anular todos os elementos na porção triangular inferior da matriz original, isto é, todas as entradas exatamente abaixo das entradas dispostas na diagonal principal;

$$\left[
\begin{array}{ccc|c}
	a_{11}&a_{12}&a_{13}&b_{1}\\
	a_{21}&a_{22}&a_{23}&b_{2}\\
	a_{31}&a_{32}&a_{33}&b_{3}
\end{array}
\right]\ \rightarrow\ 
\left[
\begin{array}{ccc|c}
	a_{11}^{(k)}&a_{12}^{(k)}&a_{13}^{(k)}&b_{1}^{(k)}\\
	0&a_{22}^{(k)}&a_{23}^{(k)}&b_{2}^{(k)}\\
	0&0&a_{33}^{(k)}&b_{3}^{(k)}
\end{array}
\right]$$

* A partir da forma triangular, realizar a substituição regressiva.

$$
\left[
\begin{array}{ccc|c}
	a_{11}^{(k)}&a_{12}^{(k)}&a_{13}^{(k)}&b_{1}^{(k)}\\
	0&a_{22}^{(k)}&a_{23}^{(k)}&b_{2}^{(k)}\\
	0&0&a_{33}^{(k)}&b_{3}^{(k)}
\end{array}
\right]\ \rightarrow\ 
\left\{
\begin{array}{c}
x_3 = \frac{b_3^{(k)}}{a_{33}^{(k)}},\ a_{33}^{(k)} \neq 0\\\\
x_2 = \frac{b_2^{(k)}-a_{23}^{(k)}.x_3}{a_{22}^{(k)}},\ a_{22}^{(k)} \neq 0\\\\
x_1 = \frac{b_1^{(k)}-a_{12}^{(k)}.x_2-a_{13}^{(k)}.x_3}{a_{11}^{(k)}},\ a_{11}^{(k)} \neq 0\\\\
\end{array}
\right.
$$

Vejamos um exemplo numérico de como funciona a Eliminação Gaussiana.

# matriz
M = np.array([[1.0,1.5,-2.0],[2.0,1.0,-1.0],[3.0,-1.0,2.0]])
print(M)

# zeramento da segunda linha 
m1 = M[1,0]/M[0,0]
M[1,:] += - m1*M[0,:]
print(M)

# zeramento da terceira linha
m2 = M[2,0]/M[0,0]
M[2,:] += - m2*M[0,:]
print(M)

# eliminação
M = np.array([[1.0,1.5,-2.0],[2.0,1.0,-1.0],[3.0,-1.0,2.0]])
b = np.array([-2,3,1])

m,n = M.shape
for i in range(m):
    for j in range(i+1,n):
        pivo = M[j,i]/M[i,i]                        
        for k in range(m):
            M[j,k] += -pivo*M[i,k]

print(M)            

# função simples para eliminação
def eliminacao(M):
    m,n = M.shape
    for i in range(m):
        for j in range(i+1,n):
            pivo = M[j,i]/M[i,i]                        
            for k in range(m):
                M[j,k] += -pivo*M[i,k]
    return M

# matriz randômica 5x5
M2 = np.random.rand(5,5)
print(eliminacao(M2))

## Condicionamento

Vamos ver como pequenas "perturbações" em matrizes podem provocar mudanças drásticas 
nas soluções de sistemas. Isto ocorre quando temos um problema *mal condicionado*.

A1 = np.array([[1,2],[1.1,2]])
b1 = np.array([10,10.4])
print('matriz')
print(A1)
print('vetor')
print(b1)

# solução do sistema A1x1 = b1
x1 = linalg.solve(A1,b1)
print(x1)

d = 0.045
A2 = np.array([[1,2],[1.1-d,2]])
b2 = np.array([10,10.4])
print('matriz')
print(A2)
print('vetor')
print(b2)

# solução do sistema perturbado A2x1 = b2
x2 = linalg.solve(A2,b2)
print(x2)

A solução muda drasticamente aqui! Isto se deve à quase dependência linear em que a matriz se encontra. Ou seja, $\det({\bf A}_2) \approx 0$.

print(linalg.det(A1),linalg.det(A2))

linalg.norm(A)*linalg.norm(linalg.inv(A))

## Método de Gauss-Jordan

O método de Gauss-Jordan é uma variação da eliminação de Gauss, em que não apenas as entradas da porção inferior da matriz plena do sistema são anuladas, mas também as entradas da porção superior, resultando em uma matriz diagonal. 

Além disso, todas as linhas são normalizadas através da sua divisão pelo respectivo elemento pivô. Por exemplo, $a_{11}$ é o elemento pivô da primeira equação, $a_{22}$ da segunda, e assim por diante). A partir daí, a obtenção dos valores das variáveis é imediata. 

O método é melhor ilustrado no seguinte exemplo.

# Matriz aumentada
AB = np.array([[3. , -0.1, -0.2, 7.85], [0.1, 7., -0.3, -19.3], [0.3, -0.2, 10., 71.4]])
print(AB)

# Normalização da 1a. linha
AB[0,:] /= AB[0,0] # L1 <- L1/a11
print(AB)

# Eliminação de x1 da 2a. e 3a. linhas
m1 = AB[1,0]
AB[1,:] -= m1*AB[0,:] # L2 <- L2 - m1*L1
m2 = AB[2,0]
AB[2,:] -= m2*AB[0,:] # L3 <- L3 - m2*L1
print(AB)

# Normalização da 2a. linha
AB[1,:] /= AB[1,1] # L2 <- L2/a22
print(AB)

# Eliminação de x2 da 1a. e 3a. linhas
m3 = AB[0,1]
AB[0,:] -= m3*AB[1,:] # L1 <- L1 - m3*L2  
m4 = AB[2,1]
AB[2,:] -= m4*AB[1,:] # L3 <- L3 - m4*L2 
print(AB)

# Normalização da 3a. linha
AB[2,:] /= AB[2,2] # L3 <- L3/a33
print(AB)

# Eliminação de x3 da 1a. e 2a. linhas
m5 = AB[0,2]
AB[0,:] -= m5*AB[2,:] # L1 <- L1 - m5*L3
m6 = AB[1,2]
AB[1,:] -= m6*AB[2,:] # L2 <- L2 - m5*L3
print(AB)

Do último resultado, vemos que a matriz identidade é obtida, apontando para o vetor solução $[3 \ \ -2.5 \ \ 7]^T$.

## Notas

Para aqueles acostumados com a notação para matrizes do Matlab, o método `np.mat` pode ajudar. No exemplo a seguir, as linhas da matriz são passadas como uma expressão do tipo `str` e separadas com `;`.

# cria matriz
np.array(np.mat('1 2; 3 4'))

np.array(np.mat('1 2 3'))

## Tarefa

Implemente o algoritmo pleno para a eliminação gaussiana. Verifique exceções (erros que devem ser observados para evitar falhas no algoritmo, tal como pivôs nulos e matrizes singulares, por exemplo) e use o seu método para resolver os sistemas lineares da forma ${\bf A}{\bf x} = {\bf b}$ da lista de exercícios.

from IPython.core.display import HTML

def css_styling():
    styles = open("styles/custom.css", "r").read()
    return HTML(styles)
css_styling();