from flask import Flask, render_template, request

app = Flask("Proiect")


@app.route('/')
def login():
    return render_template("login_page.html")


@app.route('/pagina_principala')
def pagina_principala():
    return render_template("pagina_principala.html")


@app.route('/materiale')
def materiale():
    return render_template("materiale.html")


@app.route('/calcul_rezistente', methods=["POST", "GET"])
def calcul_rezistente():
    try:
        if request.method == "POST":
            rezistivitate = float(request.form["rezistivitate"])
            lungime = float(request.form["lungimea"])
            aria = float(request.form["aria"])
            rezistenta = f"{round(rezistivitate * lungime / aria, 2)}^(-8) Ω "
            return render_template("calcul_rezistente.html", rezis=rezistenta)
        else:
            return render_template("calcul_rezistente.html")
    except ValueError:
        print("Introduceti numai numere!")
    except TypeError:
        print("Introduceti numai numere!")


@app.route('/legea_Ohm', methods=["POST", "GET"])
def legea_ohm():
    return render_template("legea_ohm.html")


@app.route('/calcul_ohm', methods=["POST", "GET"])
def calcul_ohm():
    if request.method == "POST":
        sursa1 = float(request.form["sursa_ohm"])
        rezistenta = float(request.form["rezistenta_ohm"])
        rezistenta_int = float(request.form["rez_int_ohm"])
        intensitatea_ohm = sursa1 / (rezistenta + rezistenta_int)
        return render_template("calcul_ohm.html", inten_ohm=intensitatea_ohm)
    else:
        return render_template("calcul_ohm.html")


@app.route('/calcul_intensitate', methods=["POST, GET"])
def calcul_int():
    if request.method == "POST":
        sursa = float(request.form["sursa"])
        rezistenta_interna = float(request.form["rezistenta_interna"])
        intensitatea = f"{round(sursa / rezistenta_interna, 2)} A"
        return render_template("calcul_intensitate.html", inten=intensitatea)
    else:
        return render_template("calcul_intensitate.html")


if __name__ == '__main__':
    app.run(debug=True)
