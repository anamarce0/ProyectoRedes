# Usa una imagen base de Python
FROM python:3

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
