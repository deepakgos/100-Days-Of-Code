person = 100

a = [0]*person

for i in range(person):
    a[i] = i + 1

pos = 0

while (len(a)>1):
    pos += 1

    pos %=len(a)

    del a[pos]

print(a[pos])