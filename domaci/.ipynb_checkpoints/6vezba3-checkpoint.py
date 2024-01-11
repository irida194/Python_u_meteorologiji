l1=[]
for i in range(101):
    l1.append(str(i))

s1="\n".join(l1)

lista=s1.split("\n")
print(lista)
lista=[int(x) for x in lista]
print(lista)
print(f"Suma je {sum(lista)}")