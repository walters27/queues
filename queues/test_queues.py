import math
import queues


# Test is_valid

print("Testing is_valid")

print(queues.is_valid(2, 5))
print(queues.is_valid(2, 5, 2))
print(queues.is_valid([1, 2], 5, 2))
print(queues.is_valid((1, 2), 5, 2))

# Invalid values
print(queues.is_valid(-2, 5))
print(queues.is_valid(2, -5))
print(queues.is_valid(2, 5, 0))
print(queues.is_valid(2, 5, 1.5))

print()


# Test is_feasible

print("Testing is_feasible")

# rho = 2 / (1 * 5) = 0.4, so it is feasible
print(queues.is_feasible(2, 5))

# rho = 5 / (1 * 5) = 1, so it is not feasible
print(queues.is_feasible(5, 5))

# rho = 2 / (2 * 5) = 0.2, so it is feasible
print(queues.is_feasible(2, 5, 2))

# Test a list of arrival rates
print(queues.is_feasible([1, 1], 5, 1))

print()


# Test calc_p0

print("Testing calc_p0")

# M/M/1: p0 = 1 - (2 / 5) = 0.6
print(queues.calc_p0(2, 5))

# M/M/2
print(queues.calc_p0(4, 3, 2))

# Test list of arrival rates
print(queues.calc_p0([1, 1], 5, 1))

# Invalid queue should return nan
print(queues.calc_p0(-2, 5))

# Infeasible queue should return infinity
print(queues.calc_p0(5, 5))

print()


# Test calc_lq_mmc

print("Testing calc_lq_mmc")

# M/M/1: Lq = rho^2 / (1-rho)
# rho = 2/5 = 0.4
# Lq = 0.4^2 / 0.6 = 0.266666...
print(queues.calc_lq_mmc(2, 5))

# M/M/2
print(queues.calc_lq_mmc(4, 3, 2))

# Test list of arrival rates
print(queues.calc_lq_mmc([1, 1], 5, 1))

# Invalid queue should return nan
print(queues.calc_lq_mmc(-2, 5))

# Infeasible queue should return infinity
print(queues.calc_lq_mmc(5, 5))