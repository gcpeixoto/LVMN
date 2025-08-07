#!/usr/bin/env python
# coding: utf-8

# # Recorte 1: Breve Histórico da Análise Numérica
# 
# O texto abaixo é um excerto do prefácio do livro _The birth of Numerical Analysis_, editado por A. Bultheel e R. Cools e publicado pela _World Scientific_, com leves adaptações.
# 
# ## As limitações dos computadores
# 
# Na _Wikipedia_, a análise numérica é descrita como a parte da matemática onde algoritmos para problemas da _matemática contínua_ são estudados (ao contrário da _matemática discreta_). Isso significa que ela lida, especialmente, com variáveis reais e complexas, soluções de equações diferenciais e outros problemas comparáveis caracterizados na física e na engenharia. 
# 
# Um número real possui, em princípio, um número infinito de dígitos, mas em um computador digital, apenas um número finito de _bits_ é reservado para armazenar um número real. Essa restrição de memória implica que somente valores arredondados e aproximados de alguns números reais podem ser armazenados. 
# 
# A idéia ingênua dos primeiros dias dos computadores digitais era que eles não cometeriam os mesmos "erros estúpidos" que os computadores humanos às vezes cometiam, como erros de transcrição, erros de leitura, sinais errados etc. Esta euforia foi, no entanto, bem temperada quando se percebeu que, na verdade, os computadores cometem erros em praticamente todos os cálculos. Erros simples, mas, apesar disso, muitos, e todos esses pequenos erros podem se acumular e crescer como um vírus através dos muitos cálculos elementares realizados que eventualmente poderiam dar um resultado bem diferente do exato.
# 
# ## 1947: o ano de um novo começo
# 
# Uma análise cuidadosa dessa propagação de erros quando se resolve um sistema linear de equações foi publicada pela primeira vez em um artigo de John von Neumann e Herman Goldstine: _Numerical inverting of matrices of high order_, publicado na edição de novembro do _Bulletin of the American Mathematical Society_ em 1947. Como esta foi a primeira vez que essa análise foi feita, esse artigo é às vezes considerado o princípio da análise numérica moderna. É claro que cálculos numéricos foram realizados bem antes desse artigo, e os problemas da física e da engenharia haviam sido resolvidos anteriormente, mas a escala e a complexidade dos cálculos aumentaram drasticamente com a introdução dos computadores digitais. 
# 
# ## Complexidade computacional: da centena ao bilhão em algumas décadas
# 
# Os "sistemas de grande porte" a que se refere o título do documento, não seriam chamados de "grandes" pelos padrões atuais. Afirma-se no artigo que problemas sérios poderiam ocorrer se alguém quisesse resolver sistemas de mais de dez equações. Em uma nota de rodapé subsequente, é sugerido que provavelmente seria possível, no futuro, resolver sistemas de cem equações. Se soubéssemos que o algoritmo _PageRank_ do Google manipula sistemas de aproximadamente dez bilhões de equações, então seria claro que chegamos a uma longa distância.
