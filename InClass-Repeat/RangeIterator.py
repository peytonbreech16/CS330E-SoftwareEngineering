class Range_Iterator():
    def __init__(self,s,a):
        self.s = s
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):
        if self.s == self.a:
            raise StopIteration()
        v = self.s
        self.s += 1
        return v

    def range_iterator_while(s,a):
        while s != a:
            yield s
            s += 1

    