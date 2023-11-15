from helpers import session, redirect, message, Blueprint

logoutBlueprint = Blueprint("logout", __name__)

@logoutBlueprint.route("/logout")
def logout():
    if "userName" in session:
        message("2", f'USER: "{session["userName"]}" LOGGED OUT')
        session.clear()
        return redirect("/")
    else:
        message("1", f"USER NOT LOGGED IN")
        return redirect("/")
