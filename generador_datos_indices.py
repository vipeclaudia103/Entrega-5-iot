import uuid
import random
import threading
from elasticsearch import Elasticsearch
from datetime import datetime, timezone

# Definir modelos y ubicaciones constantes para cada molino
info_modelos = [
    {
        "modelo": "G58",
        "ubicacion": "Biota Zona Norte"
    },    
    {
        "modelo": "SG 14-222 DD",
        "ubicacion": "Biota Zona Suroeste"
    },
    {
        "modelo": "V164-9.5 MW",
        "ubicacion": "Biota Zona Oeste"
    },    
    {
        "modelo": "EP3",
        "ubicacion": "Biota Zona Sur"
    },
    {
        "modelo": "V164-9.5 MW",
        "ubicacion": "Biota Zona Este"
    },        
    {
        "modelo": "N149",
        "ubicacion": "Biota Zona Norte"
    },    
    {
        "modelo": "SG 14-222 DD",
        "ubicacion": "Biota Zona Sur"
    },
    {
        "modelo": "N149",
        "ubicacion": "Biota Zona Oeste"
    },    
    {
        "modelo": "EP3",
        "ubicacion": "Biota Zona Central"
    },
    {
        "modelo": "G58",
        "ubicacion": "Biota Zona Este"
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
        "location": info_modelos[id]["ubicacion"],
        "timestamp":datetime.now(timezone.utc),
        "value": {
            "velocidad_viento": round(random.uniform(0, 25), 2),
            "direccion_viento": round(random.uniform(0, 360), 2),
            "produccion_energia": round(random.uniform(0, 1000), 2),
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
            "location": {"type": "text"},
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

if not es.indices.exists(index=index_name_molinos):
    es.indices.create(index=index_name_molinos, body=mapping_molinos)

espera = 5

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
