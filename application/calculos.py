import pandas as pd

def calculo_juros_compostos(montante_inicial, aportes_mensais, taxa_mensal, tempo_meses): 
    
    df = pd.DataFrame({'Capital' : [montante_inicial], 'Juros Mensais': [0.0], 'Juros Acumulados': [0.0], 'Valor Aportado' : [montante_inicial]})
    # Calcula juros compostos e guarda a evolução mês a mês do capital, juro mensal e juro acumulado
    for i in range(1, tempo_meses+1):
        df = df.append(pd.Series(0, index=df.columns), ignore_index=True)
        # Capital no mês subsequente
        montante_atualizado = df['Capital'].loc[i-1] + aportes_mensais
        df.at[i, 'Capital'] = montante_atualizado*(1.0 + taxa_mensal/100)
        df.at[i, 'Juros Mensais'] = (df['Capital'].loc[i]-montante_atualizado)
        df.at[i, 'Juros Acumulados'] = (df['Juros Acumulados'].loc[i-1] + df['Juros Mensais'].loc[i])
        df.at[i, 'Valor Aportado'] = (df['Valor Aportado'].loc[i-1] + aportes_mensais)

    return df

