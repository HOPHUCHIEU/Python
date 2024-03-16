#kiểu intger
a = 1
print(a)
print(type(a))

#kiểu float
b= 1.12345678910112131415
print(b)
print(type(b))

#lấy toàn bộ nội dung của thư viện decimal
#từ thư viện decimal -> import mọi thứ(*)
from decimal import*

#lấy tối đa 30 chữ số nguyên và phần số thập phân decimal
getcontext().prec = 30

f = 10/3
print(f)
print(type(f))


d = Decimal(10)/Decimal(3)
print(d)
print(type(d))

#phân số. tạo phân số 

