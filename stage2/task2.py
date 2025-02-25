from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import httpx
from tortoise.contrib.fastapi import register_tortoise
from tortoise.models import Model
from tortoise import fields

DATABASE_URL = "sqlite://db.sqlite3"
GOREST_URL = "https://gorest.co.in/public/v2"


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    gender = fields.CharField(max_length=10)
    status = fields.CharField(max_length=10)


class Post(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="posts")
    title = fields.CharField(max_length=200)
    body = fields.TextField()


async def fetch_and_store_data():
    async with httpx.AsyncClient() as client:
        users_response = await client.get(f"{GOREST_URL}/users")
        posts_response = await client.get(f"{GOREST_URL}/posts")

        if users_response.status_code == 200 and posts_response.status_code == 200:
            users_data = users_response.json()
            posts_data = posts_response.json()

            for user in users_data:
                await User.get_or_create(
                    id=user["id"],
                    defaults={
                        "name": user["name"],
                        "email": user["email"],
                        "gender": user["gender"],
                        "status": user["status"]
                    }
                )

            for post in posts_data:
                await Post.get_or_create(
                    id=post["id"],
                    defaults={
                        "user_id": post["user_id"],
                        "title": post["title"],
                        "body": post["body"]
                    }
                )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Виконується при старті сервера"""
    if not await User.exists():
        await fetch_and_store_data()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/users")
async def get_users():
    return await User.all()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/{user_id}/posts")
async def get_user_posts(user_id: int):
    user = await User.get_or_none(id=user_id).prefetch_related("posts")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts


register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["__main__"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
