#!/usr/bin/env python
# coding: utf-8

# # Laboratório Virtual de Métodos Numéricos - LVMN
# 
# O Laboratório Virtual de Métodos Numéricos - LVMN é constituído de uma coleção de materiais digitais para cursos de graduação em ciências exatas, computacionais e engenharias que possuam disciplinas de métodos numéricos ou afins em seus currículos. 
# 
# ## Sobre o curso
# 
# Este conteúdo é ensinado na disciplina _Cálculo Numérico_ (GDCOC0072) ministrada pelo [Prof. Gustavo Oliveira](https://gcpeixoto.github.io) (UFPB/CI/DCC). O material começou a ser desenvolvido pelo professor no âmbito do [Projeto Numbiosis](http://numbiosis.ci.ufpb.br/pt/inicio/) em 2017. Até o ano de 2020, recebeu suporte do Programa Institucional de Monitoria com contribuições ativas. Desde então, o projeto segue com suporte reduzido e possui atualizações esporádicas. Aplicações em _javascript_ que simulam diversos métodos do curso foram desenvolvidas com uma contribuição considerável do egresso [Vinícius Veríssimo](https://github.com/Vnicius) e estão disponíveis [aqui](https://vnicius.github.io/numbiosis/).
# 
# ## Objetivos do LVMN
# 
# Os objetivos gerais do LVMN são:
# 
# - Apresentar o universo dos métodos numéricos a estudantes de graduação em ciências exatas;
# - Estimular a aprendizagem ativa através da resolução de projetos e problemas do mundo real; e 
# - Fomentar a maturidade do pensamento computacional e as habilidades de programação através do ecossistema Python para métodos numéricos; 
# 
# ## Programa geral do curso
# 
# O curso contém uma série de materiais educativos que estimulam várias habilidades e proporcionam que estudantes com necessidades distintas de aprendizagem encontrem o recurso mais adequuado para si. O conteúdo está organizado em cadernos interativos que incluem:
# - exemplos teóricos e aplicados;
# - banco de dados de problemas reais;
# - algoritmos demonstrativos;
# - receitas de código; 
# - sessões práticas dedicadas;
# - dicas de programação e
# - recortes suplementares.
# 
# O curso cobre não apenas os assuntos clássicos que costumam ser ensinados em disciplinas equivalentes em qualquer curso superior de universidades nacionais ou estrangeiras, mas também traz inserções sobre assuntos modernos que se entrelaçam para produzir uma engenharia cada vez mais centrada em dados. O livro-texto pretende mostrar que conceitos tradicionais são a base para os _métodos numéricos de nova geração_, que criam interdisciplinaridade com temáticas do estado-da-arte, tais como aprendizado de máquina, redes neurais informadas pela física, modelos de ordem reduzida e outras técnicas que fazem interface com a ciência da computação e outaas áreas aplicadas.
# 
# Abaixo vemos a estrutura do livro-texto organizada em seis partes maiores:
# 
# ### I. Modelagem e computação
# 
# - [Aula 00 - Modelagem](aula-00-modelagem-programacao.ipynb)
# - [Aula 01 - Ponto flutuante](aula-01-ponto-flutuante.ipynb)
# - [Aula 02 - Erros numéricos](aula-02-erros.ipynb)
# 
# ### II. Determinação de raízes de equações unidimensionais
# 
# - [Aula 03 - Análise gráfica](aula-03-analise-grafica.ipynb)
# - [Aula 04 - Bisseção](aula-04-bissecao.ipynb) <!-- - [Aula 05 - Ponto fixo](aula-05-ponto-fixo.ipynb) -->
# - [Aula 05 - Newton](aula-06-newton.ipynb)
# - [Aula 06 - Secante](aula-07-secante.ipynb)
# - [Aula 07 - Müller](aula-08-muller.ipynb)
# 
# ### III. Solução de sistemas de equações multidimensionais
# 
# - [Aula 08 - Elementos de Álgebra Linear Computacional](aula-08a-matrizes-vetores.ipynb)
# - [Aula 09 - Eliminação Gaussiana](aula-09-eliminacao-gauss.ipynb)
# - [Aula 10 - Fatoração LU](aula-10-fatoracao-lu.ipynb)
# - [Aula 11 - Cholesky](aula-11-cholesky.ipynb)
# - [Aula 12 - Jacobi](aula-12-jacobi.ipynb)
# - [Aula 13 - Newton não-linear](aula-13-newton-nao-linear.ipynb)
# 
# ### IV. Ajuste de curvas
# 
# - [Aula 14 - Interpolação de Lagrange](aula-14-interpolacao-lagrange.ipynb)
# - [Aula 15 - Interpolação de Newton](aula-15-interpolacao-newton.ipynb)
# - [Aula 16 - Mínimos quadrados](aula-16-minimos-quadrados.ipynb)
# - [Aula 17 - Regressão não linear](aula-17-ajusteNaoLinear.ipynb)
# 
# ### V. Fórmulas de integração numérica 
# 
# - [Aula 18 - Integração por Newton-Cotes](aula-18-integracao-newtonCotes.ipynb)
# - [Aula 19 - Quadratura Gaussiana](aula-19-quadratura-gaussiana.ipynb)
# 
# ### VI. Diferenciação numérica e solução de equações diferenciais
# 
# - [Aula 20 - Diferenciação numérica](aula-20-diferenciacao-numerica.ipynb)
# - [Aula 21 - Solução numérica de EDOs](aula-21-solucoes-edo.ipynb)
# - [Aula 22 - Método de Euler](aula-22-metodo-euler.ipynb)
# - [Aula 23 - Métodos de Taylor e Runge-Kutta de 2a. ordem](aula-23-taylor-rungeKutta.ipynb)

# # _Code sessions_
# 
# As sessões de código (_code sessions_) são aulas dedicadas ao estudo de funções de utilidade predefinidas em módulos Python para resolução direta de problemas aplicados. Essas funções são apresentadas como "receitas prontas" que abrem caminhos para implementações de maior complexidade. 
# 
# - [Code session 1 - bisect](code-sessions/codeSession-1-bisect.ipynb)
# - [Code session 2 - newton](code-sessions/codeSession-2-newton.ipynb)
# - [Code session 3 - roots](code-sessions/codeSession-3-polyval.ipynb)
# - [Code session 4 - fsolve](code-sessions/codeSession-4-fsolve.ipynb)
# - [Code session 5 - solve](code-sessions/codeSession-5-solve.ipynb)
# - [Code session 6 - interp](code-sessions/codeSession-6-interp.ipynb)
# - [Code session 7 - fit](code-sessions/codeSession-7-fit.ipynb)
# - [Code session 8 - integrate](code-sessions/codeSession-8-integrate.ipynb)
# - [Code session 9 - solve_ivp](code-sessions/codeSession-9-solve_ivp.ipynb)
# 
# ## Listas de exercícios
# 
# Estes cadernos interativos contém o solucionário matemático e computacional de alguns exercícios gerais de menor complexidade. As listas são apenas para fixação de conceitos. 
# 
# _Obs.: este conteúdo será descontinuado no futuro._
# 
# - [Lista 1](lista-1-solucoes.ipynb)
# - [Lista 2](lista-2-solucoes.ipynb)
# - [Lista 3](lista-3-solucoes.ipynb) 
# - [Lista 4](lista-4-solucoes.ipynb) 
# - [Lista 5](lista-5-solucoes.ipynb)
# - [Lista 6](lista-6-solucoes.ipynb) 

# ## Conteúdo Extra
# 
# Alguns materiais complementares não contemplados no curso regular ou não explorados com maior detalhamento são fornecidos aqui para aguçar o interesse de estudantes para temas que orbitam ao redor dos métodos numéricos e são úteis para aplicações gerais.
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
# - [Documentação de código](extra/extra-docstrings.ipynb)

# ## Recortes
# 
# Os recortes contemplam curiosidades ou anedotas sobre tópicos variados. Acesse-os pela barra lateral de navegação.
# 
# _Obs.: este conteúdo está sendo gradualmente incorporado no livro-texto e será descontinuado no futuro_.

# ## Livro complementar
# 
# Python é a linguagem escolhida para o curso devido à sua disponibilidade gratuita, versatilidade e facilidade de aprendizagem. Como forma de nivelamento dos estudantes que não possuem experiência com Python, o livro [Introdução à Linguagem Python para Ciências Computacionais e Engenharia](https://gcpeixoto.github.io/lecture-ipynb/indice.html), traduzido pelo professor, tem o propósito de fornecer conhecimento básico da linguagem para uso no curso e uma oportunidade de estudo paralelo. Caso você se enquadre neste grupo de estudantes, não deixe de consultar este material.

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
