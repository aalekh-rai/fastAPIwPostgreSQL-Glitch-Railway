# Import necessary libraries and modules
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal, engine
from models import Team

# Define app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define Pydantic models
class TeamBase(BaseModel):
    name: str
    city: str

class TeamResponse(TeamBase):
    id: int

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return {"message": "Server is running!"}


# CRUD endpoints
@app.post("/teams/", response_model=TeamResponse)
def create_team(team: TeamBase, db: Session = Depends(get_db)):
    db_team = Team(name=team.name, city=team.city)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

@app.get("/teams/{team_id}", response_model=TeamResponse)
def read_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.put("/teams/{team_id}", response_model=TeamResponse)
def update_team(team_id: int, team: TeamBase, db: Session = Depends(get_db)):
    db_team = db.query(Team).filter(Team.id == team_id).first()
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db_team.name = team.name
    db_team.city = team.city
    db.commit()
    db.refresh(db_team)
    return db_team

@app.delete("/teams/{team_id}", response_model=TeamResponse)
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db.delete(team)
    db.commit()
    return team
