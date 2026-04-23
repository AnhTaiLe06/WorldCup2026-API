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

### Prerequisites
- Python 3.11+
- pip3

### Setup
 
**1. Clone the repository**
```bash
git clone https://github.com/AnhTaiLe06/WorldCup2026-API.git
cd WorldCup2026-API
```
 
**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
 
**3. Install dependencies**
```bash
pip3 install -r requirements.txt
```
 
**4. Seed the database**
```bash
python3 seed.py
```
 
**5. Start the server**
```bash
uvicorn main:app --reload
```
 
The API will be running at `http://127.0.0.1:8000`. Visit `http://127.0.0.1:8000/docs` for the interactive documentation.
 
---

## 🛠️ Tech Stack
 
| Tool | Purpose |
|------|---------|
| Python | Programming language |
| FastAPI | API framework |
| SQLAlchemy | ORM / database management |
| SQLite | Database |
| Uvicorn | ASGI server |
| Render | Cloud deployment |

---
 
## 🤝 Contributing
 
Contributions are welcome! If you spot incorrect player data or want to add stats after the tournament starts, feel free to open a pull request.
 
---
 
## 📄 License
 
This project is open source and available under the [MIT License](LICENSE).