# ─── Build Stage ─────────────────────────────────────
FROM python:3.11-slim

# Metadata
LABEL maintainer="NeoJardin Team"
LABEL description="NeoJardín - Salón de Eventos Web App"

# Working directory
WORKDIR /app

# Prevent Python from writing .pyc files / enable stdout flush
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create volume mount point for the SQLite database
RUN mkdir -p /app/instance

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
