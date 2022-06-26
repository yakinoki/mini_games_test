import random
from math import factorial

def solve_problem():
    a = random.randint(1,4)
    b = random.randint(2,3)
    x = int((factorial(a+b-1))/(factorial(b)*factorial(a-1)))
    print(str(a)+"個のものから"+str(b)+"個のものを重複を許して選ぶ方法は何通りありますか。")
    
    ans = int(input())
    if ans == x:
        print("正解です。")
    else:
        print("不正解です。正解は"+str(x)+"です。")

solve_problem()

    