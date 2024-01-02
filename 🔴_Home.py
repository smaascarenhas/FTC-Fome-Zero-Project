import streamlit as st
from PIL import Image
import webbrowser


st.set_page_config(
    page_title="Home",
    page_icon="⚙️",
)


#-----------------------------------------------------------------------
#---------Barra Lateral------------------------------------------
#-----------------------------------------------------------------------
image = Image.open( 'logo.png' )
st.sidebar.image( image, width=250 )

st.sidebar.markdown( '#  Fome Zero: Food & Delivery' )
st.sidebar.markdown( """___""")

#-------Acesse os Dados-----------
st.sidebar.markdown("### Acesse os dados no [Kaggle](https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv)")


#-------Desenvolvido por-----------
st.sidebar.markdown( """___""")
st.sidebar.markdown( 'Desenvolvido por [Samir Mascarenhas](https://www.linkedin.com/in/samir-mascarenhas/)')

#-----------------------------------------------------------------------
#---------Layout no Streamlit-------------------------------------------
#-----------------------------------------------------------------------

st.write( "# Fome Zero Restaurants Dashboard" )
st.markdown( """---""")

st.markdown(
    """
    ### O que é Fome Zero Restaurants?
    A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
    business é facilitar o encontro e negociações de clientes e restaurantes. Os
    restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
    informações como endereço, tipo de culinária servida, se possui reservas, se faz
    entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
    dentre outras informações.
    
    ### Como utilizar esse Growth Dashboard?
    O dashboard desenvolvido analisa métricas importantes relacionadas a Países, Cidades e Culinárias, 
    apresentando os resultados através de painéis interativos.
    - 🔴Home:
        - Nesta página você encontra uma breve descrição do projeto
    - ⚙️Main Page:
        - Métricas Gerais: Facilita o entendimento do negócio
        - Mapa interativo: Ajuda a localizar  o restaurante mais próximo de você
    - 📊Dashboards: 
        - Nesta aba, você encontrará gráficos interativos com três visões diferentes:
            - Visão Países: Insights de geolocalização.
            - Visão Cidades: Análise de Métricas Específicas por Cidade
            - Visão Culinárias: Avaliação de Métricas Relacionadas às Diversas Culinárias.
    - 📌Contato:
        - Nesta seção, estão listadas as principais redes para entrar em contato comigo.
    
    ### Fonte de dados:
    Este projeto foi desenvolvido de forma independente e não mantém uma conexão direta com a empresa da qual os dados foram 
    originados. O conjunto de dados é da empresa Zomato, uma plataforma global de tecnologia para alimentos e restaurantes, 
    presente em vários países. Na Índia, se destaca como uma das principais plataformas para delivery de alimentos, 
    permitindo aos usuários pesquisar, visualizar cardápios, fazer pedidos e receber entregas. 
    Além disso, oferece avaliações de usuários para auxiliar na escolha de locais para refeições. Seus dados estão disponíveis 
    publicamente na plataforma Kaggle:
        https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv

    """
        )
st.markdown( """---""")