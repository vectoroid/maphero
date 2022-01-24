"""
Spots Router
"""
import fastapi
import ..api.db
import ..api.config


router = fastapi.APIRouter(prefix='/spots', tags=["Spots"])

@router.get('/')
async def fetch_all() -> list:
    