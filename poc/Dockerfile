# Utilizar la imagen oficial de Python como imagen base
FROM python:3.11-slim

# Establecer variables de entorno para evitar el almacenamiento en b�fer
ENV PYTHONUNBUFFERED 1

# Crear y establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos y instalar las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos del proyecto Django al contenedor
COPY . /app/

# Iniciar el servidor de desarrollo
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:5000"]
