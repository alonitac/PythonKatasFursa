class RoundRobinLoadBalancer:
    """
    Distributes incoming requests evenly across a pool of servers so no single
    server is overwhelmed while others sit idle.

    "Round robin" means cycling through the list in order, wrapping back to the
    start - like dealing cards around a table. Request 1 goes to server A,
    request 2 to server B, request 3 to server C, request 4 back to server A, etc.

    Servers are identified by plain strings (e.g. "192.168.0.1").
    """

    def __init__(self):
        """
        Initializes the load balancer with an empty pool of servers.
        """
        raise NotImplementedError("Constructor not implemented.")

    def add_server(self, server: str):
        """
        Adds a server to the pool.

        Args:
            server: server address string (e.g. "192.168.0.1")
        """
        raise NotImplementedError("add_server not implemented.")

    def remove_server(self, server: str):
        """
        Removes a server from the pool.

        Args:
            server: server address string to remove
        """
        raise NotImplementedError("remove_server not implemented.")

    def route_request(self) -> str | None:
        """
        Routes a request to the next server in round-robin order.

        Returns:
            the server address string, or None if the pool is empty
        """
        raise NotImplementedError("route_request not implemented.")


if __name__ == '__main__':
    lb = RoundRobinLoadBalancer()

    lb.add_server("192.168.0.1")
    lb.add_server("192.168.0.2")
    lb.add_server("192.168.0.3")

    print(lb.route_request())  # 192.168.0.1
    print(lb.route_request())  # 192.168.0.2
    print(lb.route_request())  # 192.168.0.3
    print(lb.route_request())  # 192.168.0.1  (wraps around)

    lb.remove_server("192.168.0.2")

    print(lb.route_request())  # 192.168.0.1 or 192.168.0.3
    print(lb.route_request())  # the other one
