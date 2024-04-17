import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter
from datetime import datetime

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\pythonjr\vpp_eto\medicoes_pq99.csv'

# Leitura do arquivo CSV usando pandas
dados = pd.read_csv(caminho_arquivo, delimiter=';')

# Convertendo a coluna "timestampsourcelt" para o formato de data e hora
dados['timestampsourcelt'] = pd.to_datetime(dados['timestampsourcelt'])

# Especificando os dias inicial e final
dia_inicial = '2024-04-10'
dia_final = '2024-04-16'

# Convertendo as datas para objetos datetime
data_inicial = datetime.strptime(dia_inicial, '%Y-%m-%d')
data_final = datetime.strptime(dia_final, '%Y-%m-%d')

# Filtrando os dados para incluir apenas o intervalo de dias especificado
dados = dados[(dados['timestampsourcelt'] >= data_inicial) & (dados['timestampsourcelt'] <= data_final)]

# Extraindo as colunas de interesse
timestamps = dados["timestampsourcelt"]

coluna_tensao_a = dados["tensao.average.van[V]"]
coluna_corrente_a = dados["corrente.average.ia[A]"]
coluna_potativa_a = dados["potencia.consumo.average.kwa[kW]"]
coluna_potreativa_a = dados["potencia.consumo.average.kvara[kvar]"]
coluna_potaparente_a = dados["potencia.consumo.average.kvaa[kva]"]

coluna_tensao_b = dados["tensao.average.vbn[V]"]
coluna_corrente_b = dados["corrente.average.ib[A]"]
coluna_potativa_b = dados["potencia.consumo.average.kwb[kW]"]
coluna_potreativa_b = dados["potencia.consumo.average.kvarb[kvar]"]
coluna_potaparente_b = dados["potencia.consumo.average.kvab[kva]"]

coluna_tensao_c = dados["tensao.average.vcn[V]"]
coluna_corrente_c = dados["corrente.average.ic[A]"]
coluna_potativa_c = dados["potencia.consumo.average.kwc[kW]"]
coluna_potreativa_c = dados["potencia.consumo.average.kvarc[kvar]"]
coluna_potaparente_c = dados["potencia.consumo.average.kvac[kva]"]

coluna_potativa_tot = dados["potencia.consumo.average.kw[kW]"]
coluna_potreativa_tot = dados["potencia.consumo.average.kvar[kvar]"]
coluna_potaparente_tot = dados["potencia.consumo.average.kva[kva]"]
coluna_deseqtensao = dados["desequilibrio.tensao.seq_negativa[%]"]
#coluna_deseqtensao = dados_["desequilibrio[%]"]


# Criando uma figura com subplots organizados
fig = plt.figure(figsize=(20, 10))

# Adicionando um nome para a figura
fig.suptitle("RESUMO SEMANAL - Medições PQ99 : {} a {}".format(dia_inicial, dia_final))

#########################################################################################

# Plotando os dados de tensão (V)
ax1 = fig.add_subplot(3, 2, 1)
ax1.plot(timestamps, coluna_tensao_a, color='red', label='Fase A')
ax1.plot(timestamps, coluna_tensao_b, color='blue', label='Fase B')
ax1.plot(timestamps, coluna_tensao_c, color='green', label='Fase C')
ax1.set_ylabel("Tensão Eficaz (V)")
ax1.grid(True, linestyle='--')
ax1.set_ylim(180, 240)
ax1.axhspan(202, 231, color='lightgreen', alpha=0.5)
ax1.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax1.set_xticklabels([])
ax1.legend(loc='upper left')

# Definindo o formato dos rótulos do eixo x
date_format = DateFormatter('%d/%m/%y %H:%M')
ax1.xaxis.set_major_formatter(date_format)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax1.xaxis.set_major_locator(HourLocator(interval=3))
# Ajustando o tamanho da fonte dos rótulos do eixo x
ax1.tick_params(axis='x', labelsize=9)
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

#########################################################################################

# Plotando os dados de corrente (A)
ax2 = fig.add_subplot(3, 2, 3)
ax2.plot(timestamps, coluna_corrente_a, color='red', label='Fase A')
ax2.plot(timestamps, coluna_corrente_b, color='blue', label='Fase B')
ax2.plot(timestamps, coluna_corrente_c, color='green', label='Fase C')
ax2.set_ylabel("Corrente Eficaz (V)")
ax2.grid(True, linestyle='--')
ax2.set_ylim(0, 200)
ax2.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax2.set_xticklabels([])
ax2.legend(loc='upper left')

# Definindo o formato dos rótulos do eixo x
date_format = DateFormatter('%d/%m/%y %H:%M')
ax2.xaxis.set_major_formatter(date_format)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax2.xaxis.set_major_locator(HourLocator(interval=3))
ax2.tick_params(axis='x', labelsize=9)
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

#########################################################################################

# Plotando os dados de desequilibrio de tensão (%)
ax3 = fig.add_subplot(3, 2, 5)
ax3.plot(timestamps, coluna_deseqtensao, color='black')
ax3.set_ylabel("Desequilíbrio de Tensão (%)")
ax3.grid(True, linestyle='--')
ax3.set_ylim(0, 6)
ax3.axhspan(0, 3, color='lightgreen', alpha=0.5)
ax3.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax3.set_xticklabels([])

# Definindo o formato dos rótulos do eixo x
date_format = DateFormatter('%d/%m/%y %H:%M')
ax3.xaxis.set_major_formatter(date_format)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax3.xaxis.set_major_locator(HourLocator(interval=3))
# Ajustando o tamanho da fonte dos rótulos do eixo x
ax3.tick_params(axis='x', labelsize=9)
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

#########################################################################################

# Plotando os dados de potência ativa total (kW)
ax4 = fig.add_subplot(3, 2, 2)
ax4.plot(timestamps, coluna_potativa_tot, color='black')
ax4.set_ylabel("Potência Ativa Total (kW)")
ax4.grid(True, linestyle='--')
ax4.set_ylim(-120, 120)
ax4.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax4.set_xticklabels([])

# Definindo o formato dos rótulos do eixo x
date_format = DateFormatter('%d/%m/%y %H:%M')
ax4.xaxis.set_major_formatter(date_format)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax4.xaxis.set_major_locator(HourLocator(interval=3))
# Ajustando o tamanho da fonte dos rótulos do eixo x
ax4.tick_params(axis='x', labelsize=9)
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade



##########################################################################################

# Plotando os dados de potência aparente total (kVA)
ax4 = fig.add_subplot(3, 2, 4)
ax4.plot(timestamps, coluna_potaparente_tot, color='black')
ax4.set_ylabel("Potência Aparente Total (kVA)")
ax4.grid(True, linestyle='--')
ax4.set_ylim(0, 120)
ax4.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax4.set_xticklabels([])

# Definindo o formato dos rótulos do eixo x
date_format = DateFormatter('%d/%m/%y %H:%M')
ax4.xaxis.set_major_formatter(date_format)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax4.xaxis.set_major_locator(HourLocator(interval=3))
# Ajustando o tamanho da fonte dos rótulos do eixo x
ax4.tick_params(axis='x', labelsize=9)
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

##########################################################################################

# Plotando os dados de potência reativa total (kvar)
ax4 = fig.add_subplot(3, 2, 6)
ax4.plot(timestamps, coluna_potreativa_tot, color='black')
ax4.set_ylabel("Potência Reativa Total (kvar)")
ax4.grid(True, linestyle='--')
ax4.set_ylim(-10, 20)
ax4.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax4.set_xticklabels([])

# Definindo o formato dos rótulos do eixo x
date_format = DateFormatter('%d/%m/%y %H:%M')
ax4.xaxis.set_major_formatter(date_format)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax4.xaxis.set_major_locator(HourLocator(interval=3))
# Ajustando o tamanho da fonte dos rótulos do eixo x
ax4.tick_params(axis='x', labelsize=9)
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

##########################################################################################
plt.tight_layout()  # Ajusta o layout para evitar sobreposição de rótulos
plt.show()