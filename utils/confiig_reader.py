import json

class ConfigReader:
    default_path = "assets/config.json"

    def __init__(self, config_file_path = default_path):    
        with open(config_file_path, "r") as f:
            data = json.load(f)
        
        self.config = data

    def get_by_full_path(self, path: list[str]):     
        ''' 
        Get config by specified path
        
        Parameters: path (list[str]) - path to the file. Where the first elements of the list are closer to the root
        
        Returns: value by the specified key 
        
        '''
        
        data = self.config
        for adress in path:
            data = data[adress]

        return data
    
    def get_constant(self, relative_path: list[str] | str):
        ''' 
        Get config by specified path
        
        Parameters: path - path to the file. Where the first elements of the list are closer to the root
        
        Returns: value by the specified key 
        
        '''
        
        if isinstance(relative_path, str):
            data = self.config["constants"]
            return data[relative_path]
        else:
            data = self.config["constants"]
            for adress in relative_path:
                data = data[adress]

            return data