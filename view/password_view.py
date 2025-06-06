import string, secrets, hashlib, base64
from pathlib import Path #biblioteca que me auxilia manipular  ou criar directorios

class FernetHasher:
    RABDOM_STRINGCHARS = string.ascii_lowercase + string.ascii_uppercase #Gerando letras minúsculas e maiúsculas
    BASE_DIR = Path(__file__).resolve().parent.parent  # Caminho base do projeto
    # __file__ é uma variável especial que contém o caminho do arquivo atual
    KEY_DIR = BASE_DIR / 'keys'  # Diretório onde as chaves serão armazenadas
    # O operador / é usado para construir caminhos de forma portátil


    @classmethod
    def _get_random_string(cls, length=25):
        string = ""
        for i in range(length):
            #Desse jeito me gera senha aleatória com 25 caracteres
            #Podendo ser letras minúsculas ou maiúsculas
            string += secrets.choice(cls.RABDOM_STRINGCHARS) #Pegando as letras minusculas ou maiúsculas aleatoriamente
        return string
    
    @classmethod 
    def create_key(cls, arquive=False):
        #Pegando o conteudo do metodo _get_random_string que é uma string aleatória
        value = cls._get_random_string()
     
        #gerando o hash da string aleatória usando haslib e o sha256 para franformar em binário/byte ou codificar em binário
        #O valor é codificado em utf-8 para garantir que seja compatível com o formato de string
        hasher = hashlib.sha256(value.encode('utf-8')).digest()# o digest transforma de binário para string
       
        key = base64.b64encode(hasher)  # Desse jeito tenho o conjunto de byte da hash gerada
        
        if arquive:
            return key, cls.arquive_key(key)
        
        return key, None
    
    @classmethod
    def arquive_key(cls, key):
        file = 'key.key'

        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(length=5)}.key'

        with open(cls.KEY_DIR / file,'wb') as arq:
            arq.write(key)  # Escrevendo a chave no arquivo em formato binário

        return cls.KEY_DIR / file

print(FernetHasher.create_key(arquive=True))  # Cria uma chave e arquiva
# A classe FernetHasher gera uma chave aleatória de 25 caracteres
# A chave é composta por letras minúsculas e maiúsculas