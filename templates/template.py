import sys, os
sys.path.append(os.path.abspath(os.curdir))

from model.password import Password
from view.password_view import FernetHasher

action = input('Digite 1 para salvar uma senha nova ou 2 para ver senha salva: ')

if action == '1':
    # Verifica se há chaves salvas
    if len(Password.get()) == 0:
        key, path = FernetHasher.create_key(arquive=True)
        print("Sua chave foi criada com sucesso, salve-a com cuidado")
        print(f'Chave: {key.decode("utf-8")}')

        if path:
            print("Chave salva no arquivo, lembre-se de removê-lo após transferir")
            print(f'Caminho: {path}')
    else:
        # Aqui você pode carregar a chave do arquivo ou pedir ao usuário
        # Exemplo:
        key_str = input("Cole aqui sua chave: ")
        key = key_str.encode('utf-8')

    domain = input("Domínio: ")
    password = input("Senha: ")

    fernet_user = FernetHasher(key)
    p1 = Password(domain=domain, password=fernet_user.encrypt(password).decode('utf-8'))
    p1.save()
    print("Senha salva com sucesso!")

else:
    domain = input('Domínio: ')
    key = input('Key: ')
    fernet = FernetHasher(key=key)
    data = Password.get()

    for i in data:
        if domain in i['domain']:
            password = fernet.decrypt(i['password'])
    
    if password:
        print(f'Sua senha: {password}')
    else:
        print('Nenhuma senha encontrada para esse domínio!')