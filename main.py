class Stack:
    
    def __init__(self) -> None:
        self.data = []
        
    def isEmpty(self):
        '''Checks if stack is empty.'''
        return self.data == []
    
    def push(self, element:any):
        '''Adds an element on top of the stack.'''
        self.data.insert(0, element)
        
    def pop(self):
        '''Returns element from top of the stack. The element is deleted from it.'''
        return self.data.pop(0)
    
    def peek(self):
        '''Returns element from top of the stack. The element remains in the stack.'''
        return self.data[0]
    
    def size(self):
        '''Returns size of the stack.'''
        return len(self.data)


def isBalanced(symbols:str):
    '''Checks if bracket sequence is balanced (each opening bracket meets corresponding closing one without interseption).
    Each symbol in input string is checked if its opening or closing bracket (if it's none if it, returns invalid input error).
    Then the symbol is put in stack (if it is opening bracket) or poped out of it. 
    When popped, if the first element of the stack combines a proper open-closing brackets, the cycle continues.
    If not, sequence is not balanced. Also if there's nothing to pop (while string is not over) or stack is not empty after end of the cycle, sequence is not balanced too.'''
    
    sequence = Stack()
    
    for symbol in symbols:
        
        if symbol in '({[':
            sequence.push(symbol)
            
        elif symbol in ')}]':
            try:
                if sequence.pop() + symbol not in (r'()', r'[]', r'{}'):
                    break
            except IndexError:
                return 'Несбалансированно'
        
        else:
            return 'Неверная последовательность'
    
    if sequence.isEmpty():
        return 'Сбалансированно'
    
    return 'Несбалансированно'