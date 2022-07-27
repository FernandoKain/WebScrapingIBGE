# pip install requests
# pip install beautifulsoup4
# pip install pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrap_state_info(state: str) -> dict:
    """Retorna informações do estado brasileiro
    : param state: nome do estado
    : returns state_dict: dicionário com indicadores do estado
    """

    print(f'Picking {state} info...')
    state_url = f'https://www.ibge.gov.br/cidades-e-estados/{state}.html'
    page = requests.get(state_url)

    # Verifica se a página está respondendo. Response[200] indica um sucesso
    #print(page)

    # Permite que o html e o css possam ser selecionados
    soup = BeautifulSoup(page.content, 'html.parser')
    # Seleciona todas as divs com o nome "indicador" e armazena da variável "indicadors"
    indicadors = soup.select('.indicador')

    #Imprime todos as classes "indicador" do html
    #print(indicadors)

    #Retorna todos os valores das classes "indicador" do html
    #return indicadors

    #Retorna de maneira rústica os valores contidos nas divs "ind-label" e "ind-value"
    #return print([(ind.select('.ind-label')[0].text, ind.select('.ind-value')[0].text) for ind in indicadors])

    #Retornando um dicionário, que será posteriormente melhor aproveitado pela biblioteca pandas
    state_dict = {
        ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text
        for ind in indicadors
    }

    state_dict['Estado'] = state

    #Retorna e imprime no console as requisições
    #return print(state_dict)

    #Só retorna as informações sem imprimir no console
    return state_dict

#
states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE',
          'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
          'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
          'RJ', 'RN', 'RS', 'RO', 'RR', 'SC',
          'SP', 'SE', 'TO']

#
states_data = [scrap_state_info(state) for state in states]

df = pd.DataFrame(states_data)
df.head()
df.info()