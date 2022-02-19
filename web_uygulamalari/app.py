from flask import Flask, render_template, request, redirect, url_for, make_response
from datetime import datetime
import csv, os, numpy as np, matplotlib.pyplot as plt, io, base64, locale

os.environ['TZ'] = 'Europe/Istanbul'
locale.setlocale(locale.LC_TIME,'tr_TR.utf-8')
app=Flask(__name__)

@app.route("/")
def index():
    deger=request.args.get("isim","tanımsız")
    deger2=request.args.get("soyisim","tanımsızoğulları")
    if request.cookies.get("tarih"):
        tarih=request.cookies.get("tarih")
        return render_template("index.html",ad=deger,soyad=deger2,tarih=tarih,sayfa_adi="insanolanbiri")
    else:
        res=make_response(render_template("index.html",ad=deger,soyad=deger2,tarih="çerez yok",sayfa_adi="insanolanbiri"))
        res.set_cookie("tarih",datetime.now().strftime("%d %B %Y - %H:%M:%S"),max_age=2*24*60*60)
        return res



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
    return render_template("liste.html",kisiler=kisiler,sayfa_adi="liste | insanolanbiri")



@app.route("/kayit")
def kayit():
    return render_template("kayit_formu.html",hata="henüz hata yok",sayfa_adi="kayıt | insanolanbiri")



@app.route("/kaydet",methods=["POST"])
def kaydet():
    file=""
    ad,soyad,program=request.form.get("ad"),request.form.get("soyad"),request.form.get("program")
    if not (ad and soyad and program):
        return render_template("kayit_formu.html",hata="bilgiler eksik",sayfa_adi="kayıt | insanolanbiri")
    try:
        yol=os.path.join(os.getcwd(),"kayitlar.csv")
        file=open(yol, 'a+', newline='', encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow((ad,soyad,program))
    except:
        return render_template("kayit_formu.html",hata="veri kaydedilemedi",sayfa_adi="kayıt | insanolanbiri")
    finally:
        if file: file.close()
    return redirect(url_for('kayit'))

@app.route("/grafik",methods=["GET","POST"])
def grafik():
    if request.method=="GET":
        return render_template("grafik.html",resim="<p>henüz grafik yok</p>",sayfa_adi="grafik | insanolanbiri")
    else:
        csx,csy=request.form.get("X"),request.form.get("Y")
        xlist=csx.split(",")
        xlist=[float(i) for i in xlist]

        ylist=csy.split(",")
        ylist=[float(i) for i in ylist]
        
        plt.plot(xlist,ylist)
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        html_resim = '<img src="data:image/png;base64, {}">'.format(base64.b64encode(img.getvalue()).decode('utf-8'))
        return render_template("grafik.html",resim=html_resim,sayfa_adi="grafik | insanolanbiri")


@app.errorhandler(404)
def e404(hata):
    return f"yok ki öyle bişey :( <hr style=\"margin-top: 50px;\"> {hata}"

#app.run(host="0.0.0.0",port=5000)