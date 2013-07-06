# tests for the project
import pytest

from code_a import sort_counter


@pytest.mark.parametrize(
    ['input', 'expected'],
    [(
"""
3
2
Oksana Baiul
Michelle Kwan
3
Elvis Stojko
Evgeni Plushenko
Kristi Yamaguchi
10
Alibel Alegre
Alexei Beletski
Gloria Agogliati
Julia Abolina
Maria Balaba
Nadine Ahmed
Valentina Anselmi
Ilia Averbukh
Rinata Araslanova
Daniil Barantsev
""",
"""
Case #1: 1
Case #2: 0
Case #3: 4
""")])
def test_sort_counter(input, expected):
    """Test sort_counter function."""
    assert list(sort_counter(input.split('\n'))) == expected.strip().split('\n')
