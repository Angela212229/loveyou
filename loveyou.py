from flask import Flask, render_template






loveyouApp = Flask(__name__)

@loveyouApp.route('/')
def inicio():
    return render_template('index.html')



@loveyouApp.route("/amor")
def amor():
    return render_template("amor.html")  

@loveyouApp.route("/carta")
def carta():
    return render_template("carta.html")


@loveyouApp.route("/galeria")
def galeria():
    return render_template("galeria.html")


@loveyouApp.route("/razones")
def razones():
    return render_template("razones.html")

@loveyouApp.route('/linea')
def linea():
    return render_template('/linea.html')


@loveyouApp.route('/mapa')
def mapa():
    return render_template('/mapa.html')

@loveyouApp.route('/deseos')
def deseos():
    return render_template('/deseos.html')


@loveyouApp.route('/poemas')
def poemas():
    return render_template('/poemas.html')


@loveyouApp.route('/diario')
def diario():
    return render_template('/diario.html')

@loveyouApp.route('/cajita')
def cajita():
    return render_template('/cajita.html')

@loveyouApp.route('/detalles')
def detalles():
    return render_template('/detalles.html')

@loveyouApp.route('/adivina')
def adivina():
    return render_template('/adivina.html')

@loveyouApp.route('/cofre')
def cofre():
    return render_template('/cofre.html')

@loveyouApp.route('/poderes')
def poderes():
    return render_template('/poderes.html')

@loveyouApp.route('/final')
def final():
    return render_template('/final.html')


        


if __name__ == '__main__':
    loveyouApp.run(port=3300)



