from fastapi import APIRouter
from .database import SessionLocal
from .models import Job

router = APIRouter()

@router.post("/job")
def create_job(task: str):
    db = SessionLocal()
    job = Job(task=task)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@router.get("/jobs")
def get_jobs():
    db = SessionLocal()
    return db.query(Job).all()
