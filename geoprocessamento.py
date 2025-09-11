# geoprocessamento.py
from geopy import distance

def calcular_distancia_km(coord1, coord2):
    """
    Calcula a distância entre dois pontos geográficos em quilômetros.
    """
    ponto1 = (coord1['latitude'], coord1['longitude'])
    ponto2 = (coord2['latitude'], coord2['longitude'])
    return distance.distance(ponto1, ponto2).km