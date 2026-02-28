from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    name: str

@app.get("/")
async def read_root():
    return {"status": "ok", "message": "FastAPI server running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/items")
async def create_item(item: Item):
    return {"item": item}

if __name__ == "__main__":
    import uvicorn
    # If you run "python server.py" from the backend folder use "server:app"
    # If you run from repo root use "backend.server:app" instead
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)