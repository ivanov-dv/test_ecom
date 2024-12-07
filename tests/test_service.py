import pytest

from utils.service import check_fields


@pytest.mark.parametrize(
    'input_data, expected',
    (
        (
            {'field1': 'username@mail.com', 'field2': 'password'},
            {'field1': 'email', 'field2': 'text'}
        ),
        (
            {'field1': '+79345678901', 'field2': '31.12.2024'},
            {'field1': 'phone', 'field2': 'date'}
        ),
        (
                {'field1': '+7 934 567 89 01', 'field2': '2024-12-31'},
                {'field1': 'phone', 'field2': 'date'}
        ),
    )
)
def test_check_fields(input_data, expected):
    assert check_fields(input_data) == expected