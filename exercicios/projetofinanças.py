import requests
import os
import pprint
senha = os.environ['tolken']
ativo=input('digite um ativo:')
url = f'https://brapi.dev/api/quote/{ativo}?token={senha}'
response=requests.get(url)
data=response.json()
#pprint.pprint(data)
info = data['results'][0]

print(f"\nResumo de informações sobre {info['longName']} ({info['symbol']}):\n")
print(f"📈 Preço atual: R$ {info['regularMarketPrice']}")
print(f"💵 Lucro por ação (EPS): R$ {info['earningsPerShare']}")
print(f"📊 P/L (Preço/Lucro): {round(info['priceEarnings'], 2)}")
print(f"🏢 Valor de mercado: R$ {info['marketCap']:,.0f}")
print(f"📉 Variação diária: {info['regularMarketChange']} BRL ({info['regularMarketChangePercent']}%)")



#="tncDfegoH942k84xhJdiMf"

