lst = [1, 2, 3]
lst1 = [1, 2, 3]
lst1 = lst
#dùng id để hiển thị so sánh
print(id(lst))
print(id(lst1))
print(lst1 is lst)