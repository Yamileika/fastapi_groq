## 0. Actualizar la lista de versiones de las librerias del sistema operativo

Actualiza las lista de versionees de librerias del sistema operativo

```bash
sudo apt update
```

## 1. Instalar neofetch

Instalar neofetch para conocer las caracteristicas del sistema operativo que se esta utilizando.

```bash
    sudo apt install neofetch -y
    neofetch
    uname -a
```

## 2. Ejecutar neofetch

```bash
    neofetch
```

Alternativa para ver las caracteristicas del SO

```bash
    uname -a
```

## 3. Crear archivo os.txt

Para conocer la version del SO

```bash
neofetch > os.txt
```

## 4. Crear un espacio virtual

```bash
    virtualenv venv
```

## 5. Inicializar el ambiente virtual

```bash
source venv/bin/activate
```

## 6. Salir del ambiente virtual

```bash
deactivate
```

## 7. Crear el archivo .gitignore
```bash
*.pyc
_pycache_/
venv/
```

## 8. Instalar librerias necesarias

Para este proyecto se usaran las librerias de [FastAPI](https://fastapi.tiangolo.com/#requirements)

```bash
pip install "fastapi[standard]"
pip install groq
```

## 9. Crear el archivo requirements.txt

Se agregara el archivo requirements para listar las librerias necesarias para el proyecto y sus versiones.

```bash
pip freeze > requiremets.txt
```

## 10. Crear el archivo runtime

```bash
python3 -V > runtime
```
## 11. API_KEY de GROQ
```bash
export GROQ_API_KEY="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"
```

## 12. Ejecutar el servidor
```bash
fastapi dev main.py
```

## 13. Indexar los archivos creados con git

```bash
git add .
git commit -m "UPDATED"
git push -u origin main
```


