import pytest
from main import isBalanced

FIXTURE = [
    (r'(((([{}]))))', 'Сбалансированно'),
    (r'[([])((([[[]]])))]{()}', 'Сбалансированно'),
    (r'{{[()]}}', 'Сбалансированно'),
    (r'}{}', 'Несбалансированно'),
    (r'{{[(])]}}', 'Несбалансированно'),
    (r'[[{())}]', 'Несбалансированно') 
]

@pytest.mark.parametrize('string, etalon', FIXTURE)
def test_balance(string, etalon):
    result = isBalanced(string)
    assert result == etalon