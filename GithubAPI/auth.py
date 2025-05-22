"""
__author__ = "Marouane"
"""
from flask import Flask, redirect, request, session
import requests

app = Flask(__name__)
# app.secret_key = "YOUR_SECRET_KEY"

CLIENT_ID = "Ov23liT78750fLqNHyBJ"
CLIENT_SECRET = "5d1708e04f8161ada53ea50a44c992d60289a2bd"

@app.route("/login")
def login():
    redirect_uri = "https://yourapp.com/auth/callback"
    github_auth_url = (
        f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}"
        f"&redirect_uri={redirect_uri}&scope=repo"
    )
    return redirect(github_auth_url)

@app.route("/auth/callback")
def auth_callback():
    code = request.args.get("code")
    token_res = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
        },
    )
    token_json = token_res.json()
    access_token = token_json.get("access_token")
    session["access_token"] = access_token
    return "Logged in! Now you can fork repo programmatically."

if __name__ == "__main__":
    app.run()
