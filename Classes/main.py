class reg :
    def __init__(self, nome, cpf, datanascimento, endereco, cnpj, telefone):
        self._nome = nome
        self._cpf = cpf
        self._data = datanascimento
        self._end = endereco
        self._cnpj = cnpj
        self._telefone = telefone


class adm:
    def _init_(self, login, senha, codacess):
        self._login = login
        self._senha = senha
        self._codacess = codacess

class serv:
    def __init__(self, id, senha):
        self._id = id
        self._senha = senha
