from services.university.models.group.get_group_fail import GetGroupFail
from services.university.models.group.get_group_success import GetGroupSuccess

class TestContractgetByID:
    def test_access_denied(self, uni_service_anon):
        response = uni_service_anon.group_helper.get_group(1)
        response_data = response.json()
        response_model_obj = GetGroupFail.model_validate(response_data)
        assert response.status_code == 403, f"Expected status code 403, got {response.status_code}"
        assert response_model_obj.detail == "Access denied", f"Access denied', got {response_model_obj.detail}"

    def test_not_autorized(self, uni_service_wrong_creds):
        response = uni_service_wrong_creds.group_helper.get_group(1)
        response_data = response.json()
        response_model_obj = GetGroupFail.model_validate(response_data)
        assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
        assert response_model_obj.detail == "Invalid JWT token", f"Expected 'Invalid JWT token', got {response_model_obj.detail}"

    def test_not_found(self, uni_service):
        response = uni_service.group_helper.get_group(1)
        response_data = response.json()
        response_model_obj = GetGroupFail.model_validate(response_data)
        assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
        assert response_model_obj.detail == "Group not found", f"Expected 'Group not found', got {response_model_obj.detail}"
    
    def test_search_success(self, uni_service, clean_group_uni):
        group = uni_service.make_random_group()
        
        response = uni_service.group_helper.get_group(group.id)
        response_data = response.json()
        response_model_obj = GetGroupSuccess.model_validate(response_data)

        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert response_model_obj.id == group.id, f"Expected group ID {group.id}, to be equal {response_model_obj.id}"
        assert response_model_obj.name == group.name, f"Expected group name '{group.name}', to be equal '{response_model_obj.name}'"