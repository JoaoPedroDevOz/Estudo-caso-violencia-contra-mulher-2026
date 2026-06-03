# Obtendo informações do dataframe

import pandas as pd

df = pd.read_csv('dados_violencia_mulheres_ses_2026.csv', encoding='utf-8', sep=';')

dfAnalytic = pd.DataFrame(df);

#================================
#-------FUNÇÕES AUXILIARES-------
#================================

def convertToDateTime(df, seriesColumn):
    df[seriesColumn] = pd.to_datetime(df[seriesColumn])


def findNulls(df, columName=''):
    if (columName):
        return df[columName].isnull().sum()
    return df.isnull().sum()

#================================
#------ANALISE EXPLORATÓRIA------
#================================

def describeDF(df):
    print(df.info()) # todas as colunas contém valores não nulos
    
    ## Dependendo da IDE utilizada para compilar o projeto, os próximos comandos não são necessários
    
    ## Verificando as dimensões do DataFrame
    
    # linhas, colunas = df.shape
    # print(f'Linhas: {linhas}, Colunas: {colunas}')
    
    print(df.head()) # verificação dos tipos dos dados
    
    
    ## Descreve de forma estatística dados numéricos e quantifica valores em string ou booleano
    
    print(df.describe())
    
    
#===================================
#---LIMPEZA E TRATAMENTO DE DADOS---
#===================================

def populateBySubDates(dateInit, dateEnd):
    return 

## A limpeza e tratamento dos dados deve ser feita de forma minunciosa, como valores 'nan' ou 'null' na tabela para 
## analisar os dados de forma efetiva sem considerar ocorrências cujos valores não fomentam a investigação e estudo dos dados.

## Verificando valores nulos
print(f'Colunas com valores nulos: \n{findNulls(df)}\n')

### primeira análise: há 72 campos da coluna dt_nasc que estão nulas e apenas 3 em nu_idade_n
    #### dt_nasc        72
    #### nu_idade_n      3

df = df.dropna(subset=['nu_idade_n'])

print(f"A coluna dt_nasc possui: {findNulls(df, 'dt_nasc')} valores nulos")

## Segunda parte é popular a coluna dt_nasc a partir da subtração entre a coluna nu_idade com a dt_notific.
## Isso gera valores artificiais, não reais, mas é importante para a estimativa que será analisada.


print(df.loc[df['nu_idade_n'].astype(str).str.match(r'^7\.'), :]) # não há valores com zeros à frente.

print(df.loc[df['nu_idade_n'].astype(str).str.contains(r'^0\.0$', na=False), ['nu_idade_n']])

# Então pode transformar tudo direto para númerico

df['nu_idade_n'] = (
    df['nu_idade_n']
    .astype(str)
    .str.replace(',', '.', regex=False)
)

df['nu_idade_n'] = pd.to_numeric(df['nu_idade_n'], errors='coerce')


#===================================
#-----ESTUDO E ANÁLISE DE DADOS-----
#===================================

# Garantir que a coluna é datetime

convertToDateTime(df, "dt_nasc")

# Dividindo em partes o estudo

## São relevantes analisar os dados das colunas: 
    ### Colunas numéricas e datas:
    #### 'dt_notific' para verificar os meses com maior ocorrëncias
    #### 'dt_nasc' e 'nu_idade_n' para identificar a geração que mais faz ocorrëncias
    #### 'num_envolv' para identificar se há mais de um envolvido no caso ou não
    
    ### Colunas de texto:
    #### 'cs_raca' para identificar qual raça está em situação delicada
    #### 'local_ocor' para verificar os locais que aconteceram os fatos
    #### 'autor_sexo' para identificar a maior ocorrëncia de autores do caso
    #### 'orient_sex' para verificar qual orientação sexual está ocorrendo mais esses casos.
    #### 'identi_gen' para identificar qual o gênero da vítima.
    
    ### Colunas boleanas:
    #### 'out_vezes' para identificar se acontece mais de uma vez antes da ocorrëncia ser feita ou não
    #### 'les_autop' para identificar se a violência é auto provocada
    #### 'viol_psico' para identificar se é violência psicológica
    #### 'viol_sexu' para identificar se é violência sexual

    
def sepByDateTime():
    ## Uma informação relevante é identificar em quais meses esses casos tiveram picos.
    
    # Garantir que a coluna é datetime
    dfAnalytic["dt_notific"] = pd.to_datetime(df["dt_notific"])
    
    return (
        df.groupby([
            dfAnalytic["dt_notific"].dt.year.rename("ano"),
            dfAnalytic["dt_notific"].dt.month.rename("mes")
        ])
        .size()
        .reset_index(name="quantidade")
    )
    
df_dt_notific = sepByDateTime()

# Divisão das gerações para estudo por idades

## Geração Silenciosa (1928 – 1945)
## Baby Boomers (1946 – 1964)
## Geração X (1965 – 1980)
## Geração Y ou Millennials (1981 – 1996)
## Geração Z (1997 – 2010)
## Geração Alfa (2011 – 2024)
## Geração Beta (a partir de 2025)
