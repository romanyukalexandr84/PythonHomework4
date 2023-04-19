n = int(input("Введите количество элементов первого списка: "))
m = int(input("Введите количество элементов второго списка: "))

lst1 = list()
lst2 = list()

lst1 = [int(input(f"Введите {i}-й элемент первого списка: ")) for i in range (n)]
lst2 = [int(input(f"Введите {i}-й элемент второго списка: ")) for i in range (m)]

SortedSet = sorted(set(lst1).intersection(set(lst2)))
print ("Числа, которые встречаются в обоих наборах, в порядке возрастания:", SortedSet)