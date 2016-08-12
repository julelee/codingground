rom functools import reduce
def str2int(num_str):
    def char2int(c):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
    def mul10(x,y):
        return x*10+y
    return reduce(mul10,map(char2int,num_str))
def str2float(float_str):
    def char2int(c):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
    def mul10(x,y):
        return x*10+y
    def div10(x,y):
        return x*0.1+y
    L = float_str.split('.')
    
    return reduce(mul10,map(char2int,L[0]))+reduce(div10,map(char2int,L[1][-1::-1]))
    
    
num = str2int("12345")
print("the type of {0} is {1}".format(num,type(num)))

num = str2float("123.456")
print("the type of {0} is {1}".format(num,type(num)))