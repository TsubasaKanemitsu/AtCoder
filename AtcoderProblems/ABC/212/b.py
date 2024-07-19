numbers = list(input())

# 全て同じ場合
if len(set(numbers)) == 1:
    print("Weak")
    exit()

yes = 0
for i in range(len(numbers) - 1):
    if int(numbers[i]) == 9 and int(numbers[i + 1]) == 0:
        yes += 1
    if int(numbers[i]) + 1 == int(numbers[i + 1]):
        yes += 1

if yes == 3:
    print("Weak")
else:
    print("Strong")

