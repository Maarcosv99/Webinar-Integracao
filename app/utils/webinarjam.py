import requests
from ..schemas import webinarjam as schemas

API_KEY = '92f3cb80-1866-4ef0-b690-442db682f307'
WEBINAR_ID = 4
TIMEZONE = 'GMT-3'

def getSchedules():
    r = requests.post(
        'https://api.webinarjam.com/everwebinar/webinar',
        data={
            'api_key': API_KEY,
            'webinar_id': WEBINAR_ID,
            'timezone': TIMEZONE
        }
    )

    response = r.json()
    schedules = response['webinar']['schedules']
    
    response = []
    for schedule in schedules:
        response.append({
            'date': schedule['date'],
            'id': schedule['schedule'],
            'comment': schedule['comment']
        })
    
    return response

def register(user: schemas.UserRegister):
    r = requests.post(
        'https://api.webinarjam.com/everwebinar/register',
        data={
            'api_key': API_KEY,
            'webinar_id': WEBINAR_ID,
            'first_name': user.first_name,
            'email': user.email,
            'schedule': user.schedule,
            'phone_country_code': user.phone_country_code,
            'phone': user.phone,
        }
    )
    if r.status_code == 200:
        return user
    else:
        return 'error'