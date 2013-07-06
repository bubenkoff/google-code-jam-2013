"""Solution file for A."""
import sys
import contextlib


def sort_counter(input):
    """Solve the task and return required output."""
    num_test_cases = num_tests = operation_count = current_test = current_test_case = 0
    previous_line = None
    for line_no, line in enumerate(input):
        line = line.strip()
        if not line:
            # empty line
            continue
        if line.isdigit():
            if num_test_cases is 0:
                num_test_cases = int(line)
            else:
                num_tests = int(line)
                current_test = 0
                operation_count = 0
                previous_line = None
                current_test_case += 1
        elif current_test_case <= num_test_cases:
            if previous_line is not None and line < previous_line:
                operation_count += 1
            else:
                previous_line = line
            current_test += 1
            if current_test == num_tests:
                yield 'Case #{0}: {1}'.format(current_test_case, operation_count)


if __name__ == "__main__":
    with contextlib.closing(open(sys.argv[1])) as input:
        with contextlib.closing(open(sys.argv[2], 'w')) as output:
            for line_no, line in enumerate(sort_counter(input.readlines())):
                output.write(('\n' if line_no else '') + line)
