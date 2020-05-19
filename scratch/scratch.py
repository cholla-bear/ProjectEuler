from numpy import array, convolve

lower_bound = 1000000
n_limit = 100

def dynamic_solution_np():
    """Use Pascal's triangle to get binomial coefficients."""
    total = 0

    row_n = array((1,), dtype=object)  # 1st row of Pascal's triangle, to be updated in place using convolutions of [1, 1]
    conv_kernel = array((1, 1), dtype=object)

    for n in range(2, n_limit + 1):
        row_n = convolve(row_n, conv_kernel)
        total += len(row_n[row_n > lower_bound])

    return total


print(f"There are {dynamic_solution_np()} values of comb(n, r) that exceed {lower_bound} for natural numbers, n, up to {n_limit}")
