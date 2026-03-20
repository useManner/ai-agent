# 示例：Python 基础语法
# print('Hello, Python!')

# # 示例：TensorFlow 基础
# try:
#     import tensorflow as tf
#     print('TensorFlow 版本:', tf.__version__)
# except ImportError:
#     print('未安装 TensorFlow')

# 调用version函数获取版本信息，根据获取的版本信息判断是否需要升级
import sys

def check_python_version():
    version = sys.version_info
    print(f"当前Python版本：{version.major}.{version.minor}.{version.micro}")
    # 假设要求最低版本为3.8
    if version < (3, 8):
        print("建议升级Python到3.8及以上！")
    else:
        print("版本满足要求，无需升级。")

check_python_version()

# 也可以检查某个库的版本，比如numpy
try:
    import numpy as np
    print("numpy版本：", np.__version__)
    # 假设要求最低版本为1.20
    if tuple(map(int, np.__version__.split('.'))) < (1, 20):
        print("建议升级numpy到1.20及以上！")
    else:
        print("numpy版本满足要求，无需升级。")
except ImportError:
    print("未安装numpy")

