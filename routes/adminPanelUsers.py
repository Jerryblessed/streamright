from helpers import sqlite3, render_template, Blueprint, session, redirect, request
from delete import deleteUser

adminPanelUsersBlueprint = Blueprint("adminPanelUsers", __name__)

@adminPanelUsersBlueprint.route("/admin/users", methods=["GET", "POST"])
@adminPanelUsersBlueprint.route("/adminpanel/users", methods=["GET", "POST"])
def adminPanelUsers():
    if "userName" in session:
        connection = sqlite3.connect("db/users.db")
        cursor = connection.cursor()
        cursor.execute(
            f'select role from users where userName = "{session["userName"]}"'
        )
        role = cursor.fetchone()[0]

        if request.method == "POST":
            if "userDeleteButton" in request.form:
                deleteUser(request.form["userName"])

        if role == "admin":
            connection = sqlite3.connect("db/users.db")
            cursor = connection.cursor()
            cursor.execute("select * from users")
            users = cursor.fetchall()
            return render_template("adminPanelUsers.html", users=users)
        else:
            return redirect("/")
    else:
        return redirect("/")
