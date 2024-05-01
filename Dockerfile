FROM python:3.8

# Installieren der notwendigen Systembibliotheken
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libpng-dev \
    libjpeg-dev \
    libtiff5-dev \
    libopencv-dev \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Den Rest des aktuellen Verzeichnisses in das Arbeitsverzeichnis des Containers kopieren
COPY . /app/

# Port freigeben
EXPOSE 5000

# App starten
CMD ["python", "app.py"]
