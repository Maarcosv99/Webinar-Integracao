from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator

class Settings(BaseSettings):
    API_URL_STR = '/api/v1'
    API_URL = 'http://localhost:8000/'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:8000",
        "http://api.klow.com.br",
        "https://api.klow.com.br",
    ]
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

settings = Settings()