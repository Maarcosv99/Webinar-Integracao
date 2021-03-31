from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect as WSD
from typing import List

app = FastAPI(title='pitchPro')

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/')
def teleprompter_page(request: Request):
    return templates.TemplateResponse('teleprompter.html', {'request': request})

@app.get('/slide')
def slide_page(request: Request):
    return templates.TemplateResponse('slide.html', {'request': request})

@app.get('/control')
def control(request: Request):
    return templates.TemplateResponse('control.html', {'request': request})

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    async def disconnect(self, websocket: WebSocket):
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