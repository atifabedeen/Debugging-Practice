"""
For this task, foo should append the number to an empty list and return the list.
"""
def foo(num: int, lst=[]):
    lst.append(num)
    return lst

if __name__ == "__main__":
    lst = foo(1)
    assert len(lst) == 1
    assert lst[0] == 1

    lst = foo(2)
    assert len(lst) == 1
    assert lst[0] == 2

