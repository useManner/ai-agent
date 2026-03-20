# Python 基础知识梳理

## 1. 变量与数据类型
- 数字：int（整数）、float（浮点数）、complex（复数）
  - int：整数类型，如 1、-5、100
  - float：浮点数类型，如 3.14、-2.5
  - complex：复数类型，如 1+2j
```python
x = 10      # int 整数
y = 3.14   # float 浮点数
z = 1 + 2j # complex 复数
print(type(x), type(y), type(z))
```
- 字符串：str
  - 字符串是文本数据，可以用单引号或双引号包裹。
```python
s = 'hello world'
print(s.upper())  # 转大写
print(s.lower())  # 转小写
print(s.title())  # 首字母大写
print(s.strip())  # 去掉首尾空格
print(s.lstrip())  # 去掉左空格
print(s.rstrip())  # 去掉右空格
print(s.replace('world', 'python'))  # 替换子字符串
print(s.find('world'))  # 查找子字符串，返回索引
print(s.find('python'))  # 查找子字符串，返回索引，-1 表示未找到
print(s.find('python', 6))  # 从索引 6 开始查找，返回索引，-1 表示未找到
print(s.split())  # 分割字符串，返回列表，默认按空格分割
print(s.split('o'))  # 分割字符串，返回列表，指定分割符
print(s[0])      # 取第一个字符
print(s[2:5])    # 切片 从索引 2 开始，不包含索引 5
```
- 布尔：bool（True/False）
  - 只有 True 和 False 两个值，常用于条件判断。
```python
flag = True
print(flag)
print(3 > 2)  # 输出 True
```
- 列表：list
  - 有序可变集合，可以存放任意类型。
```python
lst = [1, 2, 3]
lst.append(4)      # 添加元素
lst.remove(2)      # 删除元素
print(lst)
print(lst[1])      # 取第二个元素
```
- 元组：tuple
  - 有序不可变集合，常用于存放不变的数据。
```python
tpl = (1, 2, 3)
print(tpl[0])
# tpl[0] = 5  # 会报错，元组不可变
```
- 字典：dict
  - 键值对集合，类似 JavaScript 的对象。
```python
d = {'name': 'Tom', 'age': 20}
print(d['name'])
d['age'] = 21  # 修改值
print(d)
```
- 集合：set
  - 无序不重复集合，常用于去重。
```python
s = set([1, 2, 2, 3])
print(s)  # 输出：{1, 2, 3}
s.add(4)
s.remove(2)
print(s)
```

## 2. 运算符
- 算术：+ - * / // % **
  - + 加法，- 减法，* 乘法，/ 除法，// 整除，% 取余，** 幂运算
```python
print(2 + 3, 2 * 3, 5 // 2, 5 % 2, 2 ** 3)
```
- 比较：== != > < >= <=
  - == 相等，!= 不等，> 大于，< 小于，>= 大于等于，<= 小于等于
```python
print(2 == 3, 2 != 3, 2 > 1)
```
- 逻辑：and or not
  - and 与，or 或，not 非
```python
print(True and False, True or False, not True)
```
- 赋值：= += -= *= /=
  - = 赋值，+= 增加，-= 减少，*= 乘，/= 除
```python
x = 1
x += 2
print(x)
```
- 成员：in, not in
  - 检查元素是否在集合中
```python
print(2 in [1,2,3])
print('a' not in 'abc')
```
- 身份：is, is not
  - 判断两个变量是否指向同一对象
```python
x = [1,2]
y = x
print(x is y)  # True
z = [1,2]
print(x is z)  # False
```

## 3. 条件语句
- 用于根据条件执行不同代码块。
```python
x = 5
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
        break  # 跳出循环
    print(i)
for i in range(5):
    if i == 2:
        continue  # 跳过本次
    print(i)
```

## 5. 函数
- 定义：def 函数名(参数):
- 返回值：return
- 匿名函数：lambda
```python
def add(a, b):
    return a + b
print(add(2,3))

f = lambda x: x * 2
print(f(3))
```

## 6. 列表、字典、元组、集合操作
- 增删查改
- 切片
- 遍历
```python
lst = [1,2,3]
lst.append(4)
lst.remove(2)
print(lst)
print(lst[1:3])  # 切片
for item in lst:
    print(item)
```

## 7. 字符串操作
- 拼接、分割、查找、替换、格式化
```python
s = 'hello world'
print(s + '!!!')
print(s.split())
print(s.find('world'))
print(s.replace('world', 'python'))
print('name: {}, age: {}'.format('Tom', 20))
print(f'name: {"Tom"}, age: {20}')  # f-string 格式化
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
- 用于捕获和处理错误，防止程序崩溃。
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
- print：打印输出内容到屏幕。
- len：获取序列（如字符串、列表、元组等）的长度。
- range：生成一个整数序列，常用于循环。
- type：查看变量的数据类型。
- input：获取用户输入（字符串类型）。
- ord：获取字符的 ASCII/Unicode 编码。
- chr：将编码转换为字符。
- sum：求和。
- max/min：求最大/最小值。
- sorted：排序。

```python
print(len([1,2,3]))  # 求长度，输出3
print(list(range(3)))  # 生成序列[0,1,2]
print(type(3.14))  # 类型 float
print(ord('A'), chr(65))  # 字符与ASCII码 65 A
print(sum([1,2,3]), max([1,2,3]), min([1,2,3]), sorted([3,1,2]))
name = input('请输入姓名：')  # 用户输入
print('你输入的是：', name)
```

注意事项：
- input 获取到的内容都是字符串，需要转换类型（如 int(input())）。
- range 生成的是迭代器，常用 list(range(10)) 转为列表。
- sorted 返回新列表，不会改变原列表。

## 13. 列表推导式、生成器、迭代器
- 列表推导式：快速生成新列表，语法简洁。
```python
lst = [x * x for x in range(5)]  # [0,1,4,9,16]
print(lst)
```
- 生成器：用 yield 语句返回一个值，函数不会一次性返回所有结果，而是每次调用生成一个结果，节省内存。
```python
def gen():
    for i in range(3):
        yield i
# 生成器对象
my_gen = gen()
print(next(my_gen))  # 取下一个值 0
for v in my_gen:
    print(v)  # 输出1,2
```
- 迭代器：用 iter() 和 next() 遍历对象。
```python
it = iter([1,2,3])
print(next(it))  # 1
print(next(it))  # 2
```

注意事项：
- next() 取不到值会抛 StopIteration 异常。
- 生成器只能遍历一次。
- 列表推导式适合简单场景，复杂逻辑建议用循环。

## 14. 装饰器、闭包
- 装饰器：用 @func 语法扩展函数功能，常用于日志、权限校验等。
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
- 闭包：函数内定义函数并返回，内部函数可以访问外部变量。
```python
def outer():
    x = 10
    def inner():
        print(x)
    return inner
f = outer()
f()  # 输出10
```

注意事项：
- 装饰器要返回 wrapper，否则原函数无法调用。
- 闭包常用于工厂函数、延迟计算。

## 15. 注释与文档字符串
- 单行注释：用 # 开头，解释代码。
- 多行注释/文档字符串：用 '''...''' 或 """...""" 包裹，常用于说明函数、类用途。
```python
# 这是单行注释
'''
这是多行注释
'''
def foo():
    '''这是函数文档字符串'''
    pass
```

注意事项：
- 注释要简洁明了，避免冗余。
- 文档字符串建议写在函数/类开头，方便自动生成文档。

## 16. 虚拟环境与包管理
- pip install 包名：安装第三方库。
- venv 创建虚拟环境：隔离项目依赖，防止不同项目冲突。
- requirements.txt 管理依赖：批量安装。
```shell
python -m venv venv  # 创建虚拟环境
venv\Scripts\activate  # 激活环境（Windows）
pip install numpy  # 安装包
pip freeze > requirements.txt  # 导出依赖
```

注意事项：
- 每个项目建议用独立虚拟环境。
- requirements.txt 可用 pip install -r requirements.txt 批量安装。
- 激活/退出虚拟环境要用对应命令（Windows/Unix不同）。

---

如需某一知识点详细代码示例，请指定。
