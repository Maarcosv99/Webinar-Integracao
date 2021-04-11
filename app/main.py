from fastapi import FastAPI, APIRouter, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketDisconnect as WSD
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .config import settings
from .routers_tag import tags_metadata

# Rotas
from .routers import webinarjam

app = FastAPI(
    title='Klow',
    description='API da Klow para Funil de Marketing',
    version='0.1.0',
    openapi_tags=tags_metadata
)

# Templates

# Rotas
api_router = APIRouter()
api_router.include_router(webinarjam.router)
app.include_router(api_router, prefix=settings.API_URL_STR) #Rota da api

# Middlewares
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Websocket teleprompter
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
    
    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection.send_json(data)

manager = ConnectionManager()

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    while True:
        try:
            # Aguardando comandos do controle
            receive = await websocket.receive_text()
            # Enviando mensagem para toda a sala
            await manager.broadcast({'event': receive})
        except WebSocketDisconnect:
            manager.disconnect(websocket)