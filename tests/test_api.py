async def test_get_forms(client, collection, forms, valid_form_data):
    for form_data, expected in valid_form_data:
        response = await client.post(
            '/get_form',
            json=form_data
        )
        assert 'form_name' in response.json()
        assert response.json()['form_name'] == expected


async def test_get_forms_invalid(client, collection, forms, invalid_form_data):
    for form_data, expected in invalid_form_data:
        response = await client.post(
            '/get_form',
            json=form_data
        )
        assert response.json() == expected
