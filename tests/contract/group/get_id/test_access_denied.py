from services.university.models.group.get_group_fail import GetGroupFail

def test_access_denied(uni_service_anon):
    response = uni_service_anon.group_helper.get_group(1)
    response_data = response.json()
    response_model_obj = GetGroupFail.model_validate(response_data)
    assert response.status_code == 403, f"Expected status code 403, got {response.status_code}"
    assert response_model_obj.detail == "Access denied", f"Access denied', got {response_model_obj.detail}"