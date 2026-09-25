import math


def is_valid(lamda, mu, c=1):
    """
       Validate the arguments of a queuing model.

       Args:
           lamda: Arrival rate. Either a numeric scalar, or a list/tuple
               of numeric scalars representing per-priority-class arrival
               rates. Every value must be strictly positive (lamda > 0).
           mu: The (per-server) service rate. Must be strictly positive.
           c: The number of servers. Must be a positive whole number.
               Defaults to 1.

       Returns:
           True if lamda, mu, and c all satisfy the rules above, False
           otherwise (wrong type, non-positive, or c not a whole number).
       """
    # check lamda
    if isinstance(lamda, (list, tuple)):
        if len(lamda) == 0:
            return False

        for value in lamda:
            if not isinstance(value, (int, float)):
                return False
            if value <= 0:
                return False
    else:
        if not isinstance(lamda, (int, float)):
            return False
        if lamda <= 0:
            return False

    # check mu
    if not isinstance(mu, (int, float)):
        return False
    if mu <= 0:
        return False

    # check c
    if not isinstance(c, (int, float)):
        return False
    if c <= 0:
        return False
    if c != int(c):
        return False

    return True


def is_feasible(lamda, mu, c=1):
    """
        Determine whether a queue is feasible.

        Args:
            lamda: Arrival rate. Either a numeric scalar, or a list/tuple
                of numeric scalars representing per-priority-class arrival
                rates. Every value must be strictly positive (lamda > 0).
            mu: The (per-server) service rate. Must be strictly positive.
            c: The number of servers. Must be a positive whole number.
                Defaults to 1.

        Returns:
            True if the queue's arguments are valid and rho < 1, False if
            the arguments are invalid, or if rho >= 1.
        """

    if not is_valid(lamda, mu, c):
        return False

    # add arrival rates together if lamda is a list or tuple
    if isinstance(lamda, (list, tuple)):
        lamda = sum(lamda)

    rho = lamda / (c * mu)

    if rho < 1:
        return True
    else:
        return False


def calc_p0(lamda, mu, c=1):
    """
        Calculate p0, the probability that a queue system is empty (zero
        customers in service or waiting).

        Args:
            lamda: Arrival rate. Either a numeric scalar, or a list/tuple
                of numeric scalars representing per-priority-class arrival
                rates. Every value must be strictly positive (lamda > 0).
            mu: The (per-server) service rate. Must be strictly positive.
            c: The number of servers. Must be a positive whole number.
                Defaults to 1.

        Returns:
            math.nan if the queue's arguments are not valid, math.inf if
            the queue is valid but not feasible, otherwise p0, calculated
            with the M/M/1 formula when c == 1, or the general M/M/c
            formula otherwise.
        """

    # check is queue inputs are valid
    if not is_valid(lamda, mu, c):
        return math.nan

    # check if queue is feasible
    if not is_feasible(lamda, mu, c):
        return math.inf

    # add the arrival rates together if lamda is a list or tuple
    if isinstance(lamda, (list, tuple)):
        lamda = sum(lamda)

    # calculate p0 for an M/M/1 queue
    if c == 1:
        p0 = 1 - (lamda / mu)
        return p0

    # calculate utilization for an M/M/c queue
    rho = lamda / (c * mu)

    # start the total at zero
    total = 0

    # calculate the sum needed for the M/M/c formula
    for n in range(c):
        total = total + (lamda / mu) ** n / math.factorial(n)

    # add the rest of the M/M/c formula
    total = total + (lamda / mu) ** c / (math.factorial(c) * (1 - rho))

    # calculate the probability that the system is empty
    p0 = 1 / total

    return p0


def calc_lq_mmc(lamda, mu, c=1):
    """
       Calculate lq, the average number of customers waiting in the
       queue, for an M/M/1 or M/M/c queue.

       Args:
           lamda: Arrival rate. Either a numeric scalar, or a list/tuple
               of numeric scalars representing per-priority-class arrival
               rates. Every value must be strictly positive (lamda > 0).
           mu: The (per-server) service rate. Must be strictly positive.
           c: The number of servers. Must be a positive whole number.
               Defaults to 1.

       Returns:
           math.nan if the queue's arguments are not valid, math.inf if
           the queue is valid but not feasible, otherwise lq, calculated
           with the M/M/1 formula when c == 1, or the general M/M/c
           formula otherwise.
       """
    if not is_valid(lamda, mu, c):
        return math.nan

    if not is_feasible(lamda, mu, c):
        return math.inf

    # add arrival rates together if needed
    if isinstance(lamda, (list, tuple)):
        lamda = sum(lamda)

    rho = lamda / (c * mu)

    # M/M/1 queue
    if c == 1:
        lq = (rho ** 2) / (1 - rho)
        return lq

    # M/M/c queue
    p0 = calc_p0(lamda, mu, c)

    lq = (p0 * ((lamda / mu) ** c) * rho) / \
         (math.factorial(int(c)) * ((1 - rho) ** 2))

    return lq