#-----------------------------------------------
# Bibliotecas Necessárias
#-----------------------------------------------
from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import folium
import pandas as pd
import streamlit as st
import datetime
from PIL import Image
import inflection
from streamlit_folium import folium_static
from millify import millify
from folium.plugins import MarkerCluster
import webbrowser

st.set_page_config( page_title='Main page', page_icon='💻', layout='wide')

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

def restaurant_map( df1 ):
    """ Esta função tem a responsabilidade de mostrar 
        A localização central de cada restaurante.
        Input: Dataframe
        Output: fig
    """
    
    cols = ['restaurant_id', 'restaurant_name', 'city', 'latitude', 'longitude', 'aggregate_rating', 'average_cost_for_two', 'cuisines']
    df_aux = df1.loc[:, cols].reset_index()

    map_aux = [df_aux['latitude'].median(), df_aux['longitude'].median()]
    map = folium.Map(location=map_aux, zoom_start=1)

    # Criando um agrupamento de marcadores
    marker_cluster = MarkerCluster().add_to(map)

    for index, location_info in df_aux.iterrows():
        popup_content = f"""
            <strong>{location_info['restaurant_name']}</strong> 
            Preço para dois: {location_info['average_cost_for_two']}\n 
            Tipo: {location_info['cuisines']}\n
            Nota: {location_info['aggregate_rating']}\n
        """
        
        # Adicionando o marcador no popup
        folium.Marker(
            location=[location_info['latitude'], location_info['longitude']],
            popup=popup_content,
            icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')
        ).add_to(marker_cluster)  

        # Exibindo o mapa no Streamlit
    folium_static(map, width=1024, height=600)


#-----------------------------------------------------------------------
#---------Importanto o Dataset------------------------------------------
#-----------------------------------------------------------------------
df = pd.read_csv( 'dataset/zomato.csv' )

#-----------------------------------------------------------------------
#---------Tratando os dados
#-----------------------------------------------------------------------


##---------Limpando o Dataset-------------------------------------------
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
default = ['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'])

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

with st.container():
        st.title( 'Fome Zero!' )
        st.header( 'O lugar perfeito para descobrir o seu novo restaurante favorito!')
        st.markdown( """---""")

        col1, col2, col3, col4, col5 = st.columns( 5, gap='large' )
        with col1:
            # Restaurantes Cadastrados
            restaurants_cadastrados = df1['restaurant_id'].nunique()
            col1.metric( 'Restaurantes Cadastrados', restaurants_cadastrados)
        
        with col2:
            # Países Cadastrados
            paises = df1['country_code'].nunique()
            col2.metric( 'Países Cadastrados', paises)

        with col3:
            # Cidades Cadastradas 
            cidades = df1['city'].nunique()
            col3.metric( 'Cidades Cadastradas', cidades )

        with col4:
            # Avaliações feitas na plataforma
            avaliacoes_formatadas = '{:,.0f}'.format(df1['votes'].sum()).replace(',', '.') 
            col4.metric('Avaliações Feitas na Plataforma', avaliacoes_formatadas)
           
        with col5:
            # Tipos de culinárias oferecidas
            tipos_culinarias = df1.loc[:,'cuisines'].nunique()
            col5.metric( 'Tipos de Culinárias Oferecidas', tipos_culinarias)

        st.markdown( """---""")
        restaurant_map(df1)
     



    


    

