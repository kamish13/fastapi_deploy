from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}
