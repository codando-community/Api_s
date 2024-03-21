import requests
import json

api = 'https://api.sympla.com.br'
def listarPedidosPorEvento(event_id):  
  pedidos = requests.get(f'{api}/public/v3/events/{event_id}/orders',  headers={'s_token':''})
  if pedidos.status_code == 200: 
    pedidosDic = pedidos.json()
    return pedidosDic
  elif pedidos.status_code == 400:
   return 'token de conta não encontrado'
  else:
    return 'Evento não encontrado'
  

def listarPedidosPorId(event_id, order_id):
  pedidos = requests.get(f'{api}/public/v3/events/{event_id}/orders/{order_id}',  headers={'s_token': ''})
  if pedidos.status_code == 200:
    pedidosDic = pedidos.json()
    return pedidosDic
  elif pedidos.status_code == 400:
    return 'token de conta não encontrado'
  elif pedidos.status_code == 401:
    return 'Evento não encontrado'
  else:
    return 'Numero do pedido não encontrado'

def listarParticipantesPorPedido(event_id,order_id):
  pedidos = requests.get(f'{api}/public/v3/events/{event_id}/orders/{order_id}/participants',  headers={'s_token': ''})
  if pedidos.status_code == 200:
    pedidosDic = pedidos.json()
    return pedidosDic
  elif pedidos.status_code == 400:
    return 'token de conta não encontrado'
  elif pedidos.status_code == 401:
    return 'Evento não encontrado'
  else:
    return 'Numero do pedido não encontrado'