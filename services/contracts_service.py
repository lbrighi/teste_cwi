class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return f'id={self.id}, debt={self.debt}'


class Contracts:
    def get_top_N_open_contracts(self, open_contracts: list, renegotiated_contracts: list, top_n: int) -> list:
        """
        Args:
            open_contracts (list): Lista de contratos abertos
            renegotiated_contracts (list): Lista de contratos renegociados
            top_n (int): Número de contratos com maior dívida que serão retornados

        Returns:
            list: Lista ordenada pela maior dívida de contratos abertos, que ainda não foram renegociados.
        """
        contracts_list = [
            contracts
            for contracts in open_contracts
            if contracts.id not in renegotiated_contracts
        ]
   
        contratos_em_aberto_ordenados = sorted(contracts_list, key=self.__contract_debt, reverse=True)

        return [contract.__str__() for contract in contratos_em_aberto_ordenados[:top_n]]
    
    def __contract_debt(self, contract):
        return contract.debt
