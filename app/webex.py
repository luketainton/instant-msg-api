import os

from typing import Optional

from pydantic import BaseModel
from webexteamssdk import WebexTeamsAPI

_api_key: str = os.environ.get("WEBEX_API_TOKEN", "test_api_key")
_api = WebexTeamsAPI(access_token=_api_key)


class WebexMsg(BaseModel):
    toPersonEmail: Optional[str]
    toRoomId: Optional[str]
    text: Optional[str]
    markdown: Optional[str]


def send_msg(msg: WebexMsg) -> dict:
    result = _api.messages.create(
        roomId=msg.toRoomId,
        toPersonEmail=msg.toPersonEmail,
        text=msg.text,
        markdown=msg.markdown
    )
    return result.to_dict()
