from fastapi import APIRouter, status, HTTPException
from ..utils import webinarjam as utils
from ..schemas import webinarjam as schemas
import requests

router = APIRouter(
    prefix='/webinarjam',
    tags=['Webinarjam']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=schemas.ListSchedulesWebinar)
def listSchedulesWebinar():
    """
    Lista de Horários disponíveis para agendamento, do webinar.
    """
    return {'schedules': utils.getSchedules()}

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserShow)
def registerUserInWebinar(user: schemas.UserRegister):
    """
    Registra usuário no webinar
    """
    register = utils.register(user)
    
    if not 'error' in register:
        return register
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Erro ao registrar usuário no webinar.'
        )