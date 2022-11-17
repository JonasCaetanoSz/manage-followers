import os
from insta import Insta
# função pra limpar o terminal

def clear():

    if os.system('clear') == 1:

        os.system('cls')
        
# usuario escolhe metodo de login

print('\n\n[+] escolha um metodo de login:\n\n(1) - login com senha\n\n(2) - login com sessionid\n\n(3) - sair\n\n')

while True:

    try:

        method = input('escolha uma opçao:')

        if  int(method) < 1 or int(method) > 3:
            print(type(method))
            print('\n\n[!] opção invlida\n\n[+] escolha um metodo de login:\n\n(1) - login com senha\n\n(2) - login com sessionid\n\n(3) - sair\n\n')
        
        else:

            break;
    
    except:

        print('\n\n[!] você não informou uma opção valida.\n\n')

# chamando o metodo de login

match int(method):

    case 1:

        ig = Insta.login_by_password()
    
    case 2:

        ig = Insta.login_by_session_id()
    
    case 3 :

        quit()
    
    case _:
        quit()

# login no instagram realizado, usuario escolhe oque quer fazer

clear()
print('\n\n[*] login realizado com sucesso, escolha oque deseja fazer:\n\n(1) - deixar de seguir quem não me segue\n\n(2) - seguir todos usuarios que me seguem\n\n(3) - importar seguidores (json)\n\n(4) - sair\n\n')
while True:

    selected = input('\n\nescolha uma opção: ')

    try:

        if int(selected) < 1 or int(selected) > 4:

            print('\n\n[!] por favor escolha uma opção valida')
        
        else:

            break;
    
    except:

        print('\n\n[!] por favor escolha uma opção valida')

# chamando função escolhida pelo usuario

match int(selected):

    case 1: Insta.ufollow(ig)
    case 2: Insta.follow(ig)
    case 3: Insta.followers_json(ig)
    case 4: quit()
    case _: quit()
