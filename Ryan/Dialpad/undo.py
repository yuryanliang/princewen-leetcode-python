from copy import deepcopy

class UndoList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.old = []

    def append(self, item):
        self.old = deepcopy(self[:])
        super().append(item)

    def extend(self, items):
        self.old = deepcopy(self[:])
        super().extend(items)

    def undo(self):
        temp = deepcopy(self[:])
        self[:] = self.old
        self.old = temp


a = UndoList([1, 2, 3])
print(a)

a.append(4)
print(a)
a.undo()
print(a)
a.undo()
print(a)

a.extend([5, 6])
print(a)
a.undo()
print(a)