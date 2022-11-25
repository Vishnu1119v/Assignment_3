str1=input('enter the string :')
def rev(str1):
    res=''
    for ch in str1:
        res=ch+res
    return res
print('The original string =',str1)
print('The reverse of the given string =',rev(str1))
