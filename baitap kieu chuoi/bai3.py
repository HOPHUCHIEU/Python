#Viết chương trình Python để đảo ngược một xâu ký tự.
def daonguoc(xau):
	a = xau[::-1]# đảo ngược kí tự 
	return a 
b = "arodnap"
a = daonguoc(b)
print (f"xâu kí tự đảo ngược của '{b}' là: {a}")