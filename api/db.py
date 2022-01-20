"""
MapHero API

Deta Base (NoSQL database) config & connection 
"""
import aiohttp
import contextlib
import deta
from . import api

# Initialize the Deta SDK 
deta = deta.Deta()

@contextlib.asynccontextmanager
async def async_detabase(db_name:str = api.config.ApiSettings.db_name):
    """
    Get asynchronous database connection from Deta.sh
    """
    db_client = deta.AsyncBase(db_name)
    try:
        yield db_client
    except aiohttp.ClientError:
        raise api.exceptions.UnprocessableEntityException("Database error")
    finally:
        await db_client.close()
    
    
