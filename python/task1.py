"""
For this task, you need to create a 2D list.
The 2D list should have 3 rows and 3 columns.
The 2D list should be initialized with 0.
The list should look like this:
1 0 0
2 0 0
3 0 0
"""


def create_2d_list():
    lst = [[0] * 3] * 3
    lst[0][0] = 1
    lst[1][0] = 2
    lst[2][0] = 3
    assert lst[0][0] == 1
    assert lst[1][0] == 2
    assert lst[2][0] == 3


if __name__ == "__main__":
    create_2d_list()
