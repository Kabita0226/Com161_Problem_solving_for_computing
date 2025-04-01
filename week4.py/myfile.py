class A:
    def __init__(self):
        self.val = 1

    def update(self):
        self.val *= 2

class B(A):
    def __init__(self):
        super().__init__()
        self.val += 1

    def update(self):
        self.val += 3
        super().update()

a = A()
b = B()

a.update()
b.update()

print(a.val, b.val)
