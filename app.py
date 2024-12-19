import streamlit as st
import pandas as pd
import plotly.express as px

municipio = 'Municípios e respectivas\nUnidades da Federação'

df = pd.read_excel("tabela_reformulada.xlsx",header=0,nrows=100)

if 'PIB (1 000 R$)' in df.columns:
    df['PIB (1 000 R$)'] = df['PIB (1 000 R$)'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.title("Análise das 100 Maiores Cidades por PIB no Brasil")
st.write("Tabela")
st.dataframe(df,hide_index=True)

count_regioes = df['regiao'].value_counts().reset_index()
count_regioes.columns = ['Região', 'Quantidade']

fig = px.bar(
    count_regioes,
    x='Região',
    y='Quantidade',
    title='Distribuição das 100 Maiores Cidades por PIB no Brasil por Região',
    color='Região',
    color_discrete_map={
        'Norte': '#1f77b4',
        'Nordeste': '#ff7f0e',
        'Centro-Oeste': '#2ca02c',
        'Sudeste': '#d62728',
        'Sul': '#9467bd'
    },
    text='Quantidade'
)

fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(yaxis_title="Quantidade de Cidades", xaxis_title="Região")


st.write("Gráfico mostrando a distribuição das cidades entre as regiões do Brasil.")
st.plotly_chart(fig)

dados_mapa = df.dropna(subset=['Latitude', 'Longitude'])

fig = px.scatter_geo(
    dados_mapa,
    lat='Latitude',
    lon='Longitude',
    hover_name='cidade',
    hover_data={'PIB (1 000 R$)': True},
    title="Mapa das 100 Maiores Cidades por PIB no Brasil",
    projection="natural earth",
    scope="south america",
    color_discrete_sequence=["red"]
)

fig.update_traces(marker=dict(size=8), textposition="top center")
fig.update_geos(
    showcountries=True, countrycolor="Black",
    showland=True, landcolor="lightgray",
    showcoastlines=True, coastlinecolor="Black",
    fitbounds="locations",
    lataxis=dict(range=[0, 30]),
    lonaxis=dict(range=[0, 50]),
)

st.title("Mapa das 100 Maiores Cidades por PIB no Brasil")
st.write("Cada ponto no mapa representa uma cidade presente na lista.")
st.plotly_chart(fig)