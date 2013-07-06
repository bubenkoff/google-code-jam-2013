"""Solution file for B."""
import sys
import contextlib


def angle_calc(input):
    """Solve the task and return required output."""
    num_test_cases = num_tests = current_test = current_test_case = 0
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
                current_test_case += 1
        elif current_test_case <= num_test_cases:
            v, d = map(int, line.split())
            angle =
            current_test += 1
            if current_test == num_tests:
                yield 'Case #{0}: {1}'.format(current_test_case, angle)


if __name__ == "__main__":
    with contextlib.closing(open(sys.argv[1])) as input:
        with contextlib.closing(open(sys.argv[2], 'w')) as output:
            for line_no, line in enumerate(angle_calc(input.readlines())):
                output.write(('\n' if line_no else '') + line)
