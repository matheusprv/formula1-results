from bs4 import BeautifulSoup
import requests
import corrida as races


def pegar_resultados_corrida(url):
    try:
        #Pegando o HTML do site
        html_text = requests.get(f'https://www.formula1.com/{url}').text
        soup = BeautifulSoup(html_text, 'lxml')
        tabelaResultado = soup.find('table', class_ = 'resultsarchive-table').tbody
        linhas_tabela = tabelaResultado.find_all('td')

        etapa = "corrida"

        #Verificando qual a etapa do fim de semana e separando o número de colunas do html
        numeroColunas = 0
        if etapa == "qualificação":
            numeroColunas = 10
        elif etapa == "largada":
            numeroColunas = 7
        elif etapa == "corrida":
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
            with open(f'{pais} - {ano}.txt', 'w') as salvar:
                for dados in pilotos:
                    salvar.write(f'{dados}\n')

    except:
        print("Ainda não há dados sobre esse Grande Prêmio")


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
            print(procurar.toString())
            codigos_corrida.append(procurar.corrida)

    while not codigo_corrida_pesquisa in codigos_corrida:
        codigo_corrida_pesquisa = input(f"Digite o código da corrida desejada: ")

    #Procurar a URL da corrida desejada
    for corridaEspecificada in corridas:
        if codigo_corrida_pesquisa == corridaEspecificada.corrida:
            pegar_resultados_corrida(corridaEspecificada.url)
            break


