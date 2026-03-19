# Python 进阶实战案例

# 1. 面向对象：银行账户类
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print('余额不足')
        else:
            self.balance -= amount
    def __str__(self):
        return f'{self.owner}账户余额：{self.balance}'

acc = BankAccount('Tom', 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)

# 2. 装饰器：计时器
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'耗时：{end-start:.4f}秒')
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(1)
    return 'done'

print(slow_func())

# 3. 生成器：斐波那契数列

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))

# 4. 并发：多线程下载模拟
import threading

def download(name):
    print(f'{name} 开始下载')
    time.sleep(1)
    print(f'{name} 下载完成')

threads = [threading.Thread(target=download, args=(f'文件{i}',)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# 5. Web开发：FastAPI 简单接口
from fastapi import FastAPI
app = FastAPI()

@app.get('/hello')
def hello():
    return {'msg': 'Hello, FastAPI'}

# 6. 数据分析：pandas处理CSV
import pandas as pd

data = pd.DataFrame({'name': ['Tom', 'Jerry'], 'score': [90, 85]})
data.to_csv('score.csv', index=False)
data2 = pd.read_csv('score.csv')
print(data2)

# 7. 深度学习：PyTorch张量运算
import torch
x = torch.randn(3, 2)
y = torch.ones(3, 2)
print('x:', x)
print('y:', y)
print('x+y:', x+y)

# 8. 自动化：批量重命名文件
import os
for i, fname in enumerate(os.listdir('.')):
    if fname.endswith('.txt'):
        os.rename(fname, f'file_{i}.txt')

# 更多案例可随时扩展，如需某一领域实战案例请指定。
