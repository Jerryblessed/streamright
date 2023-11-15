from flask import Flask, render_template
import os

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://jerryblessed.pythonanywhere.com/'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.route('/')
def hello():
    return render_template('index2.html')

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 5000  # Change to the port you prefer
    port = int(port)
    app.run(debug=True, port=port, host='0.0.0.0')
 
# on windows pc please uncomment the below and comment the above
# import socket
# import os
# from helpers import (
#     secrets,
#     message,
#     render_template,
#     getProfilePicture,
#     Flask,
# )

# from routes.post import postBlueprint
# from routes.user import userBlueprint
# from routes.index import indexBlueprint
# from routes.login import loginBlueprint
# from routes.signup import signUpBlueprint
# from routes.logout import logoutBlueprint
# from routes.search import searchBlueprint
# from routes.editPost import editPostBlueprint
# from routes.searchBar import searchBarBlueprint
# from routes.dashboard import dashboardBlueprint
# from routes.verifyUser import verifyUserBlueprint
# from routes.adminPanel import adminPanelBlueprint
# from routes.createPost import createPostBlueprint
# from routes.setUserRole import setUserRoleBlueprint
# from routes.passwordReset import passwordResetBlueprint
# from routes.changeUserName import changeUserNameBlueprint
# from routes.changePassword import changePasswordBlueprint
# from routes.adminPanelUsers import adminPanelUsersBlueprint
# from routes.adminPanelPosts import adminPanelPostsBlueprint
# from routes.accountSettings import accountSettingsBlueprint
# from routes.adminPanelComments import adminPanelCommentsBlueprint
# from routes.changeProfilePicture import changeProfilePictureBlueprint
# from dbChecker import dbFolder, usersTable, postsTable, commentsTable
# from flask_wtf.csrf import CSRFProtect
# from flask import Flask, request, render_template, jsonify, session
# import google.generativeai as palm


# dbFolder()
# usersTable()
# postsTable()
# commentsTable()

# app = Flask(__name__)
# app.secret_key = secrets.token_urlsafe(32)
# app.config["SESSION_PERMANENT"] = True
# csrf = CSRFProtect(app)

# API_KEY = "AIzaSyBgv0a3DuNlGQy6zxarbWHiVJsUIZhy4Bc"
# palm.configure(api_key=API_KEY)



# @app.context_processor
# def utility_processor():
#     getProfilePicture
#     return dict(getProfilePicture=getProfilePicture)


# @app.errorhandler(404)
# def notFound(e):
#     message("1", "404")
#     return render_template("404.html"), 404

# @app.route('/bot')
# def chat():
#     return render_template('ride.html')
# @app.route('/get_response')
# def get_response():
#     user_message = request.args.get('message')
#     conversation = chat_with_palm(user_message)
#     bot_response = conversation[-1]['content'] if conversation else "An error occurred."

#     return jsonify({"botMessage": bot_response})

# @app.route('/update_context', methods=['GET'])
# def update_context():
#     title = request.args.get('title')
#     session['context_title'] = title
#     return jsonify({"status": "success"})

# def chat_with_palm(prompt):
#     examples = [
#         ('Hello', 'Hi there, how can I assist you today?'),
#         ('I want to make a know more about health', 'Eat well, sleep regularly, and brush always.')
#     ]

#     conversation = []
#     if prompt.lower() == "exit":
#         return conversation
#     context_title  = session.get('context_title', '')
#     response = palm.chat(messages=prompt, temperature=1, context=context_title)
#     for message in response.messages:
#         conversation.append({'author': message['author'], 'content': message['content']})

#     return conversation


# app.register_blueprint(postBlueprint)
# app.register_blueprint(userBlueprint)
# app.register_blueprint(indexBlueprint)
# app.register_blueprint(loginBlueprint)
# app.register_blueprint(signUpBlueprint)
# app.register_blueprint(logoutBlueprint)
# app.register_blueprint(searchBlueprint)
# app.register_blueprint(editPostBlueprint)
# app.register_blueprint(dashboardBlueprint)
# app.register_blueprint(searchBarBlueprint)
# app.register_blueprint(adminPanelBlueprint)
# app.register_blueprint(createPostBlueprint)
# app.register_blueprint(verifyUserBlueprint)
# app.register_blueprint(setUserRoleBlueprint)
# app.register_blueprint(passwordResetBlueprint)
# app.register_blueprint(changeUserNameBlueprint)
# app.register_blueprint(changePasswordBlueprint)
# app.register_blueprint(adminPanelUsersBlueprint)
# app.register_blueprint(adminPanelPostsBlueprint)
# app.register_blueprint(accountSettingsBlueprint)
# app.register_blueprint(adminPanelCommentsBlueprint)
# app.register_blueprint(changeProfilePictureBlueprint)


# # if __name__ == "__main__":
# #     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# if __name__ == '__main__':
#     port = os.environ.get('FLASK_PORT') or 5000  # Change to the port you prefer
#     port = int(port)
#     app.run(debug=True, port=port, host='0.0.0.0')
 
