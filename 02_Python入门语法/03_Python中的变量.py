"""
演示Python中变量的相关操作
"""

# 定义一个变量, 用来记录钱包余额
money = 50

# 通过print语句, 输出变量记录的内容
print("钱包还有: ", money)

# 买了一个冰淇淋, 花费了10元
money = money - 10
print("买冰淇淋花了10元，还剩余:", money, "元")

# 假设, 每隔一小时，输出一下钱包的余额
print("现在是下午1点，钱包余额剩余: ", money)
print("现在是下午2点，钱包余额剩余: ", money)
print("现在是下午3点，钱包余额剩余: ", money)
print("现在是下午4点，钱包余额剩余: ", money)


money2 = 50
print("当前钱包余额:", 50, "元")
money2 = money2 - 10
print("购买了冰淇淋, 花费:", 10, "元")
money2 = money2 - 10
print("购买了可乐, 花费:", 10, "元")
print("最终, 钱包剩余:", money2, "元")
