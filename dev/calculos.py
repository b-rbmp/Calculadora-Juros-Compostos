
import numpy.matlib as ml

def calculo_juros_compostos(montante_inicial, aportes_mensais, taxa_mensal, tempo_meses): 
  
    # Calcula juros compostos e guarda a evolução mês a mês do capital, juro mensal e juro acumulado
    capital_mensal = ml.zeros((tempo_meses+1, 3))
    capital_mensal[0, 0] = montante_inicial
    for i in range(1, tempo_meses+1):
        # Capital no mês subsequente
        montante_atualizado = capital_mensal[i-1, 0] + aportes_mensais
        capital_mensal[i, 0] = montante_atualizado*(1 + taxa_mensal/100)
        capital_mensal[i, 1] = capital_mensal[i, 0]-montante_atualizado
        capital_mensal[i, 2] = capital_mensal[i-1, 2]+capital_mensal[i, 1]

    # Dados a retornar: Somente capital_mensal
    # capital_final = capital_mensal[i, 0]
    # juros_mensal = capital_mensal[i, 1]
    # juros_acumulados = capital_mensal[i, 2]
    # print("O montante inicial é :", montante_inicial) 
    # print("O montante final é :", capital_final) 
    # print("O ganho em juros total é :", juros_acumulados) 
    # print("O ganho em juros mensal é :", juros_mensal) 
    # print("A quantidade aportada ao longo do tempo é: ", aportes_mensais*tempo_meses)
    # print(capital_mensal)
    return capital_mensal

# DEBUG
if __name__ == "__main__":
    calculo_juros_compostos(10, 10, 10, 10)


