import pytest
from main import isBalanced

FIXTURE = [
    ('(((([{}]))))', 'Сбалансированно'),
    ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
    ('{{[()]}}', 'Сбалансированно'),
    ('}{}', 'Несбалансированно'),
    ('{{[(])]}}', 'Несбалансированно'),
    ('[[{())}]', 'Несбалансированно'),
    ('((1))', 'Неверная последовательность')
]

@pytest.mark.parametrize('string, etalon', FIXTURE)
def test_balance(string:str, etalon:str):
    '''Checks if isBalanced function works properly'''
    
    result = isBalanced(string)
    assert result == etalon