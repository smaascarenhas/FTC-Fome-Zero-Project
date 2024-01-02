#-----------------------------------------------
# Bibliotecas Necessárias
#-----------------------------------------------
import plotly.express as px
import plotly.graph_objects as go
import folium
import pandas as pd
import streamlit as st
import datetime
from PIL import Image
import inflection
import webbrowser


st.set_page_config( page_title='Dashboards', page_icon='📊', layout='wide')


#-----------------------------------------------
# Funções
#-----------------------------------------------
def country_name(country_id):
    """ Essa função tem o objetivo de trocar o Country Code pelo 
        Nome dos respectivos países.
    """
    COUNTRIES = {
        1: "India",
        14: "Australia",
        30: "Brazil",
        37: "Canada",
        94: "Indonesia",
        148: "New Zeland",
        162: "Philippines",
        166: "Qatar",
        184: "Singapure",
        189: "South Africa",
        191: "Sri Lanka",
        208: "Turkey",
        214: "United Arab Emirates",
        215: "England",
        216: "United States of America",
        }
    
    return COUNTRIES[country_id]

def create_price_tye(price_range):
    
    """ Essa função cria o Tipo de Categoria de Comida
    """
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"



def color_name(color_code):
    """ Essa função cria o nome das cores com base nos códigos de cores
    """
    COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
    }

    return COLORS[color_code]



def rename_columns(dataframe):
    """ Essa função renomeia as colunas do DataFrame, Elimina espaços
        e Letras maiúsculas"""
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new

    return df

def clean_code( df1 ):
    """Esta função tem a responsabilidade de limpar o dataframe

         Tipos de limpeza:
         1. Remove Linhas Duplicadas
         
         Input: Dataframe
         Output: Dataframe
    """
    df1 = df1.drop_duplicates()
    
    return df1

#----------Quantidade de restaurantes por país-------------------------------------------
def restaurantes_por_pais (df1):
    """ Esta função tem o objetivo de mostrar a Quantidade de restaurantes por país
         com um gráfico de barras com os países no eixo X e os restaurantes no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[:, ['restaurant_id', 'country_name']]
                 .groupby('country_name')
                 .count()
                 .sort_values(by='restaurant_id', ascending=False)
                 .reset_index())
    
    fig = px.bar(df_aux,
                    x='country_name',
                    y='restaurant_id',
                    text='restaurant_id',
                    labels={'country_name': 'País', 'restaurant_id': 'Quantidade de restaurantes'},
                    color_discrete_sequence=['indianred'],
                    title='Quantidade de restaurantes registrados por País')

        # Personalizando rótulos dos eixos e título
    fig.update_layout(width=1300,
                        xaxis_title='Países',
                        yaxis_title='Quantidade de Restaurantes',
                        title_x=0.4)
    
    return fig

#----------Quantidade de cidades por país-------------------------------------------
def cidades_por_pais (df1):
    """ Esta função tem o objetivo de mostrar a Quantidade de cidades por país
         com um gráfico de barras com os países no eixo X e as cidades no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[:, ['city', 'country_name']]
                 .groupby('country_name')
                 .nunique()
                 .sort_values(by='city', ascending=False)
                 .reset_index())
    
    fig = px.bar(df_aux, 
                    x='country_name', 
                    y='city',
                    title='Quantidade de cidades registradas por País',
                    text='city',
                    labels={'country_name': 'País', 'city': 'Quantidade de cidades'},
                    color_discrete_sequence=['indianred'])
    # Personalizando rótulos dos eixos e título
    fig.update_layout(width=1300,
                      xaxis_title='Países',
                      yaxis_title='Quantidade de cidades',
                      title_x=0.4,)
    
    return fig

#----------Média de avaliações feitas por país-------------------------------------------
def media_avaliacoes_pais(df1):
    """ Esta função tem o objetivo de mostrar a média de avaliações feitas por país
        com um gráfico de barras com os países no eixo X e a quantidade de avaliações
        no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[:,['country_name', 'votes']]
                 .groupby(['country_name'])
                 .mean()
                 .sort_values(by='votes', ascending=False)
                 .reset_index())
    df_aux['votes'] = df_aux['votes'].round(3)
           
    fig = px.bar(df_aux, 
                    x='country_name',
                    y='votes',
                    title= 'Média de avaliações feitas por País',
                    text='votes',
                    labels={'country_name': 'País', 'votes': 'Quantidade de avaliações'},
                    color_discrete_sequence=['indianred'])
    # Personalizando rótulos dos eixos e título
    fig.update_layout(width=600,
                        height=400,
                        xaxis_title='Países',
                        yaxis_title='Quantidade de avaliações',
                        title_x=0.4)
    
    return fig

#----------Média de preço de prato pra dois por país------------------------------------------- 
def media_preco_prato_dois(df1):
    """ Esta função tem o objetivo de mostrar a média de preço de prato para duas pessoas
        por país, com um gráfico de barras com os países no eixo X e a média de preço
        no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[:,['country_name', 'average_cost_for_two']]
                 .groupby(['country_name'])['average_cost_for_two']
                 .mean()
                 .sort_values(ascending=False)
                 .reset_index())
    df_aux['average_cost_for_two'] = df_aux['average_cost_for_two'].round(2)
           
    fig = px.bar(df_aux, 
                    x='country_name',
                    y='average_cost_for_two',
                    title= 'Média de preço de um prato para duas pessoas por País',
                    text='average_cost_for_two',
                    labels={'country_name': 'País', 'average_cost_for_two': 'Preço de prato para duas pessoas'},
                    color_discrete_sequence=['indianred'])
    # Personalizando rótulos dos eixos e título
    fig.update_layout(width=650,
                        height=400,
                        xaxis_title='Países',
                        yaxis_title='Preço de prato para duas pessoas',
                        title_x=0.3)
    
    return fig

#----------Top 10 Cidades com mais restaurantes-------------------------------------------
def cidades_mais_restaurantes(df1, city_slider):
    """ Esta função tem o objetivo de mostrar o Top 10 Cidades com mais restaurantes,
        com um gráfico de barras com as cidades no eixo X e a quantidade de restaurantes no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[:, ['city','restaurant_id', 'country_name']]
                 .groupby(['city', 'country_name'])['restaurant_id']
                 .count()
                 .sort_values(ascending=False)
                 .reset_index()
                 .head(city_slider))
    fig = px.bar(df_aux, 
                    x='city', 
                    y='restaurant_id',
                    title=f'Top {city_slider} Cidades com mais restaurantes',
                    text='restaurant_id',
                    color='country_name',
                    labels={'country_name': 'País', 'city': 'Cidade', 'restaurant_id': 'Quantidade de restaurantes'},
                    color_discrete_sequence=
                    ['indianred', 'mediumaquamarine', 'cornflowerblue', 'darkorange', 'indigo', 'lime', 'deeppink', 'cyan'])
    # Personalizando rótulos dos eixos e título
    fig.update_layout(width=1300,
                        xaxis_title='Cidades',
                        yaxis_title='Quantidade de Restaurantes',
                        title_x=0.3)
    
    return fig

#----------Top 7 cidades com restaurantes com média de avaliação acima de 4-------------------------------------------
def cidades_com_restaurantes_media_acima_4(df1, city_slider):
    """ Esta função tem o objetivo de mostrar o Top 7 Cidades com mais restaurantes
        com média de avaliação acima de 4, com um gráfico de barras com as cidades 
        no eixo X e a quantidade de restaurantes no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[df1['aggregate_rating'] > 4, ['city','restaurant_id', 'country_name']]
                 .groupby(['city', 'country_name'])['restaurant_id']
                 .count()
                 .sort_values(ascending=False)
                 .reset_index()
                 .head(city_slider))          
    fig = px.bar(df_aux, 
                    x='city',
                    y='restaurant_id',
                    title=f'Top {city_slider} cidades com restaurantes com média de avaliação acima de 4',
                    text='restaurant_id',
                    color='country_name',
                    labels={'country_name': 'País', 'city': 'Cidade', 'restaurant_id': 'Quantidade de restaurantes'},
                        color_discrete_sequence=
                        ['indianred', 'mediumaquamarine', 'cornflowerblue', 'darkorange', 'indigo', 'lime', 'deeppink', 'cyan'])
    # Personalizando rótulos dos eixos e título
    fig.update_layout(width=650,
                        height=400,
                        xaxis_title='Cidades',
                        yaxis_title='Quantidade de Restaurantes',
                        title_x=0.1)
    
    return fig

#----------Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5-------------------------------------------
def cidades_com_restaurantes_media_abaixo_2_5(df1, city_slider):
    """ Esta função tem o objetivo de mostrar o Top 7 Cidades com mais restaurantes
        com média de avaliação abaixo de 2.5, com um gráfico de barras com as cidades 
        no eixo X e a quantidade de restaurantes no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[df1['aggregate_rating'] < 2.5, ['city', 'restaurant_id', 'country_name']]
                             .groupby(['city', 'country_name'])['restaurant_id']
                             .count()
                             .sort_values(ascending=False)
                             .reset_index()
                             .head(city_slider))  
    fig = px.bar(df_aux, 
                    x='city',
                    y='restaurant_id',
                    title=f'Top {city_slider} cidades com restaurantes com média de avaliação abaixo de 2.5',
                    text='restaurant_id',
                    color='country_name',
                    labels={'country_name': 'País', 'city': 'Cidade', 'restaurant_id': 'Quantidade de restaurantes'},
                        color_discrete_sequence=
                        ['indianred', 'mediumaquamarine', 'cornflowerblue', 'darkorange', 'indigo', 'lime', 'deeppink', 'cyan'])           
    # Personalizando rótulos dos eixos e título
    fig.update_layout(width=650,
                            height=400,
                            xaxis_title='Cidades',
                            yaxis_title='Quantidade de Restaurantes',
                            title_x=0.1)
    
    return fig

#----------Top 7 cidades com mais restaurantes com tipos de culinárias distintos-------------------------------------------
def cidades_mais_restaurantes_tipo_de_culinaria_distintos(df1, city_slider):
    """ Esta função tem o objetivo de mostrar o Top 7 Cidades com mais restaurantes
        com tipos de culinárias distintos, com um gráfico de barras com as cidades 
        no eixo X e a quantidade de tipos de culinárias únicos no eixo Y
         Input: Dataframe
         Output: fig
    """
    
    df_aux = (df1.loc[:, ['city','cuisines', 'country_name']]
                         .groupby(['city', 'country_name'])['cuisines']
                         .nunique()
                         .sort_values(ascending=False)
                         .reset_index()
                         .head(city_slider))
    fig = px.bar(df_aux, 
                    x='city',
                    y='cuisines',
                    title=f'Top {city_slider} cidades com mais restaurantes com tipos de culinárias distintos',
                    text='cuisines',
                    color='country_name',
                    labels={'country_name': 'País', 'city': 'Cidade', 'cuisines': 'Quantidade de tipos culinários únicos'},
                    color_discrete_sequence=
                    ['indianred', 'mediumaquamarine', 'cornflowerblue', 'darkorange', 'indigo', 'lime', 'deeppink', 'cyan'])
    # Personalizando rótulos dos eixos e título       
    fig.update_layout(width=600,
                            height=400,
                            xaxis_title='Cidades',
                            yaxis_title='Quantidade de tipos de culinárias únicos',
                            title_x=0.1)
    
    return fig

#----------Top 7 Cidades com maior preço médio de um prato para duas pessoas-------------------------------------------
def cidades_top_avg_for_two (df1, city_slider):
    """ Esta função tem o objetivo de mostrar o Top 7 Cidades com maior
        preço médio de um prato para duas pessoas, com um gráfico de barras com as cidades 
        no eixo X e o preço médio no eixo Y
         Input: Dataframe
         Output: fig
    """
    df_aux = (df1.loc[:, ['city', 'average_cost_for_two', 'country_name']]
                 .groupby(['city', 'country_name'])['average_cost_for_two']
                 .mean()
                 .sort_values(ascending=False)
                 .reset_index()
                 .head(city_slider))
    # arredondando os valores para 2 casa decimais
    df_aux['average_cost_for_two'] = df_aux['average_cost_for_two'].round(2)

    fig = px.bar(df_aux, 
                    x='city',
                    y='average_cost_for_two',
                    title=f'Top {city_slider} cidades com maior preço médio de um prato para duas pessoas',
                    text='average_cost_for_two',
                    color='country_name',
                    labels={'country_name': 'País', 'city': 'Cidade', 'average_cost_for_two': 'Média de preço para dois'},
                    color_discrete_sequence=
                    ['indianred', 'mediumaquamarine', 'cornflowerblue', 'darkorange', 'indigo', 'lime', 'deeppink', 'cyan'])
    # Personalizando rótulos dos eixos e título       
    fig.update_layout(width=600,
                            height=400,
                            xaxis_title='Cidades',
                            yaxis_title='Preço médio de prato para dois',
                            title_x=0.1)

    return fig

#----------Melhores Restaurantes dos Principais tipos Culinários-------------------------------------------
def melhor_restaurante_por_cozinha (df1, cuisines):
    cols = ['restaurant_id', 'restaurant_name', 'aggregate_rating', 'country_name', 'votes', 'city', 'average_cost_for_two', 'currency']
    df_aux = (df1.loc[df1['cuisines'] == cuisines, cols]
                 .sort_values(by=['aggregate_rating', 'votes', 'restaurant_id'], ascending=[False, False, True])
                 .reset_index())
    
    return df_aux

#----------Top 10 melhores restaurantes-------------------------------------------
def best_restaurantes (df1, rest_slider):
    df_result = (df1.loc[:, ['restaurant_id','restaurant_name','country_name', 'city', 'cuisines' ,'average_cost_for_two', 'aggregate_rating', 'votes']]
          .sort_values(by=['aggregate_rating', 'votes', 'restaurant_id'], ascending=[False, False, True])
          .groupby(['restaurant_name'])
          .head(rest_slider))
    df_result.columns = ['ID do restaurante','Nome do restaurante','Nome do país', 'Cidade','Culinária', 
                         'Preço médio de prato para duas pessoas','Média da avaliaçõe média','Avaliações']
    
    return df_result

#----------Top 10 melhores/piores tipos de Culinárias-------------------------------------------
def top_10_cuisines (df1, x, title, rest_slider):
    df_aux = (df1.loc[:, ['cuisines', 'restaurant_name' ,'restaurant_id','average_cost_for_two', 'aggregate_rating', 'votes']]
          .groupby(['cuisines'])
          .mean('aggregate_rating')
          .sort_values(['aggregate_rating', 'votes', 'restaurant_id'], ascending=[x, False, True])
          .reset_index()
          .head(rest_slider))

    #df_aux = df_aux.head(10)
    
    df_aux['aggregate_rating'] = df_aux['aggregate_rating'].round(2)

    fig = px.bar(df_aux,
                 x='cuisines',
                 y='aggregate_rating',
                 title=title,
                 text='aggregate_rating',
                 labels={'cuisines': 'Culinária', 'aggregate_rating': 'Média da avaliaçõe média'},
                 color_discrete_sequence=['indianred'])
          
    # Personalizando rótulos dos eixos e título       
    fig.update_layout(width=650,
                        height=400,
                        xaxis_title='Culinárias',
                        yaxis_title='Média da avaliaçõe média',
                        title_x=0.3)
    
    return fig



#-----------------------------------------------------------------------
#---------Importanto o Dataset------------------------------------------
#-----------------------------------------------------------------------
df = pd.read_csv( 'dataset/zomato.csv' )

#-----------------------------------------------------------------------
#---------Tratando os dados
#-----------------------------------------------------------------------

#----------Limpeza-------------------------------------------
df1 = clean_code ( df )

#---------Renomeando as colunas do DataFrame-------------------------------------------
df1 = rename_columns(df1)

#---------Colocando o nome dos países com base no código de cada país-------------------
df1['country_name'] = df1['country_code'].apply(lambda x: country_name(x))

#---------Criando a categoria do tipo de comida com base no range de valores.------------
df1['price_tye'] = df1['price_range'].apply( lambda x: create_price_tye(x))

#---------Criando o nome das cores com base nos códigos de cores-------------------------
df1['color_name'] = df1['rating_color'].apply( lambda x: color_name(x))

#---------Categorizando todos os restaurantes somente por um tipo de culinária.-----------
linhas_selecionadas = df1['cuisines'].notna()
df1 = df1.loc[linhas_selecionadas, :].copy()
df1['cuisines'] = df1.loc[:, 'cuisines'].apply(lambda x: x.split(",")[0])


#-----------------------------------------------------------------------
#---------Barra Lateral------------------------------------------
#-----------------------------------------------------------------------

#image_path = r"C:\Users\Samir\repos\pa_01\logo.png"
image = Image.open( 'logo.png')
st.sidebar.image( image, width=250 )
st.sidebar.markdown( '## Os melhores restaurantes nas principais cidades do mundo' )
st.sidebar.markdown( """___""")

#----------Filtros-------------------------------------------
st.sidebar.subheader( 'Filtros')
# Criação da lista de países
country_list = list(df1['country_name'].unique())
country_options = st.sidebar.multiselect(
    'Escolha os Países que deseja visualizar',
    country_list,
default = ['India', 'United States of America', 'Brazil', 'England', 'Australia', 'South Africa'])

# Aplicação do filtro
linhas_selecionadas = df1['country_name'].isin(country_options)
df1 = df1.loc[linhas_selecionadas,:]

st.sidebar.markdown( """___""")

#-------Acesse os Dados-----------
st.sidebar.markdown(
    "### Acesse os dados no [Kaggle](https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv)")

st.sidebar.markdown( """___""")
st.sidebar.markdown( 'Desenvolvido por [Samir Mascarenhas](https://www.linkedin.com/in/samir-mascarenhas/)')


#-----------------------------------------------------------------------
#---------Layout no Streamlit-------------------------------------------
#-----------------------------------------------------------------------
st.title('📈 Dashboards')
tab1, tab2, tab3 = st.tabs( ['🌎Países', '🏙️Cidades', '👨‍🍳Culinárias'])

#----------Visão Países------------------------------------------------
with tab1:
    with st.container():
        st.subheader('🌎 Visão Países')
        

        fig = restaurantes_por_pais(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        fig = cidades_por_pais (df1)
        st.plotly_chart(fig, use_container_width=True)
        

    with st.container():
       col1, col2 = st.columns(2)

       with col1:
           fig = media_avaliacoes_pais(df1)
           st.plotly_chart(fig, use_container_width=False)
           
       with col2:
           fig = media_preco_prato_dois(df1)
           st.plotly_chart(fig, use_container_width=True)
    st.markdown( """---""")

#----------Visão Cidades------------------------------------------------
with tab2:
    with st.container():
        st.subheader('🏙️ Visão Cidades')
        st.subheader('Filtro')
        city_slider = st.slider('Selecione a quantidade que deseja visualizar',
                                        1, 20, 10, key='tab2_slider')

        fig = cidades_mais_restaurantes(df1, city_slider)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            fig = cidades_com_restaurantes_media_acima_4(df1, city_slider)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = cidades_com_restaurantes_media_abaixo_2_5(df1, city_slider)
            st.plotly_chart(fig, use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            fig = cidades_top_avg_for_two (df1, city_slider)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = cidades_mais_restaurantes_tipo_de_culinaria_distintos(df1, city_slider)
            st.plotly_chart(fig, use_container_width=True)
        st.markdown( """---""")

#----------Visão Culinárias------------------------------------------------                        
with tab3:    
    with st.container():
        st.subheader('👨‍🍳 Visão Culinárias')
        st.subheader('Filtro')
        rest_slider = st.slider('Selecione a quantidade que deseja visualizar',
                                        1, 20, 10, key='tab3_slider')
        
        st.markdown('### Melhores restaurantes das principais culinárias')  
        
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            rest_1 = melhor_restaurante_por_cozinha(df1, "Brazilian")
            col1.metric(
                label=f'Comida Brasileira: {rest_1.iloc[0,2]}',
                value=f'{rest_1.iloc[0,3]}/5.0',
                help=f"""
                País: {rest_1.iloc[0, 4]}\n
                Cidade: {rest_1.iloc[0, 6]}\n
                Média de prato para dois: {rest_1.iloc[0, 7]} ({rest_1.iloc[0, 8]})
                """ )
        with col2:
            rest_2 = melhor_restaurante_por_cozinha(df1, "Italian")
            col2.metric(
                label=f'Comida Italiana: {rest_2.iloc[0,2]}',
                value=f'{rest_2.iloc[0,3]}/5.0',
                help=f"""
                País: {rest_2.iloc[0, 4]}\n
                Cidade: {rest_2.iloc[0, 6]}\n
                Média de prato para dois: {rest_2.iloc[0, 7]} ({rest_2.iloc[0, 8]})
                """ )
        with col3:
            rest_3 = melhor_restaurante_por_cozinha(df1, "Arabian")
            col3.metric(
                label=f'Comida  Árabe: {rest_3.iloc[0,2]}',
                value=f'{rest_3.iloc[0,3]}/5.0',
                help=f"""
                País: {rest_3.iloc[0, 4]}\n
                Cidade: {rest_3.iloc[0, 6]}\n
                Média de prato para dois: {rest_3.iloc[0, 7]} ({rest_3.iloc[0, 8]})
                """ ) 
        with col4:
            rest_4 = melhor_restaurante_por_cozinha(df1, "Pizza")
            col4.metric(
                label=f'Pizzaria: {rest_4.iloc[0,2]}',
                value=f'{rest_4.iloc[0,3]}/5.0',
                help=f"""
                País: {rest_4.iloc[0, 4]}\n
                Cidade: {rest_4.iloc[0, 6]}\n
                Média de prato para dois: {rest_4.iloc[0, 7]} ({rest_4.iloc[0, 8]})
                """ )
        with col5:
            rest_5 = melhor_restaurante_por_cozinha(df1, "Japanese")
            col5.metric(
                label=f'Japanese: {rest_5.iloc[0,2]}',
                value=f'{rest_5.iloc[0,3]}/5.0',
                help=f"""
                País: {rest_5.iloc[0, 4]}\n
                Cidade: {rest_5.iloc[0, 6]}\n
                Média de prato para dois: {rest_5.iloc[0, 7]} ({rest_5.iloc[0, 8]})
                """ )
             
    with st.container():
        st.markdown( """---""")
        st.markdown(f'#### Top {rest_slider} melhores restaurantes')
        
        df_result = best_restaurantes(df1, rest_slider)
        st.dataframe(df_result.head(rest_slider), use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig = top_10_cuisines (df1, False, f'Top {rest_slider} Melhores tipos de Culinárias', rest_slider)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = top_10_cuisines (df1, True, f'Top {rest_slider} Piores tipos de Culinárias', rest_slider)
            st.plotly_chart(fig, use_container_width=True)
        st.markdown( """---""")
            
       
            
        
        
        


           

                        
       
           
