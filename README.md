# 1. **Problema de negócio**

**Contexto do Problema de Negócio:
Parabéns! Você acaba de ser contratado como Cientista de Dados da empresa
Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra
a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer
utilizando dados! A empresa Fome Zero é uma Marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.**

**O Desafio
O CEO também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados Dashboards, a partir dessas análises, para responder
às seguintes perguntas:**

 1. **Geral**
    1. **Quantos restaurantes únicos estão registrados?**
    2. **Quantos países únicos estão registrados?**
    3. **Quantas cidades únicas estão registradas?**
    4. **Qual o total de avaliações feitas?**
    5. **Qual o total de tipos de culinária registrados?**
    6. **Mapa com localização dos restaurantes**
 2. **Países**
    1. **Qual o nome do país que possui mais cidades registradas?**
    2. **Qual o nome do país que possui mais restaurantes registrados?**
    3. **Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
    registrados?**
    4. **Qual o nome do país que possui a maior quantidade de tipos de culinária
    distintos?**
    5. **Qual o nome do país que possui a maior quantidade de avaliações feitas?**
    6. **Qual o nome do país que possui a maior quantidade de restaurantes que fazem
    entrega?**
    7. **Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
    reservas?**
    8. **Qual o nome do país que possui, na média, a maior quantidade de avaliações
    registrada?**
    9. **Qual o nome do país que possui, na média, a maior nota média registrada?**
    10. **Qual o nome do país que possui, na média, a menor nota média registrada?**
    11. **Qual a média de preço de um prato para dois por país?**
3. **Cidades**
    1. **Qual o nome da cidade que possui mais restaurantes registrados?**
    2. **Qual o nome da cidade que possui mais restaurantes com nota média acima de
    4?**
    3. **Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
    2.5?**
    4. **Qual o nome da cidade que possui o maior valor médio de um prato para dois?**
    5. **Qual o nome da cidade que possui a maior quantidade de tipos de culinária
    distintas?**
    6. **Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
    reservas?**
    7. **Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
    entregas?**
    8. **Qual o nome da cidade que possui a maior quantidade de restaurantes que
    aceitam pedidos online?**
4. **Restaurantes**
    1. **Qual o nome do restaurante que possui a maior quantidade de avaliações?**
    2. **Qual o nome do restaurante com a maior nota média?**
    3. **Qual o nome do restaurante que possui o maior valor de uma prato para duas
    pessoas?**
    6. **Os restaurantes que aceitam pedido online são também, na média, os
    restaurantes que mais possuem avaliações registradas?**
    7. **Os restaurantes que fazem reservas são também, na média, os restaurantes que
    possuem o maior valor médio de um prato para duas pessoas?**
5. **Tipos de Culinárias**
    1. **Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
    restaurante com a maior média de avaliação?**
    2. **Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
    restaurante com a maior média de avaliação?**
    3. **Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
    restaurante com a maior média de avaliação?**
    4. **Qual o tipo de culinária que possui o maior valor médio de um prato para duas
    pessoas?**
    5. **Qual o tipo de culinária que possui a maior nota média?**
    6. **Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
    online e fazem entregas?**

**O CEO também pediu que fosse gerado um Dashboard que permitisse que ele
visualizasse as principais informações das perguntas que ele fez. O CEO precisa
dessas informações o mais rápido possível, uma vez que ele também é novo na
empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir
tomar decisões mais assertivas.
Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as
perguntas feitas do CEO e criar o dashboard solicitado.**

# 2. Premissas do negócio

- **Marketplace foi o modelo de negócio assumido.**
- **As 3 principais visões do negócio foram:** 
    1. **Visão Países**
    2. **Visão Cidades**
    3. **Visão Culinárias**

# 3. **Estratégia da solução**

**O painel estratégico foi desenvolvido utilizando as métricas que
refletem as 3 principais visões do modelo de negócio da empresa:**

1. **Visão dos Países**
2. **Visão das Cidades**
3. **Visão das Culinárias**
- **Cada visão é representada pelo seguinte conjunto de métricas**
1. **Geral**
    1. **Quantos restaurantes únicos estão registrados?**
    2. **Quantos países únicos estão registrados?**
    3. **Quantas cidades únicas estão registradas?**
    4. **Qual o total de avaliações feitas?**
    5. **Qual o total de tipos de culinária registrados?**
    6. **Mapa interativo com localização dos restaurantes**
2. **Visão do crescimento dos Países**
    1. **Quantidade de restaurantes por País**
    2. **Quantidade de cidades por País**
    3. **Média de avaliações feitas por país**
    4. **Média de preço de um prato para duas pessoas por País**
3. **Visão do crescimento das Cidades**
    1. **Top 10 Cidades com mais restaurantes**
    2. **Top 10 Cidades com mais restaurantes com média de avaliação acima de 4**
    3. **Top 10 Cidades com mais restaurantes com média de avaliação abaixo de 2.5**
    4. **Top 10 Cidades com maior preço médio de um prato para duas pessoas**
    5. **Top 10 Cidades com mais restaurantes com tipos de culinárias distintos**
4. **Visão do crescimento das Culinárias**
    1. **Melhores restaurantes das principais culinárias: Brasileira, Italiana, Árabe, Pizzaria e Japonesa.**
    2. **Top 10 Melhores restaurantes** 
    3. **Top 10 Melhores tipos de culinárias**
    4. **Top 10 piores tipos de culinárias**

# 4. **Top 5 Insights de dados**

- **Os restaurantes que aceitam pedidos online, são, na média, os restaurantes que possuem mais avaliações registradas.**
- **Os restaurantes que fazem reserva, são, na média, os restaurantes que possuem maior valor médio de um prato pra 2 pessoas**
- **Indonésia é o País com maior média de avaliações feitas**
- **Birmingham é a cidade com maior variedade de culinárias**
- **O melhor restaurante de comida brasileira é o Texas de Brazil, localizado na cidade de Abu Dhabi.**

# 5. **O produto final do projeto**

**Painel online, hospedado em um Cloud e disponível para acesso em
qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link:** https://ftc-fomezero-smc.streamlit.app/

# 6. **Conclusão**

**O objetivo desse projeto é criar painéis interativos com gráficos e/ou tabelas
que exibam essas métricas da melhor forma possível para o CEO.
Da visão da Restaurantes, podemos concluir que dos Top 10 melhores, 8 estão na Índia.**

# **7. Próximo passos**

- **Reduzir o número de métricas**
- **Adicionar novas visões de negócio**
- **Adicionar outros tipos de gráfico**
