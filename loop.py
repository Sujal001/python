
mylist = []
positive_no = []
l = int(input('Enter range of list:'))
for i in range(0, l):
    a = int(input('Enter number:'))
    mylist.append(a)
print('The list:', mylist)
for j in mylist:
    if j >= 0:
        positive_no.append(j)
print("The list of positive integers is:", positive_no)
