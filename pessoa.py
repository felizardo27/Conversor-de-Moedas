class Pessoa:
    def __init__(self, nome, pais):
        self.__nome = nome
        self.__pais = pais
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def pais(self):
        return self.__pais
    
    def __str__(self):
        return f'Olá {self.__nome} do pais {self.__pais}'