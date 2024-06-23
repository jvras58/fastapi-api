import os

from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Caminho base para os diretórios 'static' e 'templates'
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# ----------------------------------
#  APP Mount (jinja2)
# ----------------------------------
# Mapeia a rota "/static" para servir arquivos estáticos (jinja2)
router.mount(
    '/static',
    StaticFiles(directory=os.path.join(base_dir, 'static')),
    name='static',
)
# Configura o diretório de templates para renderização de páginas (jinja2)
templates = Jinja2Templates(directory=os.path.join(base_dir, 'templates'))

# ----------------------------------
#  Routes (jinja2)
# ----------------------------------


@router.get('/index')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/create_user')
async def create_user(request: Request):
    return templates.TemplateResponse('create_user.html', {'request': request})


@router.get('/login')
async def login_user(request: Request):
    return templates.TemplateResponse('login_user.html', {'request': request})


@router.get('/create_product')
async def create_product(request: Request):
    return templates.TemplateResponse('create_product.html', {'request': request})


@router.get('/list_product')
async def list_product(request: Request):
    return templates.TemplateResponse('list_product.html', {'request': request})
