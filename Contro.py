# O que faz?
# Qual a utilidade desta ferramenta?
# Testes - Interface de Comunicação - Desenvolvimento
# Ordem de execução
# controle financeiro em python - you

class Despesas:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor

class ControleDespesas:
    def __init__(self):
        self.despesas: list

    def adicionar_despesas(self, despesas):
        self.despesas.append(despesas)

    def listar_despesas(self):
        if self.despesas:
            for index, despesas in enumerate(self.despesas, start=1)
                print("--"*20)
                print(f"{{index}. Descrição: {despesas.descicao}}")
                print(f"Categoria: {despesas.categoria}")
                print(f"Valor")
        else:
            print("Cadastre a movimentação de despesas.")

if __name__ == "__main__"
    controle = ControleDespesas

    while True
        print("1. Adicionar Despesas")
        print("2. Listar Despesas")
        print("3. Sair")
        opcao = input("selecione uma opção")

        if opcao == 1:
            Descricao = input("Qual o produto cadastrado?")
            categoria = input("Qual a classificação?")
            valor = input("Valor de compra")
            Despesas = Despesas (Descricao, categoria, valor)
