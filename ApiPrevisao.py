import requests

cidade = input("Digite o nome da cidade: ")

API_KEY = "42604df8f38bbfbaec6e5239c2c8ba24"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)

requisicao_dic = requisicao.json()

descrição = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
vento = requisicao_dic['wind']['speed'] *3.6
umidade = requisicao_dic['main']['humidity']

print("O clima em",cidade,"é", descrição, "\nTemperatura", f"{round(temperatura, 2)}ºC", "\nUmidade do ar", f"{round(umidade)}%", "\nVento", f"{round(vento, 2)} Km")