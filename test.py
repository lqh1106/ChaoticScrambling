import math


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def lcm_of_list(numbers):
	lcm_result = numbers[0]
	for i in range(1, len(numbers)):
		lcm_result = (lcm_result * numbers[i]) // gcd(lcm_result, numbers[i])
	return lcm_result


def test(disorganized_table):
    visited = set()
    order = []

    for i, val in enumerate(disorganized_table):
        if val != -1 and i not in visited:
            cycle_length = 0
            j = i
            while j not in visited:
                visited.add(j)
                j = disorganized_table[j]
                cycle_length += 1
            order.append(cycle_length)

    return lcm_of_list(order) if order else 1
