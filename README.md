# NeoJardín — Salón de Eventos 🌿✦

Aplicación web para la gestión de un salón de eventos de lujo, construida con **Flask** y **SQLite**, desplegada en **Docker**.

---

## 🏛 Tecnologías

| Capa | Tecnología |
|------|------------|
| Backend | Flask 3 + SQLAlchemy |
| Base de datos | SQLite (persistida en Docker Volume) |
| Frontend | HTML5 + CSS3 + JavaScript (Vanilla) |
| Contenedor | Docker + Docker Compose |

---

## 🗄 Base de Datos

| Tabla | Descripción |
|-------|-------------|
| `salones` | Espacios del salón (nombre, capacidad, descripción, disponible) |
| `eventos` | Tipos de evento (nombre, descripción, capacidad, precio) |
| `reservas` | Reservas de clientes (cliente, contacto, fecha, salón, evento, notas) |

---

## 🚀 Ejecutar con Docker

### Opción 1: Docker Compose (recomendado)

```bash
# Construir y levantar el contenedor
docker compose up --build -d

# Ver logs
docker compose logs -f

# Detener
docker compose down
```

### Opción 2: Docker manual

```bash
# Construir la imagen
docker build -t neojardin-app .

# Crear volumen para la base de datos
docker volume create neojardin_database

# Ejecutar el contenedor
docker run -d \
  --name neojardin_app \
  -p 5000:5000 \
  -v neojardin_database:/app/instance \
  neojardin-app
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 🌐 Páginas

| Ruta | Descripción |
|------|-------------|
| `/` | Inicio — Hero, estadísticas, vista general |
| `/salones` | Listado de salones con edición |
| `/eventos` | Catálogo de eventos disponibles |
| `/reservas` | Historial de reservas |
| `/reservas/nueva` | Formulario de nueva reserva |
| `/api/stats` | Endpoint JSON con estadísticas |

---

## 📂 Estructura del Proyecto

```
WebDockerSalon/
├── app/
│   ├── __init__.py       # App factory + seed data
│   ├── models.py         # Modelos SQLAlchemy
│   ├── routes.py         # Rutas Flask
│   ├── templates/        # Plantillas Jinja2
│   └── static/
│       ├── css/style.css
│       └── js/main.js
├── app.py                # Entry point
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 📤 Subir a GitHub

```bash
cd WebDockerSalon
git add .
git commit -m "feat: NeoJardín salon de eventos - Flask + Docker"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/WebDockerSalon.git
git push -u origin main
```