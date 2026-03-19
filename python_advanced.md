# Python 进阶知识梳理

## 1. 面向对象编程（OOP）
- 类、对象、继承、多态、封装、魔术方法、属性装饰器
```python
class Animal:
    def speak(self):
        print('Animal speaks')
class Dog(Animal):
    def speak(self):
        print('Dog barks')
d = Dog()
d.speak()
```

## 2. 函数进阶
- 可变参数、关键字参数、函数注解、递归、函数作为对象、闭包、装饰器
```python
def func(*args, **kwargs):
    print(args, kwargs)
func(1, 2, a=3)
```

## 3. 迭代器与生成器
- 自定义迭代器、生成器表达式、yield、next
```python
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
```

## 4. 文件与IO
- 文件读写、二进制文件、CSV、JSON、pickle、with语句
```python
import json
with open('data.json', 'w') as f:
    json.dump({'a': 1}, f)
with open('data.json', 'r') as f:
    print(json.load(f))
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
