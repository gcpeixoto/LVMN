#!/usr/bin/env python
# coding: utf-8

# # Documentação de código

# O _Python Enhancement Proposal_ 257 ([PEP 257](https://peps.python.org/pep-0257/)) trata das convenções para uso de _docstrings_ em Python.
# 
# _Docstring_ é uma string literal usada para documentar um módulo, função, classe ou método. Ela pode ser acessada pelo atributo especial `__doc__`.

# In[3]:


# modelo
def fun():
    """This is function fun."""
    pass

# acesso
fun.__doc__


# ## Tipos de _docstrings_
# 
# Uma _docstring_ deve ser sempre confinada por um par de aspas triplas, podendo ser (definição própria):
# 
# - _Simples_: Não contém caracter especial. Exemplo: `"""ao."""`
# - _Literal_: Precedida por `r`. Contém pelo menos um caracter "barra invertida" (_backslash_), isto é, `\`. Exemplo: `r"""a\o."""`
# - _Unicode_: Precedida por `u`. Contém pelo menos um caracter unicode. Exemplo: `u"""áò"""`.
# 
# 
# A docstring utilizada em `fun()` acima é simples. Abaixo, vemos exemplos equivalentes para os outros dois tipos.

# In[15]:


def fun_1():
    """This is fun_1 with a \n."""
    pass

fun_1.__doc__    


# In[17]:


def fun_2():
    r"""This is fun_2 with a \n."""
    pass

fun_2.__doc__    


# No exemplo abaixo, seria necessário usar `u` à frente da docstring caso trabalhássemos fora do encoding `UTF-8`.

# In[23]:


def fun_3():
    u"""fun_3: Zażółć gęślą jaźń. Em português e polonês..."""
    pass

fun_3.__doc__  


# ## Modos de docstring
# 
# _Docstrings_ podem ser escritas em modo de _linha única_ ou de _múltiplas linhas_
# 

# No exemplo abaixo, a docstring é de linha única.

# In[27]:


def s(a:int, b:int):
    """Adiciona a e b."""
    return a + b

[s(i,j) for i,j in zip(range(4),range(1,5))]


# Agora, a docstring é de de linha múltipla (mas fora do padrão).

# In[28]:


def sp(a:int, b:int):
    """
    Adiciona e
    multiplica a e b.
    """
    return (a + b, a*b)

[sp(i,j) for i,j in zip(range(4),range(1,5))]


# ## Estrutura de docstrings de múltiplas linhas
# 
# _Docstrings_ de linha única são úteis para descrever ações simples. Quando precisamos documentar algo mais complexo, usamos docstrings com algumas estruturas (ou estilos). Existem diversas estruturas de documetnação, mas entre as mais populares, estão:
# 
# - [Google](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
# - [numpydoc](https://numpydoc.readthedocs.io/en/latest/)
# - reST (reStructured Text)

# ### Estrutura Google

# In[ ]:


"""
Esta é uma docstring em estilo Google.

Args:
    param1: Primeiro parâmetro.
    param2: Segundo parâmetro.

Returns:
    Descrição do retorno.

Raises:
    KeyError: Exceção lançada.
"""


# ### Estrutura numpydoc

# In[ ]:


"""
Esta é uma docstring em estilo numpydoc exaustiva.

Parameters
----------
first : array_like
    primeiro parâmetro
second :
    segundo parâmetro
third : {'value', 'other'}, optional
    terceiro parâmetro, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""


# ### Estrutura reST

# In[ ]:


"""
Esta é uma docstring em estilo reST.

:param param1: Primeiro parâmetro.
:param param2: Segundo parâmetro.
:returns: Descrição do retorno.
:raises keyError: Exceção lançada.
"""


# ### Sphinx
# 
# [Sphinx](https://www.sphinx-doc.org/en/master/) é um gerador de documentação em Python baseado no estilo reST de grande utilidade para desenvolvedores de código. Ele possui diversas características, tais como múltiplos formatos de saída, extensões, temas etc.
# 
# A seguir, temos um exemplo de função apropriadamente documentada para o Sphinx.

# In[55]:


def hamming(s1: str,s2: str):
    """Calcula a distância de Hamming entre strings.
    
    :param s1: primeira string .
    :param s2: segunda string.
    :returns: distância entre s1 e s2 pela métrica de Hamming.
    :raises RuntimeError: strings devem ter o mesmo comprimento.
    """
    
    # Strings devem possuir mesmo comprimento para serem comparadas.
    # Caso contrário, lança exceção
    if len(s1) != len(s2):
        raise RuntimeError
    
    # Associa False(True) para caracteres diferentes(iguais) e soma a quantidade de True. 
    return sum(c1 != c2 for c1, c2 in zip(s1,s2))


# - Teste da função de Hamming

# In[56]:


s31, s32 = 'pão', 'são'
s33, s34 = 'teu', 'tua'
s35, s36 = 'ali', 'seu'

hamming(s31,s32), hamming(s33,s34), hamming(s35,s36)


# - Impressão da documentação

# In[57]:


print(hamming.__doc__)


# - Documentação reescrita no estilo numpydoc

# In[58]:


def hamming_numpydoc(s1: str,s2: str):
    """Calcula a distância de Hamming entre strings.
 
    Parameters
    ----------
    first : str
        primeira string.
    second: str
        segunda string.

    Returns
    -------
    int
        distância de Hamming.

    Raises
    ------
    RuntimeError
        Se strings tiverem comprimento distinto
    """
    
    # Strings devem possuir mesmo comprimento para serem comparadas.
    # Caso contrário, lança exceção
    if len(s1) != len(s2):
        raise RuntimeError
    
    # Associa False(True) para caracteres diferentes(iguais) e soma a quantidade de True. 
    return sum(c1 != c2 for c1, c2 in zip(s1,s2))


# - Impressão da nova documentação

# In[61]:


print(hamming_numpydoc.__doc__)

