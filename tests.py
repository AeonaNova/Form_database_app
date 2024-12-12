from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"existing_forms": [{"name": "Form_messaging_purpose",
                                                   "fields": ["origin_date", "origin_description", "origin_email",
                                                              "origin_phone_number", "origin_ty"]},
                                                  {"name": "Form_connection_purpose",
                                                   "phone_number": "origin_phone_number",
                                                   "description": "origin_description"},
                                                  {"name": "Form_calling_purpose",
                                                   "phone_number": "origin_phone_number", "date": "origin_date"}]}


def test_main_check():
    test_json = {
        "origin_date": "12.09.2024",
        "origin_description": "string",
        "origin_email": "user@example.com",
        "origin_phone_number": "+79999999999",
        "additionalProp1": {}
    }
    response = client.post("/get_form/", json=test_json)
    assert response.status_code == 200
    assert response.json() == {"form_input_type": "Form_connection_purpose"}


test_health_check()
test_main_check()
