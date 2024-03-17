import requests
import json


api = 'https://api.sympla.com.br'

def listarEventos():
  eventos = requests.get(f'{api}/public/v4/events', headers={'s_token': '1e01ff3882e76eb5af0bc76e37a40c7f6490fe6eb2c79938996e7edfcb21a39a'})
  if eventos.status_code == 200:
    eventosDic = eventos.json()
    return eventosDic
  elif eventos.status_code == 400:
    return 'Token de conta não encontrado'
  elif eventos.status_code == 401:
    return 'Não há eventos'

def listarEventosPorId(event_id):
  eventos = requests.get(f'{api}/public/v4/events/{event_id}', headers={'s_token': '1e01ff3882e76eb5af0bc76e37a40c7f6490fe6eb2c79938996e7edfcb21a39a'})
  if eventos.status_code == 200:
    eventosDic = eventos.json()
    return eventosDic
  elif eventos.status_code == 400:
    return 'Token de conta não encontrado'
  elif eventos.status_code == 401:
    return 'Evento não encontrado'

# def listarEventosPorData(date):
#   date = date.strftime("%Y/%m/%d")
#   eventos = requests.get(f'{api}/public/v4/events/from/{date}/',  headers={'s_token': '1e01ff3882e76eb5af0bc76e37a40c7f6490fe6eb2c79938996e7edfcb21a39a'})
#   eventosDic = eventos.json()
#   return eventosDic
