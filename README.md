### Programa para otimizar os ganhos de um controlador PI ou PID. ###

#Requisitos:

*Ser um sistema sem atraso de transporte\n
*Ter a função de transferencia da planta em função dos polos e zeros\n
*Ter seus requisitos de projeto em relação a maximo sobressinal e tempo de assentamento\n\n

#Passos:

*Informar os zeros da planta.    Ex: "0" ou "1,2".
*Informar os polos da planta.    Ex: "-1","-1,-2" ou "-1-1j,-1+1j".
*Informar o ganho da planta.     Ex: "10".
*Informar se o sistema de ideal é de primeira ou segunda ordem.
*Caso o sistema ideal seja de primerira ordem, informar tempo de assentamento.
*Caso o sistema ideal seja de segunda ordem, informar tempo de assentamento e maximo sobressinal.
*Escolher se quer utilizar um controlador PI ou PID
*Analisar resultado. Conferir grafico da saida junto a margem de ganho e margem de fase.

#Como Funciona:

Em resumo, atraves do algoritimo dos minimos quadrados É gerado a saida da planta e do sistema idealizado com base no tempo de assentamento e
do maximo sobressinal informado. Após isso é usado o algoritimo dos minimos quadrados para encontrar os termos do controlador escolhido (PI ou PID)
que mais aproximem a resposta da planta do sistema ideal.



