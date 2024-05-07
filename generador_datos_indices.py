import uuid
import random
import threading
from elasticsearch import Elasticsearch
from datetime import datetime, timezone

# Definir modelos y ubicaciones constantes para cada molino
info_modelos = [
    {
        "modelo": "G58",
        "latitud": 42.7275,
        "longitud": -2.1189
    },    
    {
        "modelo": "SG 14-222 DD",
        "latitud": 42.1564,
        "longitud": -1.5006
    },
    {
        "modelo": "V164-9.5 MW",
        "latitud": 42.7966,
        "longitud": -1.5714
    },    
    {
        "modelo": "EP3",
        "latitud": 36.0268,
        "longitud": -5.6029
    },
    {
        "modelo": "V164-9.5 MW",
        "latitud": 41.2537,
        "longitud": -3.3841
    },        
    {
        "modelo": "N149",
        "latitud": 41.1931,
        "longitud": 0.9238
    },    
    {
        "modelo": "SG 14-222 DD",
        "latitud": 39.7855,
        "longitud": -1.5069
    },
    {
        "modelo": "N149",
        "latitud": 42.1561,
        "longitud": -1.4995
    },    
    {
        "modelo": "EP3",
        "latitud": 41.1707,
        "longitud": 0.8285
    },
    {
        "modelo": "G58",
        "latitud": 41.1462,
        "longitud": -1.6677
    }
]

def generate_windmill_data(id):
    """
    Función para generar datos simulados de un molino de viento.
    """
    # Construir el diccionario de datos para el molino
    data = {
        "id": str(id),
        "model": info_modelos[id]["modelo"],
        "location": {
            "lat": info_modelos[id]["latitud"],
            "lon": info_modelos[id]["longitud"]
        },
        "timestamp": datetime.now(timezone.utc),
        "value": {
            "velocidad_viento": round(random.uniform(0, 25), 2),
            "direccion_viento": round(random.uniform(0, 360), 2),
            "produccion_energia": round(random.uniform(0, 100), 2),
            "temperatura_ambiente": round(random.uniform(-10, 40), 2),
            "humedad": round(random.uniform(0, 100), 2),
            "presion_atmosferica": round(random.uniform(900, 1100), 2),
            "vibraciones": round(random.uniform(0, 5), 2)
        }
    }
    return data

# Conectar con Elasticsearch (asegúrate de que Elasticsearch está en funcionamiento)
es = Elasticsearch(['http://localhost:9200'])

# Crear el índice molinos si no existe
index_name_molinos = "molinos"
mapping_molinos = {
    "mappings": {
        "properties": {
            "timestamp": {"type": "date"},
            "id": {"type": "keyword"},
            "model": {"type": "text"},
            "location": {"type": "geo_point"},
            "value": {
                "properties": {
                    "velocidad_viento": {"type": "float"},
                    "direccion_viento": {"type": "float"},
                    "produccion_energia": {"type": "float"},
                    "temperatura_ambiente": {"type": "float"},
                    "humedad": {"type": "float"},
                    "presion_atmosferica": {"type": "float"},
                    "vibraciones": {"type": "float"}
                }
            }
        }
    }
}

# Eliminar el índice si ya existe
if es.indices.exists(index=index_name_molinos):
    es.indices.delete(index=index_name_molinos)

espera = 10

def generate_and_write_data():
    global espera
    t = threading.Timer(espera, generate_and_write_data)
    t.start()
    for i in range(len(info_modelos)):
        # Generar datos para un molino de viento
        molino_data = generate_windmill_data(i)
        # Asignar un ID único al documento del molino
        molino_doc_id = str(uuid.uuid4())

        # Indexar los datos del molino
        es.index(index=index_name_molinos, id=molino_doc_id, body=molino_data)

    print("Datos del molino de viento enviados a Elasticsearch")

# Iniciar la generación y escritura de datos
generate_and_write_data()
