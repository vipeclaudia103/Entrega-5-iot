# Usa una imagen de Python como base
FROM python:3.10.12

# Copia el archivo de requisitos a la imagen de trabajo
COPY requirements.txt /app/requirements.txt

# Establece el directorio de trabajo como /app
WORKDIR /app

# Instala las bibliotecas desde el archivo de requisitos
RUN pip install -r requirements.txt

# Copia el código fuente al directorio de trabajo en la imagen
COPY . /app

# Comando por defecto para ejecutar tu aplicación
CMD ["python", "generador_datos_indices.py"]
