from fastapi import FastAPI
import time

app = FastAPI()
@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"路径: {request.url.path}, 方法: {request.method}, 耗时: {process_time:.4f}秒")
    return response


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'耗时：{end-start:.4f}秒')
#         return result
#     return wrapper
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'接口 {func.__name__} 耗时：{end-start:.4f}秒')
        return result
    return wrapper

@app.get("/1")
def hello():
    return {"msg": "AI server running"}

@app.get("/fibonacci/n={n}")
def fibonacci(n: int = 10):
        def fibonacci(n):
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b
        return {"msg": "done","data": list(fibonacci(n))}
@app.get("/getNum")
def getNum():
    num = None
    @timer
    def add(x: int, y: int) -> int:
        for _ in range(1000000):
            num = (x + y / 2) * (x - y / 2)
            print(_)
            return num
    return {"msg": "done","data": add(2, 3)}
@app.get("/getNum2")
def slow_func():
    @timer
    def add(x: int, y: int) -> int:
        return x + y
    return {"msg": "done","data": add(2, 3)}