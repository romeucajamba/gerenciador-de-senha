from pathlib import Path #biblioteca que me auxilia manipular  ou criar directorios

class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent  # Caminho base do projeto
    # __file__ é uma variável especial que contém o caminho do arquivo atual
    DB_DIR = BASE_DIR / 'db'  # Diretório onde as chaves serão armazenadas
    # O operador / é usado para construir caminhos de forma portátil

    def save(self):
      table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')

      if not table_path.exists():
        table_path.touch()

        with open(table_path, 'a') as arq:
           arq.write("|".join(list(map(str, self.__dict__.values()))))
           arq.write('\n')

    @classmethod
    def get(cls):
        table_path = Path(cls.DB_DIR / f'{cls.__name__}.txt')

        if not table_path.exists():
            table_path.touch()
    
        with open(table_path, 'r') as arq:
           x = arq.readlines()
           
        results = [] 
        
        atributes = vars(cls())

        for i in x:
           split_v = i.split('|')
           tmp_dict = dict(zip(atributes, split_v))
           results.append(tmp_dict)
        
        return results


