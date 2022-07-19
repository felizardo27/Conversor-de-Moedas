import requests

class ConversorMoedas:
    
    def __init__(self, moeda1, moeda2):
        self.__moeda1 = moeda1
        self.__moeda2 = moeda2
        
    def __request_url(self):
        url = f"https://api.exchangerate-api.com/v4/latest/{self.__moeda1}"
        r = requests.get(url)
        dados = r.json()
        dados = dados['rates']
        return dados[self.__moeda2]

    def cotacao_atual(self):
        return self.__request_url()

    def converter(self, valor):
        return self.cotacao_atual() * valor