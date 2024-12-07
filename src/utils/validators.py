import re
from datetime import datetime, date

from constants import (
    DATE_PATTERNS,
    PHONE_NUMBER_REGEX,
    EMAIL_REGEX
)


def validate_date(
        input_date: str,
        patterns: list | tuple = DATE_PATTERNS
) -> date | None:
    """
    Валидация даты в соответствии с шаблоном.

    :param input_date: Строка с данными.
    :param patterns: Список или кортеж с паттернами даты.

    :return: Дата в формате date или None, если дата не соответствует шаблону.
    """
    if not isinstance(input_date, str):
        return None
    for pattern in patterns:
        try:
            return datetime.strptime(input_date, pattern).date()
        except ValueError:
            continue
    return None


def validate_phone_number(
        phone_number: str,
        regex: str = PHONE_NUMBER_REGEX
) -> str | None:
    """
    Валидация номера телефона в формате "+7 XXX XXX XX XX".

    :param phone_number: Строка с данными.
    :param regex: Регулярное выражения для валидации номера телефона.

    :return: Номер телефона без пробелов и знака "+"
    или None, если номер не соответствует шаблону.
    """
    if not isinstance(phone_number, str):
        return None
    if re.compile(regex).match(phone_number):
        return phone_number.replace(' ', '')[1:]
    return None


def validate_email(
        email: str,
        regex: str = EMAIL_REGEX
) -> str | None:
    """
    Валидация email.

    :param email: Строка с данными.
    :param regex: Регулярное выражение для валидации email.

    :return: Email или None, если email не соответствует шаблону.
    """
    if not isinstance(email, str):
        return None
    return email if re.compile(regex).match(email) else None
