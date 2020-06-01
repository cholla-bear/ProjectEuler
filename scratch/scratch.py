"""
This file contains material for calculating cycles in the sequence of gaps that occur between terms given by the expansion of repeating fraction in problem 57.
"""
from itertools import accumulate, chain, cycle

# Further cycles alternate between the 2nd and 3rd, switching cycles around every 3700-4700 terms of the fraction expansion
gap_map = {
    0: (8, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5, 3, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8),
    3229: [8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5, 8],
    7947: [3, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5, 8, 8, 5, 8, 5, 8, 5],
}


# Digit counter (from numb import num_digits)
def num_digits(n, base=10):
    """Return number of digits in n."""
    assert n >= 0, "Must provide a non-negative integer"
    if n == 0:
        return 1
    else:
        return math.floor(math.log(n, base)) + 1


# Timers (from common import elapsed, split_timer)
_start = time.time()
_split = None


def elapsed():
    """Print elapsed time in seconds since this module was loaded."""
    print("Elapsed time: {} seconds".format(round(time.time() - _start, 6)))


def split_timer():
    """Set split timer and, if this is not the first call to split_timer, print time since it was last set."""
    global _split
    if _split:
        print("Split time: {} seconds".format(round(time.time() - _split, 6)))
    _split = time.time()



# Begin supplemental
def expand_terms(n=3, d=2):
    while True:
        yield n, d

        d0 = d
        d = n + d
        n = d + d0


def find_cycle(gap_list):
    """Used for determining cycles during :func detect_cycles:."""
    expected_cycle_lens = (31, 32, 33)

    # Stringent on first test
    if not any(gap_list[:i] == gap_list[i:2 * i] for i in expected_cycle_lens):
        return -1

    # Actual test
    for i in expected_cycle_lens:
        failed_test = False
        test_cycle = gap_list[:i]
        test_field = gap_list[i:]

        while i <= len(test_field):
            if not test_cycle == test_field[:i]:
                failed_test = True
                break
            else:
                test_field = test_field[i:]

        if not failed_test:
            return test_cycle


def pp(dictionary):
    """Pretty print a dictionary at one level of depth."""
    print("{")
    for k, v in dictionary.items():
        print(f"    {k}: {v},")
    print("}")


def detect_cycles():
    """
    Detect cycles and update cycle_map while iterating over :expand_terms:.

    This function appears to be redundant now, as it has determined that after the 1st cycle (which is an
    offset of another cycle), the cycles seem to alternate consistently between two versions.
    """
    # NOTE: Program will crash around 567000 iterations, as the fraction terms have over 217034 digits.

    # Indeces where current count of valid terms will be reported. Program quits on last report index.
    report_indeces = [10**k for k in range(3, 6)] + [566000]
    report = dict()
    valid_terms = 0  # As determined by the statement of problem 57

    start_index = 1
    start_n, start_d = 3, 2

    while True:
        split_timer()

        # Variables for gap testing
        new_gaps = []
        last_gap = 0
        last_failure = None

        # Test for next failure and then begin cycle testing
        for i, (n, d) in enumerate(expand_terms(start_n, start_d), start_index):
            if i == 1:
                print(f"Starting cycle detection...")
                gap_cycle = accumulate(cycle(gap_map[0]))
            elif i in gap_map:
                print(f"Updated cycle at {i}...")
                gap_cycle = accumulate(chain([i], cycle(gap_map[i])))

            if i in report_indeces:
                print(f"Valid terms after {i} iterations: {valid_terms}")
                report[i] = valid_terms
                if i == report_indeces[-1]:
                    "Ending at limit"
                    return report

            if num_digits(n) > num_digits(d):
                if last_failure:
                    # Determining next gap cycle
                    new_gaps.append(i - last_gap)

                    if len(new_gaps) > 200:
                        next_cycle = find_cycle(new_gaps)
                        if next_cycle:
                            if next_cycle == -1:
                                print(f"Cycle detection error:\n{new_gaps}")
                                return report
                            else:
                                gap_map[last_failure] = next_cycle
                                start_index = last_failure
                                print(f"New cycle: {next_cycle}")
                                break

                else:
                    next_gap_accum = next(gap_cycle)
                    if not i == next_gap_accum:
                        print(f"FAILED {i}: expected {next_gap_accum}")
                        last_failure = i
                        start_n, start_d = n, d
                    else:
                        valid_terms += 1

                last_gap = i


def alternate_cycles():
    """Test alternating cycle pattern without generating new cycles while iterating over :expand_terms:."""
    # NOTE: Program will crash around 567000 iterations, as the fractions terms have over 217034 digits.

    # Indeces where current count of valid terms will be reported. Program quits on last report index.
    report_indeces = [10**k for k in range(3, 7)] + [567000]
    valid_terms = 0  # As determined by the statement of problem 57

    # Tracking cycle swaps after the initial cycle fails
    alternating_cycle_ids = (3229, 7947)
    cycle_id_pointer = 0
    swap_points = []

    print(f"Starting cycle/expansion comparison...")
    gap_cycle = accumulate(cycle(gap_map[0]))

    while True:
        # Test for next failure and then alternate cycles
        for i, (n, d) in enumerate(expand_terms(), 1):
            if i in report_indeces:
                print(f"\tValid terms after {i} iterations: {valid_terms}")
                print(f"\tFraction scale: {num_digits(n)} digits in numerator")
                if i == report_indeces[-1]:
                    "Ending at limit"
                    return swap_points

            if num_digits(n) > num_digits(d):
                next_gap_accum = next(gap_cycle)
                valid_terms += 1
                if not i == next_gap_accum:
                    print(f"Switching cycle at {i} (cycle_id={alternating_cycle_ids[cycle_id_pointer]})")
                    gap_cycle = accumulate(chain([i], cycle(gap_map[alternating_cycle_ids[cycle_id_pointer]])))
                    cycle_id_pointer = 0 if cycle_id_pointer else 1
                    swap_points.append(i)

                    assert i == next(gap_cycle), f"FAILED {i}: Cycles out of sync."


# term_report = detect_cycles()

# print("\nAll valid terms found during cycle detection:")
# pp(term_report)
# print("\nCycles detected:")
# pp(gap_map)

swap_points = alternate_cycles()
print("\nAll cycle swap points:")
print(swap_points, "\n")

last = None
spaces = []
for i in sorted(swap_points):
    if last:
        spaces.append(i - last)
    last = i
print("\nSpacing between swap points:")
print(spaces, "\n")

elapsed()