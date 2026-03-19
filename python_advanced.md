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
- 单例、工厂、观察者、装饰器、策略、迭代器

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
- tensorflow、torch、transformers、模型训练、推理

## 20. 自动化与脚本
- 批量处理、定时任务、爬虫、自动化办公

---

如需某一进阶知识点详细代码示例或实战案例，请指定。
