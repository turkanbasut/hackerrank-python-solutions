import re

if __name__ == '__main__':
    s = input()

    has_lower = bool(re.search(r"[a-z]", s))
    has_upper = bool(re.search(r"[A-Z]", s))
    has_digit = bool(re.search(r"[0-9]", s))

    print(has_lower or has_upper or has_digit)
    print(has_lower or has_upper)
    print(has_digit)
    print(has_lower)
    print(has_upper)
