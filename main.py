from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from schemas import NationResponse, NationCreate, PlayerCreate, PlayerResponse
from sqlalchemy.orm import Session
import crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "World cup 2026 API"}

@app.post("/nations", response_model=NationResponse)
def post_nation(nation: NationCreate, db: Session = Depends(get_db)):
    return crud.create_nation(db, nation)

@app.get("/nations", response_model=list[NationResponse])
def get_nations(db: Session = Depends(get_db)):
    return crud.get_nations(db)

@app.get("/nations/{nation_id}", response_model=NationResponse)
def get_nation_by_id(nation_id: int, db: Session = Depends(get_db)):
    return crud.get_nation_by_id(db, nation_id)

@app.post("/players", response_model=PlayerResponse)
def post_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db, player)

@app.get("/players", response_model=list[PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    return crud.get_players(db)

@app.get("/players/{player_id}", response_model=PlayerResponse)
def get_player_by_id(player_id: int, db: Session = Depends(get_db)):
    return crud.get_player_by_id(db, player_id)

@app.get("/nation/{nation_id}/players", response_model=list[PlayerResponse])
def get_player_by_nation(nation_id: int, db: Session = Depends(get_db)):
    return crud.get_players_by_nation(db, nation_id)

