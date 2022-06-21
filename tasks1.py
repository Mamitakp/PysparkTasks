#python pogram to demonstrate global and local variable

x='hello' #global var 
def my_fun():
    global x #global var 
    x='world'
    y='happy'#local var 
    print(y)
my_fun()
print(x)

#pogram to demonstrate nested functions 
def my_fun(str):
    for i in str:
        print(i)
    def fun():
        print(str)
    fun()
my_fun('abcd')

#pogram to demonsrate data types
list1=['a','b','c','d']
new_list=list(list1)

for i in new_list:
    print(i)
#tuples
tup=('1',2,'c')
for i in tup:
    print(tup)
i=0    
while i<len(list1):
    print(list1[i])
    i+=1
#keywords and operators
x,y=4,5
def func(n):
    x=x*n
    y=y+n
    print(x,y)
    if x<y:
        return 'True'
    else:
        return 'False'
func(3)
