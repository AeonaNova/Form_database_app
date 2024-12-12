import re

from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from datetime import datetime


class Date(BaseModel):
    origin_date: str | None = None

    @field_validator('origin_date', check_fields=True)
    def date_validation(cls, value):

        patterns = ["%Y-%m-%d", "%d.%m.%Y"]
        for pattern in patterns:
            try:
                datetime.strptime(value, pattern)
                return value
            except ValueError:
                pass
        raise ValueError(f"Not correct format date: {value}. Expecting one of: {', '.join(patterns)}")

class Phone(BaseModel):
    origin_phone_number: str | None = None

    @field_validator('origin_phone_number', check_fields=False)
    def check_phone(cls, value):

        validation = re.compile(r'^\+7\d{1}\s?\d{9}$')
        if validation.match(value):
            return value
        else:
            raise ValueError('Phone number should be in +7 xxxx xx xx format')


class Email(BaseModel):
    origin_email: EmailStr | None = None


class Description(BaseModel):
    origin_description: str | None = None


class Form(Phone, Email, Description, Date):
    _name: str | None
    model_config = ConfigDict(extra='allow')
