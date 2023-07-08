#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf


# ## _Tensorflow_ e _numpy_
# 
# - Ambas as bibliotecas compartilham similaridades. 
# - _numpy_ serve para computação numérica genérica.
# - _tensorflow_ é especificamente projetado para aplicações de aprendizagem de máquina, mas também pode ser usado para computação numérica.
# - _tensorflow_ possui algumas características adicionais não encontradas no_numpy_:
#     - Diferenciação automática (DA): suporte direto à DA permite cálculos eficientes de gradientes de retropropagação (_backpropagation_).
#     - Aceleração de hardware: suporte a GPU e TPU, enquanto o numpy se sustenta em CPU.
#     - Computação distribuída: suporte nativo para escalabilidade em múltiplas plataformas e máquinas, enquanto o numpy é para máquina única.
#     - Compatibilidade com o ecossistema TensorFlow: fácil integração com datasets e o pipeline de ML.
#     - Grafos computacionais estáticos (GCEs): tensorflow opera sobre estruturas de grafos que pode ser otimizada. A natureza estática garante eficiência em aceleradores de hardware e sistemas distribuídos, enquanto o numpy opera em modo imediato sem o conceito de GCEs.

# ## O tipo `Tensor`
# 
# - Grosso modo, são arrays multidimensionais especializados.
# - Herdam todas as operações matemáticas do `numpy.array`, mas realizam outras mais.
# - Imutáveis.
# 
# 
# _Obs.:_ conceito paralelo ao tensor da física/mecânica.

# In[6]:


# 'constant' significa 'immutable'
c1 = tf.constant(1.0)
c2 = tf.constant([1.0,2.0])
c3 = tf.constant([[1.0,2.0], [3.0,4.0]])
c1,c2,c3


# - Método e atributos principais

# In[24]:


c1.numpy(), c2.shape, c3.dtype


# - Operações matemáticas comuns

# In[31]:


print(2*c1)
print(c2/2)
print(c3 - tf.matmul(c3 + 1,tf.eye(2)))


# - Operador `@` realiza multiplicação tensorial

# In[59]:


c4 = tf.ones((3,3)) + tf.fill([3,3],2.0)
c5 = tf.one_hot(indices=[3,1,4],depth=5)
c6 = tf.transpose(c5) @ c4

print(c4)
print(c5)
print(c6)


# ### Atribuição x imutabilidade
# 
# - A imutabilidade do tensor está associada ao seu GCE.
# - Não podemos usar atribuição direta, mas isso não descreve a imutabilidae.

# In[ ]:


try:
    c1[0] = 2
except TypeError as e:
    print('--> Não posso ser alterado por atribuição indexada!\n', e)


# In[101]:


# conda install -c conda-forge tensorboard

with tf.compat.v1.Session() as sess:
    c3a = tf.constant([[1.0,2.0], [3.0,4.0]], name = "a")
    c3b = tf.constant([[-2.0,2.0], [4.0,-3.0]], name = "b")
    c3c = tf.add(c3a, c3b, name = "c")
    c3d = tf.multiply(2.0, c3c, name = "d")
    print(sess.run(c3d))


# ## O tipo `Variable`

# In[80]:


v1 = tf.Variable(2)
print(v1)

