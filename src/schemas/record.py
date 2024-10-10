from datetime import datetime
from typing import Optional

from schemas.abstract import Schema


class Record(Schema):

    id: Optional[int] = None
    category_id: int
    amount: float
    creation_date: Optional[datetime] = None
    update_date: Optional[datetime] = None
    comment: Optional[str] = None