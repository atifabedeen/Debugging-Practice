def create_2d_list():
    arr = [[0] * 3] * 3
    arr[0][0] = 1
    arr[1][0] = 2
    arr[2][0] = 3
    assert arr[0][0] == 1
    assert arr[1][0] == 2
    assert arr[2][0] == 3

if __name__ == "__main__":
    create_2d_list()
