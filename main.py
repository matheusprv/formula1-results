from bs4 import BeautifulSoup
import requests
import corrida as races

#def pegar_tipos_resultados():


def pegar_resultados_corrida(url, etapa):
    try:
        #Pegando o HTML do site
        html_text = requests.get(f'https://www.formula1.com/{url}').text
        soup = BeautifulSoup(html_text, 'lxml')
        tabelaResultado = soup.find('table', class_ = 'resultsarchive-table').tbody
        linhas_tabela = tabelaResultado.find_all('td')

        #Verificando qual a etapa do fim de semana e separando o número de colunas do html
        numeroColunas = 0
        if etapa == "qualifying" or etapa == "fastest-laps" or etapa == "pit-stop-summary":
            numeroColunas = 10

        elif etapa == "starting-grid" or etapa == "sprint-grid":
            numeroColunas = 7

        elif etapa == "practice-1" or etapa == "practice-2" or etapa == "practice-3" or etapa == "sprint-results" or etapa == "race-result":
            numeroColunas = 9


        #Pegando os valores do HTML
        pilotos = []
        piloto_atual = -1
        for index, linha in enumerate(linhas_tabela):
            if index % numeroColunas == 0:
                piloto_atual += 1
                pilotos.append([])
            pilotos[piloto_atual].append(linha.text)

        #Formatando o nome dos pilotos para remover o \n
        for index, formatar in enumerate(pilotos):
            pilotos[index][3] = formatar[3].replace('\n', ' ')

        for dados in pilotos:
            print(f'{dados}')

        salvar_dados = ""
        while salvar_dados != "s" and salvar_dados != "n":
            salvar_dados = input("Deseja salvar as informações em um arquivo .txt? s = SIM / n = NÃO : ")

        if salvar_dados == "s":
            #Salvando dados em um arquivo txt
            link = (f'https://www.formula1.com/{url}')
            link_dividido = link.split("/")
            pais = link_dividido[9]
            ano = link_dividido[6]
            with open(f'{pais.upper()} - {etapa.replace(".html", "").replace("-", " ").upper()} - {ano}.txt', 'w') as salvar:
                for dados in pilotos:
                    salvar.write(f'{dados}\n')

    except:
        print("Ainda não há dados sobre esse Grande Prêmio")


def pegar_etapas(url):
    #Pegando o HTML do site
    html_text = requests.get(f'https://www.formula1.com{url}').text
    soup = BeautifulSoup(html_text, 'lxml')
    lista = soup.find('div', class_ = 'resultsarchive-col-left')
    links_href = lista.find_all('a')

    #Salvando somente o link do elemento
    links = []
    for l in links_href:
        links.append(l['href'])

    #Exibindo o nome de cada etaoa com o que está contido no link
    for index, l in enumerate(links):
        url = l.split('/')
        exibir_etapa = url[-1].replace(".html", "").replace("-", " ").upper()
        print(f"{index+1}: {exibir_etapa}")

    #Solicitando ao usuário que digite a etapa desejada
    pesquisa = -1
    while pesquisa > len(links) or pesquisa < 0:
        pesquisa = int(input("Número do item a ser buscado: "))

    return links_href[pesquisa-1]['href']


if __name__ == '__main__':

    corridas = races.ler_corridas()

    #Verificando o ano atual e o ano limite para evitar pesquisa de dados inexistentes
    import datetime
    data = datetime.datetime.now()
    ano_atual = int(data.year)

    ano_pesquisar = int(input("Digite o ano para pesquisa: "))
    while ano_pesquisar > ano_atual or ano_pesquisar < 1950 :
        ano_pesquisar = int(input(f"Data inválida. O ano deve estar entre 1950 e {ano_atual}\nDigite o ano para pesquisa: "))

    #Procurando os dados do ano solicitado pelo usuário
    ano_pesquisar = str(ano_pesquisar)

    codigos_corrida = []
    codigo_corrida_pesquisa = 0

    for procurar in corridas:
        if procurar.ano == ano_pesquisar:
            print(procurar.informacao_grande_premio())
            codigos_corrida.append(procurar.corrida)

    while not codigo_corrida_pesquisa in codigos_corrida:
        codigo_corrida_pesquisa = input(f"Digite o código da corrida desejada: ")

    #Procurar a URL da corrida desejada
    for corridaEspecificada in corridas:
        if codigo_corrida_pesquisa == corridaEspecificada.corrida:
            url_etapa = pegar_etapas(corridaEspecificada.url)
            etapa = url_etapa.split("/")
            etapa = etapa[-1].replace(".html", "")
            break

    pegar_resultados_corrida(url_etapa, etapa)