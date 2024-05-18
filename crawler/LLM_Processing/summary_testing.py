from database import db

Relative = db["summaries"]
Article = db["articles"]
relatives = list(Relative.find())
for relative in relatives:
    if (
        relative["summary"]["easy"] == ""
        and relative["summary"]["normal"] == ""
        and relative["summary"]["detailed"] == ""
    ):
        article = Article.find_one({"_id": relative["article_id"]})
        print(article)
        print(relative)

    # print(relative)
