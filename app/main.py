from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 👉 NEU
@app.get("/")
def root():
    return {"message": "Job System API running"}

# 👉 NEU
@app.get("/health")
def health():
    return {"status": "ok"}

# bestehend
app.include_router(router)