from fastapi import FastAPI

from utils.service import check_fields
from utils.db import collection

app = FastAPI()


@app.post('/get_form')
async def get_form(data: dict):
    if valid_data := check_fields(data):
        cursor = collection.find(valid_data)
        forms = await cursor.to_list(length=None)
        if forms and 'form_name' in forms[0]:
            return {'form_name': forms[0]['form_name']}
    return valid_data
