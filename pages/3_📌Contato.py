import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Contato",
    page_icon="📌",
)

#-----------------------------------------------------------------------
#---------Barra Lateral------------------------------------------
#-----------------------------------------------------------------------
image = Image.open( 'logo.png' )
st.sidebar.image( image, width=250 )

st.sidebar.markdown( '#  Fome Zero Restaurants' )
st.sidebar.markdown( """___""")

#-------Acesse os Dados-----------
st.sidebar.markdown(
    "### Acesse os dados no [Kaggle](https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv)")

#-------Desenvolvido por-----------
st.sidebar.markdown( """___""")
st.sidebar.markdown( 'Desenvolvido por [Samir Mascarenhas](https://www.linkedin.com/in/samir-mascarenhas/)')

#-----------------------------------------------------------------------
#---------Layout no Streamlit-------------------------------------------
#-----------------------------------------------------------------------

st.write( "# 📩 Entre em contato" )
st.markdown( """___""")

st.markdown(
    """
    
    ### Minhas redes
    - LinkedIn
        - https://www.linkedin.com/in/samir-mascarenhas/
    - Portfólio
        - https://github.com/smaascarenhas
    - E-mail 
        - smascarenhas313@gmail.com
    - Discord
        - @smcardoso
"""
)
st.markdown( """---""")