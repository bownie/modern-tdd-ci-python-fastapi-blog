from uvicorn import run
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from blog.commands import CreateArticleCommand
from blog.queries import GetArticleByIDQuery, ListArticlesQuery

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

class ArticleInput(BaseModel):
    author: str
    title: str
    content: str

@app.post("/create-article/")
async def create_article(article: ArticleInput):
    cmd = CreateArticleCommand(author=article.author, title=article.title, content=article.content)
    result = cmd.execute()
    return jsonable_encoder(result.dict())


@app.get("/article/{article_id}/")
async def get_article(article_id):
    query = GetArticleByIDQuery(
        id=article_id
    )
    return jsonable_encoder(query.execute().dict())

@app.get("/article-list/")
async def list_articles():
    query = ListArticlesQuery()
    records = [record.dict() for record in query.execute()]
    return jsonable_encoder(records)

if __name__ == "__main__":
    run(app, host="localhost", port=8000)
