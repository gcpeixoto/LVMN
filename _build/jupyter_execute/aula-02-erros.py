#!/usr/bin/env python
# coding: utf-8

# # Erros e seus efeitos
# 
# Diferentemente da infindável capacidade humana para raciocinar, imaginar e criar, computadores, como máquinas de calcular, são limitados em memória e em habilidades aritméticas. Diante disso, pelo menos três situações simplificadoras ocorrem:
# 
# - o contínuo torna-se _discreto_;
# - o infinito reduz-se ao _finito_ e 
# - a exatidão limita-se à _aproximação_.
# 
# Algumas idéias impactadas por essas simplificações, por sua vez, tornam-se inadmissíveis em sentido estrito. Por exemplo:
# 
# - números reais convertem-se em números aproximados;
# - limites são exibidos através de sequências;
# - derivadas são aproximadas por quocientes de diferenças finitas;
# - integrais definidas são calculáveis por meio de somas finitas.
# 
# Por isso é comum chamar o processo de transferência de cálculos contínuos para cômputos discretos de _discretização_. 
# 
# Quando tratamos da resolução numérica de problemas realistas formulados com auxílio da Matemática, qual seja o campo do conhecimento, é quase impossível desviar-se do _erro_. Erros subsistem em qualquer formulação que tente explicar o funcionamento exato de um fenômeno, em geral, estudado pelas ciências naturais.
# 
# De forma abstrata, se um fenômeno físico $\mathcal{F}$ pode ser descrito por um modelo matemático $\mathcal{M}$ cuja solução exata é $\mathcal{S}$, a impossibilidade de obtê-la
# sugere pelo menos uma solução aproximada $\mathcal{S}'$, tal que $\mathcal{S} = \mathcal{S}' + \mathcal{E}$. Então, diremos que $\mathcal{E}$ é o _erro_. De outro modo, $\mathcal{E} = \mathcal{S} - \mathcal{S}'$.
# 
# Neste capítulo, estudaremos as diversas formas assumidas por $\mathcal{E}$ quando $\mathcal{S}'$ é implementável por meio de métodos numéricos. Evidentemente, pode haver mais de uma forma de obter $\mathcal{S}'$. Além disso, em situações difícies, é preciso estabelecer, com rigor, se $\mathcal{S}$ existe e se é única. Todavia, não discutiremos os procedimentos teóricos de verificação em profundidade.

# ## Motivação

# Como forma de demonstrar que cômputos podem ter resultados distintos, consideremos a somatória (descendente, da maior para a menor parcela)
# 
# $$S_D(n) = \sum_{k=1}^n \frac{1}{k} = 1 + \frac{1}{2} + \ldots + \frac{1}{n-1} + \frac{1}{n},$$
# 
# e a sua versão escrita de forma "refletida" (ascendente, da menor para a maior parcela), ou seja,
# 
# $$S_A(n) = \sum_{k=n}^1 \frac{1}{k} = \frac{1}{n} + 1 + \frac{1}{n-1} + \ldots + \frac{1}{2} + 1.$$
# 
# É evidente que $S_A(n)$ e $S_D(n)$ são matematicamente equivalentes e devem produzir o mesmo resultado independentemente de $n$ e do sentido em que forem somadas. Porém, vejamos o que acontece ao programarmos uma pequena função para computar ambas as formas.

# In[1]:


from prettytable import PrettyTable as pt

# define séries
def S(n):
    
    S_D = 0
    for k in range(1,n+1):
        S_D += 1/k        
         
    S_A = 0
    for k in range(n,0,-1):
        S_A += 1/k       
    
    # diferença    
    E = S_D - S_A
    
    return S_D, S_A, E
    
# cria objeto para tabela
tbl = pt()
tbl.field_names = ['n','S_A(n)','S_D(n)','S_D(n) - S_A(n)']
tbl.align = 'c'

# loop de teste
for n in [10**1, 10**2, 10**3, 10**4, 10**5]:
    sd, sa, e = S(n)    
    row = [n,sd,sa,e]
    tbl.add_row(row)
   
# imprime tabela
print(tbl)


# Como se percebe pela última coluna, os valores produzidos pelas somas para $n > 10$ não são exatamente iguais. Embora exista diferenças ínfimas nos resultados, elas não são zero, assim indicando que a maneira como computamos expressões matemáticas cujos resultados são idênticos pode levar a resultados distintos. 
# 
# O fato de $S_A(n) - S_D(n) > 0$ caracteriza um "erro" de magnitude $\epsilon$, visto que, se $S_A(n)$ fosse tomado como o valor exato, $S_D(n) = S_A(n) + \epsilon$ seria uma aproximação para $S_A(n)$. Inversamente, se $S_D(n)$ fosse tomado como o valor exato, $S_A(n) = S_D(n) + \epsilon$ seria uma aproximação para $S_D(n)$.

# 
# Naturalmente, se tomássemos a versão _infinita_ de $S_D$ (ou $S_A$), chamando-a apenas de $S$ e substituindo $n$ por $\infty$, isto é, 
# 
# $$S = \sum_{k=1}^{\infty} \frac{1}{k},$$
# 
# tanto $S_D(n)$ e $S_A(n)$ seriam consideradas _aproximações_ para $S$. 
# 
# Supondo que somente $S_D(n)$ é a forma correta de "chegar perto" de $S$, a implicação
# 
# $$S = S_D(n) + \epsilon_n \Rightarrow \epsilon_n = S - S_D(n)$$
# 
# revelaria o acréscimo $\epsilon_n$ como uma quantidade não-nula coexistindo com o valor finito $n$. Uma vez que computadores são incapazes de calcular somas infinitas por limitação de memória, $\epsilon_n$ define um tipo de _erro_. Este erro é inerente ao processo de cálculo aproximado de séries infinitas. Além disso, ele dependerá de $n$, ou seja, da quantidade de termos utilizados na soma $S_D$ para aproximar o real valor de $S$.
# 
# Entretanto, estamos ainda diante de um problema de difícil tratamento, visto que a soma $S$ só pode ser obtida aproximadamente, pois $\sum_{k=1}^{\infty} \frac{1}{k}$ não é convergente. Logo, é impossível estabelecer um valor "exato" para $S$, a fim de compará-lo com suas aproximações. Caso intentássemos medir discrepâncias no cálculo desta série, teríamos que adotar um valor já aproximado para cumprir o papel de exato e utilizar outros valores também aproximados como "aproximações de uma aproximação". Embora pareça estranho e paradoxal, o que acontece em muitas situações práticas quando lidamos com um _processo iterativo_ ou de _aproximações sucessivas_ é justamente isso.
# 
# Vamos tomar os valores da tabela de $S_D(n)$. Suponhamos que $S_D(100000) = 12.090146129863408$ assumisse o papel de valor "exato" de $S$. Fosse este o caso, poderíamos calcular pelo menos quatro erros:
# 
# $$E_{10000} = S_D(100000) - S_D(10000) = 2.3025400938190224$$
# $$E_{1000} = S_D(100000) - S_D(1000) = 4.604675269313067$$
# $$E_{100} = S_D(100000) - S_D(100) = 6.902768612223786$$
# $$E_{10} = S_D(100000) - S_D(10) = 9.161177875895154$$
# 
# Para obter cada valor acima, poderíamos escrever:

# In[25]:


# O valor de S_D(n) está na entrada (i,2) da tabela, para i = 0,1,2,3,4.
# Em Python, cada um é acessível por indexação na forma [i][2]

E_100000 = tbl.rows[4][2]           # i = 4
E_10000 = E_100000 - tbl.rows[3][2] # i = 3
E_1000 = E_100000 - tbl.rows[2][2]  # i = 2
E_100 = E_100000 - tbl.rows[1][2]   # i = 1
E_10 = E_100000 - tbl.rows[0][2]    # i = 0

# Impressão de valores
print(E_100000)
print(E_10000)
print(E_1000)
print(E_100)
print(E_10)


# Não é difícil ver que o valor de $E$ em relação a $S_D(100000)$ aumenta quando tomamos valores de $n$ cada vez menores. Em outras palavras, nossas aproximações de um valor supostamente exato (aproximado) tornam-se cada vez mais pobres quando não dispomos de parcelas suficientes para somar. Além disso, usar $S_D(100000)$ como ponto de referência não é nada confiável, já que ele apenas fará com que tenhamos uma sensação ilusória de exatidão.

# Se, em vez de uma série divergente, escolhermos outra, convergente, poderemos fazer cálculos de erro tomando como referência um valor definitivamente exato. Então, consideremos a série
# 
# $$S_2 = \sum_{k=1}^{\infty} \frac{1}{k^2}$$
# 
# A série $S_2$ ficou conhecida como [_Problema de Basel_](https://en.wikipedia.org/wiki/Basel_problem), proposto em 1650 pelo matemático italiano Pietro Mengoli, e solucionado por Leonhard Euler em 1734 – _Basel_ é o nome de uma cidade da Suíça, onde Euler nasceu. Graças a Euler e a teoria matemática operante nos bastidores, existe certeza suficiente de que $S_2 = \frac{\pi^2}{6}$.
# 
# Do mesmo modo como fizemos no caso anterior, geraremos uma nova tabela para valores de $S_2(n)$ com $n$ crescente até o limite de 100.000, até porque não temos como computar $S_2$ _ad infinitum_. Então, vejamos um código similar:

# In[26]:


from math import pi

# define série
def S2(n):
    
    S_2 = 0
    for k in range(1,n+1):
        S_2 += 1/k**2        
             
    # valor exato
    S_2ex = pi**2/6 
    
    # diferença    
    E = S_2ex - S_2
    
    return S_2ex, S_2, E
    
# cria objeto para tabela
tbl2 = pt()
tbl2.field_names = ['n','S_2','S_2(n)','S_2 - S_2(n)']
tbl2.align = 'c'

# loop de teste
for n in [10**1, 10**2, 10**3, 10**4, 10**5]:
    s2, s2n, e = S2(n)    
    row = [n,s2,s2n,e]
    tbl2.add_row(row)
   
# imprime tabela
print(tbl2)


# Neste caso, a diferença existente na última coluna caracteriza, de fato, o _erro real_ entre o valor exato $S_2$ e suas aproximações, de modo que, neste caso,
# 
# $$E_{100000} = \frac{\pi^2}{6} - S_2(100000) = 0.000009999949984074163$$
# $$E_{10000} = \frac{\pi^2}{6} - S_2(10000) = 0.00009999500016122376$$
# $$E_{1000} = \frac{\pi^2}{6} - S_2(1000) = 0.0009995001666649461$$
# $$E_{100} = \frac{\pi^2}{6} - S_2(100) = 0.009950166663334148$$
# $$E_{10} = \frac{\pi^2}{6} - S_2(10) = 0.09516633568168564$$

# A partir daí, notamos que o erro reduz-se a quase zero à medida que o valor de $n$ aumenta, assim dando-nos uma constatação, pelo menos aproximada, de que a soma, de fato, é $\pi^2/6 \approx 1.6449340668482264$. Para obtermos os valores dos erros, um código similar poderia ser implementado:

# In[27]:


# Expressões do erro real
E_100000 = pi**2/6 - tbl2.rows[4][2] # i = 4
E_10000 = pi**2/6 - tbl2.rows[3][2]  # i = 3
E_1000 = pi**2/6 - tbl2.rows[2][2]   # i = 2
E_100 = pi**2/6 - tbl2.rows[1][2]    # i = 1
E_10 = pi**2/6 - tbl2.rows[0][2]     # i = 0

# Impressão
print(E_100000)
print(E_10000)
print(E_1000)
print(E_100)
print(E_10)


# Talvez não tenha sido percebido por você, mas, até aqui, já tratamos, conceitualmente, de três tipificações de erro, a saber:
# 
# 1. _erro de truncamento_, quando limitamos o número de termos de uma expansão infinita, tornando-a finita.
# 2. _erro real aproximado_ (ou _erro verdadeiro aproximado_), quando assumimos que o valor exato da expansão infinita (série divergente) é a soma obtida até a parcela $n$, com $n$ muito grande, mas finito, e calculamos a diferença entre este valor e a soma obtida até uma parcela anterior à $n$-ésima;
# 3. _erro real_ (ou _erro verdadeiro_), quando calculamos a diferença entre a soma exata (série convergente) e a soma obtida até a parcela $n$.

# Curioso, não? E não para por aí! Ainda há outras definições de erro. Veremos mais algumas no decorrer do curso.

# ## Tipos de erros

# Consideremos avaliar o polinômio $P(x) = 0.172x^3 - 0.878x^2 + 0.042x + 0.583$
# no ponto $x=79.9$.
# 
# Vamos fazer o seguinte:
# 
# 1. Assumir que $82132.957032$ seja o valor exato para o polinômio em $x = 79.9$.
# 2. Calcular $P(79.9)$ utilizando duas formas.

# In[8]:


# Código para gerar polinômio cúbico com raízes reais

from numpy import random
from sympy.abc import x, a, b, c, d
from sympy import roots, lambdify

# Semente aleatória
random.seed(1)

# Um polinômio do terceiro grau terá as 3 raízes reais e distintas
# se o discriminante for > 0. Aqui, criamos um polinômio que 
# satisfaz tais condições por busca aleatória
Delta = -1
a,b,c,d = 0,0,0,0
while Delta <= 0:
    A,B,C,D = random.randn(1,4)[0,:]
    Delta = -27*A**2*D**2 + 18*A*B*C*D -4*A*C**3 - 4*B**3*D + B**2*C**2
    a,b,c,d = A,B,C,D
    
# Polinômio cúbico simbólico
P3 = a*x**3 + b*x**2 + c*x + d

# Polinômio cúbico numérico
P3n = lambdify(x,P3,'numpy')

# Raízes simbólicas
r = list(roots(P3,x).keys())
r1 = r[0]
r2 = r[1]
r3 = r[2]

# Raízes numéricas com os valores encontrados
r1n = r1.subs({'a':a, 'b':b, 'c':c, 'd': d}).evalf(10)
r2n = r2.subs({'a':a, 'b':b, 'c':c, 'd': d}).evalf(10)
r3n = r3.subs({'a':a, 'b':b, 'c':c, 'd': d}).evalf(10)

#print(P3)
#P3_ex = 0.172428207550436*x**3 - 0.877858417921372*x**2 + 0.0422137467155928*x + 0.582815213715822


# In[9]:


# Valor
x = 79.9

# Forma padrão
Px = 0.172*x**3 - 0.878*x**2 + 0.042*x + 0.583

# Forma estruturada (Hörner)
PHx = x*(x*(0.172*x - 0.878) + 0.042) + 0.583 

# Impressão
print(f'P({x}) = {Px:.14f}')
print(f'PH({x}) = {PHx:.14f}')
    


# Como se vê, a partir da 7a. casa decimal, começamos a notar uma leve diferença do valor do polinômio, embora ambas as formas, padrão de Hörner (estruturada), sejam matematicamente equivalentes. Embora os valores sejam próximos, a forma estruturada é uma opção menos _custosa_, sob o ponto de vista computacional, visto que ela possui menos avaliações de operações aritméticas.
# 
# A forma polinomial padrão, escrita de maneira ampliada, resulta em 
# 
# $$P(x) = 0.172{\color{red}.}x{\color{red}.}x{\color{red}.}x {\color{blue}-} 0.878{\color{red}.}x{\color{red}.}x {\color{blue}+} 0.042{\color{red}.}x {\color{blue}+} 0.583,$$
# 
# ao passo que a forma de Hörner é escrita como:
# 
# $$P_H(x) = x{\color{red}.}(x{\color{red}.}(0.172{\color{red}.}x {\color{blue}-} 0.878) {\color{blue}+} 0.042) {\color{blue}+} 0.583$$
# 
# Qual é a diferença entre ambas? O número de multiplicações (vermelho) e adições/subtrações (azul) é diferente. Enquanto na forma $P(x)$, temos 6 multiplicações e 3 adições/subtrações, a forma $P_H(x)$ reduz as operações para 3 multiplicações e 3 adições/subtrações. Isso é o mesmo que dizer que o número de operações aritméticas de multiplicação foi reduzido em 50%!
# 
# A conclusão é: a avaliação de polinômios pela forma de Hörner é mais lucrativa e propensa a um erro menor.

# ### Erro real

# O erro real (ou verdadeiro), $E$, não sinalizado, entre o valor 
# exato $x$ e o aproximado $\hat{x}$ é dado por:
# 
# $$E = \hat{x} - x.$$
# 
# Note que, por convenção, se $E > 0$, erramos por superestimação ("excesso"). Por outro lado, se $E < 0$, erramos por subestimação ("omissão").
# 
# Calculamos o erro real operando com diferença simples. 
# 
# Utilizando o exemplo da seção anterior, temos:

# In[10]:


# Valor exato
Px_ex = 82132.957032

# Erro real (forma padrão)
E_P = Px - Px_ex
print(E_P)

# Erro real (forma de Hörner)
E_PH = PHx - Px_ex
print(E_PH)


# ### Erro absoluto
# 
# O erro absoluto, $EA$, é a versão sinalizada de $E$. Dado por
# 
# $$EA = | \hat{x} - x |,$$
# 
# ele ignora a condição de subestimação ou superestimação e se atém à diferença absoluta entre o valor exato e o valor aproximado.
# 
# A função módulo, $f(x) = | x |$, pode ser diretamente calculada com `abs`.

# In[11]:


# Erro absoluto (forma padrão)
EA_P = abs(Px - Px_ex)
print(EA_P)

# Erro absoluto (forma de Hörner)
EA_PH = abs(PHx - Px_ex)
print(EA_PH)


# É evidente que $E_{PH} > E_P$. Entretanto, podemos verificar isso pelo seguinte teste lógico:

# In[32]:


# O teste é verdadeiro
EA_PH > EA_P


# ### Erro relativo
# 
# O erro relativo, $ER$, aperfeiçoa a idea de erro absoluto a partir do momento que passa a considerar a ordem de grandeza das quantidades envolvidas, mensurando uma variação que se limita ao valor exato. Assim,
# 
# $$ER = \dfrac{ | \hat{x} - x | }{|x|} = \dfrac{ EA }{|x|} = 1 - 
# \dfrac{ |\hat{x}| }{|x|}.$$

# Os erros relativos podem ser computados como:

# In[16]:


ER_P = EA_P/abs(Px_ex)
print(ER_P)

ER_PH = EA_PH/abs(Px_ex)
print(ER_PH)


# ### Erro relativo percentual
# 
# O erro relativo percentual é outra forma útil de expressar a disparidade relativa entre valores. Ele é definido por:
# 
# $$ER_{\%} = ER \times 100\% = \left(1 - 
# \dfrac{ |\hat{x}| }{|x|} \right) \times 100\%.$$
# 
# Como não temos uma forma explícita de percentual, por cálculo, o melhor a fazer é algo como:

# In[23]:


ER_Pp = ER_P * 100
print(f'{ER_Pp:e} %')

ER_PHp = ER_PH * 100
print(f'{ER_PHp:e} %')


# ### Erro relativo aproximado (_benchmark_)
# 
# Como vimos no exemplo motivacional deste capítulo, há casos (a maioria deles) em que não dispomos de valores exatos (obtidos por soluções analíticas, por exemplo), sendo possível estimar erros relativos apenas aproximadamente usando um _valor de referência_. Costuma-se chamar este valor de _benchmark_. Definido o _benchmark_ por $x'$, o _erro relativo aproximado_ é dado:
#  
# $$ER' = \dfrac{ | \hat{x} - x' | }{|x'|} = \dfrac{ EA }{|x'|} = 1 - 
# \dfrac{ |\hat{x}| }{|x'|}.$$
# 
# 
# No exemplo da avaliação dos polinômios, se não dispuséssemos do valor exato, ou $P(x=79.9)$ ou $P_H(x=79.9)$ deveria ser adotado como _benchmark_. Se optássemos pelo segundo, apenas um erro relativo aproximado poderia ser calculado, a saber:

# In[35]:


ER_ =  abs(PHx - Px)/abs(PHx)
print(f'{ER_:e}')


# ### Erro relativo aproximado percentual
# 
# O erro relativo aproximado percentual é, meramente, a versão percentual do erro relativo aproximado, logo, dado por
# 
# $$ER'_{\%} = ER' \times 100 \%.$$

# ### Erro de cancelamento
# 
# O erro de cancelamento ocorre quando números de grandezas próximas são subtraídos. Como exemplo de situação crítica, induzimos uma divisão por zero usando o valor do épsilon de máquina $\epsilon_M$ ao fazer 
# 
# $$\dfrac{1}{(1 + 0.25\epsilon_M) - 1}.$$
# 
# Isto ocorre porque o denominador sofre um _cancelamento subtrativo_ Uma vez que $0.25\epsilon_M < \epsilon_M$, a operação $0.25\epsilon_M$ não produz efeito sobre 1, de modo que a computação encontra um "limbo". Para a matemática exata, a operação deveria ser "diferente de zero".

# In[24]:


# inf
from numpy import finfo
from warnings import filterwarnings; 
filterwarnings("ignore")

e = finfo(float).eps
1/(1 + 0.25*e - 1)


# ### Erros de truncamento e de arredondamento
# 
# O erro de truncamento está relacionado ao "corte" abrupto de dígitos de precisão em um valor numérico ou de parcelas em uma expansão infinita. No início do capítulo, exemplificamos como uma série pode ser aproximada truncando um ou mais termos de sua expansão. 
# 
# No caso de números, o truncamento ocorre quando se ignora o valor da $k+1$-ésima casa decimal para finalidades de aproximação até a $k$-ésima casa. Por exemplo, se $x = 13.4256$, a aproximação de $x$ por truncamento até a terceira casa seria $x = 13.425$. O dígito 6 é ignorado nos cálculos. 
# 
# No caso do arredondamento, o $k$-ésimo dígito é somado de 1 se o dígito da $k+1$-ésima casa for maior ou igual a 5. A aproximação de $x$ por arredondamento até a terceira casa seria $x = 13.426$, visto que o dígito 6 é maior do que 5. A regra de arredondamento é a que usamos no cotidiano.

# ## Exemplo aplicado: erros pontuais na função de Airy
# 
# A função de Airy é solução da equação de Schrödinger da mecânica quântica. Ela muda o seu comportamento de oscilatório para exponencial. A fim de demonstrar como o erro é uma função, dependente do ponto onde é avaliado, criaremos uma simulação.
# 
# Criaremos uma função "perturbada" que desempenhará o papel de função de Airy aproximada, enquanto menteremos a função de Airy verdadeira como exata. Em seguida, criaremos outra função de utilidade para calcular diretamente o erro relativo pontual.
# 

# In[37]:


from scipy import special
import numpy as np

# Eixo das abscissas
x = np.linspace(-10, -2, 100)

# Funções de Airy e suas derivadas (solução exata)
A, aip, bi, bip = special.airy(x)

# Função de Airy perturbada
A_ = 1.152*A + 0.056*np.cos(x) 


# Podemos usar o conceito de _função anônima_ (`lambda`) para calcular diretamente o erro relativo percentual para cada ponto $x$. Assim, seja:
# 
# $$ER_{\text{Airy}}(x) = \frac{\mid \ \hat{A}(x) - A(x) \ \mid}{\mid \ A(x) \ \mid},$$
# 
# onde $\hat{A}(x)$ é a função de Airy aproximada e $A(x)$ é a função de Airy exata. Então:

# In[38]:


# Define função anônima para erro relativo
ai = lambda f,f_: (abs(f_ - f)/abs(f))*100

# calcula erro relativo para função de Airy e sua aproximação
E_airy = ai(A,A_)


# A seguir, mostramos a plotagem das funções exatas e aproximadas, bem como do erro relativo pontual.

# In[39]:


# Plotagem das funções 
from matplotlib.pyplot import plot, grid, legend

plot(x, A, 'k', label='Airy exata')
plot(x, A_, 'r', label='Airy aprox.')
grid()
legend(loc='upper right');


# In[40]:


# Plotagem do erro 
plot(x, E_airy)
grid()


# ## Definições de erro em aprendizagem de máquina
# 
# No século XXI, muito se tem falado em aprendizagem de máquina, inteligência artificial e dados. Diversas definições de erro também existem neste contexto, quando o interesse é medir erros em conjuntos de dados. Por exemplo, no campo das redes neurais convolucionais, o cálculo da função de _perda_ (_loss function_) entre pixels de uma imagem legendada como _ground truth_ (gabarito) e de outra imagem processada, é geralmente realizado por meio de expressões que caracterizam erros. A seguir, exploraremos algumas dessas métricas. Em todos os cálculos, $y_i$ é o valor do gabarito (exato), $\hat{y_i}$ é o valor aproximado e $n$ é o número de pontos de amostragem.

# ### Erro quadrático médio
# 
# O erro quadrático médio (_mean squared error_, MSE) é definido como:
# 
# $$MSE = \dfrac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$

# ### Erro absoluto médio
# 
# O erro absoluto médio (_mean absolute error_, MAE) é definido como:
# 
# $$MAE = \dfrac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$

# ### Erro absoluto médio percentual
# 
# O erro absoluto médio percentual (_mean absolute percentage error_, MAPE) é definido como:
# 
# $$MAPE = \dfrac{1}{n}\sum_{i=1}^n \dfrac { |y_i - \hat{y}_i| }{ | y_i | } \times 100$$

# ### Erro logarítmico quadrático médio 
# 
# O erro logarítmico quadrático médio (_mean squared logarithmic error_, MSLE) é definido como:
# 
# $$MSLE = \dfrac{1}{n}\sum_{i=1}^n [ \log(1+ y_i) - \log(1 + \hat{y}_i) ]^2$$

# ```{admonition} Curiosidade
# :class: dropdown
# 
# Nos últimos anos, métodos de aprendizagem profunda vem sendo aplicados à identificação automatizada de corpos salinos em imagens sísmicas tanto para finalidades de exploração de combustíveis fósseis, como também para armazenamento geológico de carbono. Em aplicações dessa natureza, o gabarito, em geral, é uma imagem interpretada por um geólogo profissional. Algoritmos de classificação, por sua vez, tentam delinear a mesma estrutura geológica obtida pelo humano baseando-se em métricas formuladas a partir de definições de erro como as que estudamos nesta seção. Para saber mais, veja o artigo [Identification of Salt Deposits on Seismic Images Using Deep Learning Method for Semantic Segmentation](https://www.mdpi.com/2220-9964/9/1/24).
# ```
