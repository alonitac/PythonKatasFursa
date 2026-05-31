import time


class CircuitOpenError(Exception):
    """Raised when a call is attempted while the circuit is OPEN."""
    pass


class CircuitBreaker:
    """
    Tracks consecutive failed requests and stops sending new ones when too many fail,
    giving the requested service enough time to recover instead of drowning it in requests.

    The breaker has three states:
      CLOSED    - requests pass through normally; failed requests are counted.
      OPEN      - requests are blocked immediately (raises CircuitOpenError);
                  after `recovery_timeout` seconds the breaker moves to HALF_OPEN.
      HALF_OPEN - one trial request is allowed through; if it succeeds the breaker
                  resets to CLOSED, if it fails it goes back to OPEN.

    Args:
        failure_threshold: number of consecutive failed requests that trip the breaker to OPEN
        recovery_timeout:  seconds to wait in OPEN before allowing a trial request
    """

    def __init__(self, failure_threshold, recovery_timeout):
        raise NotImplementedError("__init__ not implemented.")

    def call(self, operation):
        """
        Sends a request, respecting the current circuit state.

        Args:
            operation: the request to send (e.g. a database query or HTTP call) - a zero-argument function

        Returns:
            the response from the successful request

        Raises:
            CircuitOpenError: if the circuit is OPEN and the recovery timeout has not elapsed
            Exception: re-raises any exception from a failed request (and may trip the breaker)
        """
        raise NotImplementedError("call() not implemented.")


if __name__ == '__main__':
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=5)

    def unstable():
        raise ConnectionError("Service down")

    # First two failures trip the breaker to OPEN
    for _ in range(2):
        try:
            cb.call(unstable)
        except ConnectionError:
            pass

    # Now the breaker is OPEN - further calls raise CircuitOpenError immediately
    try:
        cb.call(unstable)
    except CircuitOpenError as e:
        print(e)  # Circuit is OPEN. Retry after 5s.
