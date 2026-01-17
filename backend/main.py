from fastapi import FastAPI, status
from backend.App.routers import match

app = FastAPI()
app.include_router(match.router)

@app.get('/', tags=['test'], status_code=status.HTTP_200_OK)
def index():
    return {'message':'Hello World'}
