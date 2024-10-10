from datetime import datetime
from typing import Optional

from schemas.abstract import Schema


class User(Schema):

    id: int
    name: str
    creation_date: Optional[datetime] = None
    update_date: Optional[datetime] = None