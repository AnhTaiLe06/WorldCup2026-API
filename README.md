# 🏆 World Cup 2026 API

A free, public REST API providing data on all **48 nations** and **1,000+ players** participating in the 2026 FIFA World Cup

Built with **FastAPI** + **SQLAlchemy** + **SQLite**.

> ⚠️ Players squads are based on predictions for now because of the official May 30, 2026 announcement. Data will be updated once official squads are confirmed.

---

## 🌐 Live API

```
https://worldcup2026-api.onrender.com
```

Interactive docs available at:
```
https://worldcup2026-api.onrender.com/docs
```

---

## 📡 Endpoints

### Nations

|Method|Endpoint|Description|
|------|--------|-----------|
|`GET`|`/nations`|Get all nations|
|`GET`|`/nations/{nation_id}`|Get a nation by its ID|
|`POST`| `/nations`|Add a new nation 🔒 Requires API key|

**Example response - `https://worldcup2026-api.onrender.com/nations/1`**
```json
{
  "id": 1,
  "name": "Algeria",
  "confederation": "CAF",
  "group_name": "J",
  "fifa_rank": 28
}
```

---

### Players

|Method|Endpoint|Description|
|------|--------|-----------|
|`GET`|`/players`|Get all players|
|`GET`|`/players/{player_id}`|Get a player by ID|
|`GET`|`/nations/{nation_id}/players`|Get all players from a nation|
|`POST`| `/nations`|Add a new nation 🔒 Requires API key|

**Example response - `https://worldcup2026-api.onrender.com/players/1`**
```json
{
  "id": 1,
  "name": "Raïs M'Bolhi",
  "age": 39,
  "position": "Goalkeeper",
  "jersey_number": 1,
  "nation": {
    "id": 1,
    "name": "Algeria",
    "confederation": "CAF",
    "group_name": "J",
    "fifa_rank": 28
  }
}
```

---

## 🚀 Run Locally
