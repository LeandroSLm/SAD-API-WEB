import pandas as pd
import utils as u

df = pd.read_excel("tabelas_completas.xlsx",header=0,skiprows=4,nrows=100)

df['estado'] = df[u.municipio].apply(u.extrair_estado)
df['cidade'] = df[u.municipio].apply(u.extrair_cidade)
df['regiao'] = df['estado'].map(u.mapa_regioes)

cidades = df[['cidade', 'estado']].drop_duplicates().values.tolist()

coordenadas = u.obter_coordenadas(cidades)

coordenadas_df = pd.DataFrame(coordenadas, columns=['cidade', 'estado', 'Latitude', 'Longitude'])

df = df.merge(coordenadas_df, on=['cidade', 'estado'], how='left')

df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

df.to_excel("tabela_reformulada.xlsx", index=False)
