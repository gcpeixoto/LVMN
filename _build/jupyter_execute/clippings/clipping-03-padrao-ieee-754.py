#!/usr/bin/env python
# coding: utf-8

# (clipping-ieee754)=
# # Recorte 3: Padrão de Ponto Flutuante IEEE 754
# 
# O texto a seguir é um excerto do artigo _IEEE Standard for Floating Point Numbers_, de Rajaraman, V., publicado na Resonance 21.1 (2016): 11-30, com adaptações.
# 
# 
# ```{admonition} Nota
# O padrão em vigor é o 754-2019, o qual está documentado neste [artigo](https://ieeexplore.ieee.org/document/8766229).
# ```
# 
# ## O antigo padrão IEEE 754-1985 
# 
# Os números binários em ponto flutuante começaram a ser usados em meados dos anos 50. Não havia uniformidade nos formatos usados para representar números em ponto flutuante e os programas não eram portáveis do computador de um fabricante para outro. Em meados da década de 1980, com o advento dos computadores pessoais, o número de bits utilizados para armazenar números em ponto flutuante foi padronizado como 32 bits. Um Comitê de Padrões foi formado pelo Instituto de Engenheiros Elétricos e Eletrônicos (IEEE) para padronizar como os números binários de ponto flutuante seriam representados nos computadores. Além disso, o padrão especificava uniformidade em arredondamento de números, tratava condições de exceção, tais como o problema da divisão por 0 e a representação de 0 e do infinito ($\infty$). 
# 
# Este padrão, chamado IEEE 754, foi adotado em 1985 por todos os fabricantes de computadores. Ele permitiu a portabilidade de programas de um computador para outro sem que as respostas fossem diferentes e definiu formatos de ponto flutuante para números de 32 bits e 64 bits. 
# 
# Com a melhoria nas tecnologias de informática, tornou-se viável usar um número maior de bits para números de ponto flutuante. Depois que o padrão foi usado por vários anos, foram sugeridas muitas melhorias. O padrão foi atualizado em 2008. 
# 
# O padrão atual é a versão IEEE 754-2008. Esta versão manteve todos os recursos do padrão de 1985 e introduziu novos padrões para 16 e 128 bits. Ele também introduziu padrões para representar números decimais de ponto flutuante.
# 
# A representação de ponto flutuante IEEE para números reais em binário é composta por três partes. Para um número de 32 bits (chamado de precisão simples), eles são:
# 
# 1. *Sinal*, para o qual 1 bit é alocado.
# 
# 2. *Mantissa* (chamado *significando* no padrão), para a qual são alocados 23 bits.
# 
# 3. *Exponente*, para o qual são alocados 8 bits. Tanto números positivo e negativos são necessários para o expoente. Em vez de usar um bit de sinal separado para o expoente, o padrão usa uma representação tendenciosa (_biased_). O valor do _bias_ é 127. Assim, um expoente 0 significa que o valor -127 é armazenado no campo do exponente. Por exemplo, um valor armazenado 198 significa que o valor do expoente é (198 - 127) = 71. Os expoentes -127 (todos 0s) e + 128 (todos 1s) são reservados para representar números especiais.
# 
# Para aumentar a precisão do significando, o padrão IEEE 754 usa um significando normalizado que implica que seu bit mais significativo é sempre 1. Como isso está implícito, presume-se estar à esquerda do ponto decimal (virtual) do significando. Assim, no padrão IEEE, o significando possui 24 bits de comprimento - 23 bits do significando que são armazenados na memória e um implícito 1 como o bit mais significativo na 24a. posição. O bit extra aumenta o número
# de dígitos no significando.
# 
# Assim, um número em ponto flutuante no Padrão IEEE é 
# $$(-1)^s \times (1.f)_2 \times 2^{e - 127},$$
# 
# onde $s$ é o bit do sinal e $f$ os bits no significando (o 1 é implícito e aqui aparece para clareza) e $e$ o expoente.
# 
# ## Valores especiais no padrão IEEE 754-1985 (32 Bits)
# 
# **Representação de Zero:** Como se assume que o significando possui um 1 oculto como o bit mais significativo, todos os 0s na parte do significando de um número serão as tomados como 1,00...0. Assim, o zero é representado no padrão IEEE por _todos os 0s para o expoente e todos os 0s para o significando_. Todos os 0s para o expoente não podem ser usados para nenhum outro número. Se o bit de sinal for 0 e todos os outros bits 0, o número é +0. Se o bit de sinal for 1 e todos os outros bits 0, é -0. Mesmo que +0 e -0 tenham representações distintas, elas são assumidas como iguais.
# 
# **Representação do Infinito:** Todos os 1s no campo exponente representam o infinito ($\infty$). Um bit de sinal 0 representa $+\infty$ e um bit de sinal 1 representa $-\infty$.
# 
# **Representação de "não" números:** quando uma operação é realizada por um computador sobre um par de operandos, o resultado pode não ser definido matematicamente. Por exemplo, se zero for dividido por zero, o resultado é indeterminado. Tal resultado é chamado de _não é um número_, ou _"not a number"_ (NaN) no padrão IEEE. Na verdade, o padrão IEEE define dois tipos de NaN. Quando o resultado de uma operação não está definido (ou seja, indeterminado) é chamado de NaN silencioso (QNaN) (_Quiet NaN_). Exemplos são: $0/0$,($\infty - \infty$), $\sqrt{-1}$. O outro tipo de NaN é chamado de NaN de sinalização (SNaN) (_Signalling NaN_), usado para dar uma mensagem de erro. Quando uma operação gera _underflow_, i.e., quando o resultado de uma computação é menor que o menor número que pode ser armazenado como um número de ponto flutuante, ou _overflow_, i.e, quando é maior que o maior número que pode ser armazenado, o SNaN é usado. Quando nenhum valor válido é armazenado em um nome de variável (i.e. indefinido) e uma tentativa é feita para usá-lo em uma operação aritmética, isto resultaria em um SNaN. O QNaN é representado por 0 ou 1 como o bit de sinal, todos os 1s como expoente e um 0 como o bit mais à esquerda do significando e pelo menos um 1 no resto do significando. Já o SNaN é representado por 0 ou 1 como o bit de sinal, todos os 1s como expoente e um 1 como o bit mais à esquerda do significando e qualquer string de bits para os restantes 22 bits.
# 
# **Números subnormais:** quando todos os bits do exponente são 0 e o bit oculto principal do siginificando é 0, o número de ponto flutuante é chamado de um _número subnormal_. Assim, uma representação lógica de um número subnormal é $(-1)^s \times 0.f \times 2^{-127}$ (todos os 0s para o expoente),
# onde $f$ tem pelo menos 1 (caso contrário, o número seria tomado como 0). No entanto, o padrão usa -126, ou seja, o _bias_ +1 para o expoente em vez de -127, que é o _bias_ por alguma razão não tão óbvia, possivelmente porque usando -126 em vez de -127, a lacuna entre o maior número subnormal e o menor número normalizado é menor.
# 
# Um resultado menor do que o menor número que pode ser armazenado em um computador é chamado _underflow_. Podemos nos perguntar por que os números subnormais são permitidos no padrão IEEE. Ao usar números subnormais, o _underflow que pode ocorrer em alguns cálculos é gradual. Além disso, o menor número que pode ser representado em uma máquina está mais próximo de zero.
# 
# ## O Epsilon de máquina e o "anão"
# 
# Em qualquer um dos formatos para representar números em ponto flutuante, o _epsilon da máquina_ é definido como a diferença entre 1 e o próximo número maior que pode ser armazenado nesse formato. Por exemplo, no formato IEEE de 32 bits com um significando de 23 bits, o _epsilon da máquina_ é $2^{-23} = 1,19 \times 10^{-7}$. Isto essencialmente nos diz que a precisão dos números decimais armazenados neste formato é de 7 dígitos. O termo _precisão_ e _acurácia_ não são os mesmos. A precisão implica _correção_, enquanto que a precisão não. 
# 
# Para a representação de 64 bits de números em ponto flutuante no padrão IEEE, o comprimento médio é de 52 bits. Assim, o epsilon da máquina é $2^{-52} = 2,22 \times 10^{-16}$. Portanto, cálculos decimais com 64 bits fornecem precisão de 16 dígitos. Esta é uma definição conservadora utilizada pela indústria. Em MATLAB, o epsilon da máquina é como definido acima. No entanto, os acadêmicos definem o epsilon da máquina como o limite superior do erro relativo quando os números são arredondados. Assim, para números de ponto flutuante de 32 bits, o epsilon da máquina é $2^{-23}/2 \approx 5,96 \times 10^{-8}$. O epsilon da máquina é útil na computação iterativa. Quando duas iterações sucessivas diferem em menos de $|\epsilon|$, pode-se assumir que a iteração convergiu. *O padrão IEEE não define o epsilon da máquina*.
# 
# O número "anão" (_dwarf_) é o menor número  subnormal que pode ser representado usando o formato de ponto flutuante especificado. Assim, para o formato IEEE de 32 bits, ele é dado por 
# 
# $0 \, \, 00000000 \, \, 00000000000000000000001$
# 
# cujo valor é  $2^{–126–23} = 2^{–149} \approx 1.4 \times 10^{–45}$. Qualquer número inferior a este irá sinalizar _underflow_. A vantagem de usar números subnormais é que o _underflow_ é gradual.
# 
