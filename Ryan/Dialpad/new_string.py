def insert_ind(line, word, ind):
    res = line[:ind] + " " + word + line[ind:]
    print(res)


def insert_before(line, before, word):
    """
    Character index
    :param line:
    :param before:
    :param word:
    :return:
    """
    index = line.find(before)
    output_line = line[:index] + word + " " + line[index:]
    print(output_line)


def insert_split(line, word, ind):
    """
    split
    :param line:
    :param word:
    :param ind:
    :return:
    """
    arr = line.split()
    arr.insert(ind, word)
    print(' '.join(arr))


def insert_split_2(line, word, ind):
    arr = line.split(" ", ind)
    arr.insert(ind, word)
    res = ' '.join(arr)
    print(res)


#
# def insert_ind_or_str(line, word, at):
#     if isinstance(at, int):
#         return


def str_insert_by_str(from_me, into_me, at):
    """
    replace
    :param from_me:
    :param into_me:
    :param at:
    :return:
    """
    s = into_me.replace(at, at + " " + from_me, 1)
    return s


# before some str or at some index
def insert_str(line, word, at):
    if isinstance(at, str):
        index = line.find(at) - 1
    else:
        index = at

    return line[:index] + " " + word + line[index:]

def remove_str(line, word):
    length = len(word)
    while line.find(word) != -1:
        index = line.find(word)
        line = line[:index-1] + line[index+length:]
    return line


with open(“hello.txt”, “w”) as f:
    f.write(“Hello World”)

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using deepcopy to deep copy
li2 = copy.deepcopy(li1)


with open(“hello.txt”) as f:
    data = f.readlines()

def main():
    # insert_ind("a book", "red", 1)

    line = 'Kong Panda is good Panda'
    res=remove_str(line,"Panda")
    print(res)
    # insert_before(line, "Panda", "Fu")
    #
    # insert_split(line, "Fu", 1)
    # insert_split_2(line, "Fu", 1)

    # res=str_insert_by_str("Fu", line, "Kong")
    # res = insert_str(line, "Fu", "Panda")
    # print(res)
    #
    # res = insert_str(line, "Fu", 4)
    #
    # print(res)
    #
    # print(line.find("dd"))


main()
