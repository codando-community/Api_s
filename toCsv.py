import eventos as ev
import pedidos as ped
import participante as part
import pandas as pd
from pathlib import Path
from tkinter.filedialog import asksaveasfilename

def eventosParaCsv():
  eventos = ev.listarEventos()
  eventos = eventos['data']
  dic = {'EventoId':[],
        'Evento':[],
        'Data':[]}
  for evento in eventos:
    dic['EventoId'].append(evento['id'])
    dic['Evento'].append(evento['name'])
    dic['Data'].append(evento['start_date'])    
  df = pd.DataFrame.from_dict(dic)
  caminho_do_arquivo = asksaveasfilename(defaultextension=".csv", filetypes=[("Documentos Excel", ".csv"), ("Todos os arquivos", ".*")])
  df.to_csv(caminho_do_arquivo, sep=';', index=False,  encoding="latin1")
  return 'Arquivo gerado com sucesso!!!'

def participantesPorEventoParaCsv(id_evento):
  participantes = part.listarParticipantesPorEvento(id_evento)
  participantes = participantes['data']
  dic = {'Nome':[],
        'Sobrenome':[],
        'email':[]}
  for participante in participantes:
    dic['Nome'].append(participante['first_name'])
    dic['Sobrenome'].append(participante['last_name'])
    dic['email'].append(participante['email'])    
  df = pd.DataFrame.from_dict(dic)
  caminho_do_arquivo = asksaveasfilename(defaultextension=".csv", filetypes=[("Documentos Excel", ".csv"), ("Todos os arquivos", ".*")])
  df.to_csv(caminho_do_arquivo, sep=';', index=False,  encoding="latin1")
  return 'Arquivo gerado com sucesso!!!'


def pedidosPorEvento(id_evento):
  pedidos = ped.listarPedidosPorEvento(id_evento)
  pedidos = pedidos['data']
  dic = {'Nome':[],
        'Sobrenome':[],
        'email':[],
        'status':[]}
  for pedido in pedidos:
    status= ''
    if pedido['order_status'] == 'A': 
      status = 'Aprovado'
    elif pedido['order_status'] == 'P': 
      status = 'Pendente'
    elif pedido['order_status'] == 'NA': 
      status = 'Não Aprovado'
    elif pedido['order_status'] == 'NP': 
      status = 'Não Pago'
    elif pedido['order_status'] == 'R': 
      status = 'Reembolsado'
    else: 
      status = 'Cancelado'
    dic['Nome'].append(pedido['buyer_first_name'])
    dic['Sobrenome'].append(pedido['buyer_last_name'])
    dic['email'].append(pedido['buyer_email'])    
    dic['status'].append(status)    
  df = pd.DataFrame.from_dict(dic)
  caminho_do_arquivo = asksaveasfilename(defaultextension=".csv", filetypes=[("Documentos Excel", ".csv"), ("Todos os arquivos", ".*")])
  df.to_csv(caminho_do_arquivo, sep=';', index=False,  encoding="latin1")
  return 'Arquivo gerado com sucesso!!!'
