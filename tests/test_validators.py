from datetime import date

import pytest

from utils.validators import (
    validate_date,
    validate_phone_number,
    validate_email
)


class TestValidators:

    @pytest.mark.parametrize(
        'input_date',
        ('2022-01-01', '2024-1-1', '31.12.2024', '1.1.2020')
    )
    def test_validate_date(self, input_date):
        assert isinstance(validate_date(input_date), date)

    @pytest.mark.parametrize(
        'input_date',
        (
            '2022-13-01',
            '024-1-1',
            '32.12.2024',
            '1.0.2020',
            '13.1',
            '1.2024',
            '22-01-32',
            '1',
            '',
            'qwerty'
        )
    )
    def test_validate_date_invalid(self, input_date):
        assert validate_date(input_date) is None

    @pytest.mark.parametrize(
        'input_phone, expected',
        (
            ('+79345678901', '79345678901'),
            ('+7 935 567 8901', '79355678901')
        )
    )
    def test_validate_phone_number(self, input_phone, expected):
        assert validate_phone_number(input_phone) == expected

    @pytest.mark.parametrize(
        'input_phone',
        (
            '7934567890',
            '7-934-567-89-01',
            ''
            'qwerty'
        )
    )
    def test_validate_phone_number_invalid(self, input_phone):
        assert validate_phone_number(input_phone) is None

    @pytest.mark.parametrize(
        'input_email',
        (
            'test@example.com',
            'test@example.ru'
        )
    )
    def test_validate_email(self, input_email):
        assert validate_email(input_email) == input_email

    @pytest.mark.parametrize(
        'input_email',
        (
            'test@example',
            'test@.com',
            'test@_.com',
            '.@qwe.com',
            'test@example.',
            'test@.com@example',
            ''
            'qwerty'
        )
    )
    def test_validate_email_invalid(self, input_email):
        assert validate_email(input_email) is None
