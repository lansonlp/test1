from fastapi import FastAPI
import uvicorn

from starlette.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World "}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

