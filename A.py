input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = int(input.readline())
b = input.readline()
for i in range(a):
    if b.count(b[i]) > 1:
        print(b[i], file=output)
        break
input.close()
output.close()