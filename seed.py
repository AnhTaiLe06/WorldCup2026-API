from database import SessionLocal, engine
import crud
from schemas import NationCreate, PlayerCreate
from csv import DictReader
from models import Nation, Base

Base.metadata.create_all(bind=engine)

db = SessionLocal()

existing = crud.get_nations(db)
if existing:
    print("Database already seeded!")
    db.close()
    exit()

with open('nations.csv', 'r') as data:
    nations = list(DictReader(data))

with open('players.csv', 'r') as data:
    players = list(DictReader(data))

for nation in nations:
    crud.create_nation(db, NationCreate(
        name=nation["name"], 
        confederation=nation["confederation"], 
        group_name=nation["group_name"],
        fifa_rank=int(nation["fifa_rank"])
    ))

id_by_nation = {}
tmp = db.query(Nation.name, Nation.id).all()
for name, ID in tmp:
    id_by_nation[name] = ID

for player in players:
    crud.create_player(db, PlayerCreate(
        name=player["name"], 
        age=int(player["age"]),
        position=player["position"],
        jersey_number=int(player["jersey_number"]),
        nation_id=id_by_nation[player["nation"]]
    ))