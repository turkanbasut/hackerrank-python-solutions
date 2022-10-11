if __name__ == '__main__':
    N = int(input())
    my_list = []
    for index in range(0, N):
        a = input()
        test_list = a.split(" ")
        for item in range(0, len(test_list)):
            if test_list[item] == "insert":
                my_list.insert(int(test_list[item + 1]), int(test_list[item + 2]))
            if test_list[item] == "print":
                print(my_list)
            if test_list[item] == "sort":
                my_list.sort()
            if test_list[item] == "pop":
                my_list.pop()
            if test_list[item] == "reverse":
                my_list.reverse()
            if test_list[item] == "append":
                my_list.append(int(test_list[item + 1]))
            if test_list[item] == "remove":
                my_list.remove(int(test_list[item + 1]))
