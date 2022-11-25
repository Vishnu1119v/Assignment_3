str1=input('enter the string :')
def string_test(str1):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in str1:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", str1)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
string_test(str1)