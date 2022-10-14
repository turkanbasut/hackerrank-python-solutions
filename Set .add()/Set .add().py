N = int(input())
my_list = []
for i in range(0, N):
    country = str(input())
    my_list.append(country)
my_list = list(set(my_list))
print(len(my_list))
