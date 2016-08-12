def str_equ(num):
    str_num = str(num)
    str_rev = str_num[-1::-1]
    return str_num == str_rev
def str_equ1(num):
    str_num = str(num)
    str_len = len(str_num)//2
    str_rev = str_num[str_len:-1:-1]
    return str_num[:str_len] == str_rev
def test1():
    L=list(filter(str_equ,range( 1,1000000)))
    print(L)
def test2():
    L=list(filter(str_equ1,range(1,1000000)))
    print(L)
    
import cProfile
print(cProfile.run('test1()'))
print(cProfile.run('test2()'))