def sort_sorted():
    test_list = [5, 2, 1]

    # sorted won't change the original
    sorted(test_list)

    # list.sort() is in-place, (it replace the original list)
    # list.sort() is only for list
    test_list.sort()

    # sorted also accept any iterable
    test_dict = {
        5: "D",
        2: "C",
        3: "A"
    }

    a = sorted(test_dict)

    print(a == [2, 3, 5])


def interview():
    list_1 = [7, -2, 2, -2, 0]

    # abs sort , neg before pos
    res = sorted(list_1, key=lambda elem: (abs(elem), elem))
    print(res)
    # res=[0, -2, -2, 2, 7]

    # abs sort, pos before neg
    res_1 = sorted(list_1, key=lambda elem: (abs(elem), -elem))
    print(res_1)

    temp = sorted(list_1)
    res_2 = sorted(temp, key=abs)
    print(res_2)


def key_func():
    string_1 = "This is a test string from Andrew"
    res = sorted(string_1.split(), key=str.lower)


# sort_sorted()


def sort_key():
    string_1 = "This is a test string from Andrew"
    res_1 = sorted(string_1.split(), key=str.lower)
    res_2 = sorted(string_1.split(), key=len)
    # print(res_1)
    # print(res_2)

    list_1 = [-3, 2, 1, -1]
    res_3 = sorted(list_1, key=abs)
    # print(res_3)

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'C', 12),
        ('dave', 'B', 12),
    ]
    res_tuples = sorted(student_tuples, key=lambda elem: (elem[2], elem[1]), reverse=True)
    print(res_tuples)


if __name__ == "__main__":
    interview()

# sort_key()
