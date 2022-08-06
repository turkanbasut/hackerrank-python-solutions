# Task
# The provided code stub read in a dictionary containing key/value pairs of name:[Marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
#
# Example
#
# marks key: value pairs are
# ‘alpha’:[20, 30, 40]
# ‘beta’:[30, 50, 70]
# query_name = ‘beta’
#
# The query_name is ‘beta’. beta’s average score is (30 + 50 + 70)/3 = 50.0.
#
# Input Format
# The first line contains the integer n, the number of students’s records.
# The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name , the name of a student to query.
#

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        x = ((float(student_marks[query_name][0]) + float(student_marks[query_name][1]) + float(
            student_marks[query_name][2])) / 3)

    print('%.2f' % x)
