# coding=utf-8
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    items = [
        {"name": "Apfel", "Anzahl": "5"},
        {"name": "Birne", "Anzahl": "5"},
        {"name": "Birne", "Anzahl": "5"},
    ]
    return render_template("start.html", name="Max Mustermann", items=items)


@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)


@app.route("/wechselkurs")
def wechselkurs():
    waehrung1 = request.args.get("waehrung1", "EUR")
    waehrung2 = request.args.get("waehrung2", "CHF")
    kurs = float(request.args.get("kurs", "2"))
    tabelle = []
    for i in range(1, 20):
        tabelle.append((i, round(kurs * i, 2)))

    tabelle2 = []
    for i in range(1,20):
        tabelle2.append((i, round(i / kurs, 2)))
    print(tabelle2)
    return render_template("wechselkurs.html", waehrung1=waehrung1, waehrung2=waehrung2, kurs=kurs, tabelle=tabelle, tabelle2=tabelle2)
