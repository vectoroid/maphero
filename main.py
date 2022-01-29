# import deta
import fastapi
from api import config
from routers import spots
# import os

app_title: str = "MapHero"
app_description: str = "A cloud app which lets you save your favorite spots."
app_root_path="/api/v1/"
app = fastapi.FastAPI(title=app_title, description=app_description)
app.state.ApiSettings = config.ApiSettings

@app.get("/")
def read_root():
	return {"data": "hello world"}

@app.get("/ping")
async def respond_to_ping():
	"""
	Ping the server.
	"""
	return 'pong'

