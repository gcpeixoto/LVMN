#!/usr/bin/env python
# coding: utf-8

# (clipping-patriot)=
# # Recorte 5: Um desastre motivado por erros numéricos
# 
# ## A falha da bateria americana _Patriot_ na Guerra do Golfo
# 
# Traduzido com adaptação da página pessoal do [Prof. Kees Vuik, da TU Delft](http://ta.twi.tudelft.nl/users/vuik/wi211/disasters.html).
# 
# Em 25 de fevereiro de 1991, durante a Guerra do Golfo, uma bateria americana _Patriot_ em Dharan, na Arábia Saudita, falhou em interceptar um míssil Scud lançado pelos iraquianos. O Scud atingiu um QG do exército americano matando 28 soldados. 
# 
# Um relatório do escritório de contabilidade geral - _General Accounting Office_ GAO/IMTEC-92-26, intitulado "Sistema de defesa Patriot: problema de software levou à falha do sistema em Dharan, Arábia Saudita" (original: _Patriot Missile Defense: Software Problem Led to System Failure at Dhahran, Saudi Arabia_) registrou a causa da falha, que foi motivada por um cálculo inacurado do tempo devido a erros aritméticos do computador. Especificamente, o tempo, em décimos de segundo, como medido pelo relógio interno do sistema, foi multiplicado por 1/10 para produzir o tempo em segundos. Este cálculo foi realizado usando um registro de ponto fixo de 24 bits.
# 
# Em particular, o valor 1/10, que tem uma expansão binária não finita, foi truncado em 24 bits após o ponto decimal. O pequeno erro de truncamento, quando multiplicado pelo grande número que dá o tempo em décimos de segundo, leva a um erro significativo. Na verdade, a bateria _Patriot_ havia aumentado cerca de 100 horas, e um cálculo fácil mostra que o erro de tempo resultante devido ao erro de truncamento aumentava aproximadamente 0,34 segundos. 
# 
# O número $1/10 = 1/2^4 + 1/2^5 + 1/2^8 + 1/2^9 + 1/2^{12} + 1/2^{13} + \ldots$
# 
# Em outras palavras, a expansão binária de 1/10 é 
# 
# $$0.0001100110011001100110011001100.$$ 
# 
# Agora, o registro de 24 bits no Patriot armazenado fora
# 
# $$0.00011001100110011001100,$$ 
# apresentando um erro de 
# 
# $0,0000000000000000000000011001100...$ ou, aproximadamente, $0,000000095$ em decimal. Multiplicando pelo número de décimos de segundo em 100 horas isto dá $0,000000095 \times 100 \times 60 \times 60 \times 10 = 0,34.$
# 
# Um Scud viaja cerca de 1,676 metros por segundo e, portanto, mais de meio quilômetro neste tempo. Isso foi o suficiente para que o Scud estivesse fora do alcance de rastreamento do Patriot. Ironicamente, o fato de que o cálculo do tempo ruim foi melhorado em algumas partes do código, mas não em todo ele, contribuiu para o problema, uma vez que isso significava que as imprecisões não deixassem de existir.
# 
# ## Relatório
# 
# O parágrafo a seguir é extraído do relatório do GAO:
# 
# A previsão da faixa de alcance de onde o Scud aparecerá em seguida é uma função da velocidade conhecida do Scud e do tempo da última detecção no radar. A velocidade é um número real que pode ser expresso como um número inteiro e um decimal (por exemplo, 3750.2563... milhas por hora). O tempo é mantido continuamente pelo relógio interno do sistema em décimos dos segundos, mas é expresso como número inteiro (por exemplo, 32, 33, 34,...). Quanto mais tempo o sistema estiver funcionando, maior o número representando o tempo. 
# 
# Para prever onde o Scud aparecerá, o tempo e a velocidade devem ser expressos como números reais. Devido ao modo como o computador do _Patriot_ executa seus cálculos e o fato de seus registros terem apenas 24 bits de comprimento, a conversão do tempo de um número inteiro para um número real não pode ser mais precisa do que 24 bits. Esta conversão resulta em uma perda de precisão causando um cálculo de tempo menos preciso. 
# 
# O efeito dessa imprecisão no cálculo da faixa de alcance é diretamente proporcional à velocidade do alvo e o comprimento do sistema em execução. Consequentemente, a conversão após o _Patriot_ ter sido executado continuamente por períodos prolongados faz com que a faixa de alcance se afaste do centro do alvo, tornando menos provável que o alvo, nesse caso, um Scud, seja interceptado com sucesso.
