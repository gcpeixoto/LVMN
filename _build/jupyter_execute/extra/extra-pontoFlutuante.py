#!/usr/bin/env python
# coding: utf-8

# # Números em ponto flutuante e seus problemas
# 
# Este capítulo é um compêndio sobre a representação numérica em computadores, sistema de ponto flutuante, bem como notas sobre causas de erros. O texto é essencialmente uma reprodução adaptada do conteúdo encontrado no site [floating-point-gui.de](https://floating-point-gui.de).
# 
# ## Perguntas e respostas
# 
# ### Por que a soma `0.1 + 0.2` não é exatamente 0.3, mas resulta em `0.30000000000000004`?

# Porque, internamente, os computadores usam um formato de ponto flutuante binário limitado que não pode representar com precisão números como 0.1, 0.2 ou 0.3. Quando o código é compilado ou interpretado, `0.1` já é arredondado para o número mais próximo consoante este formato, o que resulta em um pequeno erro de arredondamento antes mesmo de o cálculo acontecer.

# In[1]:


# ?!
0.1 + 0.2


# ### Este sistema parece um tanto estúpido. Por que os computadores o utilizam para fazer cálculos?
# 
# Não se trata de estupidez. O sistema é apenas diferente. Números decimais não podem representar com precisão qualquer número, a exemplo da fração `1/3`. Então, temos que usar algum tipo de arredondamento para algo como `0.33`. Afinal, não podemos esperar que a soma `0.33 + 0.33 + 0.33` seja exatamente igual a `1`, não é mesmo?
# 
# Os computadores usam números binários porque são mais rápidos ao lidar com eles e, para a maioria dos cálculos usuais, um pequeno erro na 17a. casa decimal não é relevante, pois, de qualquer maneira, os números com os quais trabalhamos não são "redondos" (ou exatamente "precisos"). 

# ### O que pode ser feito para evitar este problema? 
# 
# Isso depende do tipo de cálculo pretendido.
# 
# Se a precisão dos resultados for absoluta, especialmente quando se trabalha com cálculos monetários, é melhor usar um tipo de dado especial, a saber o `decimal`. Em Python, por exemplo, há um [módulo de mesmo nome](https://docs.python.org/3/library/decimal.html) para esta finalidade específica. Por exemplo:

# In[8]:


# 0.1 + 0.2 
from decimal import Decimal 

a,b = Decimal('0.1'), Decimal('0.2')
print(a+b)


# Se apenas se deseja enxergar algumas casas decimais, pode-se formatar o resultado para um número fixo de casas decimais que será exibido de forma arredondada.

# In[25]:


# imprime resultado como float
print(0.1 + 0.2)

# imprime resultado com 3 casas decimais
print(f'{0.1 + 0.2:.3f}')


# ### Por que outros cálculos como `0.1 + 0.4` funcionam corretamente?
# 
# Nesse caso, o resultado, `0.5`, **pode** ser representado exatamente como um número de ponto flutuante e é possível que haja erro de cancelamento nos números de entrada. Porém, pode não podemos confiar interamente nisto. Por exemplo, quando tais dois números são primeiro armazenados em representações de ponto flutuante de tamanhos diferentes, os erros de arredondamento podem não compensar um com o outro.
# 
# Em outros casos, como `0.1 + 0.3`, o resultado **não é realmente** `0.4`, mas próximo o suficiente para que `0.4` seja o menor número mais próximo do resultado do que qualquer outro número em ponto flutuante. Muitas linguagens de programação exibem esse número em vez de converter o resultado real de volta para a fração decimal mais próxima. Por exemplo:

# In[36]:


print(0.1 + 0.4)
print(0.1 + 0.1 + 0.1 - 0.3) # 0 !


# ## Comparação de números em ponto flutuante
# 
# Devido a erros de arredondamento, a representação da maioria dos números em ponto flutuante torna-se  imprecisa. Enquanto essa imprecisão permanecer pequena, ela poderá ser geralmente ignorada. No entanto, às vezes, os números que esperamos ser iguais (por exemplo, ao calcular o mesmo resultado por diferentes métodos corretos) diferem ligeiramente de tal forma que um mero teste de igualdade implica em falha. Por exemplo:

# In[47]:


a = 0.15 + 0.15
b = 0.1 + 0.2

# Os resultados abaixo deveriam ser verdadeiros (True),
# mas não o são!
print(a == b) 
print(a >= b) 


# ### Margens de erro: absoluto x relativo
# 
# Ao compararmos dois números reais, o melhor caminho a seguir não é verificar se os números são exatamente iguais, mas se a _diferença entre ambos é muito pequena_. A margem de erro com a qual a diferença é comparada costuma ser chamada de "epsilon". A forma mais simples seria por meio do erro absoluto. Por exemplo:

# In[48]:


# comparação por erro absoluto
if abs(a - b) < 1e-5:
    print('OK!')


# Isto é, a expressão acima é matematicamente equivalente a $|a - b| < \epsilon$ para $\epsilon=10^{-5}$. 

# Entretanto, essa é uma maneira ruim de comparar números reais, porque um _epsilon_ fixo escolhido que parece "pequeno" pode, na verdade, ser muito grande quando os números comparados também forem muito pequenos. A comparação retornaria _verdadeiro_ para números bastante diferentes. E quando os números são muito grandes, o _epsilon_ pode acabar sendo menor que o menor erro de arredondamento, de forma que a comparação sempre retorna _falso_. 
# 
# Assim, é razoável verificar se o _erro relativo_ é menor que o _epsilon_.

# In[66]:


# comparação por erro relativo
if abs((a - b)/b) < 1e-5:
    print('OK!')


# Mas, esta forma ainda não é inteiramente correta para alguns casos especiais, a saber: 
# 
# - quando tanto `a` quanto `b` são iguais a zero, a fração resultante `0.0/0.0` é uma indefinição do tipo _not a number_ (`NaN`), a qual gera uma exceção em algumas plataformas, ou retorna _falso_ para todas as comparações;

# In[175]:


a,b = 0,0
abs((a-b)/b) # exceção 'ZeroDivisionError'


# - quando apenas `b` é igual a zero, a divisão produz o _infinito_ ($\infty$), que pode gerar uma exceção ou ser maior do que epsilon mesmo quando `a` for menor;

# In[176]:


a,b = 1e-1,0
abs((a-b)/b) # exceção 'ZeroDivisionError'


# - quando `a` e `b` são muito pequenos, mas estão em lados opostos a zero, a comparação retorna _falso_, ainda que ambos sejam os menores números diferentes de zero possíveis.

# In[178]:


a,b = -0.009e-20,1.2e-19
abs((a-b)/b) < 1e-5


# Além disso, o resultado pode não ser sempre comutativo. Isto é, `abs((a-b)/b)` pode ser diferente de  `abs((b-a)/b)`.

# É possível escrever uma função – veja abaixo – capaz de passar em vários testes para casos especiais, porém ela usa uma lógica com pouca obviedade. A margem de erro deve ser definida de maneira diferente dependendo dos valores de `a` ou `b`, porque a definição clássica de erro relativo torna-se insignificante nesses casos. 

# In[297]:


def compare_float(a:float,b:float,eps:float) -> bool: # ":" e "->" são apenas anotações didáticas    
    
    import sys
    MIN = sys.float_info.min # menor float : ~ 1.80e+308
    MAX = sys.float_info.max # maior float : ~ -2.23e+308
        
    diff = abs(a-b)   
    a = abs(a)
    b = abs(b) 
    
    if (a == b): # trata 'inf'
        return True
    elif (a == 0 or b == 0 or (a + b < MIN)): # a ou b = 0 ou ambos extremamente próximos de 0
        return diff < (eps*MIN)
    else: # erro relativo
        return diff/(min(a + b, MAX)) < eps


# Exemplos:

# In[298]:


print(compare_float(1e-3,1e-3,1e-10))
print(compare_float(1e-3,1.1e-3,0.01))
print(compare_float(10.111,10.1111,1e-5))
print(compare_float(10.111,10.1111,1e-6))


# ### Referências para estudo
# 
# #### Miscelânea
# 
# - [IEEE 754-2019 - IEEE Standard for Floating-Point Arithmetic](https://standards.ieee.org/content/ieee-standards/en/standard/754-2019.html)
# - [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://download.oracle.com/docs/cd/E19957-01/806-3568/ncg_goldberg.html), artigo publicado por David Goldberg na ACM Computing Surveys, Vol. 23 (1), 1991. DOI: [10.1145/103162.103163](https://dl.acm.org/doi/abs/10.1145/103162.103163)
# - [William Kahan's Homepage (arquiteto do padrão IEEE 754, e vários outros links)](http://www.cs.berkeley.edu/~wkahan/)
# - [Decimal Arithmetic FAQ 
# (Frequently Asked Questions)](http://speleotrove.com/decimal/decifaq.html)
# - [Python documentation - `decimal` module](https://docs.python.org/3/library/decimal.html)
# - [Is floating point math broken? @StackOverflow](https://stackoverflow.com/questions/588004/is-floating-point-math-broken)
# - [The Perils of Floating Point](https://www.lahey.com/float.htm)
# 
# #### Visualizadores interativos de números no padrão IEEE 754
# 
# - [IEEE 754 Visualization](https://bartaz.github.io/ieee754-visualization/)
# - [Float exposed]
# 
# #### Exemplos de comparação de números em ponto flutuante
# 
# - [Random ASCII – tech blog of Bruce Dawson](https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/)
# 
# #### Livros
# 
# - Modern Computer Architecture and Organization, por Jim Ledin
# - Computer Organization and Architecture Designing for Performance, por William Stallings
# - Numerical Computing with IEEE Floating Point Arithmetic, por Michael L. Overton
