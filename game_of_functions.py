elem=int(input('enter the number of elements :'))
lst=[]
for i in range(elem):
    elem1=int(input('enter the element :'))
    lst.append(elem1)
print('list of elements=',lst)
def summation(lst):
    res=0
    for i in lst:
        res+=i
    return res
print('the sum of the elements=',summation(lst))
