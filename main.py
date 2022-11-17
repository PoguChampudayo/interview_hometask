class Stack:
    
    def __init__(self) -> None:
        self.data = []
        
    def isEmpty(self):
        return self.data == []
    
    def push(self, element):
        self.data.insert(0, element)
        
    def pop(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]
    
    def size(self):
        return len(self.data)

def isBalanced(symbols:str):
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
            break
    if sequence.isEmpty():
        return 'Сбалансированно'
    return 'Несбалансированно'
