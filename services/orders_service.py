class Orders:
    def combine_orders(self, requests: list[int], n_max: int) -> int:
        """
        Args:
            requests (list[int]): Uma lista de inteiros com os valores monetários
            n_max (int): Um inteiro representando o valor máximo permitido para a soma de cada viagem

        Returns:
            int: O número de viagens possíveis após a combinação dos pedidos
        """
        requests.sort()
        first_element= 0
        last_element = len(requests) - 1
        deliveries = 0

        while first_element <= last_element:
            if requests[first_element] + requests[last_element] <= n_max:
                first_element+= 1
            last_element -= 1
            deliveries += 1
        return deliveries
