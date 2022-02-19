from flask import Flask, render_template, request
import sqlite3, os

db_yol=os.path.join(os.getcwd(),"yazilar.db")

app=Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html",sayfa="insanolanbiri | blog")

@app.route("/yazar_ekle",methods=["GET","POST"])
def yazar_ekle():
    hata="henüz hata yok"
    if request.method=="POST":
        id=request.form.get("id")
        ad=request.form.get("ad")
        soyad=request.form.get("soyad")
        if not(id or ad or soyad):
            return render_template("yazar.html",hata="doğru düzgün gir",buton="ekle")
        try:
            DB=sqlite3.connect(db_yol)
            imlec=DB.cursor()
            imlec.execute("insert into yazar values(?,?,?)",[int(id),ad,soyad])#update yok şu an
            DB.commit()
            hata="yazar eklendi"
        except:
            hata="bir şey oldu"
        finally:
            DB.close()
    else:
        action=request.args.get("action")
        id=request.args.get("id")
        if action=="delete" and id:
            try:
                DB=sqlite3.connect(db_yol)
                imlec=DB.cursor()
                imlec.execute("delete from yazar where id=?",[int(id)])
                DB.commit()
                hata="yazar silindi"
            except:
                hata="bir şey oldu"
            finally:
                DB.close()
        elif action=="update" and id:
            return render_template("yazar.html",hata=hata,buton="güncelle",id=id)
    DB=sqlite3.connect(db_yol)
    imlec=DB.cursor()
    imlec.execute("select * from yazar")
    yazarlar=imlec.fetchall()
    return render_template("yazar.html",hata=hata,yazarlar=yazarlar,buton="ekle")
    #return render_template("yazar.html",sayfa="insanolanbiri | yazar ekle")

@app.route("/konu_ekle",methods=["GET","POST"])
def konu_ekle():
    return render_template("konu.html",sayfa="insanolanbiri | konu ekle")

@app.route("/yazi_ekle",methods=["GET","POST"])
def yazi_ekle():
    return render_template("yazi.html",sayfa="insanolanbiri | yazı ekle")

@app.errorhandler(404)
def e404(hata):
    return f"yok ki öyle bişey :( <hr style=\"margin-top: 50px;\"> {hata}"
