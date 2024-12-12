from typing import get_type_hints, Optional

from fastapi import FastAPI
from schema import Form
from database_type_form import get_from_db, SeparateForms, Undefined

app = FastAPI()


@app.get('/')
def get_url(request) -> dict:
    if request:
        response = get_from_db()
        return {'existing_forms': response}


@app.post('/get_form')
def get_form(fields: Form) -> dict:

    response = SeparateForms(fields)
    response.define()
    response.check_in_existed()
    response.write()
    form_output = response.is_unknown()
    return form_output
