#!/usr/bin/env python
# coding: utf-8

# # Análise gráfica e aproximações sucessivas
# 
# Saber realizar plotagens básicas para analisar o comportamento de funções-alvo (aquelas para as quais procuramos raízes) é essencial para a compreensão de métodos baseados em aproximações sucessivas.
# 
# ```{figure} figs/ga-ai.png
# ---
# width: 400px
# name: fig-gaai
# ---
# 
# ```
# 
# Neste capítulo, abordaremos os seguintes tópicos: 
# 
# - plotagem básica de funções matemáticas com _matplotlib_;
# - desenvolvimento de software científico;
# - fluxo de controle aplicado a processos iterativos e aproximações sucessivas;

# ## Estudo de caso: o salto do paraquedista
# 
# Faremos a análise gráfica da função do salto do paraquedista já vista anteriormente, isto é: 
# 
# $$v = \dfrac{gm}{c}(1 - e^{-(c/m)t}).$$
# Entretanto, antes de continuarmos, vale tecer breves comentários sobre dimensionalidade.
# 
# ### Variáveis e parâmetros
# 
# Em nosso curso, tratamos da determinação de raízes de equações não-lineares em uma dimensão (1D). Isto significa que apenas uma variável é usada como dependente, embora a variável dependente possa requerer depender de outras quantidades para ser computada. No caso da função $v$ acima, o tempo$t$está sendo tomado como a única variável independente, ao passo que a aceleração da gravidade$g$, a massa$m$e o coeficiente de arrasto$c$tornam-se _parâmetros_. 
# 
# Aplicando-se uma notação matemática estendida, poderíamos escrever 
# 
# $$v = f({\color{red}t};{\color{blue}g},{\color{blue}m},{\color{blue}c}),$$
# 
# onde destacamos a variável independente em vermelho e os parâmetros em azul, após o ponto-e-vírgula. Entretanto, qualquer um dos parâmetros poderia ser analisado sob o ponto de vista de variável, assumindo-se as outras quantidades como parâmetros. Para este mesmo exemplo, se quiséssemos estudar a dependência de $v$ por variação de$g$, teríamos de manter $m$, $c$ e $t$ _fixados_, obtendo uma forma tal que
# 
# $$v = f({\color{red}g};{\color{blue}m},{\color{blue}c},{\color{blue}t}).$$
# 
# Se o mesmo raciocínio for utilizado para$c$, a forma 
# 
# $$v = f({\color{red}c};{\color{blue}t},{\color{blue}g},{\color{blue}m})$$
# 
# indicaria que$c$é a variável independente, enquanto $t$, $g$ e $m$ seriam parâmetros com um valor fixado e conhecido.
# 
# Assim, por indução, a busca por raízes de equações não-lineares que dependam de$n$variáveis em apenas uma dimensão deve considerar _uma variável independente com valor mutável_ e $n-1$ _parâmetros com valor fixado_. Usando o Cálculo a várias variáveis, se 
# 
# $$
# f: \mathbb{R}^n \to \mathbb{R} \\
# (x_1,x_2,\ldots,x_n) \mapsto y
# $$
# 
# é a função não-linear a ser estudada, a forma
# 
# $$y = f({\color{red}x_k}; {\color{blue}x_1},{\color{blue}x_2},\ldots,{\color{blue}x_{k-1}},{\color{blue}x_{k+1}},\ldots,{\color{blue}x_{n-1}},{\color{blue}x_n})$$
# 
# significaria que a análise é _unidimensional_ sobre a variável$x_k$nos parâmetros$x_1$a$x_n$, excluindo-se$x_k$.
# 
# Para o nosso exemplo, $n=4$, $y = v$, a variável independente $x_k$ é o coeficiente de arrasto $c$ – note que $k$ pode ser qualquer valor entre 1 e 4 –, $f$ é a expressão matemática $\dfrac{gm}{c}(1 - e^{-(c/m)t})$ e os demais símbolos $x_j$, para $j \neq k$, são os parâmetros.
# 
# A visualização de "cortes" paralelos aos eixos coordenados que resultam da fixação de uma variável (tornando-se parâmetro) e da liberação de outra para um caso em que $f$ é bivariada está disponível abaixo. Ao interagir com a representação visual somos capazes de reconhecer que $f(x_1,x_2)$ recai em uma função univariada se a variável $x_1$ ou $x_2$ for fixada – de modo exclusivo – , assim podendo ser estudada pelas ferramentas aprendidas neste curso.

# In[1]:


from plotly.offline import plot
from IPython.display import display, HTML
import plotly.graph_objects as go
import numpy as np

# Define the function f(x, y) (you can replace this with your own function)
def f(x, y):
    return np.sin(x) + np.cos(y)

# Generate data for the function surface plot
x_values = np.linspace(-2, 0, 100)
y_values = np.linspace(0, 5, 100)
x_mesh, y_mesh = np.meshgrid(x_values, y_values)
z_values = f(x_mesh, y_mesh)

# Create a surface plot for the function
fig = go.Figure(data=[go.Surface(z=z_values)])

fig.update_traces(showscale=False,
                  hoverinfo='skip',
                  colorscale='Viridis',opacity=0.6)

# Update layout for better presentation
fig.update_layout(    
    template='simple_white',
    title='Análise de função de duas variáveis',
    width=600,
    height=400,
    margin=dict(l=40, r=40, b=40, t=40),
    scene=dict(
        xaxis_title='x1',
        yaxis_title='x2',
        zaxis_title='y',
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            gridcolor='#bdbdbd',
            gridwidth=2,
            zerolinecolor='#969696',
            zerolinewidth=4,
            linecolor='#636363',
            linewidth=6,
            nticks=3,
            tickmode='linear',
            tick0=x_values[0],
            dtick=51),
        yaxis=dict(
            nticks=3,
            tickmode='linear',
            tick0=y_values[0],
            dtick=51)
        
    )
)


# In[2]:


plot(fig, show_link=False,filename='figs/analise-grafica.html')
display(HTML('figs/analise-grafica.html'))


# ### Análise gráfica do coeficiente de arrasto

# Aplicaremos a redução de dimensionalidade proposta anteriormente fixando como parâmetros o tempo $t$, a velocidade $v$, a massa $m$ e a aceleração da gravidade $g$, e permitindo a livre variação do coeficiente de arrasto $c$. A análise gráfica servirá para visualizar o comportamento desta variável e detectar, pelo menos aproximadamente, onde há possíveis raízes. Este processo é conhecido como _localização_. 

# ```{admonition} Dica
# :class: tip, dropdown
# A plotagem básica de funções matemáticas via _matplotlib_ pode ser realizada pela simples chamada de `plt.plot(x,y)`, quando `plt` é o _placeholder_ da biblioteca `pyplot`. As variáveis de código `x` e `y` funcionam como domínio e contradomínio.
# ```

# Vejamos como realizar a plotagem da função $y = f(c; t,v,m,g)$. Observe que, sendo $c$ a única variável e, além disso, a variável independente, podemos, sem prejuízo, escrever $y = f(c)$, ressalvada a fixação dos demais parâmetros. Neste caso, a imagem desta função, $y$, não necessariamente possui um sentido físico e não temos que nos preocupar em interpretar o que ela significa. O importante é identificar se há um ou mais valores de$c$que produzem uma imagem nula. Em caso positivo, teremos encontrado uma ou mais raízes de $f$.
# 
# Em outras palavras, as perguntas que queremos responder são: 
# 
# - Existe algum coeficiente de arrasto que produz o cenário determinado pelos parâmetros? 
# - Se houver, o cenário que se forma é realista? Ele respeita as leis da física?
# 
# Vamos fazer experimentos numéricos e começar com alguns valores iniciais para os parâmetros.

# In[3]:


import numpy as np
import matplotlib.pyplot as plt 

# Parâmetros fixados 
t = 12.0
v = 42.0
m = 70.0
g = 9.81


# In[4]:


# Localização
a,b = 5,20
c = np.linspace(a,b,100)
f = g*m/c*(1 - np.exp(-c/m*t)) - v # f(c) = 0

plt.plot(c,f,'g-',c,c*0,'r--');
plt.xlabel('c')
plt.ylabel('f(c)')
plt.title('Variação do coeficiente de arrasto')
plt.grid(True)


# ### Refinamento
# 
# Observa-se que existe uma raiz para $f(c)$ próxima a $c = 15$. Todavia, é difícil precisar seu valor apenas por observação visual. A fim de buscar melhores aproximações, podemos refinar o gráfico realizando uma espécie de _zoom_ até obter um intervalo adequado para aplicação algorítmica.
# 
# Nos gráficos abaixo, produzimos uma espécie de refinamento apenas através de plotagens. Até aí, não há nada numérico acontecendo. Porém, isso nos ajuda a selecionar ainda melhor uma condição inicial para o processo iterativo subsequente.

# In[5]:


# Refinamento
a,b = 10,20
c = np.linspace(a,b,100)
f = g*m/c*(1 - np.exp(-c/m*t)) - v

plt.plot(c,f,'g-')
plt.plot(c,0*c,'r--')
plt.grid()


# In[6]:


# Refinamento
a,b = 14,16
c = np.linspace(a,b,100)
f = g*m/c*(1 - np.exp(-c/m*t)) - v

plt.plot(c,f,'g-')
plt.plot(c,0*c,'r--')
plt.grid()


# In[7]:


# Refinamento
a,b = 14.75,15.5
c = np.linspace(a,b,100)
f = g*m/c*(1 - np.exp(-c/m*t)) - v

plt.plot(c,f,'g-')
plt.plot(c,0*c,'r--')
plt.grid()


# In[8]:


# Refinamento
a,b = 15.12,15.14
c = np.linspace(a,b,100)
f = g*m/c*(1 - np.exp(-c/m*t)) - v

plt.plot(c,f,'g-')
plt.plot(c,0*c,'r--')
plt.grid()


# Apenas com esses refinamentos, já é possível determinar a raiz única com um erro absoluto de 0.02 unidades, visto que ela está entre 15.12 e 15.14. Além disso, note como, neste intervalo, a curvatura da função não é mais identificável. Isso mostra que, no intervalo $15.10 \leq c \leq 15.20$, $f$ é praticamente "linear". 
# 
# Porém, nos casos reais, requeremos precisão muito mais elevada. Então, para melhorarmos a precisão de nossa raiz, precisamos avançar para a segunda etapa, que apoia-se na _aproximação algorítmica_ por processos iterativos.

# #### Sistemas métricos e homogeneidade dimensional
# 
# Ao lidarmos com o problema anterior, não foi necessário saber como as grandezas envolvidas são quantificadas e quais são as suas unidades em algum sistema métrico. Entretanto, cabe ressaltar que problemas realistas da ciência e engenharia computacional devem estar associados a um sistema métrico consistente e as equações envolvidas devem ser dimensionalmente homogêneas, ou seja, corretas e fisicamente válidas. 
# 
# De acordo com o Sistema Internacional (SI) [[NIST]](https://www.nist.gov/pml/weights-and-measures/si-units), há 7 de unidades básicas, estabelecidas pela mensuração de 7 quantidades básicas ({numref}`Tabela %s <tbl-si>`).
# 
# ```{table} Unidades e Quantidades Básicas do SI
# :name: tbl-si
# | Quantidade          | Unidade SI         | Símbolo da Unidade |
# |:--------------------|:-------------------|:-------------------|
# | Comprimento         | metro              |$m$                 |
# | Massa               | quilograma         |$kg$                |
# | Tempo               | segundo            |$s$                 |
# | Corrente elétrica   | ampere             |$A$                 |
# | Temperatura termodinâmica | kelvin       |$K$                 |
# | Quantidade de substância | mol           |$mol$               |
# | Intensidade luminosa| candela            |$cd$                |
# ```
# A descrição das unidades básicas é a seguinte:
# 
# - **Metro** ($m$): Unidade de comprimento. O metro é definido pela distância que a luz percorre no vácuo em um intervalo de tempo de 1/299.792.458 de segundo.
# - **Quilograma** ($kg$): Unidade de massa. O quilograma é definido em termos da constante de Planck.
# - **Segundo** ($s$): Unidade de tempo. O segundo é definido pela duração de 9.192.631.770 períodos da radiação correspondente à transição entre dois níveis hiperfinos do estado fundamental do átomo de césio-133.
# - **Ampere** ($A$): Unidade de corrente elétrica. O ampere é definido pela força eletromagnética entre dois condutores paralelos infinitamente longos e de seção transversal desprezível.
# - **Kelvin** ($K$): Unidade de temperatura termodinâmica. O kelvin é definido em termos da energia térmica absoluta (temperatura) e da constante de Boltzmann.
# - **Mol** ($mol$): Unidade de quantidade de substância. O mol é definido pelo número de átomos em 12 gramas de carbono-12, o que corresponde ao número de Avogadro.
# - **Candela** ($cd$): Unidade de intensidade luminosa. A candela é definida pela intensidade luminosa em uma direção específica de uma fonte que emite radiação monocromática de frequência$540 \times 10^{12}$Hz e tem uma intensidade radiante nessa direção de 1/683 watt por esterradiano.
# 
# As unidades básicas relacionam-se com unidades derivadas por meio de multiplicação e divisão, assim produzindo o grande conjunto de quantidades que usamos para quantificar os fenômenos de nosso universo ({numref}`fig-si`).
# 
# ```{figure} figs/si.png
# ---
# width: 400px
# name: fig-si
# ---
# Diagrama de unidades básicas e derivadas do SI. Fonte: [[NIST]](https://www.nist.gov/pml/weights-and-measures/si-units).
# ```
# 
# ##### Princípio da Homogeneidade Dimensional
# 
# Para que uma equação física seja dimensionalmente homogênea, todas as suas partes devem ter as mesmas dimensões. Isso implica que, ao realizar operações matemáticas como adição, subtração, multiplicação ou divisão, as dimensões resultantes devem ser coerentes. Aplicando as unidades do SI à análise de nossa equação original, verificamos que a equação da velocidade terminal é dimensionalmente homogênea, pois cada termo da equação possui a dimensão de velocidade$[L/T]$, confirmando a consistência e validade da fórmula ({numref}`Tabela %s <tbl-ad>`; {numref}`Tabela %s <tbl-ad2>`).
# 
# 
# ```{table} Análise dimensional da equação da velocidade terminal do paraquedista
# :name: tbl-ad
# 
# | Variável/Símbolo      | Descrição                         | Dimensão      | Unidade     |
# |:----------------------|:----------------------------------|:--------------|:-----------:|
# |$g$              | Aceleração devido à gravidade     |$[LT^{-2}]$| $m/s^2$        |
# |$m$              | Massa do paraquedista             |$[M]$      | $kg$          |
# |$c$              | Coeficiente de arrasto            |$[M/T]$    | $kg/s$        |
# |$t$              | Tempo                             |$[T]$      | $s$           |
# |$v$           | Velocidade em função do tempo     |$[L/T]$    | $m/s$         |
# |$\frac{gm}{c}$   | Termo de velocidade               |$[L/T]$    | $m/s$         |
# |$\exp\left(-\frac{c}{m}t\right)$| Termo exponencial | Adimensional  | N/A         |
# ```
# 
# ```{table} Verificação dimensional da equação completa
# :name: tbl-ad2
# 
# | Termo da Equação                              | Dimensão Resultante |
# |:----------------------------------------------|:-------------------:|
# |$\frac{gm}{c}$                           |$[L/T]$          |
# |$\exp\left(-\frac{c}{m}t\right)$         | Adimensional        |
# |$1 - \exp\left(-\frac{c}{m}t\right)$     | Adimensional        |
# |$v(t) = \frac{gm}{c} \left(1 - \exp\left(-\frac{c}{m}t\right)\right)$|$[L/T]$|
# ```
# 
# Dispondo da análise dimensional, podemos desenvolver programas de computador para finalidades de simulação, por exemplo, com muito mais confiabilidade e poder de verificação, visto que saberemos dizer quando uma situação romperá uma lei física. 

# #### Desenvolvimento de software: mini-simulador de saltos
# 
# A seguinte classe é um protótipo de código com maior carga de abstração para simulações genéricas do modelo de velocidade terminal do paraquedista. O propósito é criar plotagens diretas do comportamento de uma variável a partir de parâmetros pré-fixados pelo usuário.

# In[45]:


import numpy as np, matplotlib.pyplot as plt

class Parachute:
    '''Cria objetos para realizar simulações com o modelo 1D de velocidade terminal
       com base em opções do usuário.
    '''
    
    # Variáveis de classe
    base_param = None
    unit = None
    
    # Construtor
    def __init__(self, lim_inf: float, lim_sup: float, num: int, **kwargs):
        self.dict = kwargs
        self.a = lim_inf
        self.b = lim_sup
        self.num = num        
            
    # Função definidora do modelo matemático 
    def f(self):
                
        params = self.dict.keys()        
        
        # Variável: gravidade
        if 'g' not in params:            
            self.dict['g'] = np.linspace(self.a, self.b, self.num, dtype=np.float32)
            x = self.dict['g']
            self.base_param = 'g'
            self.unit = '$m/s^2$'
        
        # Variável: massa  
        elif 'm' not in params:            
            self.dict['m'] = np.linspace(self.a, self.b, self.num, dtype=np.float32)
            x = self.dict['m']
            self.base_param = 'm'
            self.unit = '$kg$'
            
        # Variável: coef. de arrasto
        elif 'c' not in params:            
            self.dict['c'] = np.linspace(self.a, self.b, self.num, dtype=np.float32)
            x = self.dict['c']
            self.base_param = 'c'
            self.unit = '$kg/s$'
            
        # Variável: tempo
        elif 't' not in params:            
            self.dict['t'] = np.linspace(self.a, self.b, self.num, dtype=np.float32)
            x = self.dict['t']
            self.base_param = 't'
            self.unit = '$s$'
            
        # Variável: velocidade (padrão)
        else:                
            self.dict['v'] = 0.0
            self.dict['t'] = np.linspace(self.a, self.b, self.num, dtype=np.float32)      
            x = self.dict['t']    
            self.base_param = 't'    
            self.unit = '$s$'        

        # Modelo para velocidade terminal
        y = self.dict['g']*self.dict['m']/self.dict['c']*(1 - np.exp( - self.dict['c']/self.dict['m']*self.dict['t'])) - self.dict['v']
        
        return x, y
    
    
    # Função de suporte para plotagem 
    def plot(self, label: str):
        
        x,y = self.f()
            
        h = plt.plot(x,y,label=label)
        plt.xlabel(f'{self.base_param} [{self.unit}]', fontsize=10)
        plt.ylabel(f'y = f({self.base_param})', fontsize=10)              
        plt.grid(True)
        
        return h        


# A partir daí, podemos criar diversos testes e analisar comportamentos.

# - Simulações para intervalo de massa em 4 durações de tempo diferentes:
#     - Essa faixa de massa corresponde a de adultos?

# In[51]:


curves = []
for ti in np.linspace(10,30,4,dtype='float32'):
    line, = Parachute(30, 40, num=30, c=10, g=9.85, v=32, t=ti).plot(label=f't={ti:.2f} s')
    curves.append(line)
plt.legend(handles=curves,bbox_to_anchor=(1,1));


# - Simulações para coeficiente de arrasto em 4 acelerações gravitacionais diferentes:
#     - Qual é a característica das atmosferas para eses casos?

# In[50]:


curves = []
for gi in np.linspace(9.8,10.4,4,dtype='float32'):
    line, = Parachute(13, 22, num=30, m=70, g=gi, t=60, v=40).plot(label=f'g={gi:.2f} $m/s^2$')
    curves.append(line)
plt.legend(handles=curves,bbox_to_anchor=(1.,1));


# ## Processo iterativo
# 
# Processos iterativos em métodos numéricos assumem o caráter de _aproximações sucessivas_, pelo fato de buscarem aproximações melhores para uma quantidade a partir de uma estimativa inicial predefinida. Ou seja, levando em conta que estamos trabalhando com funções em uma dimensão, um processo iterativo a uma variável pode ser descrito por
# 
# $$x^{({k})} = \phi(x^{(k-1)}), \ \ k = 1, \ldots, n < \infty$$
# $$x^{(0)} = x_0,$$
# 
# Acima, $\phi$ é a função de iteração, ao passo que $x_0$ é a _estimativa inicial_ (_initial guess_). Nesta notação, $x^{(k)}$ é a $k$-ésima _iterada_ de uma _sequência numérica discreta_.

# ### Fluxo de controle
# 
# A primeira estrutura de controle fundamental para computação numérica de processos iterativos é o laço `for`. Vamos ver como usá-lo para computar algumas funções iterativas, inclusive plotar os resultados.

# -$\phi_1 = \dfrac{ (x^{(k-1)})^{1/2}}{\pi} - x^{(k-1)}, \ \  x^{(0)} = 1, \ \ k < N$

# In[9]:


# No. de elementos
N = 30

# Função de iteração
x = [1/2]

print(f'x(0) = {x[0]}')
for k in range(1,N):
    phi = x[k-1]**1/2/np.pi - x[k-1]
    x.append(phi)
    print(f'x({k}) = {phi:.4f}')

# Plotagem
plt.figure(figsize=(8,3))
plt.plot(x,'go',label=r'$\dfrac{ (x^{(k)})^{1/2}}{\pi} - x^{(k)}$')
plt.xticks(range(N))
plt.xlabel('$x^{(k)}$',fontsize=12)
plt.ylabel('$\phi_1^{(k)}$',fontsize=12)
plt.grid(axis='both')
plt.legend(loc='upper right');


# -$\phi_2 = \dfrac{k}{x^{(k-1)}}, \ \  x^{(0)} = 1/5, \ \ k < 10$

# In[10]:


from math import factorial

# No. de elementos
N = 10

# Função de iteração
y = [1/5]
print(f'y(0) = {y[0]}')
for k in range(1,N):
    phi = k/(y[k-1])
    y.append(phi)
    print(f'y({k}) = {phi:.4f}')

# Plotagem
plt.figure(figsize=(8,3))
plt.plot(y,'go',label=r'$\dfrac{k}{x^{(k-1)}}$')
plt.xticks(range(N))
plt.xlabel('$x^{(k)}$',fontsize=12)
plt.ylabel('$\phi_2^{(k)}$',fontsize=12)
plt.grid(axis='both')
plt.legend(loc='center right');


# ## Determinação de raízes por força bruta
# 
# No computador, sabemos que uma função matemática $f(x)$ pode ser representada de duas formas principais:
# 
# - através de uma função programada (em Python, por exemplo) que retorna o valor da função para um dado argumento 
# - uma coleção de pontos $(x,f(x))$ na forma de uma tabela.
# 
# A segunda forma é bem mais útil para análise gráfica. Esta forma é também adequada para resolver problemas de determinação de raízes e de otimização com simplicidade. No primeiro caso, basta pesquisar todos os pontos e procurar onde a função cruza o eixo $x$, como fizemos anteriormente. No segundo caso, buscamos um ponto de mínimo ou máximo local, ou global.
# 
# Abordagens que seguem esse caminho podem chegar a examinar uma grande quantidade de pontos. Por essa razão, são chamados de métodos de _força bruta_, isto é, não seguem uma técnica elaborada.

# ### Algoritmo numérico
# 
# Em geral, queremos resolver o problema $f(x) = 0$ especialmente quando $f$ é não-linear. Para isso, desejamos encontrar os $x$ onde $f$ cruza o eixo. Um algoritmo em força bruta deverá percorrer todos os pontos sobre a curva e verificar se um ponto está abaixo do eixo e seu sucessor imediato está acima, ou vice-versa. Se isto ocorrer, então deve haver uma raiz neste intervalo. 
# 
# **Algoritmo.** Dado um conjunto de $n+1$ pontos $(x_i,y_i)$, $y_i = f(x_i), \, i = 0,\ldots,n$, onde $x_0 < \ldots < x_n$. Verificamos se $y_i < 0$ e se $y_{i+1} > 0$. Uma expressão compacta para esta checagem é o teste $y_i \, y_{i+1} < 0$. Se o produto for negativo, então a raiz de $f$ está no intervalo $[x_i,x_{i+1}]$. Assumindo uma variação linear entre os pontos, temos a aproximação
# 
# $$f(x) \approx \dfrac{ y_{i+1} - y_i }{ x_{i+1} - x_i }(x - x_i) + y_i.$$
# 
# Logo, $f(x) = 0$ implica que a raiz é 
# 
# $$x = x_i - \dfrac{ x_{i+1} - x_i }{ y_{i+1} - y_i }y_i.$$

# **Exemplo.** Encontre a raiz da função $f(x) = \exp(-x^2)\cos(3x)$ usando o algoritmo de força bruta.

# Vamos plotar esta função apenas para visualizar seu comportamento.

# In[11]:


from numpy import exp, cos

f = lambda x: exp(-x**2)*cos(3*x)
x = np.linspace(0,4,1000)
plt.plot(x,f(x),'g'); plt.grid()


# Nesta plotagem, vemos claramente que a função possui duas raizes: uma próxima de $x = 0.5$ e outra em $x = \pi/6$. 
# 
# Implementemos o algoritmo.

# In[12]:


def forca_bruta(f,a,b,n):
    from numpy import linspace
    x = linspace(a,b,n)
    y = f(x)
    raizes = []
    for i in range(n-1):
        if y[i]*y[i+1] < 0:
            raiz = x[i] - (x[i+1] - x[i])/(y[i+1] - y[i])*y[i]
            raizes.append(raiz)
    if len(raizes) == 0:               
        print('Nenhuma raiz foi encontrada')
    return raizes


# Agora aplicamos o algoritmo na mesma função.

# In[13]:


a,b,n = 0,4,1000
raizes = forca_bruta(f,a,b,n)
print(raizes)


# Temos, na verdade, 4 raízes! Plotemos o gráfico ampliado no intervalo [2.5,3.8].

# In[14]:


x2 = np.linspace(2.5,3.8,100)
plt.plot(x2,f(x2),'g',x2,0*f(x2),'r:'); plt.grid()


# Conseguimos enxergar mais uma raiz. Agora, plotemos um pouco mais ampliado entre [3.6,3.7].

# In[15]:


x3 = np.linspace(3.6,3.7,100)
plt.plot(x3,f(x3),'g',x3,0*f(x3),'r:'); plt.grid()


# Dessa forma, podemos identificar que, de fato existe uma quarta raiz.

# Este exemplo mostrou uma aplicação do método de força bruta para determinação de raízes. Para finalizar, podemos embelezar o gráfico.

# In[16]:


r = np.array(raizes) # vetoriza a lista
plt.plot(x,0*f(x),'r:',x,f(x),'g-',r,np.zeros(4),'ok',)
plt.xlabel('$x$',fontsize=14)
plt.ylabel('$f(x)$',fontsize=14)        
plt.grid()
plt.title('Raízes de $e^{-x^2}\cos(3x)$');


# ## Receitas prontas para visuais
# 
# Na análise gráfica de funções não lineares, alguns elementos úteis para as plotagens são:
# 
# - o gráfico da função $f(x)$ sob análise;
# - o gráfico da função $g(x) = 0$ ou o gradeado do plano Cartesiano;
# - as legendas dos eixos;
# - o intervalo de estimativas iniciais;
# 
# Um bloco de código baseado em `matplotlib` replicável que contempla tudo isso é fornecido a seguir:

# In[43]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,2) # domínio de análise
f = np.exp(-x**2)*np.cos(3*x) # função-alvo

fig, ax = plt.subplots(figsize=(6,4), constrained_layout=True) # figura
#ax.grid(axis='both') # gradeado
ax.plot(x,f,label='$f(x)$') # plotagem
ax.axhline(y=0, ls=':', color='orange', label='$y=0$') # g(x) = 0
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_title('Exemplo de plotagem para análise gráfica')

# 1o. intervalo de busca
ax.plot(-0.7,0,'|',c='k')
ax.plot(-0.4,0,'|',c='k')

# 2o. intervalo de busca
ax.plot(0.4,0,'|',c='r')
ax.plot(0.7,0,'|',c='r')

# 3o. intervalo de busca
ax.plot(1.4,0,'|',c='m')
ax.plot(1.7,0,'|',c='m')

ax.legend();


# ## Tarefas
# 
# - Faça a implementação computacional do algoritmo da "força bruta".
# - Verifique a correção e aperfeiçoe a mini-classe para simulações de salto e use o mesmo raciocínio para criar uma classe própria aplicável a outro modelo matemático.
