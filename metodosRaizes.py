#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:10:55 2018

@author: gustavo
"""

import inspect, re
from numpy import *
from matplotlib.pyplot import plot, legend


# Método da Bissecao
def bissecao(f,a,b,tol,N,var):
    """
    Metodo da bissecao para funcoes unidimensionais

    entrada:     
        f - uma string dependendo de x, i.e., a funcao
            (e.g., 'x**2 + 1', 'x**2*cos(x)', etc.) 
        a - limite inferior do dominio
        b - limite superior do dominio
      tol - tolerancia    
        N - numero maximo de iteracoes

    saida: 
    
       xm - raiz da funcao
"""
        
    # TODO identificar a variável usada na função 
    #      Aqui, tentei assumir que apenas uma era usada (e.g. 'x'),
    #      mas foi complicado generalizar quando há objeto numpy
    #var = re.search('[a-zA-Z]+',f)
    #var = var.group()

    # cria função anônima
    f = eval('lambda ' + var + ' :' + f)

    # Se função não for de uma variável, lança erro.
    # Mais aplicável se o caso geral fosse implementado.        
    if len(inspect.getfullargspec(f).args) - 1 > 0:    
        raise ValueError('O código é válido apenas para uma variável.')

    # calcula valor da função nos extremos
    fa = f(a) 
    fb = f(b)
    
    # verifica sinal da função para o intervalo passado     
    if fa*fb >= 0:
        raise ValueError('A função deve ter sinais opostos em a e b!')
    
    # flag usada para prevenir a obtenção da raiz 
    # antes de o intervalo ter sido 
    # suficientemente reduzido
    done = 0;

    # loop principal

    # bisecta o intervalo
    xm = (a+b)/2

    i = 1 # contador 

    while abs(a-b) >= tol and abs(f(xm)) >= tol and ( not done or N != 0 ):
    # avalia a função no ponto médio
        fxm = f(xm)
        
        print("i={0:d} a={1:f} b={2:f} xm={3:f} f(a)={4:f} f(b)={5:f} f(xm)={6:f} b-a={7:f}".format(i,a,b,xm,fa,fb,fxm,abs(a-b)))
   
        if fa*fxm < 0:       # Raiz esta à esquerda de xm
            b = xm
            fb = fxm
            xm = (a+b)/2
        elif fxm*fb < 0:     # Raiz esta à direita de xm
            a = xm
            fa = fxm
            xm = (a+b)/2
        else:               # Achamos a raiz
            done = 1
    
        N -= 1              # Atualiza passo
        i += 1              # Atualiza contador
   
    print("i={0:d} a={1:f} b={2:f} xm={3:f} f(a)={4:f} f(b)={5:f} f(xm)={6:f} b-a={7:f}".format(i,a,b,xm,fa,fb,f(xm),abs(a-b)))
    print("Solução encontrada: {0}".format(xm))

    return xm

def falsa_posicao(f,a,b,tol,N,var):
        
    # TODO identificar a variável usada na função 
    #      Aqui, tentei assumir que apenas uma era usada (e.g. 'x'),
    #      mas foi complicado generalizar quando há objeto numpy
    #var = re.search('[a-zA-Z]+',f)
    #var = var.group()

    # cria função anônima
    f = eval('lambda ' + var + ' :' + f)

    # Se função não for de uma variável, lança erro.
    # Mais aplicável se o caso geral fosse implementado.        
    if len(inspect.getfullargspec(f).args) - 1 > 0:    
        raise ValueError('O código é válido apenas para uma variável.')

    # calcula valor da função nos extremos
    fa = f(a) 
    fb = f(b)
    
    # verifica sinal da função para o intervalo passado     
    if fa*fb >= 0:
        raise ValueError('A função deve ter sinais opostos em a e b!')
    
    # flag usada para prevenir a obtenção da raiz 
    # antes de o intervalo ter sido 
    # suficientemente reduzido
    done = 0;

    # loop principal

    # bisecta o intervalo
    xm = ( a*fb - b*fa )/( fb - fa )

    i = 1 # contador 

    while abs(a-b) >= tol and abs(f(xm)) >= tol and ( not done or N != 0 ):
    # avalia a função no ponto médio
        fxm = f(xm)
        print("i={0:d} a={1:f} b={2:f} xm={3:f} f(a)={4:f} f(b)={5:f} f(xm)={6:f} b-a={7:f}".format(i,a,b,xm,fa,fb,fxm,abs(a-b)))
        
        if fa*fxm < 0:       # Raiz esta à esquerda de xm
            b = xm
            fb = fxm
            xm = ( a*fb - b*fa )/( fb - fa )
        elif fxm*fb < 0:     # Raiz esta à direita de xm
            a = xm
            fa = fxm
            xm = ( a*fb - b*fa )/( fb - fa )
        else:               # Achamos a raiz
            done = 1
    
        N -= 1              # Atualiza passo
        i += 1              # Atualiza contador
            
    print("i={0:d} a={1:f} b={2:f} xm={3:f} f(a)={4:f} f(b)={5:f} f(xm)={6:f} b-a={7:f}".format(i,a,b,xm,fa,fb,f(xm),abs(a-b)))    
    print("Solução encontrada: {0}".format(xm))

    return xm

   
def newton(x0,f,df,tol,N,vis):
    """ 
    Resolve problema de determinacao de raizes pelo 
    metodo de Newton.
    
    entrada: 
    
       x0  - aproximacao inicial        (float)
        f  - funcao a ser resolvida     (str)
       df  - derivada da funcao         (str)
       tol - tolerancia                 (float)       
         N - numero maximo de iteracoes (int)
      vis  - flag para plotagem         (bool)
      
    saida:  
    
       x   - raiz aproximada para f     (float)      
    """
  
    f = eval('lambda x:' + f)
    df = eval('lambda x:' + df)

    # imprime estimativa inicial
    print('Estimativa inicial: x0 = {0}\n'.format(x0))  

    # tabela
    print('i\t x\t\t f(x)\t\t df(x)\t\t ER')  
    print('{0:d}\t {1:f}\t {2:f}\t {3:f}\t -'.format(0,x0,f(x0),df(x0)))       
    
    # Loop 
    for i in range(0,N):
        
        x = x0 - f(x0)/df(x0) # funcao de iteracao 
        
        e = abs(x-x0)/abs(x) # erro
        
        # tabela
        print('{0:d}\t {1:f}\t {2:f}\t {3:f}\t {4:e}'.format(i+1,x,f(x),df(x),e))       
        
        if e < tol and abs(f(x)) < tol:
            break
        x0 = x                
        
    if i == N:
        print('Solução não obtida em {0:d} iterações'.format(N))
    else:
        print('Solução obtida: x = {0:.10f}'.format(x))

    # plotagem
    if vis == True:        
        dx = 2*x
        dom = linspace(x - dx,x + dx,30)
        plot(dom,f(dom),label='$f(x)$')
        plot(x,f(x),'ro')

    return x
      
def ponto_fixo(x0,f,g,tol,N,vis):
    """ 
    Resolve problema de determinacao de raizes pelo 
    metodo do ponto fixo (iteracao linear).
    
    entrada: 
    
       x0  - aproximacao inicial        (float)
        f  - funcao a ser resolvida     (str)
        g  - funcao de iteracao         (str)
       tol - tolerancia                 (float)
        N  - numero maximo de iteracoes (int)
      vis  - flag para plotagem         (bool)
      
    saida:  
    
       x   - raiz aproximada para f     (float)      
    """
 
    # funcoes
    f = eval('lambda x:' + f)
    g = eval('lambda x:' + g)
    
    # inicializacao
    it = 0 # contador 
    x, xn = x0, x0 + 1 # iteradas atual, anterior
    
    e = abs(x-xn)/abs(x) # erro    

    # tabela
    print('i\t x\t\t f(x)\t\t ER')
    print('{0:d}\t {1:f}\t {2:f}\t {3:e}'.format(it,x,f(x),e))       
    
    # laco
    while e >= tol and it <= N:
        it += 1    
        xn = x                             
        x = g(xn)               
        e = abs(x-xn)/abs(x)         
        print('{0:d}\t {1:f}\t {2:f}\t {3:e}'.format(it,x,f(x),e))      
        
        if it > N:
            print('Solução nao alcancada com N iteracoes.')
            break
       
    if vis == True:
        dx = 2*x
        dom = linspace(x - dx,x + dx,30)
        plot(dom,f(dom),label='$f(x)$')
        plot(dom,dom*0,label='$y=0$')
        plot(dom,g(dom),label='$g(x)$')
        plot(dom,dom,label='$y=x$')
        legend()
        
    return x
        
    
def secante(xa,xb,f,tol,N,vis):
    """ 
    Resolve problema de determinacao de raizes pelo 
    metodo das secantes.
    
    entrada: 
    
       xa  - 1a. aproximacao inicial    (float)
       xb  - 2a. aproximacao inicial    (float)
        f  - funcao a ser resolvida     (str)
        g  - funcao de iteracao         (str)
       tol - tolerancia                 (float)       
        N  - numero maximo de iteracoes (int)
      vis  - flag para plotagem         (bool)
      
    saida:  
    
       x   - raiz aproximada para f     (float)      
    """
        
    f = eval('lambda x:' + f)

    # imprime estimativas iniciais
    print('Estimativas iniciais: xa = {0}; xb = {1} \n'.format(xa,xb))  

    # tabela
    print('i\t x\t\t f(x)\t\t ER')        
   
    # Loop         
    for i in range(0,N):
        
        x = (xa*f(xb) - xb*f(xa))/(f(xb) - f(xa))
                        
        e = abs(x-xb)/abs(x) # erro
                
        # tabela
        print('{0:d}\t {1:f}\t {2:f}\t {3:e}'.format(i+1,x,f(x),e)) 
        
        if e < tol:
            break
        xa = xb
        xb = x
        
    if i == N:
        print('Solução não obtida em {0:d} iterações'.format(N))
    else:
        print('Solução obtida: x = {0:.10f}'.format(x))

    # plotagem
    if vis == True:        
        dx = 2*x
        dom = linspace(x - dx,x + dx,30)        
        plot(dom,f(dom),label='$f(x)$')
        plot(x,f(x),'ro')

    return x        

if __name__ == '__main__':
    None
