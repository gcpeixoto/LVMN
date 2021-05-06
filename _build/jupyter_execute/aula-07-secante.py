# Implementação do método da secante 

%matplotlib inline

# Método da Secante

from numpy import linspace
from matplotlib.pyplot import plot

def secante(xa,xb,f,tol,nmax,var,plotar):

    f = eval('lambda x:' + f)

    # imprime estimativas iniciais
    print('Estimativas iniciais: xa = {0}; xb = {1} \n'.format(xa,xb))  

    # Loop 
    for i in range(0,nmax):
        
        x = (xa*f(xb) - xb*f(xa))/(f(xb) - f(xa))
                        
        e = abs(x-xb)/abs(x) # erro
        
        # tabela
        print('{0:d}  {1:f}  {2:f}  {3:e}'.format(i,x,f(x),e))
        
        if e < tol:
            break
        xa = xb
        xb = x
        
    if i == nmax:
        print('Solução não obtida em {0:d} iterações'.format(nmax))
    else:
        print('Solução obtida: x = {0:.10f}'.format(x))

    # plotagem
    if plotar:        
        delta = 3*x
        dom = linspace(x-delta,x+delta,30)
        plot(dom,f(dom),x,f(x),'ro')

    return x
      
    
# parametros    
xa = 1.0 # estimativa inicial 1
xb = 2.0 # estimativa inicial 2
tol = 1e-3 # tolerancia
nmax = 100 # numero maximo de iteracoes
f = '-0.9*x**2 + 1.7*x + 2.5'   # funcao
var = 'x'
plotar = True

# chamada da função
xm = secante(xa,xb,f,tol,nmax,var,plotar)

## Problema

Determinar a raiz positiva da equação: $f(x) = \sqrt{x} - 5e^{-x}$, pelo método das secantes com erro inferior a $10^{-2}$. 

### Resolução

Para obtermos os valores iniciais $x_0$ e $x_1$ necessários para iniciar o processo iterativo, dividimos a equação original $f(x) = 0$ em outras duas $y_1$ e $y_2$, com $y_1 = \sqrt{x}$ e $y_2(x) = e^{-x}$, que colocadas no mesmo gráfico, produzem uma interseção próximo a $x = 1.5$. Assim, podemos escolher duas estimativas iniciais próximas deste valor. Podemos escolher $x_0 = 1.4$ e $x_1=1.5$.

from numpy import sqrt, exp
from matplotlib.pyplot import plot,legend

fx = lambda x: sqrt(x) - 5*exp(-x) 

x = linspace(0,3,100)
plot(x,fx(x),label='$f(x) = x^{1/2} - 5e^{-x}$');
plot(x,sqrt(x),label='$y_1(x) = x^{1/2}$');
plot(x,5*exp(-x),label='$y_2(x) = 5e^{-x}$');
plot(x,fx(x)*0,'--');
legend();

Vejamos o valor de $f(x=1.5)$.

fx(1.5)

Vamos montar uma função anônima para computar o valor da interseção da secante com o eixo $x$, a saber:

xm = lambda a,b: ( a*fx(b) - b*fx(a) ) / (fx(b) - fx(a) )

Vamos usar os nosso valores estimados: 

x0 = 1.4
x1 = 1.5
x2 = round(xm(x0,x1),3) 
print(x2)

Agora, usamos este novo valor e o anterior.

x3 = round(xm(x1,x2),3)
print(x3)

Calculemos o erro relativo entre as estimativas $x_1$ e $x_2$:

err = lambda a,b: abs(a - b)/abs(a)
e1 = err(x2,x1)
print(round(e1,3))
print("{0:e}".format(e1))

Agora, calculemos o erro relativo entre as estimativas $x_2$ e $x_3$:

e2 = err(x3,x2)
print(round(e2,3))
print("{0:e}".format(e2))

O erro está diminuindo. Além disso, o valor da raiz está se estabilizando em torno de 1.430. Isto significa que as estimativas iniciais foram muito boas. Com efeito, o uso das interseções proporcionou uma boa escolha.