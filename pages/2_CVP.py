# ============= IMPORTAÇÕES DAS BIBLIOTECAS ======================
import streamlit as st 
import plotly.express as px 
import pandas as pd 
import datetime

# ============= LAYOUT EXIBIÇÃO ======================
st.set_page_config(layout='centered')

# ============= IMPORTAÇÃO E TRATAMENTO DOS DADOS ======================
df_homicidio = pd.read_excel("Teste_dip.xlsx",sheet_name='Homicidio')
df_feminicidio = pd.read_excel("Teste_dip.xlsx", sheet_name='Feminicidio')
df_roubo_morte = pd.read_excel("Teste_dip.xlsx", sheet_name='Roubo com Morte')
df_lesao_morte = pd.read_excel("Teste_dip.xlsx", sheet_name="Lesao com Morte")
df_roubo_coletivo = pd.read_excel("Teste_dip.xlsx", sheet_name="Roubo a Coletivo")
df_veiculo = pd.read_excel("Teste_dip.xlsx", sheet_name= "Furto e Roubo Veiculo")
df_geral = pd.read_excel("Teste_dip.xlsx", sheet_name="Geral")


# ============= SIDEBAR ======================
cvps = st.sidebar.multiselect(
    label = "Qual CVP deseja visualizar?",
    options = ['Roubo a Coletivo', 'Furto e Roubo de Veículo'],
    default = 'Furto e Roubo de Veículo',
    placeholder = "Escolha um CVP para visualização"
)

st.sidebar.divider()

st.sidebar.write("Quais as RISP's desejadas?")
capital = st.sidebar.checkbox("Capital", True)
rms = st.sidebar.checkbox("RMS", True)

st.sidebar.divider()

data_escolhida = st.sidebar.date_input(
        label = "Escolha a data desejada para visualização",
        value = datetime.date(2024,4,7),
        min_value = datetime.date(2024,1,1),
        max_value = datetime.datetime.now(),
        format = "YYYY-MM-DD"
)

# ============= MENU PRINCIPAL ======================
st.title("Crimes Violentos Patrimoniais")

for option in cvps:
    
    # 1 - Roubo a Coletivo 
    if(option == "Roubo a Coletivo"):
        df_roubo_coletivo_filtrado = df_roubo_coletivo[df_roubo_coletivo['DATA'] == pd.to_datetime(data_escolhida)]
        
        # Capital e RMS
        if(capital == True and rms == True):
            st.subheader('Número de Roubos a Coletivos por Região')
            fig = px.bar(x=df_roubo_coletivo_filtrado.columns[1:], 
                        y=df_roubo_coletivo_filtrado.iloc[0, 1:].values, 
                        labels={'y': 'Número de Roubos a Coletivo', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
        
        # Apenas Capital 
        if(capital == True and rms == False):
            st.subheader('Número de Roubos a Coletivos por Região')
            fig = px.bar(x=[df_roubo_coletivo_filtrado.columns[1]], 
                        y=[df_roubo_coletivo_filtrado.iloc[0, 1]], 
                        labels={'y': 'Número de Roubos a Coletivo', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # Apenas RMS 
        if(capital == False and rms == True):
            st.subheader('Número de Roubos a Coletivos por Região')
            fig = px.bar(x=[df_roubo_coletivo_filtrado.columns[2]], 
                        y=[df_roubo_coletivo_filtrado.iloc[0, 2]], 
                        labels={'y': 'Número de Roubos a Coletivo', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
    # 2 - Roubo e Furto a Veículo 
    if(option == 'Furto e Roubo de Veículo'):
        df_veiculo_filtrado = df_veiculo[df_veiculo['DATA'] == pd.to_datetime(data_escolhida)]
            
        # Capital e RMS 
        if(capital == True and rms == True):
            st.subheader('Número de Roubos e Furtos a Veículos por Região')
            fig = px.bar(x=df_veiculo_filtrado.columns[1:], 
                        y=df_veiculo_filtrado.iloc[0, 1:].values, 
                        labels={'y': 'Número de Roubos e Furtos a Veículos', 'x': 'Região'},
                        color_discrete_sequence=[['orange', 'red', 'orange', 'red']])
            st.plotly_chart(fig)
        
        # Apenas Capital 
        if(capital == True and rms == False):
            st.subheader('Número de Roubos e Furtos a Veículos por Região')
            fig = px.bar(x=df_veiculo_filtrado.columns[[1,2]], 
                        y=df_veiculo_filtrado.iloc[0, [1,2]].values, 
                        labels={'y': 'Número de Roubos e Furtos a Veículos', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
        
        # Apenas RMS 
        if(capital == False and rms == True):
            st.subheader('Número de Roubos e Furtos a Veículos por Região')
            fig = px.bar(x=df_veiculo_filtrado.columns[[3,4]], 
                        y=df_veiculo_filtrado.iloc[0, [3,4]].values, 
                        labels={'y': 'Número de Roubos e Furtos a Veículos', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
            