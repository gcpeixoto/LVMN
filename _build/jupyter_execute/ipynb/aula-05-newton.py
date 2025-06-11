#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
plt.style.use('styles/gcpeixoto-book.mplstyle')


# # Método de Newton: Sair pela Tangente sem Perder o Rumo
# 
# <div class="chapter-thumb">
#     <div class="chapter-oa">
#         <h2>Objetivos de aprendizagem</h2>
#         <ul>
#         <li>Compreender o funcionamento do método de Newton, seu algoritmo e as condições necessárias para sua aplicação;</li>
# 	    <li>Aplicar o método de Newton na resolução de equações não lineares;</li>
# 	    <li>Analisar o comportamento da convergência do método de Newton, sua precisão e limitações;</li>	    
#         <li>Reconhecer variantes do Método de Newton para problemas de otimização, bem como o Método de Halley.</li>
#         </ul>
#     </div>        
#     <div class="quote-box">
#         <p><em>"Nenhuma grande descoberta jamais foi feita sem um palpite ousado." (Isaac Newton)
#         </p></em>
#     </div>        
# </div>
# 
# O método de Newton, também conhecido como método de Newton-Raphson, é uma técnica iterativa poderosa para encontrar aproximações das raízes de equações não lineares. Sua ideia central é usar a reta tangente à curva da função em um ponto de aproximação inicial para estimar onde essa reta cruza o eixo $x$, fornecendo assim uma nova aproximação.  Esse processo é repetido até que a diferença entre iterações sucessivas seja suficientemente pequena, indicando convergência para uma raiz.
# 
# Apesar de ser um método rápido e eficiente com convergência quadrática quando a aproximação inicial está suficientemente próxima da raiz, ele também apresenta desafios. Ele exige que a derivada $f’(x)$ esteja disponível e bem comportada. Além disso, se o ponto inicial estiver longe da raiz, ou se a função tiver pontos de inflexão ou derivadas próximas de zero, o método pode divergir ou oscilar. Por isso, é comum combiná-lo com outras técnicas, como a inspeção gráfica ou métodos mais estáveis (como bisseção) para estimar bons pontos iniciais.
# 
# ```{figure} ../figs/newton-ai.png
# ---
# width: 400px
# name: fig-newtonai
# ---
# 
# ```

# 
# ## Explicação do algoritmo
# 
# O processo iterativo do método é dado pela seguinte função de iteração:
# 
# $$
# x^{(k)} = \phi(x^{(k-1)}) = x^{(k-1)} - \dfrac{ f(x^{(k-1)} )}{ f'(x^{(k-1)}) }, \ \ x^{(0)} = x_0, \ \ k = 1,2, \ldots < \infty, \ \ f'(x^{(k-1)}) \neq 0, \ \ \forall k.
# $$
# 
# 
# onde:
# - $x^{(k-1)}$ é a aproximação atual.
# - $f(x^{(k-1)})$ é o valor atual da função.
# - $f'(x^{(k-1)})$ é o valor atual da primeira derivada da função.
# 
# A ideia é que a interseção da tangente à curva $f(x)$ no ponto $x^{(k-1)}$ com o eixo $x$ forneça uma nova aproximação $x^{(k)}$. O Método de Newton é uma ferramenta essencial no arsenal de métodos numéricos, oferecendo uma abordagem eficiente e poderosa para a solução de uma ampla variedade de problemas matemáticos.
# 
# O algoritmo funciona da seguinte forma: 
# 
# 1. Inicialize $x^{(0)}$ (chute inicial)
# 
# 2. Para $k$ de 1 até $N$:
# 
#     a. Calcule $f(x^{(k)})$
# 
#     b. Calcule $f'(x^{(k)})$ (derivada da função no ponto $x^{(k)}$)
# 
#     c. Se $f'(x^{(k)}) = 0$, retorne erro (derivada zero, o método falha)
# 
#     d. Calcule $x^{(k)} = \phi(x^{(k-1)})$ (como o processo iterativo acima)
# 
#     e. Se $ER(x^{(k)}, x^{(k-1)}) < \epsilon$, então a solução foi encontrada com a precisão desejada. Retorne $x^{(k)}$.
# 
# 3. Se o número máximo de iterações for atingido, retorne a última aproximação $x^{(k-1)}$.
# 

# ## Implementação do algoritmo

# No algoritmo proposto abaixo, a função `newton` requererá 5 argumentos: 
# 
# - a estimativa inicial, representada pela variável `x0`;
# - a função $f(x)$ propriamente dita, representada por `f`;
# - a derivada $f'(x)$, representada por `df`;
# - o erro relativo assumido, representado por `tol`;
# - o número máximo de iterações $N$ para tentativa de solução, representado por `nmax`.

# In[2]:


import inspect, re, numpy as np
from matplotlib.pyplot import plot
from prettytable import PrettyTable as pt

def newton(x0,f,df,tol,N):
    """Algoritmo para determinação de raízes pelo método de Newton.

    Parâmetros: 
        x0: estimativa inicial
        f: string dependendo de uma variável, i.e., a função-alvo
            (e.g., 'x**2 - 1', 'x**2*cos(x)', etc.) 
        df: string dependendo de uma variável, i.e., a derivada da função-alvo
        tol: erro desejado (tolerância)
        N: número máximo de iterações a repetir

    Retorno: 
        x: aproximação para a raiz da função    
    """

    # construtor de tabela
    table = pt()
    
    # substitui expressões da string pelas chamadas das funções do numpy
    f = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', f)
    df = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', df)
    
    # identifica a variável independente em f
    var = re.search(r'([a-zA-Z][\w]*) ?([\+\-\/*]|$|\))', f).group(1)

    
    # cria função
    f = eval('lambda ' + var + ' :' + f)
    
    # checa se a função é de uma variável, senão lança erro        
    try: 
        len(inspect.getfullargspec(f).args) - 1 > 0
    except:
        raise ValueError('O código é válido apenas para uma variável.')
    finally:
        # cria função derivada
        df = eval('lambda ' + var + ' :' + df)
    
    it = 0 # contador de iteracoes
    
    # cabeçalho de tabela
    table.field_names = ['i','x','f(x)','f\'(x)','ER']

    # imprime estimativa inicial
    print(f'Estimativa inicial: x0 = {x0:.6f}\n')  

    # Loop 
    for i in range(0,N):
        
        x = x0 - f(x0)/df(x0) # funcao de iteracao 
        
        e = abs(x-x0)/abs(x) # erro
        
        # tabela
        # impressão de tabela
        table.add_row([i,np.round(x,8),np.round(f(x),8),np.round(df(x),4),f'{e:e}'])
        table.align = 'c';      
        
        if e < tol:
            break
        x0 = x                
        
    print(table)
       
    if i == N:
        print(f'Solução não obtida em {N:d} iterações')
    else:
        print(f'Solução obtida: x = {x:.6f}')


    return x


# ## _Playground_ interativo
# 
# Utilize o _playground_ interativo abaixo para testar o método da bisseção para funções não lineares quaisquer. Como dado de entrada para $f(x)$, utilize funções escritas nos moldes de Python científico como um tipo `str`. Para os parâmetros do intervalo inicial e de erro, utilize `float`.

# In[ ]:


import dash
import re
from dash import dcc, html, Input, Output
import numpy as np
import plotly.graph_objects as go
import sympy as sp
import inspect

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    
    # Function input
    html.Label("f(x): ",
               style={'display': 'inline-block', 'padding': '5px'}),
    dcc.Input(id="function-input",
              type="text",
              placeholder="Insira f(x)...",
              value="cosh(x)*cos(x) - 1",
              style={'width': '20%', 'margin-right': '20px'}),
    
    # Derivative input
    html.Label("f'(x): ",
               style={'display': 'inline-block', 'padding': '5px'}),
    dcc.Input(id="df-input",
              type="text",
              placeholder="Insira f'(x)...",
              value="-sin(x)*cosh(x) + cos(x)*sinh(x)",
              style={'width': '20%', 'margin-right': '20px'}),
    
    # Initial guess input
    html.Label("x0: ",
               style={'display': 'inline-block', 'padding': '5px'}),
    dcc.Input(id="x0-input",
              type="number",
              placeholder="Insira x0...",
              value=4.3,
              style={'width': '10%', 'margin-right': '20px'}),
    
    # Tolerance input
    html.Label("eps: ",
               style={'display': 'inline-block', 'padding': '5px'}),
    dcc.Input(id="tol-input",
              type="number",
              placeholder="Insira a tol. ...",
              value=1e-3,
              style={'width': '10%', 'margin-right': '20px'}),
    
    html.Hr(),
    
    # Graph to display the Newton's method visualization
    dcc.Graph(id="newton-graph"),
    
    html.Hr(),
    
    # Information about the method
    html.Div(id="info-output")
    
], style={'font-family': 'Inter'})


# Algoritmo de Newton
def newton_method(f, f_prime, x0, tol=1e-5, max_iter=100):
    
    points = []  # List to store Newton's points
    
    
    # substitui expressões da string pelas chamadas das funções do numpy
    f = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', f)
    f_prime = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', f_prime)
    
    # identifica a variável independente em f
    var = re.search(r'([a-zA-Z][\w]*) ?([\+\-\/*]|$|\))', f).group(1)

    # cria função
    f = eval('lambda ' + var + ' :' + f)
    
    # checa se a função é de uma variável, senão lança erro        
    try: 
        len(inspect.getfullargspec(f).args) - 1 > 0
    except:
        raise ValueError('O código é válido apenas para uma variável.')
    finally:
        # cria função derivada
        f_prime = eval('lambda ' + var + ' :' + f_prime)
    

    x = x0
    
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        
        if fpx == 0:
            return None, "Derivada é zero. Método falhou."
        
        x_new = x - fx / fpx
        points.append(x_new)
        
        if abs(x_new - x) < tol:
            break
        
        x = x_new
        
    return x, points, f, f_prime

# Callback
@app.callback(
    [Output("newton-graph", "figure"),
     Output("info-output", "children")],
    [Input("function-input", "value"),
     Input("df-input", "value"),
     Input("x0-input", "value"),
     Input("tol-input", "value")]
)
def update_newton_graph(func_str, func_prime, x0, tol):
    
    # Run Newton's method
    root, points, func, func_prime  = newton_method(func_str, func_prime, x0, tol)
    
    if root is None:
        return {}, "O método de Newton não pode ser aplicado."
    
    # Graph
    x_vals = np.linspace(x0 - 2, x0 + 2, 400)
    y_vals = func(x_vals)
    
    # Create the figure
    fig = go.Figure()

    # y = 0 
    fig.add_trace(go.Scatter(x=x_vals,
                             y=y_vals*0,
                             mode='lines', 
                             name="y=0", 
                             line=dict(
                                 color='#b2b2b2',
                                 dash='dash')))
    

    # Plot the function curve
    fig.add_trace(go.Scatter(x=x_vals,
                             y=y_vals,
                             mode='lines',
                             name="f(x)",
                             line=dict(color='#4c9265')))
    
    
    # Approximations
    points_y = [func(p)*0 for p in points]    
    fig.add_trace(go.Scatter(x=points,
                             y=points_y,
                             mode='markers',
                             name="Aproximações",
                             marker=dict(
                                 color='#000000',
                                 symbol='circle',
                                 size=8)))
    
    
        
    # Tangents
    points_y = [func(p) for p in points]
    fig.add_trace(go.Scatter(x=points, 
                             y=points_y, 
                             mode='markers', 
                             name="f'(x) starts", 
                             marker=dict(
                                 color='#FF5733', 
                                 size=8)))
    
    # Plot the root point
    fig.add_trace(go.Scatter(x=[root], 
                             y=[func(root)], 
                             mode='markers', 
                             name="Raiz", 
                             marker=dict(
                                 color='#eeab00', 
                                 size=10)))
    
    
    # Update the layout of the graph
    fig.update_layout(
        template='simple_white',
        width=600,
        height=500,
        margin=dict(l=40, r=40, b=10, t=40),
        xaxis_title="x",
        yaxis_title="f(x)",
        showlegend=True
    )
    
    # Display information about the result
    info_text = f"Raiz encontrada: {root:.6f}\n"
    info_text += f"Número de iterações: {len(points)}"
    
    return fig, info_text

# Run the app
if __name__ == '__main__':
    app.run(port=8082)
    #app.run(debug=True)


# ## Aplicações
# 
# **Exemplo:** Resolva o problema $f(x) = 0$, para $f(x) = -\text{arccos}(x) + 4\text{sen}(x) + 1.7$, no intervalo $-0.2 \le x \le 1.0$ e $\epsilon = 10^{-3}$.

# In[3]:


# Chamada da função
xm = newton(-0.1,
            '-arccos(x) + 4*sin(x) + 1.7',
            '4*cos(x) - 1/(1 - x**2)**1/2',
            1e-3,
            30)


# **Exemplo:** Resolva o problema $h(z) = 0$, para $h(z) = -z(1-2z)^{-1} - \text{tan}(z+1)$, no intervalo $[1,8]$ e $\epsilon = 10^{-5}$.

# Como no exemplo anterior, para utilizarmos o método de Newton é preciso saber a derivada da função $h(z)$. Vamos encontrá-la utilizando o módulo de computação simbólica `sympy`.

# In[4]:


# Importa variável z como símbolo
from sympy.abc import z 
import sympy as sym

# Derivada
dh = sym.diff(-z/(1 - 2*z) - sym.tan(z+1))

# Impressão
print(dh)


# A partir daí, utilizamos a expressão normalmente na função.

# In[5]:


zm = newton(5,
            'z/(1 - 2*z) - tan(z+1)',
            '-2*z/(1 - 2*z)**2 - tan(z + 1)**2 - 1 - 1/(1 - 2*z)',
            1e-5,30)


# Compare a quantidade de iterações obtidas com o mesmo exemplo resolvido com o algoritmo da bisseção.

# ### Derivação para otimização
# 
# O método de Newton, originalmente desenvolvido para encontrar raízes de equações, pode ser adaptado com grande eficácia para problemas de otimização. Nesse contexto, seu objetivo é encontrar os pontos críticos de uma função — ou seja, valores onde a derivada é nula e que podem corresponder a mínimos, máximos ou pontos de sela. A ideia central é usar uma aproximação quadrática da função por meio da série de Taylor de segunda ordem. O processo pode ser resumido nos passos a seguir:
# 
# 1. _Função Objetivo_ (FO): seja $f(x)$ uma função escalar diferenciável cujo mínimo queremos encontrar.
# 
# 2. _Expansão de Taylor de Segunda Ordem_: expandimos $f(x)$ em torno de um ponto $x^{(k)}$ usando a série de Taylor até a segunda ordem:
#    
#    $$
#    f(x) \approx f(x^{(k)}) + f'(x^{(k)}) (x - x^{(k)}) + \frac{1}{2} f''(x^{(k)}) (x - x^{(k)})^2,
#    $$
#    
#    onde $f'(x^{(k)})$ é a primeira derivada (gradiente) de $f$ em $x^{(k)}$ e $f''(x^{(k)})$ é a segunda derivada (Hessiana) de $f$ em $x^{(k)}$.
# 
# 3. _Condição de otimização_: para encontrar o ponto $x$ que minimiza $f(x)$, devemos encontrar um ponto onde a derivada da função seja zero. Definimos a direção de descida $t$ como $x - x^{(k)}$:
#    
#    $$
#    f(x^{(k+1)}) \approx f(x^{(k)}) + f'(x^{(k)}) t + \frac{1}{2} f''(x^{(k)}) t^2
#    $$
#    
# 4. _Derivada da expansão_: para minimizar $f(x)$, tomamos a derivada da expressão acima em relação a $t$ e igualamos a zero:
#    
#    $$
#    \frac{d}{dt}\left[ f(x^{(k)}) + f'(x^{(k)}) t + \frac{1}{2} f''(x^{(k)}) t^2 \right] = 0
#    $$
#    
#    Uma vez que $f(x^{(k)})$ não depende de $t$, é uma constante. Assim obtemos:
#   
#    $$
#    f'(x^{(k)}) + f''(x^{(k)}) t = 0
#    $$
# 
# 5. _solução para a direção $t$: resolvendo para $t$, temos:
#    
#    $$
#    t = -\frac{f'(x^{(k)})}{f''(x^{(k)})}
#    $$
# 
# 6. _Atualização da Iteração_: a próxima aproximação $x^{(k+1)}$ é obtida somando $t$ ao ponto atual $x^{(k)}$:
#    
#    $$
#    x^{(k+1)} = x^{(k)} + t = x^{(k)} - \frac{f'(x^{(k)})}{f''(x^{(k)})}
#    $$
# 
# A derivada $f'(x^{(k)})$ indica a inclinação da função em $x^{(k)}$. A segunda derivada $f''(x^{(k)})$ fornece informações sobre a curvatura da função. Se $f''(x^{(k)}) > 0$, estamos em um ponto onde a função está curvando para cima (mínimo local), enquanto $f''(x^{(k)}) < 0$ indica um ponto onde a função está curvando para baixo (máximo local). O passo $t$ determina a magnitude e a direção do ajuste necessário para aproximar-se do ponto de mínimo (ou máximo).

# ## Método de Halley
# 
# O método de Halley é uma extensão do método de Newton e utiliza até a terceira derivada da função. Enquanto o método de Newton tem convergência quadrática, o método de Halley converge mais rapidamente e alcança convergência cúbica, pois usa mais informações sobre a curvatura da função. De maneira similar ao que já fizemos, vamos derivar a fórmula partindo diretamente da expansão de Taylor:
# 
# 1. _Expansão de Taylor_: expandimos a função $f(x)$ em torno de um ponto $x^{(k)}$:
#    
#    $$
#    f(x) \approx f(x^{(k)}) + f'(x^{(k)}) (x - x^{(k)}) + \frac{1}{2} f''(x^{(k)}) (x - x^{(k)})^2 + \frac{1}{6} f'''(x^{(k)})(x - x^{(k)})^3,
#    $$
# 
# 2. _Estimativa da raiz_: supondo que $x^{(k+1)} = x^{(k)} + \Delta x$ é a nova estimativa da raiz, então queremos $f(x^{(k+1)}) = 0 $. Substituindo $\Delta x = x^{(k+1)} - x^{(k)}$ na expansão de Taylor e igualando a zero, temos:
#    
#    $$
#    f(x^{(k)}) + f'(x^{(k)})\Delta x + \frac{1}{2} f''(x^{(k)})(\Delta x)^2 + \frac{1}{6} f'''(x^{(k)})(\Delta x)^3 = 0
#    $$
# 
# 3. _Isolamento do passo_: a solução para $\Delta x$ (que nos dá a atualização para $x$) é dada pela fórmula:
#    
#    $$
#    \Delta x = -\frac{f(x^{(k)})}{f'(x^{(k)})} \left( \frac{2}{2 - \frac{f(x^{(k)}) f''(x^{(k)})}{f'(x^{(k)})^2}} \right)
#    $$
# 
# 4. _Iteração do Método de Halley_: a fórmula iterativa do método de Halley é então:
#    
#    $$
#    x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})} \left( \frac{2}{2 - \frac{f(x^{(k)}) f''(x^{(k)})}{f'(x^{(k)})^2}} \right)
#    $$
# 
# As vantagens do método de Halley sobre o método de Newton são a taxa de convergência e o alcance de uma solução mais precisa com menos iterações em comparação. Por outro lado, o cálculo das derivadas de ordem superior pode ser computacionalmente custoso e complexo, especialmente para funções complicadas. A precisão do método também depende da precisão das derivadas de segunda e terceira ordem. Portanto, erros nessas derivadas podem afetar a convergência e a precisão da solução.

# ## Problemas propostos
# 
# - Crie um código genérico que implemente o algoritmo do método de Newton de modo que a derivada seja calculada diretamenta por computação simbólica, sem intervenção manual, quando for possível. Dica: use `sympy.lambdify`.
# - Faça uma implementação do método de Newton para otimização e uma para o método de Halley. Em seguida, incorpore a capacidade de cálculo das derivadas de maneira automática.

# In[6]:


plt.rcdefaults()

