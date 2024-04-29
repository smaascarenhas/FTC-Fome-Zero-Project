# Contexto do Problema de negócio📊

A Fome Zero é uma plataforma de marketplace voltada para restaurantes, facilitando a conexão e negociações entre clientes e estabelecimentos. Os restaurantes se cadastrarem na plataforma, fornecendo informações como localização, tipo de culinária, disponibilidade de reservas, serviço de entrega e avaliações dos serviços e produtos, entre outros detalhes. Meu objetivo neste projeto é auxiliar a zomato através da análise de dados para responder às suas perguntas. 
**

## O Desafio

O CEO precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados Dashboards, a partir dessas análises, para responder
às seguintes perguntas:_

 ## Geral
   #### I. Quantos restaurantes únicos estão registrados? 
   #### II. Quantos países únicos estão registrados?
   #### III. Quantas cidades únicas estão registradas?
   #### IV. Qual o total de avaliações feitas?
   #### V. Qual o total de tipos de culinária registrados?
   #### VI. Mapa com localização dos restaurantes
##  Países
   #### I. Qual o nome do país que possui mais cidades registradas?
   #### II. Qual o nome do país que possui mais restaurantes registrados?
   #### III. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
   #### IV. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
   #### V. Qual o nome do país que possui a maior quantidade de avaliações feitas?
   #### VI. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
   #### VII. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
   #### VIII. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
   #### IX. Qual o nome do país que possui, na média, a maior nota média registrada?
   #### X. Qual o nome do país que possui, na média, a menor nota média registrada?
   #### XI. Qual a média de preço de um prato para dois por país?


 ## Cidades
   #### I. Qual o nome da cidade que possui mais restaurantes registrados?
   #### II. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
   #### III. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
   #### IV. Qual o nome da cidade que possui o maior valor médio de um prato para dois?**
   #### V. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
   #### VI. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
   #### VII. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
   #### VIII. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
   
 ## Restaurantes
   #### I. Qual o nome do restaurante que possui a maior quantidade de avaliações?
   #### II. Qual o nome do restaurante com a maior nota média?
   #### III. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
   #### IV. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
   #### V. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?

    
 ## Tipos de Culinárias
   #### I. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
   #### II. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
   #### III. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
   #### IV. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
   #### V. Qual o tipo de culinária que possui a maior nota média?
   #### VI. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?
   ---

__O CEO também pediu que fosse gerado um Dashboard que permitisse que ele
visualizasse as principais informações das perguntas que ele fez. O CEO precisa
dessas informações o mais rápido possível, uma vez que ele também é novo na
empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir
tomar decisões mais assertivas.
Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as
perguntas feitas do CEO e criar o dashboard solicitado.__

# 2. Premissas do negócio

- **Marketplace foi o modelo de negócio assumido.**
- **As 3 principais visões do negócio foram:** 
  ##### I. Visão Países
  ##### II. Visão Cidades
  ##### III. Visão Culinárias

# 3. **Estratégia da solução**

**A estratégia utilizada foi selecionar algumas das mais importantes perguntas de negócio que tragam os melhores insights acionáveis para o CEO,
para isso, utilizei python e streamlit para desenvolver o painel estratégico utilizando as métricas que
refletem as 3 principais visões do modelo de negócio da empresa:**

1. **Visão dos Países**
2. **Visão das Cidades**
3. **Visão das Culinárias**


# 4. **Top 5 Insights de dados**

- **Os restaurantes que aceitam pedidos online, são, na média, os restaurantes que possuem mais avaliações registradas.**
- **Os restaurantes que fazem reserva, são, na média, os restaurantes que possuem maior valor médio de um prato pra 2 pessoas**
- **Indonésia é o País com maior média de avaliações feitas**
- **Birmingham é a cidade com maior variedade de culinárias**
- **O melhor restaurante de comida brasileira é o Texas de Brazil, localizado na cidade de Abu Dhabi.**

# 5. **O produto final do projeto**

**Painel online, hospedado em um Cloud e disponível para acesso em
qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link:** https://ftc-fomezero-sm.streamlit.app/

# 6. **Conclusão**

**O objetivo desse projeto é criar painéis interativos com gráficos e/ou tabelas
que exibam essas métricas da melhor forma possível para o CEO.
Da visão da Restaurantes, podemos concluir que dos Top 10 melhores, 8 estão na Índia.**

# **7. Próximo passos**

- **Reduzir o número de métricas**
- **Adicionar novas visões de negócio**
- **Adicionar outros tipos de gráfico**
