from flask import Flask, render_template, request, flash
import sqlite3


app=Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html",sayfa="insanolanbiri | blog")

@app.errorhandler(404)
def e404(hata):
    return f"yok ki öyle bişey :( <hr style=\"margin-top: 50px;\"> {hata}"
