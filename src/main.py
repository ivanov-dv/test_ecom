from fastapi import FastAPI, HTTPException

from utils.service import check_fields
from utils.db import collection

app = FastAPI()


@app.post('/get_form')
async def get_form(data: dict[str, str]):
    """
    Получение имени формы по переданным данным, если такая форма существует,
    иначе возвращает типы полей в форме.
    """
    valid_data = check_fields(data)
    if not valid_data:
        raise HTTPException(
            status_code=400,
            detail='Invalid data'
        )
    try:
        cursor = collection.find(valid_data)
        forms = await cursor.to_list(length=None)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
    if forms and 'form_name' in forms[0]:
        return {'form_name': forms[0]['form_name']}
    return valid_data
