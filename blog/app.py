from flask import Flask, render_template, request, redirect
import sqlite3, os

db_yol=os.path.join(os.getcwd(),"yazilar.db")

app=Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html",sayfa="insanolanbiri | blog")

@app.route("/yazar_ekle",methods=["GET","POST"])
def yazar_ekle():
    hata=""
    kisi=["","",""]
    if request.method=="POST":
        id=request.form.get("id")
        ad=request.form.get("ad")
        soyad=request.form.get("soyad")
        if not(id or ad or soyad):
            return render_template("yazar.html",hata="doğru düzgün gir",buton="ekle")
        try:
            DB=sqlite3.connect(db_yol)
            imlec=DB.cursor()
            imlec.execute("insert or replace into yazar values(?,?,?)",[int(id),ad,soyad])
            DB.commit()
        except: hata="bir şey oldu"
        finally: DB.close()
    else:
        action=request.args.get("action")
        id=request.args.get("id")
        if action=="update" and id:
            try:
                DB=sqlite3.connect(db_yol)
                imlec=DB.cursor()
                imlec.execute("select * from yazar where id=?",[int(id)])
                kisi=imlec.fetchone()
            except: hata="bir şey oldu"
            finally: DB.close()
    DB=sqlite3.connect(db_yol)
    imlec=DB.cursor()
    imlec.execute("select * from yazar")
    yazarlar=imlec.fetchall()
    DB.close()
    return render_template("yazar.html",hata=hata,yazarlar=yazarlar,kisi=kisi,buton="ekle/güncelle",sayfa="insanolanbiri | yazar ekle")

@app.route("/yazar_sil")
def yazar_sil():
    id=request.args.get("id")
    if id:
        try:
            DB=sqlite3.connect(db_yol)
            imlec=DB.cursor()
            imlec.execute("delete from yazar where id=?",[int(id)])
            DB.commit()
        finally: DB.close()
    return redirect("/yazar_ekle")


@app.route("/konu_ekle",methods=["GET","POST"])
def konu_ekle():
    return render_template("konu.html",sayfa="insanolanbiri | konu ekle")


@app.route("/yazi_ekle",methods=["GET","POST"])
def yazi_ekle():
    return render_template("yazi.html",sayfa="insanolanbiri | yazı ekle")


@app.errorhandler(404)
def e404(hata):
    return f"yok ki öyle bişey :( <hr style=\"margin-top: 50px;\"> {hata}"
