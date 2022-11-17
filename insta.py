
import  os
from instagrapi import Client
import time
import json

# intervalo entre cada ação (em segundos, o default é 10)

interval = 10

# função pra limpar o terminal

def clear():

    if os.system('clear') == 1:

        os.system('cls')
    
class Insta:

    def login_by_password():
        
        try:

            clear()

            username = input('\n\n[+] digite seu usuario: ')
            while True:

                if username.isspace() == True or username == '':

                    username = input('\n\n[!] usuario invalido, por favor digite seu usuario: ')

                else:

                    break;
            
            password = input('\n\n[+] agora digite sua senha: ')
            while True:
                

                    if password.isspace() == True or password == '':

                        password = input('\n\n[!] senha invalida , por favor digite sua senha: ')
                    
                    else:
                        break;
            
            clear()
            print('\n\n[*] fazendo login no instagram, aguarde...')
            ig = Client()
            ig.login(username, password)

        except Exception as login_erro:

            clear()
            print('\n\n[!] erro ao fazer login.\n\n')
            print('motivo:' , login_erro)
            quit()
        
        return ig

    def login_by_session_id():

        clear()
        sessionid = input('\n\n[+] por favor cole o sessionid aqui: ')

        if sessionid.isspace() or sessionid == '':

            print('\n\n[!] sesionid invalido, por favor reinicie o programa.')
            quit()
        
        print('\n\n[*] fazendo login no instagram, aguarde...')
        try:

            ig = Client()
            ig.login_by_sessionid(sessionid)

        except Exception as login_erro:

            clear()
            print('\n\n[!] erro ao fazer login.\n\n')
            print('motivo:' , login_erro)
            quit()
        
        return ig

    def ufollow(ig):

        try:

            not_follower = []
            clear()
            print("\n\n[*] obtendo lista de seguidores...")
            user_info = ig.account_info()
            pk_id = user_info.pk
            followers = ig.user_followers(user_id=pk_id, amount=0)
            print('\n\n[*] obtendo lista de pessoas que você segue...')
            following = ig.user_following(user_id=pk_id, amount=0)
            print('\n\n[*] comparando listas....')
            for user_id in following.keys():

                if user_id in followers.keys():

                    # usuario segue a conta atual
                    pass

                else:
                    
                    not_follower.append(user_id)
            
            if len(not_follower) == 0:

                print('\n\n[*] todos usuarios que você segue te seguem de volta.')
                quit()
            
            else:

                
                while True:

                    print(f'\n\n[+] {len(not_follower)} usuarios não te seguem de volta, deseja para de seguir todos [s/n]?')
                    selected = input('').upper()

                    if selected == 'S' or selected == 'SIM':

                        clear()
                        break;

                    elif selected == 'N' or selected == 'NÃO':

                        clear()
                        print('\n\n[*] muito bem, obrigado por usar meu programa!')
                        quit()
                    
                    else:

                        clear()
                        print('\n\n[!] a opção selecionada não é valida.')

                 # deixando de seguir usuarios

                file_list = open('users_uffolow.txt', 'w')
                for user in not_follower:
                    
                    print(f'\n[*] deixando de seguir : {following[user].username}')
                    ig.user_unfollow(user)
                    print(f'\n[*] concluido, aguardando {interval} segundos...')
                    time.sleep(interval)
                    file_list.write(f'https://www.instagram.com/{following[user].username}\n')

                file_list.close()
                print('\n\n[*] concluido! a lista de usuarios deixados de seguir foi gravado em:\n')
                print(f"{os.getcwd()}/users_uffolow.txt")
                quit()




        
        except Exception as erro_unfollow:

            clear()
            print('\n\n[!] erro de execução ao deixar de seguir.\n\n')
            print('motivo: ', erro_unfollow)

    def follow(ig):

        try:

            print("\n\n[*] obtendo lista de seguidores...")
            clear()
            not_mutual = []
            user_info = ig.account_info()
            pk_id = user_info.pk
            #print("\n\n[*] obtendo lista de seguidores...") tava tendo um lag 
            followers = ig.user_followers(user_id=pk_id, amount=0)
            print('\n\n[*] obtendo lista de pessoas que você segue...')
            following = ig.user_following(user_id=pk_id, amount=0)
            print('\n\n[*] comparando listas....')

            for user_id in followers.keys():

                if user_id in following.keys(): pass
                else: not_mutual.append(user_id)
            
            if len(not_mutual) == 0:

                print('\n\n[*] você segue todos usuarios que segue.')
                quit()
            
            else:

                print(f'\n\n[+] você não segue de volta {len(not_mutual)} usuarios, deseja seguir todos [s/n] ? ')
            
            while True:

                selected = input('').upper()

                if selected == 'S' or selected == 'SIM':

                    break;

                elif selected == 'N' or selected == 'NÃO':

                    print('\n\n[*] muito bem, obrigado por usar meu programa!')
                    quit()
                
                else:

                    print('\n\n[!] por favor escolha uma opção valida.')
            
            # começar a seguir usuarios
            new_followings_file = open('new_followings.txt', 'w', encoding='utf-8')
            for user_id in not_mutual:

                private = followers[user_id].is_private
                if private == 'true' or private == True:

                    print(f'\n\n[*] pedindo usuario {followers[user_id].username} pra seguir ele.')
                
                else:

                    print(f'\n\n[*] seguindo o usuario {followers[user_id].username} ')
                
                ig.user_follow(user_id)
                new_followings_file.write(f'https://www.instagram.com/{followers[user_id].username}\n')
                print(f'\n[*] concluido, aguardando {interval} segundos...')
            
            new_followings_file.close()
            print('\n\n[*] concluido! a lista de usuarios que você começou a seguir foi gravado em:\n')
            print(f"{os.getcwd()}/new_followings.txt")
            quit()

        except Exception as erro_follow:

            clear()
            print('\n\n[!] erro de execução seguir usuarios que te segue..\n\n')
            print('motivo: ', erro_follow)


    def followers_json(ig):

        try:

            followers_dict = {'users':[]}
            clear()
            print('\n\n[*] obtendo lista de seguidores...')
            user_info = ig.account_info()
            pk_id = user_info.pk
            followers = ig.user_followers(user_id=pk_id, amount=0)
            print('\n\n[*] analisando lista de seguidores...')

            for user_id in followers.keys():

                followers_dict['users'].append(
                    {'username': followers[user_id].username,
                    'full_name': followers[user_id].full_name,
                    'is_private': followers[user_id].is_private,
                    'profile_pic_url': followers[user_id].profile_pic_url,
                    'profile_url': f'https://www.instagram.com/{followers[user_id].username}',
                    'pk_id': followers[user_id].pk
                    })
            
            print('\n\n[*] gerando arquivo json...')
            followers_json = json.dumps(followers_dict, indent=4)
            file_json = open('followers.json', 'w', encoding='utf-8')
            file_json.write(followers_json)
            file_json.close()
            print('\n\n[*] concluido, o arquivo json foi gerado em:\n')
            print(f'{os.getcwd()}/followers.json')
            quit()
            

        except Exception as erro_json_followers:

            clear()
            print('\n\n[!] falha ao importar lista de seguidores.\n') 
            print('motivo:', erro_json_followers)