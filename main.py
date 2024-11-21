from enum import Enum

# Enum para Unidade Federativa
class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla


# Enum para Sexo
class Sexo(Enum):
    MASCULINO = ('M', "Masculino")
    FEMININO = ('F', "Feminino")

    def __init__(self, caractere, texto):
        self.caractere = caractere
        self.texto = texto


# Enum para Estado Civil
class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"

    def __init__(self, texto):
        self.texto = texto


# Enum para Setor
class Setor(Enum):
    ENGENHARIA = "Engenharia"
    SAUDE = "Saúde"
    JURIDICO = "Jurídico"

    def __init__(self, nome):
        self.nome = nome


# Classe Endereco
class Endereco:
    def __init__(self, logradouro, numero, complemento, cep, cidade, uf):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf


# Classe abstrata Pessoa
class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


# Classe abstrata Fisica (Pessoa Física)
class Fisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento):
        super().__init__(nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento


# Classe abstrata Juridica (Pessoa Jurídica)
class Juridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj, inscricaoEstadual):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual


# Classe Funcionario (subclasse de Pessoa Física ou Jurídica)
class Funcionario(Fisica):
    def __init__(self, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento,
                 cpf, rg, matricula, setor, salario):
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario


# Classe Engenheiro (subclasse de Funcionario)
class Engenheiro(Funcionario):
    def __init__(self, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento,
                 cpf, rg, matricula, setor, salario, crea, crm):
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento,
                         cpf, rg, matricula, setor, salario)
        self.crea = crea
        self.crm = crm


# Classe Médico (subclasse de Funcionario)
class Medico(Funcionario):
    def __init__(self, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento,
                 cpf, rg, matricula, setor, salario):
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento,
                         cpf, rg, matricula, setor, salario)


# Classe Advogado (subclasse de Funcionario)
class Advogado(Funcionario):
    def __init__(self, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento,
                 cpf, rg, matricula, setor, salario, oab):
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento,
                         cpf, rg, matricula, setor, salario)
        self.oab = oab


# Classe Cliente
class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, endereco, protocoloAtendimento):
        super().__init__(nome, telefone, email, endereco)
        self.protocoloAtendimento = protocoloAtendimento


# Classe Fornecedor
class Fornecedor(Juridica):
    def __init__(self, nome, telefone, email, endereco, cnpj, inscricaoEstadual, produto):
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = produto


# Classe PrestacaoServico
class PrestacaoServico:
    def __init__(self, contratoInicio, contratoFim):
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim
