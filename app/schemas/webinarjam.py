from typing import List, Optional
from pydantic import BaseModel

class ScheduleWebinar(BaseModel):
    date: str
    id: int
    comment: str

class ListSchedulesWebinar(BaseModel):
    schedules: List[ScheduleWebinar]
    
class UserRegister(BaseModel):
    first_name: str
    email: str
    schedule: int
    phone_country_code: Optional[str] = '+55'
    phone: str

class UserShow(BaseModel):
    message: str