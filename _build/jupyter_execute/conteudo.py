#!/usr/bin/env python
# coding: utf-8

# # Laboratório Virtual de Métodos Numéricos - LVMN
# 
# O LVMN é constituído de uma coleção de materiais digitais para cursos de graduação em ciências exatas, computacionais e engenharias que possuam disciplinas de métodos numéricos ou afins em seus currículos. 
# 
# ## Curso
# 
# Este conteúdo é ensinado na disciplina _Cálculo Numérico_ (GDCOC0072) ministrada pelo [Prof. Gustavo Oliveira](https://gcpeixoto.github.io) (UFPB/CI/DCC). O material começou a ser desenvolvido pelo professor no âmbito do [Projeto Numbiosis](http://numbiosis.ci.ufpb.br/pt/inicio/) em 2017 e recebeu suporte do Programa Institucional de Monitoria até o ano de 2020.
# 
# Aplicações específicas em Javascript que simulam diversos métodos do curso foram desenvolvidas pelo egresso [Vinícius Veríssimo](https://github.com/Vnicius) e estão disponíveis [aqui](https://vnicius.github.io/numbiosis/).
# 
# ## Objetivos do curso
# 
# - Apresentar o universo dos métodos numéricos a estudantes de graduação em ciências exatas;
# - Estimular a aprendizagem ativa através da resolução de projetos e problemas do mundo real;
# - Fomentar a maturidade do pensamento computacional e as habilidades de programação através do ecossistema Python para métodos numéricos; 
# 
# ## Programa geral do curso
# 
# O curso contém cadernos interativos, exemplos resolvidos, algoritmos,  exercícios de programação, sessões de código
# 
# ### I. Introdução
# 
# - [Aula 00 - Modelagem](aula-00-modelagem-programacao.ipynb)
# - [Aula 01 - Ponto flutuante](aula-01-ponto-flutuante.ipynb)
# - [Aula 02 - Erros numéricos](aula-02-erros.ipynb)
# 
# ### II. Determinação de raízes
# 
# - [Aula 03 - Análise gráfica](aula-03-analise-grafica.ipynb)
# - [Aula 04 - Bisseção](aula-04-bissecao.ipynb)
# - [Aula 05 - Ponto fixo](aula-05-ponto-fixo.ipynb)
# - [Aula 06 - Newton](aula-06-newton.ipynb)
# - [Aula 07 - Secante](aula-07-secante.ipynb)
# - [Aula 08 - Müller](aula-08-muller.ipynb)
# 
# ### III. Solução de sistemas de equações
# 
# - [Aula 09 - Eliminação Gaussiana](aula-09-eliminacao-gauss.ipynb)
# - [Aula 10 - Fatoração LU](aula-10-fatoracao-lu.ipynb)
# - [Aula 11 - Cholesky](aula-11-cholesky.ipynb)
# - [Aula 12 - Jacobi](aula-12-jacobi.ipynb)
# - [Aula 13 - Newton não-linear](aula-13-newton-nao-linear.ipynb)
# 
# ### IV. Interpolação e ajuste de curvas
# 
# - [Aula 14 - Interpolação de Lagrange](aula-14-interpolacao-lagrange.ipynb)
# - [Aula 15 - Interpolação de Newton](aula-15-interpolacao-newton.ipynb)
# - [Aula 16 - Mínimos quadrados](aula-16-minimos-quadrados.ipynb)
# - [Aula 17 - Ajuste não linear](aula-17-ajusteNaoLinear.ipynb)
# 
# ### V. Integração e diferenciação numérica
# 
# - [Aula 18 - Integração por Newton-Cotes](aula-18-integracao-newtonCotes.ipynb)
# - [Aula 19 - Quadratura Gaussiana](aula-19-quadratura-gaussiana.ipynb)
# - [Aula 20 - Diferenciação numérica](aula-20-diferenciacao-numerica.ipynb)
# 
# 
# ### VI. Métodos numéricos para EDOs
# 
# - [Aula 21 - Solução numérica de EDOs](aula-21-solucoes-edo.ipynb)
# - [Aula 22 - Método de Euler](aula-22-metodo-euler.ipynb)
# - [Aula 23 - Métodos de Taylor e Runge-Kutta de 2a. ordem](aula-23-taylor-rungeKutta.ipynb)
# 
# ## _Code sessions_
# 
# _Notebooks_ com um compêndio de funções de utilidade predefinidas em módulos Python para resolução direta de problemas aplicados às ciências matemáticas, computacionais e engenharias.
# 
# - [Code session 1 - bisect](codeSession-1-bisect.ipynb)
# - [Code session 2 - newton](codeSession-2-newton.ipynb)
# - [Code session 3 - roots](codeSession-3-polyval.ipynb)
# - [Code session 4 - fsolve](codeSession-4-fsolve.ipynb)
# - [Code session 5 - solve](codeSession-5-solve.ipynb)
# - [Code session 6 - interp](codeSession-6-interp.ipynb)
# - [Code session 7 - fit](codeSession-7-fit.ipynb)
# - [Code session 8 - integrate](codeSession-8-integrate.ipynb)
# - [Code session 9 - solve_ivp](codeSession-9-solve_ivp.ipynb)
# 
# ## _Listas de exercícios_
# 
# _Notebooks_ contendo solucionário matemático e computacional de exercícios gerais de menor complexidade.
# 
# - [Lista 1](lista-1-solucoes.ipynb)
# - [Lista 2](lista-2-solucoes.ipynb)
# - [Lista 3](lista-3-solucoes.ipynb) 
# - [Lista 4](lista-4-solucoes.ipynb) 
# - [Lista 5](lista-5-solucoes.ipynb)
# - [Lista 6](lista-6-solucoes.ipynb) 

# ## _Conteúdo Extra_
# 
# _Notebooks_ com conteúdos complementares não contemplados no curso regular.
# 
# - [Números em ponto flutuante e seus problemas](extra/extra-pontoFlutuante.ipynb)
# - [Malhas numéricas](extra/extra-malhasNumericas.ipynb)
# - [Plotagem com _matplotlib_: tópicos especiais](extra/extra-matplotlibTopicos.ipynb)
# - [Campos de direção para EDOs](extra/extra-camposDirecaoEDO.ipynb)
# - [Melhoramentos do método de Euler](extra/extra-eulerMelhorado.ipynb)
# - [Estabilidade do método de Euler](extra/extra-estabilidadeEuler.ipynb)
# - [Método de Euler implícito](extra/extra-eulerImplicito.ipynb)
# - [Métodos de múltiplos passos: _Adams-Bashfort_](extra/extra-multistep-adamsBashfort.ipynb)
# - [EDOs de ordem superior](extra/extra-edoSuperior.ipynb)
# - [Sistemas de EDOs](extra/extra-sistemasEDO.ipynb)
# - [Transformada de Fourier](extra/extra-fft.ipynb)
# - [Otimização de código](extra/extra-numba.ipynb)

# ## Livro complementar
# 
# O livro [Introdução à Linguagem Python para Ciências Computacionais e Engenharia](https://gcpeixoto.github.io/lecture-ipynb/indice.html), traduzido pelo professor, fornece conhecimento básico para discentes que não possuam experiência com Python, permitindo que acompanhem o curso em paralelo.

# ## Como contribuir?
# 
# O projeto Numbiosis não recebe financiamento direto para bolsas. Todo o conteúdo é desenvolvido pelo Prof. Gustavo Oliveira e alunos (monitores e/ou tutores bolsistas ou voluntários, bem como aqueles que se matriculam no curso e contribuem com melhorias). O material passa por revisões periodicamente, mas possui suporte limitado.
# 
# Você é estudante da UFPB e gostaria de contribuir com o projeto? Entre em contato com o Prof. Gustavo.
# 
# ### Alguns temas abertos no âmbito do projeto Numbiosis
# 
# - Implementação de gráficos interativos para visualização 3D de processos iterativos.
# - Desenvolvimento de APIs para integração de códigos da base Numbiosis em Github/Gitlab.
# - Configuração de web server JupyterHub para hospedagem de materiais para mini-cursos remotos.
# - Desenvolvimento de códigos demonstrativos em Python para aplicações em Engenharias.
# - Geração de material didático portável (projeto de ensino).
# - Integração de ferramentas de _autograding_.
# - Programação orientada a objetos para criação de _smart courses_ (módulos para geração de questões customizadas, avaliações e compilações em Latex).

# ## Iniciação científica e outros projetos
# 
# Consulte projetos nos horizontes estratégicos do [TRIL Lab](http://tril.ci.ufpb.br). Estamos no [Centro de Informática](http://ci.ufpb.br) da UFPB. Alguns temas de interesse são:
# 
# - Computação científica para aplicações em engenharia
# - Ciência de dados para o setor energético 
# - Dinâmica dos fluidos computacional
