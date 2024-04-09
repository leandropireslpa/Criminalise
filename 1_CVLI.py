# ============= IMPORTAÇÕES DAS BIBLIOTECAS ======================
import streamlit as st 
import plotly.express as px 
import plotly.graph_objects as go 
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
cvlis = st.sidebar.multiselect(
    label = "Qual CVLI deseja visualizar?",
    options = ['Homicídio', 'Feminicídio', 'Lesão com Morte', 'Roubo com Morte'],
    default = 'Homicídio',
    placeholder = "Escolha um CVLI para visualização"
)

st.sidebar.divider()

st.sidebar.write("Quais as RISP's desejadas?")
atlantico = st.sidebar.checkbox("Atlântico", True)
bts = st.sidebar.checkbox("BTS", True)
central = st.sidebar.checkbox("Central", True)
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
st.title("Crimes Violentos Letais Intencionais")

for option in cvlis:
    
# 1 - HOMICIDIOS
    if (option == 'Homicídio'):
        df_homicidio_filtrado = df_homicidio[df_homicidio['DATA'] == pd.to_datetime(data_escolhida)]
        # a) Todas as RISP's
        if (atlantico == True and bts == True and central == True and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[1:], 
                        y=df_homicidio_filtrado.iloc[0, 1:].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # b) Sem Atlantico 
        if (atlantico == False and bts == True and central == True and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[2:], 
                        y=df_homicidio_filtrado.iloc[0, 2:].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # c) Sem BTS
        if (atlantico == True and bts == False and central == True and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[1,3,4]], 
                        y=df_homicidio_filtrado.iloc[0, [1,3,4]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # d) Sem Central
        if (atlantico == True and bts == True and central == False and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[1,2,4]], 
                        y=df_homicidio_filtrado.iloc[0, [1,2,4]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # e) Sem RMS
        if (atlantico == True and bts == True and central == True and rms == False):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[1,2,3]], 
                        y=df_homicidio_filtrado.iloc[0, [1,2,3]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # f) Sem Atlantico e BTS
        if (atlantico == False and bts == False and central == True and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[3,4]], 
                        y=df_homicidio_filtrado.iloc[0, [3,4]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # g) Sem Atlantico e Central
        if (atlantico == False and bts == True and central == False and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[2,4]], 
                        y=df_homicidio_filtrado.iloc[0, [2,4]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # h) Sem Atlantico e RMS 
        if (atlantico == False and bts == True and central == True and rms == False):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[2,3]], 
                        y=df_homicidio_filtrado.iloc[0, [2,3]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # i) Sem BTS e Central
        if (atlantico == True and bts == False and central == False and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[1,4]], 
                        y=df_homicidio_filtrado.iloc[0, [1,4]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # j) Sem BTS e RMS
        if (atlantico == True and bts == False and central == True and rms == False):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[1,3]], 
                        y=df_homicidio_filtrado.iloc[0, [1,3]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # k) Sem Central e RMS 
        if (atlantico == True and bts == True and central == False and rms == False):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=df_homicidio_filtrado.columns[[1,2]], 
                        y=df_homicidio_filtrado.iloc[0, [1,2]].values, 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # l) Apenas Atlantico 
        if (atlantico == True and bts == False and central == False and rms == False):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=[df_homicidio_filtrado.columns[1]], 
                        y=[df_homicidio_filtrado.iloc[0, 1]], 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # m) Apenas BTS 
        if (atlantico == False and bts == True and central == False and rms == False):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=[df_homicidio_filtrado.columns[2]], 
                        y=[df_homicidio_filtrado.iloc[0, 2]], 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # n) Apenas Central 
        if (atlantico == False and bts == False and central == True and rms == False):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=[df_homicidio_filtrado.columns[3]], 
                        y=[df_homicidio_filtrado.iloc[0, 3]], 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # o) Apenas RMS 
        if (atlantico == False and bts == False and central == False and rms == True):
            st.subheader("Número de Homicídios por Região")
            fig = px.bar(x=[df_homicidio_filtrado.columns[4]], 
                        y=[df_homicidio_filtrado.iloc[0, 4]], 
                        labels={'y': 'Número de Homicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            

    # 2 - FEMINICIDIO
    if(option == 'Feminicídio'):
        df_feminicio_filtrado = df_feminicidio[df_feminicidio['DATA'] == pd.to_datetime(data_escolhida)]
        # a) Todas as RISP's
        if (atlantico == True and bts == True and central == True and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[1:], 
                        y=df_feminicio_filtrado.iloc[0, 1:].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # b) Sem Atlantico 
        if (atlantico == False and bts == True and central == True and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[2:], 
                        y=df_feminicio_filtrado.iloc[0, 2:].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # c) Sem BTS
        if (atlantico == True and bts == False and central == True and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[1,3,4]], 
                        y=df_feminicio_filtrado.iloc[0, [1,3,4]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # d) Sem Central
        if (atlantico == True and bts == True and central == False and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[1,2,4]], 
                        y=df_feminicio_filtrado.iloc[0, [1,2,4]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # e) Sem RMS
        if (atlantico == True and bts == True and central == True and rms == False):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[1,2,3]], 
                        y=df_feminicio_filtrado.iloc[0, [1,2,3]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # f) Sem Atlantico e BTS
        if (atlantico == False and bts == False and central == True and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[3,4]], 
                        y=df_feminicio_filtrado.iloc[0, [3,4]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # g) Sem Atlantico e Central
        if (atlantico == False and bts == True and central == False and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[2,4]], 
                        y=df_feminicio_filtrado.iloc[0, [2,4]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # h) Sem Atlantico e RMS 
        if (atlantico == False and bts == True and central == True and rms == False):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[2,3]], 
                        y=df_feminicio_filtrado.iloc[0, [2,3]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # i) Sem BTS e Central
        if (atlantico == True and bts == False and central == False and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[1,4]], 
                        y=df_feminicio_filtrado.iloc[0, [1,4]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # j) Sem BTS e RMS
        if (atlantico == True and bts == False and central == True and rms == False):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[1,3]], 
                        y=df_feminicio_filtrado.iloc[0, [1,3]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # k) Sem Central e RMS 
        if (atlantico == True and bts == True and central == False and rms == False):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=df_feminicio_filtrado.columns[[1,2]], 
                        y=df_feminicio_filtrado.iloc[0, [1,2]].values, 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # l) Apenas Atlantico 
        if (atlantico == True and bts == False and central == False and rms == False):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=[df_feminicio_filtrado.columns[1]], 
                        y=[df_feminicio_filtrado.iloc[0, 1]], 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # m) Apenas BTS 
        if (atlantico == False and bts == True and central == False and rms == False):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=[df_feminicio_filtrado.columns[2]], 
                        y=[df_feminicio_filtrado.iloc[0, 2]], 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # n) Apenas Central 
        if (atlantico == False and bts == False and central == True and rms == False):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=[df_feminicio_filtrado.columns[3]], 
                        y=[df_feminicio_filtrado.iloc[0, 3]], 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # o) Apenas RMS 
        if (atlantico == False and bts == False and central == False and rms == True):
            st.subheader("Número de Feminicídios por Região")
            fig = px.bar(x=[df_feminicio_filtrado.columns[4]], 
                        y=[df_feminicio_filtrado.iloc[0, 4]], 
                        labels={'y': 'Número de Feminicídios', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
    # 3 - ROUBO COM MORTE 
    if(option == 'Roubo com Morte'):
        df_roubo_morte_filtrado = df_roubo_morte[df_roubo_morte['DATA'] == pd.to_datetime(data_escolhida)]
        # a) Todas as RISP's
        if (atlantico == True and bts == True and central == True and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[1:], 
                        y=df_roubo_morte_filtrado.iloc[0, 1:].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # b) Sem Atlantico 
        if (atlantico == False and bts == True and central == True and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[2:], 
                        y=df_roubo_morte_filtrado.iloc[0, 2:].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # c) Sem BTS
        if (atlantico == True and bts == False and central == True and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[1,3,4]], 
                        y=df_roubo_morte_filtrado.iloc[0, [1,3,4]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # d) Sem Central
        if (atlantico == True and bts == True and central == False and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[1,2,4]], 
                        y=df_roubo_morte_filtrado.iloc[0, [1,2,4]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # e) Sem RMS
        if (atlantico == True and bts == True and central == True and rms == False):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[1,2,3], 
                        y=df_roubo_morte_filtrado.iloc[0, [1,2,3]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # f) Sem Atlantico e BTS
        if (atlantico == False and bts == False and central == True and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[3,4]], 
                        y=df_roubo_morte_filtrado.iloc[0, [3,4]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # g) Sem Atlantico e Central
        if (atlantico == False and bts == True and central == False and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[2,4]], 
                        y=df_roubo_morte_filtrado.iloc[0, [2,4]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # h) Sem Atlantico e RMS 
        if (atlantico == False and bts == True and central == True and rms == False):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[2,3]], 
                        y=df_roubo_morte_filtrado.iloc[0, [2,3]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # i) Sem BTS e Central
        if (atlantico == True and bts == False and central == False and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[1,4]], 
                        y=df_roubo_morte_filtrado.iloc[0, [1,4]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # j) Sem BTS e RMS
        if (atlantico == True and bts == False and central == True and rms == False):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[1,3]], 
                        y=df_roubo_morte_filtrado.iloc[0, [1,3]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # k) Sem Central e RMS 
        if (atlantico == True and bts == True and central == False and rms == False):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=df_roubo_morte_filtrado.columns[[1,2]], 
                        y=df_roubo_morte_filtrado.iloc[0, [1,2]].values, 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # l) Apenas Atlantico 
        if (atlantico == True and bts == False and central == False and rms == False):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=[df_roubo_morte_filtrado.columns[1]], 
                        y=[df_roubo_morte_filtrado.iloc[0, 1]], 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # m) Apenas BTS 
        if (atlantico == False and bts == True and central == False and rms == False):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=[df_roubo_morte_filtrado.columns[2]], 
                        y=[df_roubo_morte_filtrado.iloc[0, 2]], 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # n) Apenas Central 
        if (atlantico == False and bts == False and central == True and rms == False):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=[df_roubo_morte_filtrado.columns[3]], 
                        y=[df_roubo_morte_filtrado.iloc[0, 3]], 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # o) Apenas RMS 
        if (atlantico == False and bts == False and central == False and rms == True):
            st.subheader("Número de Roubos com Morte por Região")
            fig = px.bar(x=[df_roubo_morte_filtrado.columns[4]], 
                        y=[df_roubo_morte_filtrado.iloc[0, 4]], 
                        labels={'y': 'Número de Roubos com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
    # 4 - LESA0 COM MORTE 
    if(option == 'Lesão com Morte'):
        df_lesao_morte_filtrado = df_lesao_morte[df_lesao_morte['DATA'] == pd.to_datetime(data_escolhida)]
        # a) Todas as RISP's
        if (atlantico == True and bts == True and central == True and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[1:], 
                        y=df_lesao_morte_filtrado.iloc[0, 1:].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # b) Sem Atlantico 
        if (atlantico == False and bts == True and central == True and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[2:], 
                        y=df_lesao_morte_filtrado.iloc[0, 2:].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # c) Sem BTS
        if (atlantico == True and bts == False and central == True and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[1,3,4]], 
                        y=df_lesao_morte_filtrado.iloc[0, [1,3,4]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # d) Sem Central
        if (atlantico == True and bts == True and central == False and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[1,2,4]], 
                        y=df_lesao_morte_filtrado.iloc[0, [1,2,4]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # e) Sem RMS
        if (atlantico == True and bts == True and central == True and rms == False):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[1,2,3]], 
                        y=df_lesao_morte_filtrado.iloc[0, [1,2,3]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # f) Sem Atlantico e BTS
        if (atlantico == False and bts == False and central == True and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[3,4]], 
                        y=df_lesao_morte_filtrado.iloc[0, [3,4]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # g) Sem Atlantico e Central
        if (atlantico == False and bts == True and central == False and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[2,4]], 
                        y=df_lesao_morte_filtrado.iloc[0, [2,4]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # h) Sem Atlantico e RMS 
        if (atlantico == False and bts == True and central == True and rms == False):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[2,3]], 
                        y=df_lesao_morte_filtrado.iloc[0, [2,3]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # i) Sem BTS e Central
        if (atlantico == True and bts == False and central == False and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[1,4]], 
                        y=df_lesao_morte_filtrado.iloc[0, [1,4]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # j) Sem BTS e RMS
        if (atlantico == True and bts == False and central == True and rms == False):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[1,3]], 
                        y=df_lesao_morte_filtrado.iloc[0, [1,3]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # k) Sem Central e RMS 
        if (atlantico == True and bts == True and central == False and rms == False):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=df_lesao_morte_filtrado.columns[[1,2]], 
                        y=df_lesao_morte_filtrado.iloc[0, [1,2]].values, 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # l) Apenas Atlantico 
        if (atlantico == True and bts == False and central == False and rms == False):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=[df_lesao_morte_filtrado.columns[1]], 
                        y=[df_lesao_morte_filtrado.iloc[0, 1]], 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # m) Apenas BTS 
        if (atlantico == False and bts == True and central == False and rms == False):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=[df_lesao_morte_filtrado.columns[2]], 
                        y=[df_lesao_morte_filtrado.iloc[0, 2]], 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)

        # n) Apenas Central 
        if (atlantico == False and bts == False and central == True and rms == False):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=[df_lesao_morte_filtrado.columns[3]], 
                        y=[df_lesao_morte_filtrado.iloc[0, 3]], 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)
            
        # o) Apenas RMS 
        if (atlantico == False and bts == False and central == False and rms == True):
            st.subheader("Número de Lesões com Morte por Região")
            fig = px.bar(x=[df_lesao_morte_filtrado.columns[4]], 
                        y=[df_lesao_morte_filtrado.iloc[0, 4]], 
                        labels={'y': 'Número de Lesões com Morte', 'x': 'Região'},
                        template='plotly')
            st.plotly_chart(fig)