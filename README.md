# Entrega-5-iot
Claudia Viñals Perlado

# Explicación de los pasos seguidos

1. **Crear Docker Compose con Elasticsearch y Kibana:**

   Creé un archivo llamado `docker-compose.yml`, en este archivo Docker Compose define dos servicios: Elasticsearch y Kibana. Elasticsearch está configurado para ejecutarse en un nodo único (`discovery.type=single-node`) y se expone en el puerto 9200. Kibana se expone en el puerto 5601 y depende de Elasticsearch.

2. **Generar Datos y Enviarlos a Elasticsearch:**

   Utilicé mi script Python existente (`generador_datos_indices.py`) para generar datos simulados y enviarlos a Elasticsearch. Me aseguré de que el script esté configurado para conectarse a `http://localhost:9200` donde se ejecutará Elasticsearch.

3. **Crear Dashboard en Kibana para los Datos de los Molinos:**

   Después de enviar los datos, abrí mi navegador y visité http://localhost:5601 para acceder a Kibana. Una vez en Kibana, seguí estos pasos para crear un dashboard:

   - Fui a la pestaña "Dashboard" en el menú lateral.
   - Hice clic en el botón "Create dashboard".
   - En el nuevo dashboard, hice clic en "Add" para agregar visualizaciones.
   - Seleccioné el tipo de visualización que deseaba utilizar (por ejemplo, gráfico de líneas, histograma, mapa, etc.).
   - Configuré los datos para mi visualización seleccionando el índice de Elasticsearch y definiendo los campos que deseaba visualizar.
   - Repetí estos pasos para cada visualización que deseaba agregar a mi dashboard.

4. **Elegir Gráficas para Representar los Datos:**

   En cada visualización que agregué a mi dashboard, elegí los tipos de gráficos que mejor representaban mis datos. Por ejemplo, para datos de producción de energía de molinos de viento, utilicé gráficos de líneas para mostrar tendencias de producción a lo largo del tiempo, o un mapa para mostrar la distribución geográfica de los molinos y su producción de energía.



# Instrucciones de uso
Para levantar el entorno de Elasticsearch y Kibana utilizando Docker Compose, ejecutar el script Python y visualizar los datos en Kibana:

1. **Levantar el Docker Compose de Elasticsearch y Kibana:**
   
   ```bash
   docker-compose up -d
   ```

   Este comando levantará los contenedores de Elasticsearch y Kibana en segundo plano, según la configuración definida en el archivo `docker-compose.yml`.

2. **Ejecutar el script Python:**
   
   Una vez que Elasticsearch y Kibana estén en funcionamiento, ejecuta tu script Python para generar y enviar datos a Elasticsearch:

   ```bash
   /bin/python3 /home/cvp/Entrega-5-iot/generador_datos_indices.py
   ```

   Esto iniciará la generación y escritura de datos simulados en Elasticsearch.

3. **Abrir Kibana en el navegador:**
   
   Abre tu navegador web y navega a la dirección http://localhost:5601/. Esto te llevará al tablero de control de Kibana.

4. **Ir a Dashboards y visualizar los datos:**
   
   Una vez en Kibana, ve a la sección de "Dashboards" en el menú lateral. Si has configurado tus visualizaciones y tableros correctamente, deberías poder ver y explorar tus datos generados en Elasticsearch a través de los tableros creados.

# Posibles vías de mejora
- **Escalabilidad y Alta Disponibilidad**: En lugar de tener solo un nodo de Elasticsearch y un nodo de Kibana, considera implementar una arquitectura escalable y altamente disponible. Puedes configurar un clúster de Elasticsearch con múltiples nodos para distribuir la carga y garantizar la disponibilidad de los datos. También podrías configurar un balanceador de carga para distribuir las solicitudes entre los nodos de Elasticsearch.
- **Seguridad**: Agrega capas de seguridad a tu plataforma. Configura autenticación y autorización en Elasticsearch y Kibana para proteger los datos y limitar el acceso a usuarios autorizados. También puedes considerar el uso de SSL/TLS para cifrar la comunicación entre los clientes y los nodos de Elasticsearch.
# Problemas / Retos encontrados
- Desconexión de WSL:experimento desconexiones repentinas de mi entorno Linux dentro de Windows, lo que interrumpe mi trabajo en curso. Esto puede ocurrir debido a actualizaciones de Windows, recursos insuficientes del sistema o configuraciones de red problemáticas.

- Error 137 de Docker:Problema: El error 137 de Docker es un error común que ocurre cuando un contenedor Docker se detiene debido a una señal SIGKILL, que generalmente indica que el contenedor se quedó sin memoria
# Alternativas posibles
Apache Solr y Apache Superset: 
- Apache Solr es una plataforma de búsqueda y análisis de código abierto que ofrece capacidades similares a Elasticsearch.
- Apache Superset es una herramienta de visualización de datos de código abierto que te permite crear paneles interactivos y gráficos.
