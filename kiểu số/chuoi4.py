a = 'hiếu pandora'
# "capotalize()" viết hoa kí tự đầu tiên
b = a.capitalize()
# "upper()" tất cả các chữ đều được viết hoa
c = a.upper()
# "lower()" tất cả đều viết thường"
d = a.lower()
# "swapcase() chữ viết thường sẽ chuyển thành viết hoa, chữ viết hoa thành chữ thường"
e = a.swapcase()
# "title() viết hoa đầu tiên còn lại viết thường"
f = a.title()
# "center(width,[fillchar])" trả về chuỗi được căn giữ với chiều rộng width
ab = a.center(20, '.')
# "rjust" căn phải
ac = a.rjust(20, '.')
# "rjust" căn trái
ad = a.ljust(20, '.')
#encode(encoding='utf-8', errors='strict') encode một chuỗi mã hóa)
aa = a.encode()
#"join() cộng một danh sách vào một chuỗi"
abb = a.join(['1','2','3'])
# "replace" thay thế kí tự hoặc chuỗi trong danh sách
acc = a.replace('ồ','pandora', 2)
# "strip" cắt chữ trong dãy số đã cho đó
bb = a.rstrip('h')
# lstrip cắt trái rstrip cắt phải
print(b)
print(bb)