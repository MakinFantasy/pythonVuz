file = open('file2.txt')


text = file.readlines()

nums = []
for line in text:
    el = line.split(' ')
    for i in el:
        nums.append(int(i))
print(nums)
