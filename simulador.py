import numpy as np
import matplotlib.pyplot as plt
from math import floor

def juros_Compostos_Aporte(capital, taxa, tempo, aporte):
    tempo *= 12
    taxa = (taxa / 12) / 100
    return floor((capital * ((1 + taxa) ** 1)) + (aporte * ((((1 + taxa) ** tempo) - 1) / taxa)))
    
def informacoes_De_Investimento():
    modalidade_De_Investimento = input("Digite qual é o tipo de investimento desejado (Poupança, CDB...): ")
    taxa = float(input(f"Digite a taxa de juros referente à {modalidade_De_Investimento}: ")) 
    return modalidade_De_Investimento, taxa

coresDoGrafico = ['b', 'c', 'g', 'r', 'm', 'y', 'k'] # Lista que contém os 'comandos' que passam cores para cada linha do gráfico ('b' = blue, por exemplo)
indiceCores = 0

tempoInvestimento = float(input("Digite o período de investimento (em anos): "))
tempo = np.arange(0, tempoInvestimento + 1)
aporte = float(input(f'Digite o valor mensal que será investido: R$ '))

controleDeLeitura = 0
while(controleDeLeitura != '1'):
    tipoDeInvestimento = informacoes_De_Investimento()
    montante = [juros_Compostos_Aporte(1000, tipoDeInvestimento[1], t, aporte) for t in tempo]
    plt.plot(tempo, montante, marker = 'o', linestyle = '-', color = coresDoGrafico[indiceCores], label=f'{tipoDeInvestimento[0]} Taxa = {tipoDeInvestimento[1]}')
    indiceCores += 1
    controleDeLeitura = input("\nDeseja encerrar a leitura? \n1. Sim\n2. Não\n -> ")

indiceCores = 0

# GRÁFICO

plt.xlabel('Anos Decorridos')
plt.ylabel('Montante Acumulado (R$)')
plt.title('Gráfico de Juros Compostos ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()
