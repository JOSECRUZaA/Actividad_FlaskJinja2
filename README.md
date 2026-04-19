# Proyecto Final - Empresa de Servicios (Carnet Terminado en 6)

Este proyecto es una aplicación web desarrollada con **Flask** y **Jinja2** que simula la página de una empresa de servicios ("TechServe"). Cumple con los requerimientos de la práctica para estudiantes cuyo número de carnet termina en el rango 4-6 (Empresa de servicios con formulario de contacto).

## Tecnologías Utilizadas

- **Backend:** Python con el microframework Flask
- **Plantillas:** Jinja2
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Framework CSS:** Bootstrap 5 (Iconos de Bootstrap incluidos)
- **Servidor WSGI:** Gunicorn (para despliegue en Render)

## Estructura del Proyecto

```text
/
├── app.py                  # Archivo principal de la aplicación Flask
├── requirements.txt        # Dependencias del proyecto (Flask, gunicorn, etc)
├── static/
│   ├── css/
│   │   └── style.css       # Estilos personalizados
│   └── js/
│       └── script.js       # Scripts personalizados (Validación y animaciones)
└── templates/
    ├── base.html           # Plantilla base con navbar y footer (Jinja2)
    ├── index.html          # Página principal con listado de servicios
    └── contact.html        # Página de contacto con formulario
```

## Requisitos Previos

- Python 3.8+
- pip (Gestor de paquetes de Python)

## Instalación y Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd PRACTICAJINJAFLASK
   ```

2. Crear y activar un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

5. Abrir el navegador y acceder a: `http://127.0.0.1:5000/`

## Despliegue en Render

Este proyecto está configurado para ser desplegado fácilmente en [Render](https://render.com/). Asegúrate de conectar tu repositorio de GitHub y utilizar el comando de inicio de Gunicorn:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
