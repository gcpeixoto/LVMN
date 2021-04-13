# Fatoração LU com Python

## Decomposição LU

Suponha o sistema de equações

$$AX = B$$

A motivação para a decomposição LU baseia-se na observação de que sistemas triangulares são mais fáceis de resolver. Semelhantemente à Eliminação Gaussiana, a decomposição LU (que, na verdade, é uma segunda abordagem da própria Eliminação Gaussiana), explora a ideia de "fatoração" de matrizes, em que a matriz original do sistema é fatorada ("quebrada") como

$$A = LU,$$

onde $L$ é uma matriz triangular inferior e $U$ é triangular superior. Nosso objetivo é determinar $L$ e $U$, de maneira que o vetor $X$ seja obtido através da resolução de um par de sistemas cujas matrizes são triangulares.

### Exemplo

Consideraremos que as matrizes triangulares inferiores $L$ sempre terão a sua diagonal principal formada por entradas iguais a 1. Este tipo de fatoração é conhecido como _Fatoração de Doolittle_.

$${\bf A} = \begin{bmatrix}
1 & 2 & 4\\
3 & 8 & 14\\
2 & 6 & 13
\end{bmatrix} = LU$$
onde

$${\bf L} = \begin{bmatrix}
1 & 0 & 0\\
L_{21} & 1 & 0\\
L_{31} & L_{32} & 1
\end{bmatrix}
\quad \text{e} \quad
{\bf U} = \begin{bmatrix}
U_{11} & U_{12} & U_{13}\\
0 & U_{22} & U_{23}\\
0 & 0 & U_{33}
\end{bmatrix}
$$

Multiplicando $LU$ e definindo a resposta igual a $A$ temos:

$$\begin{bmatrix}
U_{11} & U_{12} & U_{13}\\
L_{21} U_{11} & L_{21} U_{12} + U_{22} & L_{21} U_{13} + U_{23}\\
L_{31} U_{11} & L_{31} U_{12} + L_{32} U_{22} & L_{31} U_{13} + L_{32} U_{23} + U_{33}
\end{bmatrix} = \begin{bmatrix}
1 & 2 & 4\\
3 & 8 & 14\\
2 & 6 & 13
\end{bmatrix}
$$

Agora, através de substituição de recorrência, facilmente encontramos $L$ e $U$.

$$
{\bf A} = \begin{bmatrix}
1 & 2 & 4\\
3 & 8 & 14\\
2 & 6 & 13
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 0\\
3 & 1 & 0\\
2 & 1 & 1
\end{bmatrix} \begin{bmatrix}
1 & 2 & 4\\
0 & 2 & 2\\
0 & 0 & 3
\end{bmatrix}
$$

## Usando a decomposição LU para resolver sistemas de equações

Uma vez decomposta a matriz $A$ no produto $LU$, podemos obter a solução $X$ de forma direta. O procedimento, equivalente à substituição de recorrência mencionada anteriormente, pode ser resumido como segue: dada $A$, encontre $L$ e $U$ tal que $A = LU$, ou seja, $(LU)X = B$. Em outras palavras:

- Defina $Y = UX$.
- Resolva o sistema triangular $LY = B$ para $Y$.
- Finalmente, resolva o sistema triangular $UX = Y$ para $X$.

O benefício desta abordagem é a resolução de somente sistemas triangulares. Por outro lado, o custo empregado é termos de resolver dois sistemas.

### Exemplo

Encontre a solução $X = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ do sistema 

$$
\begin{bmatrix} 
1 & 2 & 4\\ 
3 & 8 & 14\\ 
2 & 6 & 13 
\end{bmatrix} 
\begin{bmatrix} 
x_1 \\ x_2 \\ x_3 
\end{bmatrix} 
= 
\begin{bmatrix} 
3 \\ 13 \\ 4
\end{bmatrix}.
$$

- As matrizes $L$ e $U$ já foram obtidas anteriormente.

$$L = \begin{bmatrix}
1 & 0 & 0\\
3 & 1 & 0\\
2 & 1 & 1
\end{bmatrix},
\quad 
U = \begin{bmatrix}
1 & 2 & 4\\
0 & 2 & 2\\
0 & 0 & 3
\end{bmatrix}$$

- A próxima etapa é resolver $LY = B$, para o vetor $Y = \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix}$.

$$LY = \begin{bmatrix}
1 & 0 & 0\\
3 & 1 & 0\\
2 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix} =
\begin{bmatrix}
3 \\ 13 \\ 4
\end{bmatrix} = B$$

Este sistema pode ser resolvido por substituição direta, obtendo $Y = \begin{bmatrix} 3 \\ 4 \\ -6 \end{bmatrix}$.

- Agora que encontramos $Y$, concluímos o procedimento resolvendo $UX = Y$ para $X$. Ou seja, resolvemos:

$$
UX = \begin{bmatrix}
1 & 2 & 4\\
0 & 2 & 2\\
0 & 0 & 3
\end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = 
\begin{bmatrix} 3 \\ 4 \\ -6 \end{bmatrix}
$$

Realizando a substituição regressiva (baixo para cima; da direita para a esquerda), obtemos a solução do problema.

$$X = \begin{bmatrix} 3 \\ 4 \\ -2 \end{bmatrix}$$

Abaixo, temos uma implementação de uma fatoração LU sem pivoteamento. 

import numpy as np 

def lu_nopivot(A):
    '''
    Realiza fatoração LU para a matriz A
    
    entrada: 
        A  -  matriz:  array (nxn) 
    
    saida: 
        L,U  - matriz triangular inferior, superior : array (nxn)         
    '''
        
    n = np.shape(A)[0] # dimensao
    L = np.eye(n) # auxiliar 
    
    for k in np.arange(n):
        L[k+1:n,k] = A[k+1:n,k]/A[k,k]        
        for l in np.arange(k+1,n):
            A[l,:] = A[l,:] - np.dot(L[l,k],A[k,:])
            
    U = A
    return (L,U)

**Exemplo:** Fatoração $\bf{ LU }$ da matriz 

$${\bf A} =
\begin{bmatrix}
4 & -2 & -3 &  6 \\  
1 &  4 &  2 &  3 \\
2 & -3 &  3 & -2 \\ 
1 &  5 &  3 &  4
\end{bmatrix}$$

A = np.array([[ 4., -2., -3.,  6.],[ 1.,  4.,  2.,  3.],[ 2.,  -3.,  3., -2.],[ 1.,  5.,  3.,  4.]])

L,U = lu_nopivot(A)

L

U

from IPython.core.display import HTML

def css_styling():
    styles = open("styles/custom.css", "r").read()
    return HTML(styles)
css_styling();