def divide_numbers(a, b):
    result = a / b
    return result

def add_numbers(a, b):
    result = a * b
    return result

def subtract_numbers(a, b):
    result = a - b
    return result

def add_one(lst):
    for i in range(len(lst)):
        lst[i] += 1
    print("The list is now:", lst)
if __name__ == "__main__":
    nums = []

    num1 = divide_numbers(16, 2)
    nums.append(num1)

    num2 = add_numbers(10, 3)
    nums.append(num2)
    num3 = subtract_numbers(num1, 4)
    nums.append(num3)
    add_one(nums)
    print("The final result is 8 + 13 + 4 = ", num1 + num2 + num3)