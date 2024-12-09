import enum
from dataclasses import dataclass
import uuid
import datetime




@dataclass
class Todo:
    """
    Encapsulates the properties of a to-do item.
    Provides a structured way to manage
    and access these properties

    Fields:
    id: int -- the unique identifier of the to-do item
    title: str -- the title of the to-do item
    description: str -- the description of the to-do item
    done: bool -- the status of the to-do item
    user_id: uuid.UUID -- the unique identifier of the user

    """
    id: uuid.UUID
    title: str
    description: str
    user_id: uuid.UUID
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime