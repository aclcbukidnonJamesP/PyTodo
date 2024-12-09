import uuid
from dataclasses import dataclass


@dataclass
class User:
    """
    Represents a user with unique identification and personal information.

    Fields:
        id (uuid.UUID): Unique identifier for the user.
        last_name (str): The user's last name.
        first_name (str): The user's first name.
        password (str): The user's password.
        email (str): The user's email address.
    """

    id: uuid.UUID
    last_name: str
    first_name: str
    password: str
    email: str





