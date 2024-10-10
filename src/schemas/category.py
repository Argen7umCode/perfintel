from datetime import datetime
from typing import Optional

from schemas.abstract import Schema


class Category(Schema):

    id: int
    name: str
    user_id: int
    creation_date: Optional[datetime] = None
    update_date: Optional[datetime] = None