from datetime import datetime

from pydantic import BaseModel


class AuditableBaseModel(BaseModel):
    creation_date: datetime = datetime.now()
