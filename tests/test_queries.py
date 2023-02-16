from blog.models import Article
from blog.queries import ListArticlesQuery, GetArticleByIDQuery


AUTHOR_EMAIL="jane@doe.com"

def test_list_articles():
    """
    GIVEN 2 articles stored in the database
    WHEN the execute method is called
    THEN it should return 2 articles
    """
    Article(
        author=AUTHOR_EMAIL,
        title="New Article",
        content="Super extra awesome article"
    ).save()
    Article(
        author=AUTHOR_EMAIL,
        title="Another Article",
        content="Super awesome article"
    ).save()

    query = ListArticlesQuery()

    assert len(query.execute()) == 2


def test_get_article_by_id():
    """
    GIVEN ID of article stored in the database
    WHEN the execute method is called on GetArticleByIDQuery with an ID
    THEN it should return the article with the same ID
    """
    article = Article(
        author=AUTHOR_EMAIL,
        title="New Article",
        content="Super extra awesome article"
    ).save()

    query = GetArticleByIDQuery(
        id=article.id
    )

    assert query.execute().id == article.id
