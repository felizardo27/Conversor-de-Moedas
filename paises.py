
class Moedas:
    def __init__(self):
        self.__dados_moedas = {
            'africa': {
                 1 :{'pais':'África do Sul',        'moeda' : 'ZAR'},
                 2 :{'pais': 'Angola',              'moeda' : 'AOA'},
                 3 :{'pais': 'Camarões',            'moeda' : 'XAF'},
                 4 :{'pais': 'Costa do Marfim',     'moeda' : 'XOF'},
                 5 :{'pais': 'Egito',               'moeda' : 'EGP'},
                 6 :{'pais': 'Gabão',               'moeda' : 'XAF'},
                 7 :{'pais': 'Guiné',               'moeda' : 'GNF'},
                 8 :{'pais': 'Marrocos',            'moeda' : 'MAD'},
                 9 :{'pais': 'Moçambique',          'moeda' : 'MZN'},
                10:{'pais' : 'Nigéria',             'moeda' : 'NGN'},
                11:{'pais' : 'República do Congo',  'moeda' : 'XAF'},
                12:{'pais' : 'Senegal',             'moeda' : 'XOF'},
                13:{'pais' : 'Tanzânia',            'moeda' : 'TZS'},
                14:{'pais' : 'Tunísia',             'moeda' : 'TND'},
                15:{'pais' : 'Zâmbia',              'moeda' : 'ZMW'}
            },
            'america do norte': {
                1: {'pais' : 'Estados Unidos' , 'moeda': 'USD'},
                2: {'pais' : 'Canada' ,         'moeda': 'CAD'},
                3: {'pais' : 'Mexico' ,         'moeda': 'MXN'}
            },
            'america do sul': {
                1: {'pais' : 'Argentina' ,  'moeda': 'ARS'},
                2: {'pais' : 'Bolívia' ,    'moeda': 'BOB'},
                3: {'pais' : 'Brasil' ,     'moeda': 'BRL'},
                4: {'pais' : 'Chile' ,      'moeda': 'CLP'},
                5: {'pais' : 'Colômbia' ,   'moeda': 'COP'},
                6: {'pais' : 'Equador' ,    'moeda': 'USD'},
                7: {'pais' : 'Guiana' ,     'moeda': 'GYD'},
                8: {'pais' : 'Paraguai' ,   'moeda': 'PYG'},
                9: {'pais' : 'Peru' ,       'moeda': 'PEN'},
                10: {'pais' : 'Suriname' ,  'moeda': 'SRD'},
                11: {'pais' : 'Uruguai' ,   'moeda': 'UYU'},
                12: {'pais' : 'Venezuela' , 'moeda': 'VED'},
            },
            'asia': {
                    1:{'pais': 'Afeganistão',              'moeda' : 'AFN' },
                    2:{'pais': 'Arábia Saudita',           'moeda' : 'SAR' },
                    3:{'pais': 'Azerbaijão',               'moeda' : 'AZN' },
                    4:{'pais': 'Bahrein',                  'moeda' : 'BHD' },
                    5:{'pais': 'Bangladesh',               'moeda' : 'BDT' },
                    6:{'pais': 'Brunei',                   'moeda' : 'BND' },
                    7:{'pais': 'Camboja',                  'moeda' : 'KHR' },
                    8:{'pais': 'Cazaquistão',              'moeda' : 'KZT' },
                    9:{'pais': 'Catar',                    'moeda' : 'QAR' },
                    10:{'pais': 'China',                    'moeda' : 'CNY' },
                    11:{'pais': 'Chipre',                   'moeda' : 'EUR' },
                    12:{'pais': 'Singapura',                'moeda' : 'SGD' },
                    13:{'pais': 'Coreia do Norte',          'moeda' : 'KPW' },
                    14:{'pais': 'Coreia do Sul',            'moeda' : 'KRW' },
                    15:{'pais': 'Egito',                    'moeda' : 'EGP' },
                    16:{'pais': 'Emirados Árabes Unidos',   'moeda' : 'AED' },
                    17:{'pais': 'Geórgia',                  'moeda' : 'GEL' },
                    18:{'pais': 'Índia',                    'moeda' : 'INR' },
                    19:{'pais': 'Indonésia',                'moeda' : 'IDR' },
                    20:{'pais': 'Iraque',                   'moeda' : 'IQD' },
                    21:{'pais': 'Israel',                   'moeda' : 'ILS' },
                    22:{'pais': 'Jordânia',                 'moeda' : 'JOD' },
                    23:{'pais': 'Kuwait',                   'moeda' : 'KWD' },
                    24:{'pais': 'Laos',                     'moeda' : 'LAK' },
                    25:{'pais': 'Líbano',                   'moeda' : 'LBP' },
                    26:{'pais': 'Malásia',                  'moeda' : 'MYR' },
                    27:{'pais': 'Myanmar',                  'moeda' : 'MMK' },
                    28:{'pais': 'Mongólia',                 'moeda' : 'MNT' },
                    29:{'pais': 'Nepal',                    'moeda' : 'NPR' },
                    30:{'pais': 'Omã',                      'moeda' : 'OMR' },
                    31:{'pais': 'Paquistão',                'moeda' : 'PKR' },
                    32:{'pais': 'Quirguistão',              'moeda' : 'KGS' },
                    33:{'pais': 'Rússia',                   'moeda' : 'RUB' },
                    34:{'pais': 'SriLanka',                 'moeda' : 'LKR' },
                    35:{'pais': 'Tajiquistão',              'moeda' : 'TJS' },
                    36:{'pais': 'Tailândia',                'moeda' : 'THB' },
                    37:{'pais': 'Timor-Leste',              'moeda' : 'USD' },
                    38:{'pais': 'Turquemenistão',           'moeda' : 'TMT' },
                    39:{'pais': 'Turquia',                  'moeda' : 'TRY' },
                    40:{'pais': 'Uzbequistão',              'moeda' : 'UZS' },
                    41:{'pais': 'Vietnã',                   'moeda' : 'VND' }
            },
            'europa': { 
                    1:{'pais': 'Albânia',              'moeda' : 'ALL' },
                    2:{'pais': 'Alemanha',             'moeda' : 'EUR' },
                    3:{'pais': 'Andorra',              'moeda' : 'EUR' },
                    4:{'pais': 'Áustria',              'moeda' : 'EUR' },
                    5:{'pais': 'Bélgica',              'moeda' : 'EUR' },
                    6:{'pais': 'Bielorrússia',         'moeda' : 'BYN' },
                    7:{'pais': 'Bósnia e Herzegovina', 'moeda' : 'BAM' },
                    8:{'pais': 'Bulgária',             'moeda' : 'BGN' },
                    9:{'pais': 'Cazaquistão',          'moeda' : 'KZT' },
                    10:{'pais': 'Chipre',               'moeda' : 'EUR' },
                    11:{'pais': 'Croácia',              'moeda' : 'HRK' },
                    12:{'pais': 'Dinamarca',            'moeda' : 'DKK' },
                    13:{'pais': 'Eslováquia',           'moeda' : 'EUR' },
                    14:{'pais': 'Eslovénia',            'moeda' : 'EUR' },
                    15:{'pais': 'Espanha',              'moeda' : 'EUR' },
                    16:{'pais': 'Estónia',              'moeda' : 'EUR' },
                    17:{'pais': 'Finlândia',            'moeda' : 'EUR' },
                    18:{'pais': 'França',               'moeda' : 'EUR' },
                    19:{'pais': 'Grécia',               'moeda' : 'EUR' },
                    20:{'pais': 'Hungria',              'moeda' : 'HUF' },
                    21:{'pais': 'República da Irlanda', 'moeda' : 'EUR' },
                    22:{'pais': 'Islândia',             'moeda' : 'ISK' },
                    23:{'pais': 'Itália',               'moeda' : 'EUR' },
                    24:{'pais': 'Letónia',              'moeda' : 'EUR' },
                    25:{'pais': 'Liechtenstein',        'moeda' : 'CHF' },
                    26:{'pais': 'Lituânia',             'moeda' : 'EUR' },
                    27:{'pais': 'Luxemburgo',           'moeda' : 'EUR' },
                    28:{'pais': 'Malta',                'moeda' : 'EUR' },
                    29:{'pais': 'Moldávia',             'moeda' : 'MDL' },
                    30:{'pais': 'Mónaco',               'moeda' : 'EUR' },
                    31:{'pais': 'Montenegro',           'moeda' : 'EUR' },
                    32:{'pais': 'Noruega',              'moeda' : 'NOK' },
                    33:{'pais': 'Polónia',              'moeda' : 'PLN' },
                    34:{'pais': 'Portugal',             'moeda' : 'EUR' },
                    35:{'pais': 'Chéquia',              'moeda' : 'CZK' },
                    36:{'pais': 'Macedónia do Norte',   'moeda' : 'MKD' },
                    37:{'pais': 'Reino Unido',          'moeda' : 'GBP' },
                    38:{'pais': 'Reino Unido',          'moeda' : 'GBP' },
                    39:{'pais': 'Romênia',              'moeda' : 'RON' },
                    40:{'pais': 'Rússia',               'moeda' : 'RUB' },
                    41:{'pais': 'San Marino',           'moeda' : 'EUR' },
                    42:{'pais': 'Sérvia',               'moeda' : 'RSD' },
                    43:{'pais': 'Suécia',               'moeda' : 'SEK' },
                    44:{'pais': 'Suíça',                'moeda' : 'CHF' },
                    45:{'pais': 'Turquia',              'moeda' : 'TRY' },
                    46:{'pais': 'Vaticano',             'moeda' : 'EUR' }
            },
            'oceania': {
                     1: { 'pais': 'Austrália',                          'moeda' : 'AUD' },
                     2: { 'pais': 'Estados Federados da Micronésia',    'moeda' : 'USD' },
                     3: { 'pais': 'Fiji',                               'moeda' : 'FJD' },
                     4: { 'pais': 'Ilhas Marshall',                     'moeda' : 'USD' },
                     5: { 'pais': 'Ilhas Salomão',                      'moeda' : 'SBD' },
                     6: { 'pais': 'Kiribati',                           'moeda' : 'AUD' },
                     7: { 'pais': 'Nauru',                              'moeda' : 'AUD' },
                     8: { 'pais': 'Nova Zelândia',                      'moeda' : 'NZD' },
                     9: { 'pais': 'Palau',                              'moeda' : 'USD' },
                    10: { 'pais': 'Papua Nova Guiné',                   'moeda' : 'PGK' },
                    11: { 'pais': 'Samoa',                              'moeda' : 'WST' },
                    12: { 'pais': 'Tonga',                              'moeda' : 'TOP' },
                    13: { 'pais': 'Tuvalu',                             'moeda' : 'AUD' },
                    14: { 'pais': 'Vanuatu',                            'moeda' : 'VUV' }
            }
        }
    
    def imprimir(self, lista):
        for i, objeto in enumerate(lista):
            print(i+1, objeto)
    
    def continentes(self):
        lista = []
        for continentes in self.__dados_moedas:
            lista.append(continentes)
        return lista
    
    def continente(self, continente):
        lista = []
        for paises in self.__dados_moedas[continente]:
            lista.append(self.__dados_moedas[continente][paises]['pais'])
        return lista
    
    def pais(self, continente, pais):
        return self.__dados_moedas[continente][pais]


    def escolher(self):
        print('\nContinentes: ')
        self.imprimir(self.continentes())
        op_cont = int(input('opcao: '))
        continente = self.continentes()[op_cont-1]
        
        print('\nPaises:')
        self.imprimir(self.continente(continente))
        pais = int(input('opcao: '))
        
        return self.pais(continente, pais)
