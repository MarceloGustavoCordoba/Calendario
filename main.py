from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from pydav import create_dav_app

app = FastAPI()

# Directorio para almacenar los archivos del servidor WebDAV
webdav_dir = "calendar"

# Crea una aplicación WebDAV usando pydav
dav_app = create_dav_app(webdav_dir)

# Monta la aplicación WebDAV en FastAPI
app.mount("/webdav", app=dav_app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
