from fastapi import FastAPI

app = FastAPI()

users = []
profiles = []
messages = []

@app.get("/users")
async def users_list():
    return users

@app.post("/users")
async def user_add(user: dict):
    users.append(user)
    return {"message": "User qoshildi", "data": user}

@app.get("/profiles")
async def profile_list():
    return profiles

@app.post("/profiles")
async def profile_add(profile: dict):
    profiles.append(profile)
    return {"message": "Profil yaratildi", "data": profile}

@app.get("/messages")
async def message_list():
    return messages

@app.post("/messages")
async def mesage_send(message: dict):
    messages.append(message)
    return {"message": "Xabar yuborildi", "data": message}