import csv
import os
def substituir_delimitador(input_path, output_path):
    with open(input_path, 'r', newline='') as arquivo_entrada:
        # Lê o arquivo CSV usando ponto e vírgula como delimitador
        leitor_csv = csv.reader(arquivo_entrada, delimiter=';')

        linhas = list(leitor_csv)  # Lê todas as linhas

        # Substitui o delimitador
        for linha in linhas:
            for i in range(len(linha)):
                linha[i] = linha[i].replace(';', ',')

    with open(output_path, 'w', newline='') as arquivo_saida:
        # Escreve o arquivo CSV usando vírgula como delimitador
        escritor_csv = csv.writer(arquivo_saida, delimiter=',')
        escritor_csv.writerows(linhas)

# Caminhos dos arquivos de entrada e saída
pasta = r'C:\pythonjr\vpp_eto\\'
nome_arquivo_entrada = 'trafo_133489_Original.csv'
nome_arquivo_saida = 'arquivo_saida.csv'

# Construindo os caminhos completos
caminho_arquivo_entrada = os.path.join(pasta, nome_arquivo_entrada)
caminho_arquivo_saida = os.path.join(pasta, nome_arquivo_saida)

# Chamando a função para substituir os delimitadores
substituir_delimitador(caminho_arquivo_entrada, caminho_arquivo_saida)
