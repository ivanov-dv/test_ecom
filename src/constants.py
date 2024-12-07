TYPE_FIELD_DATE = 'date'
TYPE_FIELD_PHONE = 'phone'
TYPE_FIELD_EMAIL = 'email'
TYPE_FIELD_TEXT = 'text'
TYPE_FIELD_UNKNOWN = 'unknown'

DATE_PATTERNS = (
    '%Y-%m-%d',
    '%d.%m.%Y'
)

PHONE_NUMBER_REGEX = r'(\+7)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}'
EMAIL_REGEX = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,5})$'