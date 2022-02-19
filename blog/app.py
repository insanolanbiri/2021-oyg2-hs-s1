from flask import Flask, render_template, request, flash
import sqlite3


app=Flask(__name__)

@app.route("/")
def anasayfa():
    return "<b>anasayfa</b>"