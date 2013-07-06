# tests for the project
import pytest

from code_b import angle_calc


@pytest.mark.parametrize(
    ['input', 'expected'],
    [(
"""
3
98 980
98 490
299 1234
""",
"""
Case #1: 45.0000000
Case #2: 15.0000000
Case #3: 3.8870928
""")])
def test_angle_calc(input, expected):
    """Test angle_calc."""
    assert list(angle_calc(input.split('\n'))) == expected.strip().split('\n')
