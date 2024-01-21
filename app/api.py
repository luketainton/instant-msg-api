from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader

from app.webex import WebexMsg, send_msg


API_KEYS = [
    "my_api_key"
]


webapp = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key")

def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=401,
        detail="Invalid or missing API Key",
    )

@webapp.get("/")
async def root():
    return {"detail": "App is alive."}

@webapp.post("/webex")
async def message_via_webex(msg: WebexMsg, api_key: str = Security(get_api_key)):
    if msg.toPersonEmail and msg.toRoomId:
        raise HTTPException(
            status_code=422,
            detail="Cannot provide both toPersonEmail and toRoomId."
        )
    return send_msg(msg)
