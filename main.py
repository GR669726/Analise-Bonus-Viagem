import pandas as pd
import openpyxl as op
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC06508ce253b0039cb54b3d2dc8bfffdf"
# Your Auth Token from twilio.com/console
auth_token  = "ecaefa78d9bd7ac1eb8e9f1ab58209a9"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
             to="+5511965423131",
             from_="+17205136584",
             body=f'No mês {mes} alguém bateu a meta. vendedor: {vendedor}, Vendas: {vendas}')
print(message.sid)



# Para cada arquivo:
# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000
# Se for mair do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
# Caso não seja maior que 55.000 não quero fazer nada

# pandas -> Integração Phyton com Excel
# openpyxl -> Integração Phyton com Excel
# twilio -> Integração Phyton com SMS

