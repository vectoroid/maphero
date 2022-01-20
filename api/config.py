import deta
import functools
import logging
import os
import pydantic

# init logging
log = logging.getLogger(__name__)

class ApiSettings(pydantic.BaseSettings):
    """
    """
    app_name: str = "MapHero: 'bookmarks' for your favorite (geographical) places"
    admin = 'calculuslab'
    deta_project_key: str = os.environ.get('DETA_PROJECT_KEY', '')
    deta_root_url: str = os.environ.get('DETA_ROOT_URL', '')
    db_name = 'spots_db'
    #pagination
    max_records_per_page: int = 10
    
    
@functools.lru_cache
def get_settings() -> ApiSettings:
    log.info("Loading API settings (including env vars) ...")
    return ApiSettings()