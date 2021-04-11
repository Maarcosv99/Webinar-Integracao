'''
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/teleprompter',
    tags=['Teleprompter']
)

router.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@router.get('/')
def teleprompter_page(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse('teleprompter.html', {'request': request})

@router.get('/slide')
def slide_page(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse('slide.html', {'request': request})

@router.get('/control')
def control(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse('control.html', {'request': request})
'''