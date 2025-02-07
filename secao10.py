""" Secretaria do meio Ambiente controla o nível de poluição. O índice varia de 0,05 até 0,25. Se o índice sobe para
    0,3 empresas do 1º grupo devem ser notificadas. Subindo para 0,4 empresas do 1º e 2º grupo devem ser avisados. Se
    chegar a 0,5 todos os grupos são avisados a pararem suas atividades"""

nivel_poluicao = float(input('Digite o nível de poluição: '))
if nivel_poluicao >= 0.3 and nivel_poluicao < 0.4:
    print('Grupo 01 suspender suas atividades!')
elif nivel_poluicao >= 0.4 and nivel_poluicao < 0.5:
    print('Grupo 01 e 02 suspender suas atividades!')
elif nivel_poluicao >= 0.5:
    print('Todos os Grupos devem suspender suas atividades!')
else:
    print('Níveis aceitáveis.')
