def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)
assert avg([2]) == 2
assert avg([1,2,3]) == 2