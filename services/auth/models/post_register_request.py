from pydantic import BaseModel, ConfigDict, model_validator

class PostRegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    username: str
    password: str
    password_repeat: str
    email: str

    @model_validator(mode='after')
    def validate_repeat_password(self):
        if self.password != self.password_repeat:
            raise ValueError('Passwords do not match')
        return self