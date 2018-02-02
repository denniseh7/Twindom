#Dennis Hsu
#Twindom Application Code Review
#February 1st, 2018

#hello
set_1=set([1,2,3])
vec_1=[3,2,1]

#does not include negative integer testing
def yyy(x):
    l=len(x)
    for i in range(0,l):
        set_1=set([])
        for j in range (0,l):
            if i==j:
                continue
            if (x[j]*x[j]) in set_1:
                print(set_1)
                return True
            else:
                set_1.add(x[i]*x[i]-x[j]*x[j])
    print(set_1)
    return False

print(yyy([4,5,3]))


print("Hello World")