class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass(name={self.name})'

    def __add__(self, other):
        print(f'You called + on {self.name} and {other.name}')
        return MyClass(self.name + other.name)

    def __iadd__(self, other):
        self.name += other.name
        return self


c1 = MyClass('instance 1')
c2 = MyClass(' instance 2')

result = c1 + c2
print(result)

c1 += c2
print(c1)
