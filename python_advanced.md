# Python 进阶知识梳理

## 1. 面向对象编程（OOP）
- 类：用 class 关键字定义，描述一类事物的属性和行为。
- 对象：类的实例。
- 继承：子类继承父类的属性和方法。
- 多态：不同子类可以有不同实现。
- 封装：通过方法和属性隐藏内部实现。
- 魔术方法：如 __init__、__str__、__repr__、__add__ 等特殊方法。
- 属性装饰器：@property 用于将方法变为属性。
```python
class Animal:
    def __init__(self, name):  # 构造方法
        self.name = name
    def speak(self):
        print(f'{self.name} makes a sound')

class Dog(Animal):  # 继承
    def speak(self):  # 重写父类方法
        print(f'{self.name} barks')

d = Dog('Buddy')
d.speak()  # 输出：Buddy barks

# 属性装饰器
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('年龄不能为负数')
        self._age = value
p = Person(18)
p.age = 20
print(p.age)
```

## 2. 函数进阶
- 可变参数：*args（元组），**kwargs（字典），接收不定数量参数。
- 函数注解：为参数和返回值添加类型提示。
- 递归：函数调用自身。
- 函数作为对象：函数可以赋值、作为参数、返回值。
- 闭包：函数内部定义函数并引用外部变量。
- 装饰器：用于扩展函数功能。
```python
def func(a, b, *args, **kwargs):
    print('a:', a, 'b:', b)
    print('args:', args)
    print('kwargs:', kwargs)
func(1, 2, 3, 4, x=5, y=6)

# 函数注解
def add(x: int, y: int) -> bool:
    return x + y
print(add(2, 3))

# 递归
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# 闭包
def outer(msg):
    def inner():
        print(msg)
    return inner
f = outer('hello')
f()

# 装饰器
def logger(func):
    def wrapper(*args, **kwargs):
        print('调用前')
        result = func(*args, **kwargs)
        print('调用后')
        return result
    return wrapper

@logger
def say_hi():
    print('hi')
say_hi()
```

## 3. 迭代器与生成器
- 迭代器：实现 __iter__ 和 __next__ 方法的对象。
- 生成器：带 yield 的函数，返回一个迭代器。
- 生成器表达式：类似列表推导式，但用 ()。
```python
# 自定义迭代器
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration
for i in Counter(3):
    print(i)

# 生成器函数
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fib(5):
    print(num)

# 生成器表达式
g = (x * x for x in range(3))
for v in g:
    print(v)
```

## 4. 文件与IO
- 文本文件读写：open、read、write、with。
- 二进制文件：以 'rb'、'wb' 模式打开。
- CSV 文件：用 csv 模块读写表格数据。
- JSON 文件：用 json 模块序列化和反序列化。
- pickle：序列化 Python 对象。
```python
# 文本文件
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('hello world')
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# JSON
import json
data = {'a': 1, 'b': 2}
with open('data.json', 'w') as f:
    json.dump(data, f)
with open('data.json', 'r') as f:
    print(json.load(f))

# CSV
import csv
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'score'])
    writer.writerow(['Tom', 90])
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# pickle
import pickle
obj = {'x': [1,2,3]}
with open('obj.pkl', 'wb') as f:
    pickle.dump(obj, f)
with open('obj.pkl', 'rb') as f:
    print(pickle.load(f))
```

## 5. 异常与断言
- 自定义异常、断言、try/except/else/finally
```python
class MyError(Exception):
    pass
try:
    raise MyError('自定义异常')
except MyError as e:
    print(e)
```

## 6. 标准库与第三方库
- os、sys、datetime、random、re、collections、itertools、functools、logging、requests、numpy、pandas、matplotlib
```python
import os, sys, datetime, random, re
from collections import Counter
import requests
r = requests.get('https://www.example.com')
print(r.status_code)
```

## 7. 多线程与多进程
- threading、multiprocessing、队列、锁、并发、异步
```python
import threading

def worker():
    print('Thread running')
t = threading.Thread(target=worker)
t.start()
t.join()
```

## 8. 网络编程
- socket、http、web框架（Flask、FastAPI）、API开发
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello Flask'
```

## 9. 数据库操作
- sqlite3、MySQL、ORM（SQLAlchemy）、MongoDB
```python
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO user(name) VALUES (?)', ('Tom',))
conn.commit()
conn.close()
```

## 10. 单元测试与调试
- unittest、pytest、assert、pdb、logging
```python
import unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1+1, 2)
if __name__ == '__main__':
    unittest.main()
```

## 11. 包与模块管理
- __init__.py、相对/绝对导入、包结构、虚拟环境、pip、conda

## 12. 类型注解与静态检查
- typing、mypy、类型提示
```python
def add(a: int, b: int) -> int:
    return a + b
```

## 13. 元编程
- eval、exec、反射、属性操作、装饰器、类装饰器
```python
code = 'print("hello")'
eval(code)
```

## 14. 内存管理与性能优化
- gc、内存分析、性能分析、timeit、cProfile、缓存
```python
import timeit
print(timeit.timeit('sum(range(1000))', number=1000))
```

## 15. 设计模式
- 设计模式是解决特定问题的通用代码结构和思想，提升代码可维护性、可复用性。
- 常见设计模式：单例、工厂、观察者、装饰器、策略、迭代器。

### 单例模式
- 保证一个类只有一个实例，常用于数据库连接、配置管理等。
```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True，始终同一个对象
```

### 工厂模式
- 用工厂函数/类根据参数创建不同类型对象，解耦对象创建。
```python
def animal_factory(kind):
    class Dog:
        def speak(self):
            return '汪汪'
    class Cat:
        def speak(self):
            return '喵喵'
    if kind == 'dog':
        return Dog()
    elif kind == 'cat':
        return Cat()
    else:
        raise ValueError('未知动物类型')

pet = animal_factory('dog')
print(pet.speak())
```

### 观察者模式
- 一对多通知，常用于事件系统。
```python
class Subject:
    def __init__(self):
        self.observers = []
    def attach(self, observer):
        self.observers.append(observer)
    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

class Observer:
    def update(self, msg):
        print('收到消息:', msg)

sub = Subject()
obs1 = Observer()
obs2 = Observer()
sub.attach(obs1)
sub.attach(obs2)
sub.notify('事件发生')
```

### 装饰器模式
- 用装饰器扩展对象功能，见前文装饰器示例。

### 策略模式
- 多种算法/行为可切换，常用于排序、支付等。
```python
class PayStrategy:
    def pay(self, amount):
        pass
class AliPay(PayStrategy):
    def pay(self, amount):
        print(f'支付宝支付{amount}元')
class WeChatPay(PayStrategy):
    def pay(self, amount):
        print(f'微信支付{amount}元')

def pay(strategy, amount):
    strategy.pay(amount)

pay(AliPay(), 100)
pay(WeChatPay(), 200)
```

### 迭代器模式
- 统一遍历集合对象。
```python
class MyList:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return iter(self.data)

for x in MyList([1,2,3]):
    print(x)
```

# 注意事项：
# - 设计模式不是强制，适合场景再用。
# - Python有些模式可用内置语法简化（如迭代器、装饰器）。
# - 设计模式提升代码结构，但过度使用会让代码复杂。
# - 推荐先理解需求，再选择合适模式。

## 16. 并发与异步
- async/await、asyncio、协程、事件循环
```python
import asyncio
async def main():
    print('async running')
asyncio.run(main())
```

## 17. Web开发进阶
- RESTful API、模板渲染、认证、路由、WebSocket

## 18. 数据分析与科学计算
- numpy、pandas、matplotlib、scipy、sklearn

## 19. 深度学习与AI
- 深度学习是机器学习的一种，主要用神经网络处理图像、文本、语音等复杂数据。
- 常用库：
  - tensorflow：Google开发，支持多平台，适合生产环境。
  - torch（PyTorch）：Facebook开发，易用、灵活，适合研究和原型开发。
  - transformers：Hugging Face开发，支持各种大语言模型（如GPT、BERT等）。

### 基本流程
1. 数据准备：加载、预处理数据。
2. 模型定义：搭建神经网络结构。
3. 损失函数与优化器：定义目标和训练方法。
4. 训练：循环迭代，更新参数。
5. 推理：用训练好的模型做预测。

### TensorFlow 示例
```python
import tensorflow as tf
import numpy as np
# 构建简单的线性回归模型
X = np.array([[1],[2],[3],[4]], dtype=np.float32)
Y = np.array([[2],[4],[6],[8]], dtype=np.float32)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])
model.compile(optimizer='sgd', loss='mse')
model.fit(X, Y, epochs=100, verbose=0)
print('预测:', model.predict([[5]]))
```

### PyTorch 示例
```python
import torch
import torch.nn as nn
X = torch.tensor([[1.],[2.],[3.],[4.]], dtype=torch.float32)
Y = torch.tensor([[2.],[4.],[6.],[8.]], dtype=torch.float32)
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1,1)
    def forward(self, x):
        return self.linear(x)
model = LinearModel()
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for epoch in range(100):
    pred = model(X)
    loss = loss_fn(pred, Y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print('预测:', model(torch.tensor([[5.]])))
```

### transformers 示例（大语言模型）
```python
from transformers import pipeline
# 加载英文文本生成模型
generator = pipeline('text-generation', model='gpt2')
result = generator('Hello, AI', max_length=20)
print(result)
```

### 常见注意事项
- 深度学习训练需要大量数据和算力，建议用GPU。
- 模型参数、超参数要合理设置，否则效果差。
- 数据预处理、归一化、分批训练很重要。
- 训练过程要监控损失、准确率，防止过拟合。
- 推理时要用训练好的模型权重。
- transformers等大模型需联网下载，注意环境和依赖。

---

如需某一库或场景详细代码、实战案例、Notebook，请指定。

## 20. 自动化与脚本
- 批量处理、定时任务、爬虫、自动化办公

---

如需某一进阶知识点详细代码示例或实战案例，请指定。
