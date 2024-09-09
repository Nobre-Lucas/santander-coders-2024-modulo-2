import streamlit as st
import pandas as pd
import altair as alt
from snowflake.snowpark.context import get_active_session

st.title("Analisando a Eficiência de Veículos para Mobilidade Urbana :car:")

session = get_active_session()

query = "SELECT * FROM TRIP"
trip = session.sql(query).to_pandas()

trip['TRIP_DURATION'] = pd.to_timedelta(trip['TRIP_DURATION'])

trip['TRIP_DURATION_MINUTES'] = trip['TRIP_DURATION'].dt.total_seconds() / 60

transport_modes = {
    'BICICLETA': trip[trip['INCLUDES_BICYCLE'] == 1]['TRIP_DURATION_MINUTES'].mean().round(2),
    'METRÔ': trip[trip['INCLUDES_SUBWAY'] == 1]['TRIP_DURATION_MINUTES'].mean().round(2),
    'ÔNIBUS': trip[trip['INCLUDES_BUS'] == 1]['TRIP_DURATION_MINUTES'].mean().round(2),
    'CARRO': trip[trip['INCLUDES_CAR_AS_DRIVER'] == 1]['TRIP_DURATION_MINUTES'].mean().round(2)
}


df_modes = pd.DataFrame(list(transport_modes.items()), columns=['Modo de Transporte', 'Duração Média (min)'])
df_modes = df_modes.sort_values(by='Duração Média (min)', ascending=False)

chart = alt.Chart(df_modes).mark_bar().encode(
    x=alt.X('Modo de Transporte:N', title=''),
    y=alt.Y('Duração Média (min):Q', title='Duração Média (min)'),
    text='Duração Média (min):Q'
).properties(
    title='Duração Média das Viagens por Modo de Transporte'
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=16,
    anchor='middle'
)

chart = chart.encode(text=alt.Text('Duração Média (min):Q'))

st.altair_chart(chart, use_container_width=True)

transport_usage = {
    'BICICLETA': trip['INCLUDES_BICYCLE'].sum(),
    'METRÔ': trip['INCLUDES_SUBWAY'].sum(),
    'ÔNIBUS': trip['INCLUDES_BUS'].sum(),
    'CARRO (MOTORISTA)': trip['INCLUDES_CAR_AS_DRIVER'].sum(),
    'CARRO (PASSAGEIRO)': trip['INCLUDES_CAR_AS_PASSENGER'].sum(),
    'MOTOCICLETA (MOTORISTA)': trip['INCLUDES_MOTORCYCLE_AS_DRIVER'].sum(),
    'MOTOCICLETA (PASSAGEIRO)': trip['INCLUDES_MOTORCYCLE_AS_PASSENGER'].sum(),
    'TÁXI': trip['INCLUDES_TAXI'].sum(),
    'APLICATIVOS DE TRANSPORTE': trip['INCLUDES_PRIVATE_DRIVER'].sum(),
    'OUTROS MODOS': trip['INCLUDES_OTHER_MODES'].sum()
}

df_transport_usage = pd.DataFrame(list(transport_usage.items()), columns=['Modo de Transporte', 'Quantidade de Viagens'])

df_transport_usage = df_transport_usage.sort_values(by='Quantidade de Viagens', ascending=False)

df_transport_usage

query = "SELECT * FROM AVG_FAMILY_INCOME"
household = session.sql(query).to_pandas()

bins = [0, 4400, 8800, 13200, 17600, 26400, float('inf')]
labels = ['Até R$4,400', 'Até R$8,800', 'Até R$13,200', 'Até R$17,600', 'Até R$26,400', 'Acima de R$26,400']
household['faixa_renda'] = pd.cut(household['AVG_INCOME'], bins=bins, labels=labels)

veiculos_media = household.groupby('faixa_renda')['VEHICLES'].mean().reset_index()

chart = alt.Chart(veiculos_media).mark_bar().encode(
    x=alt.X('faixa_renda:N', title='Faixa de Renda (R$)', sort=labels, axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('VEHICLES:Q', title='Média de Veículos por Domicílio'),
    color=alt.value('steelblue')
).properties(
    title='Média de Veículos por Faixa de Renda',
    width=600,
    height=400
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=16,
    anchor='middle'
)

st.altair_chart(chart)

