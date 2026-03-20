# FastAPI 基础知识详解
"""
本文件适合零基础学习 FastAPI，内容涵盖环境安装、基本用法、路由、请求参数、响应、数据校验、依赖注入、异常处理、API文档、常见坑等。
"""

# 1. 环境安装
# 推荐用命令行安装：
# pip install fastapi uvicorn
# uvicorn 是 FastAPI 推荐的运行服务器

# 2. 创建应用与路由
from fastapi import FastAPI
app = FastAPI()

# 3. 基本路由
@app.get("/")
def home():
    """GET请求，访问根路径"""
    return {"msg": "Hello, FastAPI!"}

# 4. 路由方法与路径参数
@app.get("/user/{user_id}")
def get_user(user_id: int):
    """路径参数自动类型校验"""
    return {"user_id": user_id}

# 5. 查询参数
@app.get("/search")
def search(q: str = "", page: int = 1):
    """URL查询参数，支持默认值"""
    return {"q": q, "page": page}

# 6. 请求体与数据校验
from pydantic import BaseModel
class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    """POST请求，自动校验请求体"""
    return {"msg": "User created", "data": user.dict()}

# 7. 响应与状态码
from fastapi import Response, status
@app.get("/status")
def custom_status():
    return Response(content="ok", status_code=status.HTTP_201_CREATED)

# 8. 异常处理
from fastapi import HTTPException
@app.get("/error")
def error():
    raise HTTPException(status_code=404, detail="Not found")

# 9. 依赖注入
from fastapi import Depends

def get_token():
    return "token123"

@app.get("/secure")
def secure(token: str = Depends(get_token)):
    return {"token": token}

# 10. 中间件
from fastapi import Request
@app.middleware("http")
def log_middleware(request: Request, call_next):
    print(f"请求路径: {request.url.path}")
    response = call_next(request)
    return response

# 11. 文件上传
from fastapi import File, UploadFile
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    content = file.file.read()
    return {"filename": file.filename, "size": len(content)}

# 12. API文档与调试
# FastAPI 自动生成 Swagger 文档，访问 /docs 或 /redoc

# 13. 异步支持
import asyncio
@app.get("/async")
async def async_demo():
    await asyncio.sleep(1)
    return {"msg": "async done"}

# 14. 数据库操作（以 sqlite3 为例）
import sqlite3
@app.get("/db")
def db_demo():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO user(name) VALUES (?)', ('Tom',))
    conn.commit()
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()
    conn.close()
    return {"users": users}

# 15. 常见坑与注意事项
"""
- 路由路径不要重复，否则后者会覆盖前者。
- 路由参数类型要与声明一致，否则会报错。
- POST请求必须用 BaseModel 校验，否则参数无法自动解析。
- 文件上传要用 UploadFile，否则大文件会卡死。
- 异步函数要用 async def，否则 await 无效。
- 数据库操作要注意关闭连接，防止资源泄漏。
- 依赖注入要用 Depends，否则参数不会自动传递。
- FastAPI 默认只支持 JSON，文件/表单需特殊声明。
- API文档自动生成，调试非常方便。
"""

# 运行方式
# uvicorn fastapi_guide:app --reload

# 更多进阶内容（如 OAuth2、WebSocket、后台任务、复杂依赖、ORM、测试等）可单独补充。
