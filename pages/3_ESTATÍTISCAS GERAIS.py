# ============= IMPORTAÇÕES DAS BIBLIOTECAS ======================
import streamlit as st 
import plotly.express as px 
import pandas as pd 
import datetime  

# ============= LAYOUT EXIBIÇÃO ======================
st.set_page_config(layout='wide')

# ============= IMPORTAÇÃO E TRATAMENTO DOS DADOS ======================
df_homicidio = pd.read_excel("Teste_dip.xlsx",sheet_name='Homicidio')
df_feminicidio = pd.read_excel("Teste_dip.xlsx", sheet_name='Feminicidio')
df_roubo_morte = pd.read_excel("Teste_dip.xlsx", sheet_name='Roubo com Morte')
df_lesao_morte = pd.read_excel("Teste_dip.xlsx", sheet_name="Lesao com Morte")
df_roubo_coletivo = pd.read_excel("Teste_dip.xlsx", sheet_name="Roubo a Coletivo")
df_veiculo = pd.read_excel("Teste_dip.xlsx", sheet_name= "Furto e Roubo Veiculo")
df_geral = pd.read_excel("Teste_dip.xlsx", sheet_name="Geral")


# ============= SIDEBAR ======================
st.sidebar.subheader("Escolha o que deseja visualizar")
polinter = st.sidebar.checkbox("POLINTER", True)
ar = st.sidebar.checkbox("Morte por Intervenção de Agente do Estado", True)
cenflag = st.sidebar.checkbox("CENFLAG", True)
violencia_domestica = st.sidebar.checkbox("Violência Doméstia e Familiar", True)
dai = st.sidebar.checkbox("DAI", True)
dercca = st.sidebar.checkbox("DERCCA", True)

st.sidebar.divider()

data_escolhida = st.sidebar.date_input(
        label = "Escolha a data desejada para visualização",
        value = datetime.date(2024,4,7),
        min_value = datetime.date(2024,1,1),
        max_value = datetime.datetime.now(),
        format = "YYYY-MM-DD"
)

# ============= MENU PRINCIPAL ======================

# ORGANIZANDO EM COLUNAS 
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

# FILTRANDO DF_GERAL PELA DATA ESCOLHIDA 
df_geral_data = df_geral[df_geral['DATA'] == pd.to_datetime(data_escolhida)]

# POLINTER
with col1:
    if(polinter == True):
        st.header("POLINTER")
        fig = px.bar(x=df_geral_data.iloc[0, [1,2]].values, 
                    y=df_geral_data.columns[[1,2]],
                    orientation = 'h', 
                    labels={'y': 'Espécie do Mandado de Prisão', 'x': 'Número de Mandados de Prisão'},
                    color_discrete_sequence = [['blue', 'red']])
        st.plotly_chart(fig)  

# MORTE POR INTERVENÇÃO DE AGENTE DO ESTADO 
with col2:
    if(ar == True):
        st.subheader("Morte por Intervenção de Agente do Estado")
        fig = px.pie(df_geral_data, names = df_geral_data.columns[[3,4]],       values=df_geral_data.iloc[0, [3,4]].values, color_discrete_sequence=px.colors.sequential.RdBu_r)
        fig.update_traces(
            textinfo = 'value',
            textfont_color='aliceblue',
            textfont_size=26
        )
        fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.75,
        font=dict(
            family="Arial",
            size=13,
            color="white"
            )
        ))
        st.plotly_chart(fig)

with col3:
    if(cenflag == True):
        st.header("CENFLAG")
        fig = px.pie(df_geral_data, names = df_geral_data.columns[[5,6,7]],     values=df_geral_data.iloc[0, [5,6,7]].values)
        fig.update_traces(
            textinfo = 'value',
            textfont_color='aliceblue',
            textfont_size=26
        )
        fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.75,
        font=dict(
            family="Arial",
            size=13,
            color="white"
            )
        ))
        st.plotly_chart(fig)
        
with col4:
    if(violencia_domestica == True):
        st.subheader("Violência Doméstica e Familiar")
        fig = px.bar(x = df_geral_data.columns[[8,9,10,11]], 
                    y = df_geral_data.iloc[0, [8,9,10,11]].values, 
                        labels={'y': 'Número de Ocorrências', 'x': 'Procedimento Policial Cabível'},
                        color_discrete_sequence=[['blue', 'red', 'red', 'blue']])
        
                        
        st.plotly_chart(fig)
        
with col5:
    if(dai == True):
        st.header("DAI")
        fig = px.pie(df_geral_data, names = df_geral_data.columns[[12,13,14]],  values=df_geral_data.iloc[0, [12,13,14]].values, color_discrete_sequence=px.colors.sequential.Plasma)
        fig.update_traces(
            textinfo = 'value',
            textfont_color='aliceblue',
            textfont_size=26,
           )
        fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.75,
        font=dict(
            family="Arial",
            size=13,
            color="white"
            )
        ))
        st.plotly_chart(fig)
        
with col6:
    if(dercca == True):
        st.header("DERCCA")
        fig = px.pie(df_geral_data, names = [df_geral_data.columns[15]],     values=[df_geral_data.iloc[0, 15]], color_discrete_sequence=px.colors.sequential.RdBu_r)
        fig.update_traces(
            textinfo = 'value',
            textfont_color='aliceblue',
            textfont_size=26
        )
        fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.75,
        font=dict(
            family="Arial",
            size=13,
            color="white"
            )
        ))
        st.plotly_chart(fig)