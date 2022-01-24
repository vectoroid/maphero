"""
Spots Router
"""
import fastapi
from api import db
from api import config


router = fastapi.APIRouter(prefix='/spots', tags=["Spots"])

@router.get('/')
async def fetch_all() -> list:
    