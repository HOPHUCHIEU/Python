# lưu ý: các toán tử của tuple (giống) toán tử của chuỗi
# toán tử của list gần giống với toán tử của chuỗi
tup = (i for i in range(10) if i % 2 == 0)
a = tuple(tup)
print(a)