import requests
import json

api = 'https://api.sympla.com.br'

def listarParticipantesPorEvento(event_id):
  participantes = requests.get(f'{api}/public/v3/events/{event_id}/participants', headers={'s_token': ''})
  if participantes.status_code == 200:
    participantesDic = participantes.json()  
    return participantesDic
  elif participantes.status_code == 200:
    return 'Token de conta não encontrado'
  else:
    return 'Evento não encontrado'

def listarParticipantesPorIdDoIngresso(event_id,participant_id):
  participantes = requests.get(f'{api}/public/v3/events/{event_id}/participants/{participant_id}', headers={'s_token': ''})
  if participantes.status_code == 200:
    participantesDic = participantes.json()  
    return participantesDic
  elif participantes.status_code == 400:
    return 'Token de conta não encontrado'
  if participantes.status_code == 401:
    return'Evento não encontrado'
  else:
    return 'Participante inexistente'

def listarParticipantesPorNumeroDoticker(event_id, ticket_number):
  participantes = requests.get(f'{api}/public/v3/events/{event_id}/participants/ticketNumber/{ticket_number}', headers={''})
  if participantes.status_code == 200:
    participantesDic = participantes.json()  
    return participantesDic
  elif participantes.status_code == 400:
    return 'Token de conta não encontrado'
  if participantes.status_code == 401:
    return'Evento não encontrado'
  else:
    return 'Numero do ticket inexistente'
  

