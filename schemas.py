from pydantic import BaseModel, ConfigDict

class NationCreate(BaseModel):
    name: str
    confederation: str
    group_name: str
    fifa_rank: int | None = None

class NationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    confederation: str
    group_name: str
    fifa_rank: int | None = None

class PlayerCreate(BaseModel):
    name: str
    age: int
    position: str
    jersey_number: int
    nation_id: int

class PlayerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    age: int
    position: str
    jersey_number: int
    nation: NationResponse