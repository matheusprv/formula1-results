from bs4 import BeautifulSoup
import requests

def pegar_tipos_resultados():
    #Pegando o HTML do site
    html_text = requests.get(f'https://www.formula1.com/en/results.html/2021/races/1104/brazil/race-result.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    lista = soup.find('div', class_ = 'resultsarchive-col-left')
    links_href = lista.find_all('a')

    links = []
    for l in links_href:
        links.append(l['href'])

    for index, l in enumerate(links):
        url = l.split('/')
        exibir_etapa = url[-1].replace(".html", "").replace("-", " ").upper()
        print(f"{index+1}: {exibir_etapa}")

    pesquisa = -1
    while pesquisa > len(links) or pesquisa < 0:
        pesquisa = int(input("Número do item a ser buscado: "))

    print(links[pesquisa-1])


#/en/results.html/2021/races/1104/brazil/race-result.html
#/en/results.html/2021/races/1104/brazil/fastest-laps.html
#/en/results.html/2021/races/1104/brazil/pit-stop-summary.html
#/en/results.html/2021/races/1104/brazil/starting-grid.html
#/en/results.html/2021/races/1104/brazil/sprint-results.html
#/en/results.html/2021/races/1104/brazil/sprint-grid.html
#/en/results.html/2021/races/1104/brazil/practice-2.html
#/en/results.html/2021/races/1104/brazil/qualifying.html
#/en/results.html/2021/races/1104/brazil/practice-1.html


if __name__ == '__main__':
    pegar_tipos_resultados()


def pegar():
    urls = []

    urls.append("/en/results.html/2021/races/1104/brazil/race-result.html")
    urls.append("/en/results.html/2021/races/1104/brazil/fastest-laps.html")
    urls.append("/en/results.html/2021/races/1104/brazil/pit-stop-summary.html")
    urls.append("/en/results.html/2021/races/1104/brazil/starting-grid.html")
    urls.append("/en/results.html/2021/races/1104/brazil/sprint-results.html")
    urls.append("/en/results.html/2021/races/1104/brazil/sprint-grid.html")
    urls.append("/en/results.html/2021/races/1104/brazil/practice-2.html")
    urls.append("/en/results.html/2021/races/1104/brazil/qualifying.html")
    urls.append("/en/results.html/2021/races/1104/brazil/practice-1.html")

    for i in urls:
        print(f"#############################\n{i}")
        html_text = requests.get(f'https://www.formula1.com/{i}').text
        soup = BeautifulSoup(html_text, 'lxml')
        tabelaResultado = soup.find('table', class_='resultsarchive-table').tbody
        linhas_tabela = tabelaResultado.find_all('td')

        pilotos = []
        for index, linha in enumerate(linhas_tabela):
            pilotos.append(linha.text)
            pilotos[-1] = pilotos[-1].replace("\n","-")

        for l in pilotos:
            print(l)