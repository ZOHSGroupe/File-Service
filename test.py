from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://192.168.1.121"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    # Use uvicorn to run the FastAPI app
    uvicorn.run(app, host="localhost", port=3000)