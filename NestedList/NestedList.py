if __name__ == '__main__':
    new_list = []
    score_list = []
    name_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_list.append([name, score])
        score_list.append(score)
    score_list = list(set(score_list))
    score_list.sort()
    for item in range(len(new_list)):
        if score_list[1] == new_list[item][1]:
            name_list.append(new_list[item][0])
    name_list.sort()
    for item in name_list:
        print(item)
