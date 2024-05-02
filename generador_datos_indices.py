import uuid
import random
import threading
import time
from elasticsearch import Elasticsearch

def generate_casa_data():
    # Generar datos ficticios para una casa
    data = {
        "timestamp": int(time.time()),
        "house": {
            "rooms": random.randint(1, 10),
            "bathrooms": random.randint(1, 5),
            "size_sqft": random.randint(500, 5000),
            "year_built": random.randint(1900, 2022),
            "price_usd": random.randint(100000, 1000000)
        }
    }
    return data

def generate_ciudad_data(ciudades, poblacion_minima, poblacion_maxima):
    # Generar datos ficticios para una ciudad
    data = {
        "timestamp": int(time.time()),
        "city": {
            "name": random.choice(ciudades),
            "population": random.randint(poblacion_minima, poblacion_maxima),
            "country": "España"
        }
    }
    return data

def generate_and_write_data():
    global espera
    t = threading.Timer(espera, generate_and_write_data)
    t.start()
    
    # Conectar con Elasticsearch (asegúrate de que Elasticsearch está en funcionamiento)
    es = Elasticsearch(['http://localhost:9200'])

    # Crear el índice casas si no existe
    index_name_casas = "casas"
    mapping_casas = {
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "house": {
                    "properties": {
                        "rooms": {"type": "integer"},
                        "bathrooms": {"type": "integer"},
                        "size_sqft": {"type": "integer"},
                        "year_built": {"type": "integer"},
                        "price_usd": {"type": "integer"}
                    }
                }
            }
        }
    }
    if not es.indices.exists(index=index_name_casas):
        es.indices.create(index=index_name_casas, body=mapping_casas)

    # Crear el índice ciudades si no existe
    index_name_ciudades = "ciudades"
    mapping_ciudades = {
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "city": {
                    "properties": {
                        "name": {"type": "keyword"},
                        "population": {"type": "integer"},
                        "country": {"type": "keyword"}
                    }
                }
            }
        }
    }
    if not es.indices.exists(index=index_name_ciudades):
        es.indices.create(index=index_name_ciudades, body=mapping_ciudades)

    # Generar y enviar datos a Elasticsearch
    casa_data = generate_casa_data()
    ciudad_data = generate_ciudad_data(ciudades, poblacion_minima, poblacion_maxima)

    # Asignar IDs únicos a los documentos
    casa_id = str(uuid.uuid4())
    ciudad_id = str(uuid.uuid4())

    print(casa_data)
    print(ciudad_data)
    # Indexar los datos con los IDs únicos
    es.index(index=index_name_casas, id=casa_id, body=casa_data)
    es.index(index=index_name_ciudades, id=ciudad_id, body=ciudad_data)
    print("Datos enviados a Elasticsearch")

espera = 5
ciudades = [
    "Madrid",
    "Barcelona",
    "Valencia",
    "Sevilla",
    "Zaragoza",
    "Málaga",
    "Murcia",
    "Palma de Mallorca",
    "Las Palmas de Gran Canaria",
    "Bilbao",
    "Alicante",
    "Córdoba",
    "Valladolid",
    "Vigo",
    "Gijón",
    "L'Hospitalet de Llobregat",
    "Vitoria-Gasteiz",
    "La Coruña",
    "Granada",
    "Elche",
    "Oviedo",
    "Santa Cruz de Tenerife",
    "Pamplona",
    "Cartagena",
    "Sabadell",
    "Jerez de la Frontera",
    "Móstoles",
    "Alcalá de Henares",
    "Fuenlabrada",
    "Almería",
    "Terrassa",
    "Badalona",
    "Getafe",
    "Donostia-San Sebastián",
    "Leganes",
    "Santander",
    "Burgos",
    "Salamanca",
    "Alcorcón",
    "Albacete",
    "Castellón de la Plana",
    "Logroño",
    "Badajoz",
    "Huelva",
    "Marbella",
    "León",
    "Tarragona",
    "Cádiz",
    "Lleida",
    "Jaén",
    "Ourense",
    "Mataró",
    "Algeciras",
    "Alcobendas",
    "Cáceres",
    "Reus",
    "Telde",
    "Torrejón de Ardoz",
    "Barakaldo",
    "Parla",
    "Santiago de Compostela",
    "San Fernando",
    "Lugo",
    "Girona",
    "Coslada",
    "Talavera de la Reina",
    "Cornellà de Llobregat",
    "El Puerto de Santa María",
    "Melilla",
    "Orihuela",
    "Pontevedra",
    "Pozuelo de Alarcón",
    "Roquetas de Mar",
    "Chiclana de la Frontera",
    "Torrent",
    "San Sebastián de los Reyes",
    "Rubí",
    "Benidorm",
    "Fuengirola",
    "Ciudad Real",
    "Las Rozas de Madrid",
    "Benalmádena",
    "Sanlúcar de Barrameda",
    "Vélez-Málaga",
    "Torrevieja",
    "Zamora",
    "Rivas-Vaciamadrid",
    "Vilanova i la Geltrú",
    "Torrelavega",
    "Línea de la Concepción",
    "Gandia",
    "Manresa",
    "San Vicente del Raspeig",
    "Santa Lucía de Tirajana",
    "Mijas",
    "Majadahonda",
    "Sagunto",
    "Paterna",
    "San Sebastián de La Gomera",
    "Viladecans",
    "Torremolinos",
    "Estepona",
    "Rubí",
    "Molina de Segura",
    "Torrelodones",
    "Elda",
    "Ponferrada",
    "Alcobendas",
    "Arrecife",
    "Cuenca",
    "Valdemoro",
    "Pinto",
    "Sant Cugat del Vallès",
    "Palencia",
    "Alcantarilla",
    "Linares",
    "San Bartolomé de Tirajana",
    "Roquetas de Mar",
    "Coslada",
    "Tudela",
    "El Prat de Llobregat",
    "San Juan de Alicante",
    "Vinaròs",
    "Coslada",
    "Segovia",
    "Cártama",
    "Avilés",
    "Aranda de Duero",
    "Zarautz",
    "Vic",
    "Oliva",
    "Sestao",
    "Irun",
    "Ávila",
    "Parets del Vallès",
    "Paterna",
    "Alzira",
    "Benicarló",
    "Carballo",
    "Vila-real",
    "Sant Adrià de Besòs",
    "Villanueva y Geltrú",
    "Narón",
    "Camargo",
    "Puerto del Rosario",
    "El Ejido",
    "Arona",
    "Manacor",
    "Pineda de Mar",
    "Xàtiva",
    "Mogán",
    "Maó",
    "Los Realejos",
    "Vélez-Málaga",
    "Villaquilambre",
    "El Masnou",
    "La Orotava",
    "Ripollet",
    "Santurtzi",
    "Mazarrón",
    "Begur",
    "Benavente",
    "Leganés",
    "Castro-Urdiales",
    "Caldes de Montbui",
    "Tàrrega",
    "La Oliva",
    "Mijas",
    "Sant Andreu de la Barca",
    "Portugalete",
    "Molina de Aragón",
    "Adra"
  ]

poblacion_minima = 100000
poblacion_maxima = 3000000

generate_and_write_data()
