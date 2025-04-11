from test_frame.services.university.models.group.get_group_fail import GetGroupFail
from test_frame.services.university.models.group.get_group_success import GetGroupSuccess
import pytest

class TestContractgetByID:
    def access_denied(self, uni_service_anon):
        response = uni_service_anon.group_helper.get_group(1)
        response_data = response.json()
        response_model_obj = GetGroupFail.model_validate(response_data)
        return response, response_model_obj
    
    @pytest.mark.access_denied
    def test_access_denied_status_code(self, uni_readiness_check, uni_service_anon):
        response, _ = self.access_denied(uni_service_anon)
        assert response.status_code == 403, f"Expected status code 403, got {response.status_code}"
    
    @pytest.mark.access_denied
    def test_access_denied_response(self, uni_service_anon):
        _, response_model_obj = self.access_denied(uni_service_anon)
        assert response_model_obj.detail == "Access denied", f"Expected 'Access denied', got {response_model_obj.detail}"

    def not_autorized(self, uni_service_wrong_creds):
        response = uni_service_wrong_creds.group_helper.get_group(1)
        response_data = response.json()
        response_model_obj = GetGroupFail.model_validate(response_data)
        return response, response_model_obj
    
    @pytest.mark.not_autorized
    def test_not_autorized_status_code(self, uni_service_wrong_creds):
        response, _ = self.not_autorized(uni_service_wrong_creds)
        assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    
    @pytest.mark.not_autorized
    def test_not_autorized_response(self, uni_service_wrong_creds):
        _, response_model_obj = self.not_autorized(uni_service_wrong_creds)
        assert response_model_obj.detail == "Invalid JWT token", f"Expected 'Invalid JWT token', got {response_model_obj.detail}"
    
    def not_found(self, uni_service):
        response = uni_service.group_helper.get_group(1)
        response_data = response.json()
        response_model_obj = GetGroupFail.model_validate(response_data)
        return response, response_model_obj

    @pytest.mark.not_found
    def test_not_found_status_code(self, uni_service):
        response, _ = self.not_found(uni_service)
        assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

    @pytest.mark.not_found
    def test_not_found_response(self, uni_service):
        _, response_model_obj = self.not_found(uni_service)
        assert response_model_obj.detail == "Group not found", f"Expected 'Group not found', got {response_model_obj.detail}"
    
    def search_success(self, uni_service):
        group = uni_service.make_random_group()
        
        response = uni_service.group_helper.get_group(group.id)
        response_data = response.json()
        response_model_obj = GetGroupSuccess.model_validate(response_data)
        return response, response_model_obj, group

    @pytest.mark.search_success
    def test_search_success_status_code(self, uni_service, clean_group_uni): 
        response, _, _ = self.search_success(uni_service)   
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    @pytest.mark.search_success    
    def test_search_success_response_id(self, uni_service, clean_group_uni):   
        _, response_model_obj, group = self.search_success(uni_service)
        assert response_model_obj.id == group.id, f"Expected group ID {group.id}, to be equal {response_model_obj.id}"
    
    @pytest.mark.search_success    
    def test_search_success_response_name(self, uni_service, clean_group_uni):   
        _, response_model_obj, group = self.search_success(uni_service)
        assert response_model_obj.name == group.name, f"Expected group name '{group.name}', to be equal '{response_model_obj.name}'"