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