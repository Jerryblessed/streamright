import os
import ssl
import smtplib
import secrets
import sqlite3
from os import mkdir
from random import randint
from os.path import exists
from datetime import datetime
from email.message import EmailMessage
from passlib.hash import sha256_crypt
from flask import render_template, Blueprint
from forms import (
    loginForm,
    signUpForm,
    commentForm,
    createPostForm,
    verifyUserForm,
    passwordResetForm,
    changePasswordForm,
    changeUserNameForm,
    changeProfilePictureForm,
)
from flask import (
    Flask,
    flash,
    request,
    session,
    redirect,
    Blueprint,
    render_template,
    send_from_directory,
)


def currentDate():
    return datetime.now().strftime("%d.%m.%y")


def currentTime(seconds=False):
    if not seconds:
        return datetime.now().strftime("%H:%M")
    else:
        return datetime.now().strftime("%H:%M:%S")


def message(color, message):
    with open("log.log", "a") as logFile:
        logFile.write(f"[{currentDate()}|{currentTime(True)}] {message}\n")
    print(
        f"\n\033[94m[{currentDate()}\033[0m"
        f"\033[95m {currentTime(True)}]\033[0m"
        f"\033[9{color}m {message}\033[0m\n"
    )


def addPoints(points, user):
    connection = sqlite3.connect("db/users.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE users SET points = points + ? WHERE userName = ?', (points, user))
    connection.commit()
    message("2", f'{points} POINTS ADDED TO "{user}"')


def getProfilePicture(userName):
    connection = sqlite3.connect("db/users.db")
    cursor = connection.cursor()
    cursor.execute('SELECT profilePicture FROM users WHERE lower(userName) = ?', (userName.lower(),))
    return cursor.fetchone()[0]
