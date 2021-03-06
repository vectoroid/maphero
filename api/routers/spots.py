"""
Spots Router
"""
import fastapi
from api import db
from api import config


db = db.async_detabase()
router = fastapi.APIRouter(prefix='/spots', tags=["Spots"])

@router.get('/')
async def fetch_all() -> list:
    result = db.fetch()
    return result.items