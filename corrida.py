class corrida:
    def __init__(self, ano, corrida, pais, url):
        self.ano = ano
        self.corrida = corrida
        self.pais = pais
        self.url =url

    def toString(self):
        return (f'Ano: {self.ano} - Corrida: {self.corrida} - País: {self.pais} - URL: {self.url}')

    def informacao_grande_premio(self):
        return (f'Etapa: {self.corrida} - País: {(self.pais).replace("-"," ").title()}')

def ler_corridas():

    arquivo = open('corridas.txt', 'r')
    linhas = arquivo.readlines()

    for index, linha in enumerate(linhas):
        linhas[index] = linha.replace("\n", "")
    arquivo.close()

    corridas = []
    for i in range (0, len(linhas), 4):
        corridas.append(corrida(linhas[i+1], linhas[i], linhas[i+2], linhas[i+3]))

    return corridas




#ano = int(input("Digite o ano para pesquisa: "))
#html_text = requests.get(f"https://www.formula1.com/en/results.html/{ano}/races.html").text
#soup = BeautifulSoup(html_text, 'lxml')
#corridas = soup.find_all('ul', class_='ResultFilterScrollable')
#locais = corridas[2].find_all('a')
#locais.pop(0)

#with open('corridas.txt', 'a') as file:
#    for l in locais:
#       infoCompleta = l.get('href')
#        info = infoCompleta.split('/')
#        ano = info[3]
#        codigoCorrida = info[5]
#        pais = info[6]

#        file.write(f'{codigoCorrida}\n{ano}\n{pais}\n{infoCompleta}\n')

#        print(info)
#    file.close()