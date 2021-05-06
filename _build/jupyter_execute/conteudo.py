# Laboratório Virtual de Métodos Numéricos - LVMN


Conteúdo para formação complementar empregável em cursos de graduação introdutórios sobre métodos numéricos para aprendizagem ativa baseada em problemas. 

Este conteúdo é ensinado na disciplina _Cálculo Numérico_ (GDCOC0072) ministrada pelo [Prof. Gustavo Oliveira](https://gcpeixoto.github.io) (UFPB/CI/DCC). Todo material é desenvolvido no âmbito do [Projeto Numbiosis](http://numbiosis.ci.ufpb.br/pt/inicio/) com suporte do Programa Institucional de Monitoria.

Aplicações específicas em Javascript que simulam diversos métodos do curso foram desenvolvidas pelo egresso [Vinícius Veríssimo](https://github.com/Vnicius) e estão disponíveis [aqui](https://vnicius.github.io/numbiosis/).


## Programa geral do curso

_Notebooks_ com notas de aula, exemplos resolvidos, algoritmos e exercícios de programação.

### I. Introdução

- [Aula 00 - Modelagem](aula-00-modelagem-programacao.ipynb)
- [Aula 01 - Ponto flutuante](aula-01-ponto-flutuante.ipynb)
- [Aula 02 - Erros numéricos](aula-02-erros.ipynb)

### II. Determinação de raízes

- [Aula 03 - Análise gráfica](aula-03-analise-grafica.ipynb)
- [Aula 04 - Bisseção](aula-04-bissecao.ipynb)
- [Aula 05 - Ponto fixo](aula-05-ponto-fixo.ipynb)
- [Aula 06 - Newton](aula-06-newton.ipynb)
- [Aula 07 - Secante](aula-07-secante.ipynb)
- [Aula 08 - Müller](aula-08-muller.ipynb)

### III. Solução de sistemas de equações

- [Aula 09 - Eliminação Gaussiana](aula-09-eliminacao-gauss.ipynb)
- [Aula 10 - Fatoração LU](aula-10-fatoracao-lu.ipynb)
- [Aula 11 - Cholesky](aula-11-cholesky.ipynb)
- [Aula 12 - Jacobi](aula-12-jacobi.ipynb)
- [Aula 13 - Newton não-linear](aula-13-newton-nao-linear.ipynb)

### IV. Interpolação e ajuste de curvas

- [Aula 14 - Interpolação de Lagrange](aula-14-interpolacao-lagrange.ipynb)
- [Aula 15 - Interpolação de Newton](aula-15-interpolacao-newton.ipynb)
- [Aula 16 - Mínimos quadrados](aula-16-minimos-quadrados.ipynb)
- [Aula 17 - Ajuste não linear](aula-17-ajusteNaoLinear.ipynb)

### V. Integração e diferenciação numérica

- [Aula 18 - Integração por Newton-Cotes](aula-18-integracao-newtonCotes.ipynb)
- [Aula 19 - Quadratura Gaussiana](aula-19-quadratura-gaussiana.ipynb)
- [Aula 20 - Diferenciação numérica](aula-20-diferenciacao-numerica.ipynb)


### VI. Métodos numéricos para EDOs

- [Aula 21 - Solução numérica de EDOs](aula-21-solucoes-edo.ipynb)
- [Aula 22 - Método de Euler](aula-22-metodo-euler.ipynb)
- [Aula 23 - Métodos de Taylor e Runge-Kutta de 2a. ordem](aula-23-taylor-rungeKutta.ipynb)

## _Code sessions_

_Notebooks_ com um compêndio de funções de utilidade predefinidas em módulos Python para resolução direta de problemas aplicados às ciências matemáticas, computacionais e engenharias.

- [Code session 1 - bisect](codeSession-1-bisect.ipynb)
- [Code session 2 - newton](codeSession-2-newton.ipynb)
- [Code session 3 - roots](codeSession-3-polyval.ipynb)
- [Code session 4 - fsolve](codeSession-4-fsolve.ipynb)
- [Code session 5 - solve](codeSession-5-solve.ipynb)
- [Code session 6 - interp](codeSession-6-interp.ipynb)
- [Code session 7 - fit](codeSession-7-fit.ipynb)
- [Code session 8 - integrate](codeSession-8-integrate.ipynb)
- [Code session 9 - solve_ivp](codeSession-9-solveivp.ipynb)

## _Listas de exercícios_

_Notebooks_ contendo solucionário matemático e computacional de exercícios gerais de menor complexidade.

- [Lista 1](lista-1-solucoes.ipynb)
- [Lista 2](lista-2-solucoes.ipynb)
- [Lista 3](lista-3-solucoes.ipynb) 
- [Lista 4](lista-4-solucoes.ipynb) 
- [Lista 5](lista-5-solucoes.ipynb)
- [Lista 6](lista-6-solucoes.ipynb) 

## _Conteúdo Extra_

_Notebooks_ com conteúdos complementares não contemplados no curso regular.

- [Malhas numéricas](extra/extra-malhasNumericas.ipynb)

- [Campos de direção para EDOs](extra/extra-camposDirecao.ipynb)
- [Melhoramentos do método de Euler](extra/extra-eulerMelhorado.ipynb)
- [Estabilidade do método de Euler](extra/extra-estabilidadeEuler.ipynb)
- [Método de Euler implícito](extra/extra-eulerImplicito.ipynb)
- [Métodos de múltiplos passos: _Adams-Bashfort_](extra/extra-multistep-adamsBashfort.ipynb)
- [EDOs de ordem superior](extra/extra-edo-superior.ipynb)
- [Sistemas de EDOs](extra/extra-sistemas-edp.ipynb)

- [Transformada de Fourier](extra/extra-fft.ipynb)

- [Otimização de código](extra/extra-numba.ipynb)

## Como contribuir?

O projeto Numbiosis não recebe financiamento direto para bolsas. Todo o conteúdo é desenvolvido pelo Prof. Gustavo Oliveira e alunos (monitores e/ou tutores bolsistas ou voluntários, bem como aqueles que se matriculam no curso e contribuem com melhorias). O material é revisado constantemente, mas possui suporte limitado.

Você é estudante da UFPB e gostaria de contribuir com o projeto? Entre em contato com o Prof. Gustavo.

### Temas abertos no âmbito do projeto Numbiosis

- Implementação de gráficos interativos para visualização 3D de processos iterativos.
- Desenvolvimento de APIs para integração de códigos da base Numbiosis em Github/Gitlab.
- Configuração de web server JupyterHub para hospedagem de materiais para mini-cursos remotos.
- Desenvolvimento de códigos demonstrativos em Python para aplicações em Engenharias.
- Geração de material didático portável (projeto de ensino).

## Iniciação científica

Consulte projetos do LaMEP/CI/UFPB em: 

- Computação científica em petróleo e gás
- Ciência de dados para o setor energético 
- Inteligência artificial e visão computacional em sísmica


```{toctree}
:hidden:
:titlesonly:
:numbered: True
:caption: Cadernos

aula-00-modelagem-programacao
aula-01-ponto-flutuante
aula-02-erros
aula-03-analise-grafica
aula-04-bissecao
aula-05-ponto-fixo
aula-06-newton
aula-07-secante
aula-08-muller
aula-09-eliminacao-gauss
aula-10-fatoracao-lu
aula-11-cholesky
aula-12-jacobi
aula-13-newton-nao-linear
aula-14-interpolacao-lagrange
aula-15-interpolacao-newton
aula-16-minimos-quadrados
aula-17-ajusteNaoLinear
aula-18-integracao-newtonCotes
aula-19-quadratura-gaussiana
aula-20-diferenciacao-numerica
aula-21-solucoes-edo
aula-22-rungeKutta2
```


```{toctree}
:hidden:
:titlesonly:
:caption: Code sessions

codeSession-1-bisect
codeSession-2-newton
codeSession-3-polyval
codeSession-4-fsolve
codeSession-5-solve
codeSession-6-interp
codeSession-7-fit
codeSession-8-integrate
```


```{toctree}
:hidden:
:titlesonly:
:caption: Exercícios resolvidos

lista-1-solucoes
lista-2-solucoes
lista-3-solucoes
lista-4-solucoes
lista-5-solucoes
lista-6-solucoes
```


```{toctree}
:hidden:
:titlesonly:
:numbered: True
:caption: Extra

extra/extra-fft
extra/extra-numba
```
