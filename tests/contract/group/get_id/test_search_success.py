from services.university.models.group.get_group_success import GetGroupSuccess

def test_search_success(uni_service, clean_uni):
    group = uni_service.make_random_group()
    
    response = uni_service.group_helper.get_group(group.id)
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    response_data = response.json()
    response_model_obj = GetGroupSuccess.model_validate(response_data)

    assert response_model_obj.id == group.id, f"Expected group ID {group.id}, to be equal {response_model_obj.id}"
    assert response_model_obj.name == group.name, f"Expected group name '{group.name}', to be equal '{response_model_obj.name}'"