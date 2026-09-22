import math


def is_valid(lamda, mu, c=1):

    # check lamda
    if isinstance(lamda, (list, tuple)):
        if len(lamda) == 0:
            return False

        for value in lamda:
            if not isinstance(value, (int, float)):
                return False
            if value < 0:
                return False
    else:
        if not isinstance(lamda, (int, float)):
            return False
        if lamda < 0:
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
        return 

    return True


def is_feasible(lamda, mu, c=1):

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

    if not is_valid(lamda, mu, c):
        return math.nan

    if not is_feasible(lamda, mu, c):
        return math.inf

    # add arrival rates together if lamda is list or tuple
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