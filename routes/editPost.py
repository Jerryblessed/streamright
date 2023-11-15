from helpers import (
    session,
    sqlite3,
    request,
    flash,
    message,
    redirect,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    createPostForm,
)

editPostBlueprint = Blueprint("editPost", __name__)

@editPostBlueprint.route("/editpost/<int:postID>", methods=["GET", "POST"])
def editPost(postID):
    if "userName" in session:
        # Check if the post exists
        connection = sqlite3.connect("db/posts.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM posts WHERE id = ?", (postID,))
        post = cursor.fetchone()

        if post:
            message("2", f'POST: "{postID}" FOUND')

            # Check if the post belongs to the logged-in user
            if post[4] == session["userName"]:
                form = createPostForm(request.form)
                form.postTitle.data = post[1]
                form.postTags.data = post[2]
                form.postContent.data = post[3]

                if request.method == "POST":
                    postTitle = request.form["postTitle"]
                    postTags = request.form["postTags"]
                    postContent = request.form["postContent"]

                    if not postContent.strip():
                        flash("Post content cannot be empty", "error")
                        message(
                            "1",
                            f'POST CONTENT CANNOT BE EMPTY, USER: "{session["userName"]}"',
                        )
                    else:
                        # Update the post
                        cursor.execute(
                            "UPDATE posts SET title = ?, tags = ?, content = ?, "
                            "lastEditDate = ?, lastEditTime = ? WHERE id = ?",
                            (
                                postTitle,
                                postTags,
                                postContent,
                                currentDate(),
                                currentTime(),
                                postID,
                            ),
                        )
                        connection.commit()

                        message("2", f'POST: "{postTitle}" EDITED')
                        flash("Post edited", "success")
                        return redirect(f"/post/{postID}")

                return render_template(
                    "/editPost.html",
                    title=post[1],
                    tags=post[2],
                    content=post[3],
                    form=form,
                )
            else:
                flash("This post does not belong to you", "error")
                message(
                    "1",
                    f'THIS POST DOES NOT BELONG TO USER: "{session["userName"]}"',
                )
                return redirect("/")
        else:
            message("1", f'POST: "{postID}" NOT FOUND')
            return render_template("404.html")
    else:
        message("1", "USER NOT LOGGED IN")
        flash("You need to log in to edit a post", "error")
        return redirect("/login")

# from helpers import (
#     session,
#     sqlite3,
#     request,
#     flash,
#     message,
#     redirect,
#     currentDate,
#     currentTime,
#     render_template,
#     Blueprint,
#     createPostForm,
# )

# editPostBlueprint = Blueprint("editPost", __name__)

# @editPostBlueprint.route("/editpost/<int:postID>", methods=["GET", "POST"])
# def editPost(postID):
#     if "userName" in session:
#         connection = sqlite3.connect("db/posts.db")
#         cursor = connection.cursor()
#         cursor.execute(f"select id from posts")
#         posts = str(cursor.fetchall())
#         if str(postID) in posts:
#             connection = sqlite3.connect("db/posts.db")
#             cursor = connection.cursor()
#             cursor.execute(f"select * from posts where id = {postID}")
#             post = cursor.fetchone()
#             message("2", f'POST: "{postID}" FOUND')
#             connection = sqlite3.connect("db/users.db")
#             cursor = connection.cursor()
#             cursor.execute(
#                 f'select userName from users where userName="{session["userName"]}"'
#             )
#             if post[4] == session["userName"]:
#                 form = createPostForm(request.form)
#                 form.postTitle.data = post[1]
#                 form.postTags.data = post[2]
#                 form.postContent.data = post[3]
#                 if request.method == "POST":
#                     postTitle = request.form["postTitle"]
#                     postTags = request.form["postTags"]
#                     postContent = request.form["postContent"]
#                     if postContent == "":
#                         flash("post content not be empty", "error")
#                         message(
#                             "1",
#                             f'POST CONTENT NOT BE EMPTY USER: "{session["userName"]}"',
#                         )
#                     else:
#                         connection = sqlite3.connect("db/posts.db")
#                         cursor = connection.cursor()
#                         cursor.execute(
#                             f'update posts set title = "{postTitle}" where id = {post[0]}'
#                         )
#                         cursor.execute(
#                             f'update posts set tags = "{postTags}" where id = {post[0]}'
#                         )
#                         cursor.execute(
#                             f'update posts set content = "{postContent}" where id = {post[0]}'
#                         )
#                         cursor.execute(
#                             f'update posts set lastEditDate = "{currentDate()}" where id = {post[0]}'
#                         )
#                         cursor.execute(
#                             f'update posts set lastEditTime = "{currentTime()}" where id = {post[0]}'
#                         )
#                         connection.commit()
#                         message("2", f'POST: "{postTitle}" EDITED')
#                         flash("Post edited", "success")
#                         return redirect(f"/post/{post[0]}")

#                 return render_template(
#                     "/editPost.html",
#                     title=post[1],
#                     tags=post[2],
#                     content=post[3],
#                     form=form,
#                 )
#             else:
#                 flash("this post not yours", "error")
#                 message(
#                     "1",
#                     f'THIS POST DOES NOT BELONG TO USER: "{session["userName"]}"',
#                 )
#                 return redirect("/")
#         else:
#             message("1", f'POST: "{postID}" NOT FOUND')
#             return render_template("404.html")
#     else:
#         message("1", "USER NOT LOGGED IN")
#         flash("you need login for edit a post", "error")
#         return redirect("/login")
