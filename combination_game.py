import random
import time
import datetime
from math import factorial

#計算に掛かった時間を計る。
def time_log(func):
    def time_record():
        start = datetime.datetime.today()
        print("---start:" + func.__name__)
        result = func()
        end = datetime.datetime.today()
        delta = end - start
        print(delta, "秒であなたはこの問題に解答しました。")
    return time_record

@time_log
def solve_problem() -> None:
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

    