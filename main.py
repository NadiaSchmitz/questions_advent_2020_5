answers = []
groups = []
check = 0
sum = 0

with open("answers.txt", "r") as file1:
    for line in file1:
        answers.append(line)
    print(answers)

string = "".join(answers)
string = string.replace("\n\n", "0 ")
string = string.replace("\n", " ")

print(string)

groups = string.split('0')

print(groups)

for item in groups:
    item = set(item.replace(" ", ""))
    sum = sum + len(item)
    print(sum)
