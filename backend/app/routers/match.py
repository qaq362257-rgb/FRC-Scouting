from fastapi import APIRouter, Body, status, HTTPException
from .. import schemas

router = APIRouter()

@router.post('/match', tags=["match"], status_code=status.HTTP_201_CREATED)
def match(data:schemas.MatchData=Body()):
    print(data)
    return {'status':'OK', 'data':data}