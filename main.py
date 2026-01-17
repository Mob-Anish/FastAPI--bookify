from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello world"}


@app.get('/greet')
async def greet_name(name: str, age: int) -> dict:
    return {"message": f"Hello {name}", "age": age}
