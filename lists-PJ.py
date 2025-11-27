def sort(list):
    return sorted(list)
def reverse(list):
    return list[::-1]
def list_in_str(list):
    return ", ".join(list)

amount = int(input("кількість елементів в списку: "))
lists = [input("el: ") for i in range(amount)]

print("____list-convertor____")
print("1: сортуввання")
print("2: задом наперед")
print("3: об'єдняння")

user = int(input("Введіть ваш вибір: "))

if user == 1:
    print(sort(lists))
elif user == 2:
    print(reverse(lists))
elif user == 3:
    print(list_in_str(lists))
