from services.university.models.get_group_fail import GetGroupFail

def test_not_found_group(uni_service):
    response = uni_service.group_helper.get_group(1)
    response_data = response.json()
    response_model_obj = GetGroupFail.model_validate(response_data)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    assert response_model_obj.detail == "Group not found", f"Expected 'Group not found', got {response_model_obj.detail}"