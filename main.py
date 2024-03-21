import eventos as ev
import participante as part
import pedidos  as ped
import toCsv 
import time

while(True):
  print('\nEscolha uma das opções abaixo\n')  
  print('1 - Eventos\n')
  print('2 - participantes\n')
  print('3 - Pedidos - Eventos\n')
  print('4 - Excel - Gerar arquivo .CSV\n')
  print('5 - Sair\n')
  opcao = int (input())   

  if(opcao == 1):
    print('1 - Listar Todos os Eventos\n')
    print('2 - Listar Eventos por Id\n')
    print('3 - Sair')
    # print('3 - Listar Eventos por Data\n')
    opcao = int(input())
    if(opcao == 1):
      listar = ev.listarEventos()
      for evento in listar['data']:
        print(f'idEvento: {evento["id"]} || Evento: {evento["name"]} || Data: {evento["start_date"]}')    
    elif(opcao == 2):
      eventoId = input("Informe o Id do evento")
      listar = ev.listarEventosPorId(eventoId)
      for evento in listar['data']:
        print(f'idEvento: {evento["id"]} || Evento: {evento["name"]} || Data: {evento["start_date"]}')
    else:
      continue 
    # else:
    #   listar = ev.listarEventosPorData()
    #   print(listar)

  elif(opcao == 2):
    print('1 - Listar Participantes por Evento\n')
    print('2 - Listar Participanes pot id do Ingresso\n')
    print('3 - Listar Participantes por Número do Ingresso\n')
    print('4 - Sair\n')
    opcao = int(input())
    if(opcao == 1):
      eventoId = input("Informe o Id do evento")
      listar = part.listarParticipantesPorEvento()
      for evento in listar['data']:
        print(f'Nome: {evento["first_name"]} || Sobrenome: {evento["last_name"]} || Email: {evento["email"]}') 
    
    elif(opcao == 2):
      idIngresso = input("Informe o id do ingresso")
      eventoId = input("Informe o id do evento")
      listar = part.listarParticipantesPorIdDoIngresso(eventoId, idIngresso)
      for evento in listar['data']:
        print(f'Nome: {evento["first_name"]} || Sobrenome: {evento["last_name"]} || Email: {evento["email"]}') 

    elif(opcao == 3):      
      idIngresso = input("Informe o id do ingresso")
      eventoId = input("Informe o id do ticket")
      listar = part.listarParticipantesPorNumeroDoticker(idIngresso, eventoId)
      for evento in listar['data']:
        print(f'Nome: {evento["first_name"]} || Sobrenome: {evento["last_name"]} || Email: {evento["email"]}') 
    else:
      continue 
  
  elif(opcao == 3):
    print('1 - Listar Pedidos por Evento\n')
    # print('2 - Listar Pedidos Por Id\n')
    # print('3 - Listar Participantes por pedido\n')
    opcao = int(input())
    # if(opcao == 1):

    #   listar = ped.listarParticipantesPorPedido()
    #   print(listar['data'][0])    
  
    if(opcao == 1):
      eventoId = input("Informe o Id do evento")
      listar = ped.listarPedidosPorEvento(eventoId)
      for evento in listar['data']:
        print(f'Nome: {evento["buyer_first_name"]} || Sobrenome: {evento["buyer_last_name"]} || Email: {evento["buyer_email"]}') 
    else:
      continue
    # else:
    #   listar = ped.listarPedidosPorId()
    #   print(listar)
  if(opcao == 4):
    print('\n1 -Gerar arquivo .csv com todos os eventos \n')
    print('2 -Gerar arquivo .csv com todos os participantes em um determinado evento \n')
    print('3 -Gerar arquivo .csv com todos pedidos por evento\n')
    print('4 -Sair\n')    
    csv = int(input())
    if csv == 1:
      csv = toCsv.eventosParaCsv()
      print(csv)
      time.sleep(2)
    elif (csv == 2):
      eventoId = input('Informe o id do evento')
      csv = toCsv.participantesPorEventoParaCsv(eventoId)
      print(csv)
      time.sleep(2)

    elif(csv == 3):
      eventoId = input('Informe o id do evento')
      csv = toCsv.pedidosPorEvento(eventoId)
      print(csv)
      time.sleep(2)

    else:
      continue
  else:
    break