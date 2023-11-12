class Lampada:
    def __init__(self):
        self.__acesa = False

    def acender(self, pessoa):
        self.__acesa = True
        return f"A lâmpada foi acesa por {pessoa}."

    def apagar(self):
        self.__acesa = False
        return "A lâmpada foi apagada."

    def __str__(self):
        return f"Lâmpada: {'Acesa' if self.__acesa else 'Apagada'}"


class Interruptor:
    def __init__(self, lampada):
        self.__lampada = lampada

    def acionar(self, pessoa):
        if self.__lampada._Lampada__acesa:
            return self.__lampada.apagar()
        else:
            return self.__lampada.acender(pessoa)

    def __str__(self):
        return f"Interruptor: {str(self.__lampada)}"


class Fechadura:
    def __init__(self, tipo, chave_ou_senha):
        self.__tipo = tipo
        self.__chave_ou_senha = chave_ou_senha

    def abrir(self, pessoa, chave_ou_senha):
        if chave_ou_senha == self.__chave_ou_senha:
            return f"A porta foi aberta por {pessoa}."
        else:
            return f"Chave ou senha incorreta. A porta permanece fechada."

    def __str__(self):
        return f"Fechadura {self.__tipo}"


class Comodo:
    def __init__(self, nome, cor, ar_condicionado=False, fechadura_tipo="Simples", fechadura_chave_ou_senha="chave123"):
        self.__nome = nome
        self.__cor = cor
        self.__ar_condicionado = ar_condicionado
        self.__lampada = Lampada()
        self.__interruptor = Interruptor(self.__lampada)
        self.__fechadura = None

        if fechadura_tipo == "Simples" or fechadura_tipo == "Inteligente":
            self.__fechadura = Fechadura(fechadura_tipo, fechadura_chave_ou_senha)
            print(f"Comodo '{self.__nome}' criado.")
        else:
            print(f"Comodo '{self.__nome}' criado sem fechadura.")

    def __str__(self):
        info_fechadura = str(self.__fechadura) if self.__fechadura else "Sem fechadura"
        return f"Cômodo: {self.__nome} | Cor: {self.__cor} | Ar Condicionado: {'Sim' if self.__ar_condicionado else 'Não'} | {info_fechadura}"

    def acionar_ar_condicionado(self, pessoa):
        if self.__ar_condicionado:
            return f"Ar-condicionado ligado por {pessoa}."
        else:
            return "Este cômodo não possui ar-condicionado."

    def acionar_lampada(self, pessoa):
        return self.__interruptor.acionar(pessoa)

    def abrir_porta(self, pessoa, chave_ou_senha):
        if self.__fechadura:
            return self.__fechadura.abrir(pessoa, chave_ou_senha)
        else:
            return "Este cômodo não possui uma porta."


class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def visitar_casa(self, casa):
        result = [f"{self.__nome} está visitando a casa."]
        for comodo in casa.obter_comodos():
            result.append(str(comodo))
            result.append(comodo.acionar_ar_condicionado(self.__nome))
            result.append(comodo.acionar_lampada(self.__nome))
            result.append(comodo.abrir_porta(self.__nome, "senha_incorreta"))
            result.append(comodo.abrir_porta(self.__nome, "chave123"))
        result.append("\n")
        return "\n".join(result)


class Casa:
    def __init__(self):
        self.__comodos = []

    def adicionar_comodo(self, nome, cor, ar_condicionado=False, fechadura_tipo="Simples", fechadura_chave_ou_senha="chave123"):
        comodo = Comodo(nome, cor, ar_condicionado, fechadura_tipo, fechadura_chave_ou_senha)
        self.__comodos.append(comodo)

    def obter_comodos(self):
        return self.__comodos

    def __str__(self):
        return "\n".join(str(comodo) for comodo in self.__comodos)


# Cenário de Teste
casa = Casa()
casa.adicionar_comodo("Quarto", cor="Azul", ar_condicionado=True, fechadura_tipo="Inteligente", fechadura_chave_ou_senha="senha123")
casa.adicionar_comodo("Sala", cor="Verde")

# Simulando a execução com uma pessoa visitando a casa
pessoa = Pessoa("João")
print(pessoa.visitar_casa(casa))
