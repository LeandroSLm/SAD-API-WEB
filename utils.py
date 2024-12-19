from geopy.geocoders import Nominatim
import re 

geolocator = Nominatim(user_agent="pib-brasil")

def obter_coordenadas(cidades):
    geolocator = Nominatim(user_agent="geopy_app")
    coordenadas = []
    for cidade, estado in cidades:
        try:
            localizacao = geolocator.geocode(f"{cidade}, {estado}, Brasil")
            if localizacao:
                coordenadas.append((cidade, estado, localizacao.latitude, localizacao.longitude))
            else:
                coordenadas.append((cidade, estado, None, None))
        except Exception as e:
            coordenadas.append((cidade, estado, None, None))
    return coordenadas

def extrair_estado(cidade_estado):
    match = re.search(r'\((\w{2})\)', cidade_estado) 
    return match.group(1) if match else None

def extrair_cidade(cidade_estado):
    return cidade_estado.split('(')[0].strip()

municipio = 'Municípios e respectivas\nUnidades da Federação'

mapa_regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}