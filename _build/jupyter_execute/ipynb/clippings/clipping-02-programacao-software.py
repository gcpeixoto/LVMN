#!/usr/bin/env python
# coding: utf-8

# # Recorte 2: Programação e _Software_
# 
# ## Pacotes e programação
# 
# ### Eis o dilema: usuário x desenvolvedor? 
# 
# Hoje em dia, grande parte de _softwares_, pacotes ou aplicativos com os quais interagimos possui uma interface gráfica, ou o que se chama em computação de **Interface Gráfica do Utilizador**. Em inglês, o esta nomenclatura é abreviado por GUI (_Graphical User Interface_). 
# 
# O propósito de uma GUI é, portanto, construir um ambiente amigável para que qualquer usuário interaja de modo simples, rápido e objetivo com a máquina a fim de atingir produtividade. Graças às interfaces, o usuário, através de cliques (com mouses) ou toques em tela (em dispositivos _touchscreen_), pode realizar diversas operações. No entanto, por trás desses "botões" pressionados por cliques de mouse ou por toques existe muitas instruções computacionais que são definidas por uma ou mais linguagens de programação. Às pessoas que programam essas instruções damos os nomes de _desenvolvedores_. Portanto, dois perfis surgem em um ambiente de programação de computadores: _usuário_ e _desenvolvedor_. Agora, o que isso tem a ver conosco? 
# 
# No universo dos métodos numéricos e disciplinas correlatas, nem sempre um cientista tem à sua disposição um software ou aplicativo com uma interface gráfica que facilite a sua vida. Além disso, na maioria das vezes, o aplicativo pode ser limitado na realização de funções específicas, ou ser ainda de "código fechado" - isto é, de caixa preta, _black-box_, em oposição ao que se conhece como código aberto - e, portanto, impossível de ser modificado por uma pessoa qualquer que não tenha acesso ao código-fonte do aplicativo. 
# 
# Quando não temos essas ferramentas específicas, o que fazemos? 
# 
#  - podemos girar a _web_ de ponta cabeça à procura do nosso _software_ dos sonhos;
#  - pesquisar por um pacote pré-existente;
#  - desenvolver o que queremos;
# 
# Como matemáticos, físicos, engenheiros, isto é, pessoas sem um perfil exímio de desenvolvedor de software, buscamos aplicações. No entanto, veremos também podemos programar um pouquinho. 
# 
# Pelo menos, uma qualidade que essa turma pode se gabar de ter é o espírito de correr atrás da solução de problemas. Então, se o software que você tem não calcula a solução para aquela exótica equação contra a qual você se deparou, que tal você tentar a sua própria solução? É assustador? Esperamos que não. 
# 
# Até mesmo o famoso Microsoft Excel pode se tornar uma ferramenta útil para você realizar alguns cálculos que seriam manualmente tediosos de fazer. Na verdade.
# 
# 
# ### Programas computacionais
# 
# _Programas computacionais_ são um conjunto de instruções que orientam o computador para executar tarefas específicas. Atualmente, diversas instruções, ou linguagens, existem por aí. O website [99 Bottles of Beer](http://www.99-bottles-of-beer.net), por exemplo, lista 1500 diferentes linguagens para uma música popular americana que leva o nome do próprio website! É claro que dessas 1500, algumas são mais adequadas para um estudante de métodos numéricos do que outras, tais como Matlab, C++ e Python.
# 
# 
# ## Programação estruturada
# 
# Hoje em dia, defende-se que um programa seja escrito de modo legível e organizado, prezando-se pela alta qualidade, uma característica que não era muito levada em conta no passado. Legibilidade é, portanto, sinônimo de eficiência, já que facilita o compartilhamento e a compreensão por parte de programadores que trabalham em um projeto colaborativo.
# 
# A _programação estruturada_ é um conjunto de regras que tem por base o princípio de que qualquer algoritmo pode ser composto usando as três estruturas de controle fundamentais: i) sequencia; ii) seleção e iii) repetição.
# 
# O entendimento dessas estruturas de controle pode ser facilitado por _fluxogramas_ e _pseudocódigos_, embora não haja consenso de preferência por essas técnicas. Ambos servem como ferramentas didáticas. Um algoritmo pode ser representado graficamente por símbolos que constituirão um fluxograma. Em contrapartida, um _pseudocódigo_ é uma técnica que utiliza palavras similares a códigos no lugar de símbolos. Essa palavras são especiais e reservadas. Em algumas linguagens, elas são também denominadas palavras-chave (_keywords_). É o caso de `if`, `else`, `switch` e `do`, por exemplo. 

# ### Representação lógica
# 
# **Sequencia:** expressa a ideia de direção. No código computacional, a estrutura é implementada uma instrução por vez.
# 
# **Seleção:** provê um meio de separar o fluxo do programa em ramos com base no valor lógico de uma condição. (`if... else... end`, `if... else... elseif... end`,
# `switch... case...`). O estudante interessado em saber mais sobre as estruturas de código deve pesquisar por estruturas de _controle de fluxo_ em livros introdutórios de programação. 
# 
# **Repetição:** provê os meios para executar uma instrução repetidamente. Os dois aspectos distintos são as estruturas `while... end` e `for... end`.
# 
# ## Programação modular 
# 
# Neste tipo de programação, o código é divido em subcódigos. Essas porções menores são chamadas de _módulos_. Por sua vez, a programação modular permite que o desenvolvimento seja particionado e localizado. Em um grande projeto, por exemplo, vários desenvolvedores podem concentrar esforços em uma parte do programa, enquanto outros trabalham em uma segunda parte. Entre os benefícios da programação modular estão a independência e o auto-conteúdo.
# 
# A filosofia útil para nós é **pensar modularmente**, no sentido de que um programa particular possa ser agregado à uma classe maior, compondo uma biblioteca de funções. Por exemplo, supondo que queiramos construir uma biblioteca para realizar operações  matemáticas, podemos criar um módulo chamado `Vector` para realizar operações vetoriais, tais como adição, subtração e multiplicação por escalar. Assim, nosso módulo, em uma espécie de _pseudocódigo_ poderia ser como: 
# 
# ```
# Vector:
# 	sumVec(v1,v2) { v1+v2 }
# 	subtVec(v1,v2) { v1-v2 }
# 	multVec(a,v) { a*v }
# ``` 
# Qualitativamente, os exemplos acima dizem que o módulo `Vector` contém 3 funções matemáticas que dependem de dois argumentos cada, de tipos diferentes. Ela podem ser definidas, abstratamente, como: 
# 
# $$\oplus: V_1 \times V_2 \to V; \\ (v_1,v_2) \in V_1 \times V_2 \mapsto v_1 + v_2 \in V$$
# 
# $$\ominus: V_1 \times V_2 \to V; \\ (v_1,v_2) \in V_1 \times V_2 \mapsto v_1 - v_2 \in V$$
# 
# $$\otimes: A \times V \to U; \\ (a,v) \in A \times V \mapsto av \in U,$$ 
# 
# para subespaços vetoriais $U,V_1,V_2 \subset V$ e $A \in \mathbb{R}$.
# 
