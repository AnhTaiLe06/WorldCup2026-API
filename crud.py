from sqlalchemy.orm import Session
from schemas import NationCreate, PlayerCreate
from models import Nation, Player

def create_nation(db: Session, nation: NationCreate):
    # tmp = Nation(
    #     name = nation.name,
    #     confederation = nation.confederation,
    #     group_name = nation.group_name,
    #     fifa_rank = nation.fifa_rank
    # )
    tmp = Nation(**nation.model_dump())
    db.add(tmp)
    db.commit()
    db.refresh(tmp)
    return tmp

def get_nations(db: Session):
    return db.query(Nation).all()

def get_nation_by_id(db:Session, nation_id: int):
    return db.query(Nation).filter(Nation.id == nation_id).first()

def create_player(db: Session, player: PlayerCreate):
    # tmp = Player(
    #     name = player.name,
    #     age = player.age,
    #     position = player.position,
    #     jersey_number = player.jersey_number,
    #     nation_id = player.nation_id
    # )
    tmp = Player(**player.model_dump())
    db.add(tmp)
    db.commit()
    db.refresh(tmp)
    return tmp

def get_players(db: Session):
    return db.query(Player).all()

def get_player_by_id(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()

def get_players_by_nation(db: Session, nation_id: int):
    return db.query(Player).filter(Player.nation_id == nation_id).all()