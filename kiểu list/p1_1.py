#mỗi giá trị có 1 biến riêng biệt
#giới hạn bởi cặp ngoặc vuông []
#các phần tử của list cách nhau bởi dấu phẩy ,
#list có khả năng chứa mọi giá trị đối tượng của python và bao gồm chính nó
#i là tên biến
a = [[i,i*5,i*2] for i in range(1,4)]
#print(a)

#contructor list
b = list('h1234')
#print(b)

# kiểm tra trong kiểu a có chữ số hay không
a = [1,2,'a','b','c',[3,4]] # 1 kiểu dữ liệu mới cộng được
b = 2 in a
print(b)