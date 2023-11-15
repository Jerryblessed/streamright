from helpers import (
    sqlite3,
    render_template,
    Blueprint,
)

searchBlueprint = Blueprint("search", __name__)

@searchBlueprint.route("/search/<query>", methods=["GET", "POST"])
def search(query):
    queryNoWhiteSpace = query.replace("+", "")
    query = query.replace("+", " ")

    connection = sqlite3.connect("db/users.db")
    cursor = connection.cursor()
    queryUsers = cursor.execute(f"select * from users where userName like '%{query}%'").fetchall()
    queryUsersNoWhiteSpace = cursor.execute(f"select * from users where userName like '%{queryNoWhiteSpace}%'").fetchall()

    connection = sqlite3.connect("db/posts.db")
    cursor = connection.cursor()
    queryTags = cursor.execute(f"select * from posts where tags like '%{query}%'").fetchall()
    queryTitles = cursor.execute(f"select * from posts where title like '%{query}%'").fetchall()
    queryAuthors = cursor.execute(f"select * from posts where author like '%{query}%'").fetchall()
    queryTagsNoWhiteSpace = cursor.execute(f"select * from posts where tags like '%{queryNoWhiteSpace}%'").fetchall()
    queryTitlesNoWhiteSpace = cursor.execute(f"select * from posts where title like '%{queryNoWhiteSpace}%'").fetchall()
    queryAuthorsNoWhiteSpace = cursor.execute(f"select * from posts where author like '%{queryNoWhiteSpace}%'").fetchall()

    posts = []
    users = []
    empty = False

    if queryTags:
        posts.append(queryTags)
    if queryTitles:
        posts.append(queryTitles)
    if queryAuthors:
        posts.append(queryAuthors)

    if queryTagsNoWhiteSpace:
        posts.append(queryTagsNoWhiteSpace)
    if queryTitlesNoWhiteSpace:
        posts.append(queryTitlesNoWhiteSpace)
    if queryAuthorsNoWhiteSpace:
        posts.append(queryAuthorsNoWhiteSpace)

    if queryUsers:
        users.append(queryUsers)
    if queryUsersNoWhiteSpace:
        users.append(queryUsersNoWhiteSpace)

    if not posts and not users:
        empty = True

    resultsID = []
    for post in posts:
        for p in post:
            if p[0] not in resultsID:
                resultsID.append(p[0])

    posts = []
    for postID in resultsID:
        cursor.execute(f"select * from posts where id = {postID}")
        posts.append(cursor.fetchall())

    return render_template(
        "search.html",
        posts=posts,
        users=users,
        query=query,
        empty=empty,
    )
