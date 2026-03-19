# Python 基础知识梳理

## 1. 变量与数据类型
- 数字：int（整数）、float（浮点数）、complex（复数）
```python
x = 10      # int
y = 3.14   # float
z = 1 + 2j # complex
```
- 字符串：str
```python
s = 'hello world'
print(s.upper())
```
- 布尔：bool（True/False）
```python
flag = True
print(flag)
```
- 列表：list
```python
lst = [1, 2, 3]
lst.append(4)
print(lst)
```
- 元组：tuple
```python
tpl = (1, 2, 3)
print(tpl[0])
```
- 字典：dict
```python
d = {'name': 'Tom', 'age': 20}
print(d['name'])
```
- 集合：set
```python
s = set([1, 2, 2, 3])
print(s)
```

## 2. 运算符
- 算术：+ - * / // % **
```python
print(2 + 3, 2 * 3, 5 // 2, 5 % 2, 2 ** 3)
```
- 比较：== != > < >= <=
```python
print(2 == 3, 2 != 3, 2 > 1)
```
- 逻辑：and or not
```python
print(True and False, True or False, not True)
```
- 赋值：= += -= *= /=
```python
x = 1
x += 2
print(x)
```
- 成员：in, not in
```python
print(2 in [1,2,3])
```
- 身份：is, is not
```python
x = [1,2]
y = x
print(x is y)
```

## 3. 条件语句
```python
if x > 0:
    print('正数')
elif x == 0:
    print('零')
else:
    print('负数')
```

## 4. 循环语句
- for 循环：遍历序列
```python
for i in [1,2,3]:
    print(i)
```
- while 循环：条件成立时循环
```python
n = 0
while n < 3:
    print(n)
    n += 1
```
- break/continue：跳出/跳过本次循环
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

## 5. 函数
- 定义：def 函数名(参数):
```python
def add(a, b):
    return a + b
print(add(2,3))
```
- 返回值：return
- 匿名函数：lambda
```python
f = lambda x: x * 2
print(f(3))
```

## 6. 列表、字典、元组、集合操作
- 增删查改
```python
lst = [1,2,3]
lst.append(4)
lst.remove(2)
print(lst)
```
- 切片
```python
print(lst[1:3])
```
- 遍历
```python
for item in lst:
    print(item)
```

## 7. 字符串操作
- 拼接、分割、查找、替换、格式化
```python
s = 'hello world'
print(s.split())
print(s.find('world'))
print(s.replace('world', 'python'))
print('name: {}, age: {}'.format('Tom', 20))
```

## 8. 文件操作
- 打开：open()
- 读写：read()/write()
- with 语句自动关闭
```python
with open('test.txt', 'w') as f:
    f.write('hello')
with open('test.txt', 'r') as f:
    print(f.read())
```

## 9. 异常处理
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print('除零错误:', e)
finally:
    print('结束')
```

## 10. 模块与包
- import、from ... import ...、as
- 自定义模块
```python
import math
print(math.sqrt(4))
from math import pi
print(pi)
```

## 11. 类与对象
- class 定义
- 属性、方法
- 继承、封装、多态
```python
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello,', self.name)
p = Person('Tom')
p.greet()
```

## 12. 常用内置函数
- print, len, range, type, input, ord, chr, sum, max, min, sorted
```python
print(len([1,2,3]))
print(range(3))
print(type(3.14))
print(ord('A'), chr(65))
print(sum([1,2,3]), max([1,2,3]), min([1,2,3]), sorted([3,1,2]))
```

## 13. 列表推导式、生成器、迭代器
- 列表推导式：[x for x in range(10)]
```python
lst = [x * x for x in range(5)]
print(lst)
```
- 生成器：yield
```python
def gen():
    for i in range(3):
        yield i
g = gen()
print(next(g))
```
- 迭代器：iter, next
```python
it = iter([1,2,3])
print(next(it))
```

## 14. 装饰器、闭包
- 装饰器：@func
```python
def log(func):
    def wrapper(*args, **kwargs):
        print('调用前')
        result = func(*args, **kwargs)
        print('调用后')
        return result
    return wrapper

@log
def hello():
    print('hello')
hello()
```
- 闭包：函数内定义函数并返回
```python
def outer():
    x = 10
    def inner():
        print(x)
    return inner
f = outer()
f()
```

## 15. 注释与文档字符串
- 单行注释：#
- 多行注释/文档字符串：'''...'''
```python
# 这是单行注释
'''
这是多行注释
'''
def foo():
    '''这是函数文档字符串'''
    pass
```

## 16. 虚拟环境与包管理
- pip install 包名
- venv 创建虚拟环境
- requirements.txt 管理依赖
```shell
python -m venv venv
venv\Scripts\activate
pip install numpy
pip freeze > requirements.txt
```

---

如需某一知识点详细代码示例，请指定。
