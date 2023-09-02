#resolução de um problema basico volume de controle diferencial , exemplo 4.9 fox
#Aplicação da equação de bernoulli

"""
Considerações;
    -Escoamento em regime permanente (1)
    -Ausencia de atrito (2)
    -escoamento em regime incompressivel (3)
    -Escoamento interno, não ha pressão atmosferica atuando no Volume de controle (4)
"""

#Deduzir uma expressão para a pressão manométrica mínima necessária na entrada do bocal para produzir uma vazão volumetrica qualquer.

"""
Pre-Codigo:

Equação da Continuidade:
    DM/dt= Integral[Taxa_de_Variação_massica_dentro_do_volume_de_controle](Intervalo) + Integral[Fluxo_massico_na_Superficie_de_Controle](Intervalo)=0
    
    Para a condição 1,  [Taxa_de_Variação_massica_dentro_do_volume_de_controle] = 0
    Portanto, o fluxo de massa que entra é igual ao que sai!
    
        Influxo= Efluxo
    
    Logo, 
        
        Area_1*Velocidade_inicial+ Area_2*Velocidade_Final=0 (Observar o referencial)
        
        DM/dt= Area_1*Velocidade_inicial+ Area_2*Velocidade_Final= 0 
        Com isso, prova-se que a vazao de entrada é igual a de saiu, ou seja, a taxa de variação massica em relação ao tempo é 0
      
 
 Sem ideia          
"""