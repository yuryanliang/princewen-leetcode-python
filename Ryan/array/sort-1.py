from operator import itemgetter


def sort_key():
    string_1 = "This is a test string from Andrew"
    res_1 = sorted(string_1.split(), key=str.lower)
    res_2 = sorted(string_1.split(), key=len)
    # print(res_1)
    # print(res_2)

    list_1 = [-3, 2, 1, -1]
    res_3 = sorted(list_1, key=abs)
    print(res_3)

    def f(elem):
        return abs(elem)

    res_4 = sorted(list_1, key=f)
    print(res_4)
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'C', 12),
        ('dave', 'B', 12),
    ]
    res_tuples = sorted(student_tuples, key=lambda elem: (elem[2], elem[1]), reverse=True)
    # print(res_tuples)

    res_tuples_1 = sorted(student_tuples, key=itemgetter(2, 1), reverse=True)
    # print(res_tuples_1)


# sort_key()


def complex_sort():
    data = [('red', 1), ('blue', 2), ('red', 2), ('blue', 1)]
    # how the two records for blue retain their original order
    res_1 = sorted(data, key=itemgetter(0))
    # print(res_1)

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 11),
        ('dave', 'B', 10),
        ('ss', 'C', 11)
    ]
    # For example, to sort the student data by descending grade and then ascending age, do the age sort first and then sort again using grade
    s = sorted(student_tuples, key=itemgetter(2))
    print(s)
    res_2 = sorted(s, key=itemgetter(1), reverse=True)
    print(res_2)

    res_3 = sorted(student_tuples, key=itemgetter(1, 2))
    print(res_3)


# complex_sort()


def key_external():
    students = ['dave', 'john', 'jane']
    newgrades = {'john': 'F', 'jane': 'A', 'dave': 'C'}
    res = sorted(students, key=newgrades.__getitem__)
    print(res)
    from collections import namedtuple
    StudentFinal = namedtuple('StudentFinal', 'name grade')
    bill = StudentFinal('Bill', 90)
    patty = StudentFinal('Patty', 94)
    bart = StudentFinal('Bart', 89)
    students = [bill, patty, bart]
    res_1 = sorted(students, key=lambda x: x.grade, reverse=True)
    print(res_1)


key_external()
