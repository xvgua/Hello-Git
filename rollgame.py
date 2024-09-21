# !/user/bin/python3
import random

def roll():
    return random.randint(1,6)+random.randint(1,6)

def game(seed):
    random.seed(seed)
    print(f"输入一个无符号整数作为随机数种子={seed}")

    result=roll()
    print(f"骰子抛投结果：{result}")

    if result==7 or result==11:
        return"胜利"
    elif result==2 or result==3 or result==12:
        return"负"
    
    nextpoint=result
    print(f"你当前点数是{nextpoint}")

    while True:
      result=roll()
      print(f"骰子抛投结果：{result}")
      if result == nextpoint:
        return("胜利")
      elif result == 7:
        return("负")
    
seed = int(input("请输入一个无符号整数作为随机数的种子: "))
result = game(seed)
print(f"游戏结束，结果是: {result}")