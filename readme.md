# API Copa América

## Descripción
Esta API, desarrollada con Flask, permite consultar información sobre partidos, estadios, selecciones y otros datos relacionados con la Copa América 2024 celebrada en los Estados unidos.
Proporciona endpoints RESTful para acceder a la información de manera estructurada y eficiente.

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/tuusuario/flask-football-api.git](https://github.com/jeremiasolivera/api-copa-america-v1
   cd api-copa-america
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```sh
   flask run
   ```

## Endpoints

### Selecciones
- `GET /selecciones` → Retorna todas las selecciones.
- `GET /selecciones/{id}` → Retorna los detalles de una selección específica.

### Estadios
- `GET /estadios` → Retorna todos los estadios.
- `GET /estadios/{id}` → Retorna los detalles de un estadio específico.

### Partidos
- `GET /partidos` → Retorna todos los partidos.
- `GET /partidos/{id}` → Retorna los detalles de un partido específico.

## Configuración
Puedes modificar la configuración en el archivo `config.py` para cambiar parámetros como la base de datos o el puerto del servidor.

## Tecnologías utilizadas
- Flask
- Flask-RESTful
- SQLAlchemy 
- Marshmallow 

## Contribución
Si deseas contribuir, puedes hacer un fork del repositorio y abrir un pull request con tus mejoras.


