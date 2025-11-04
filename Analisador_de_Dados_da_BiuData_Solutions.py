# 📊 Desafio: “Analisador de Dados da BiuData Solutions”
import time 
# Você foi contratado pela BiuData Solutions, uma empresa que está desenvolvendo um sistema de análise de dados de vendas.
# Sua missão é coletar os dados de vendas de vários vendedores e gerar um pequeno relatório inteligente com base nas médias e totais.
print('Olá! Sou a Inteligência Artificial Biu Solutions!')
time.sleep(1)
print('Mas, o que eu faço? Fui desenvolvido pela BiuData Solutions para ajudar e falicitar as empresas nos relatórios relacionados as vendas, lucros e armazenagem de dados.')
time.sleep(2)
print('Vamos começar a análise.')
time.sleep(1)
print('Sistema carregando...')
print('__________________________________________')
time.sleep(2)

nomes = []
quantidades = []
totais = []

while True:
    nome = input('Digite o Nome do Vendedor:')
    qtd_vendas = float(input('Digite o número de vendas realizadas:'))
    total_vendas = float(input('Digite o valor total das vendas (R$):'))

    nomes.append(nome)
    quantidades.append(qtd_vendas)
    totais.append(total_vendas)
    # O sistema deve calcular:
    media_valor_por_vendas = (total_vendas / qtd_vendas)
    # Avaliador de desempenho
    if media_valor_por_vendas >= 1000:
        print('Desempenho excepcional 💎')
    elif 500 <= media_valor_por_vendas <= 999:
        print('Bom desempenho 💼')
    else:
        print('Desempenho baixo ⚠️')

    deseja_mais_vendas = input('Deseja adicionar mais um vendedor?(s/n)').lower()
    if deseja_mais_vendas == 'n':
        break

total_geral = sum(totais)
quant_vendedores = len(nomes)

# Final e resultado do Relatório:
print('O total de Vendedores cadastrados foram:',quant_vendedores,'.')
print('O Total de Vendas foram de:', total_geral,'.')