# Find common characters between two strings
def commonCharacters(s1, s2):
    s1unique = set(s1)
    s2unique = set(s2)

    # print(s1unique)
    # print(s2unique)

    result = s1unique & s2unique

    print(result)



s1 = input("Enter First String\n")
s2 = input("Enter Second String\n")
commonCharacters(s1,s2)