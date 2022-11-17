num = [2, 5, 5, 9 ,1]
#num[2] = 3
#num.append(7)
#num.sort() #reverse = True
#num.insert(2, 0)
#num.pop() #Elimina o ultimo item da lista
#num.remove(5)
num.sort(reverse= True)
print(num)

a = [2, 3, 4, 7]
b = a[:] # criar uma copia da lista
b[2] = 8
print(a)
print(b)