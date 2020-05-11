user_input = 'random'
data = []

menu = """
Menu:
1. Adicionar item
2. Marcar como feito
3. Ver items
4. Sair
"""

def show_menu():
  print(menu)


while user_input != '4':
  show_menu()
  user_input = input('O que deseja fazer: ')
  print('Você escolheu:', user_input)

  if user_input == '1':
    item = input('Novo item:')
    data.append(item)
    print('Item adicionado: ', item)
  elif user_input == '2':
    item = input('O que você já fez?')
    if item in data:
      data.remove(item)
      print('Item removido: ', item)
    else:
      print('Item não existe.')
  elif user_input == '3':
    print('Checklist')
    for item in data:
      print(item)
  elif user_input == '4':
    print('Goodbye')
  else:
    print('Please enter 1, 2, 3 or 4')