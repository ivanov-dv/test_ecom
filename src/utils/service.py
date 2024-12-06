from constants import (
    TYPE_FIELD_DATE,
    TYPE_FIELD_PHONE,
    TYPE_FIELD_EMAIL,
    TYPE_FIELD_TEXT,
    TYPE_FIELD_UNKNOWN
)
from utils.validators import (
    validate_date,
    validate_phone_number,
    validate_email
)


def check_fields(input_data: dict) -> dict:
    """
    Идентификация типов полей.

    :param input_data: Словарь с данными.
    :return: Словарь (ключи - названия полей, значения - типы полей).
    """
    res = {}
    for key, value in input_data.items():
        if validate_date(value):
            res[key] = TYPE_FIELD_DATE
        elif validate_phone_number(value):
            res[key] = TYPE_FIELD_PHONE
        elif validate_email(value):
            res[key] = TYPE_FIELD_EMAIL
        elif isinstance(value, str):
            res[key] = TYPE_FIELD_TEXT
        else:
            res[key] = TYPE_FIELD_UNKNOWN
    return res