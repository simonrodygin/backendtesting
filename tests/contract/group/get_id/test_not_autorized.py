from services.university.models.group.get_group_fail import GetGroupFail

def test_not_autorized(uni_service_wrong_creds):
    response = uni_service_wrong_creds.group_helper.get_group(1)
    response_data = response.json()
    response_model_obj = GetGroupFail.model_validate(response_data)
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    assert response_model_obj.detail == "Invalid JWT token", f"Expected 'Invalid JWT token', got {response_model_obj.detail}"