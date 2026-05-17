file = open('test.txt')

# print(file.read(7))

# print(file.readline())
# print(file.readline())
# print(file.readline())

line = file.readline()
while line != "":
    print(line)
    line=file.readline()

# print(file.readlines())

# for line in file.readlines():
#     print(line)



file.close()