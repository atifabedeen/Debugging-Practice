def create_2d_list():
    arr = [[] * 3] * 3
    for i in range(3):
        for j in range(3):
            arr[i][j] = i * j
    assert arr[2][2] == 4


if __name__ == "__main__":
    create_2d_list()
