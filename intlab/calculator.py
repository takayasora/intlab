def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "割る数は0にできません。"
    else:
        return num1 / num2

# 例として、各関数を使用する方法
result = add(5, 3)  # 5 + 3 を計算
print(result)  # 出力は 8

result = subtract(10, 2)  # 10 - 2 を計算
print(result)  # 出力は 8

result = multiply(6, 4)  # 6 * 4 を計算
print(result)  # 出力は 24

result = divide(8, 2)  # 8 / 2 を計算
print(result)  # 出力は 4

result = divide(6, 0)  # ゼロで割ることはできません
print(result)  # 出力は "割る数は0にできません。"

