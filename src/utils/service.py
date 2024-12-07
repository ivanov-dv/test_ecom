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


CHECK_MAPPING = {
    validate_date: TYPE_FIELD_DATE,
    validate_phone_number: TYPE_FIELD_PHONE,
    validate_email: TYPE_FIELD_EMAIL,
    (lambda x: isinstance(x, str)): TYPE_FIELD_TEXT,
    (lambda x: True): TYPE_FIELD_UNKNOWN
}


def check_fields(input_data: dict) -> dict:
    """
    Идентификация типов полей.

    :param input_data: Словарь с входными данными.

    :return: Словарь (ключи - названия полей, значения - типы полей).
    """
    if not input_data or not isinstance(input_data, dict):
        return {}
    typing_form = {}
    for field_name, field_value in input_data.items():
        for func_validate, field_type in CHECK_MAPPING.items():
            if func_validate(field_value):
                typing_form[field_name] = field_type
                break
    return typing_form