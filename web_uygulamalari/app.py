from flask import Flask, render_template, request, redirect, url_for
import csv, os
app=Flask(__name__)



@app.route("/")
def index():
    deger=request.args.get("isim","tanımsız")
    deger2=request.args.get("soyisim","tanımsızoğulları")
    return render_template("index.html",ad=deger,soyad=deger2)



@app.route("/test")
def test():
    return "test"



@app.route("/liste")
def liste():
    file=""
    try:
        kisiler=[]
        yol=os.path.join(os.getcwd(),"kayitlar.csv")
        file=open(yol, 'r', encoding="utf-8")
        reader=csv.reader(file)
        kisiler=list(reader)
    except:
        kisiler=["bir", "şey", "oldu"]
    finally:
        if file: file.close()
    return render_template("liste.html",kisiler=kisiler)



@app.route("/kayit")
def kayit():
    return render_template("kayit_formu.html",hata="henüz hata yok")



@app.route("/kaydet",methods=["POST"])
def kaydet():
    file=""
    ad,soyad,program=request.form.get("ad"),request.form.get("soyad"),request.form.get("program")
    if not (ad and soyad and program):
        return render_template("kayit_formu.html",hata="bilgiler eksik")
    try:
        yol=os.path.join(os.getcwd(),"kayitlar.csv")
        file=open(yol, 'a+', newline='', encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow((ad.capitalize(),soyad.upper(),program))
    except:
        return render_template("kayit_formu.html",hata="veri kaydedilemedi")
    finally:
        if file: file.close()
    return redirect(url_for('kayit'))




@app.errorhandler(404)
def e404(hata):
    return f"yok ki öyle bişey :( <hr style=\"margin-top: 50px;\"> {hata}"

#app.run(host="0.0.0.0",port=5000)
