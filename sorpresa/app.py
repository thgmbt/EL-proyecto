from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(
        "index.html",
        nombre="Mi niña",
        remitente="Tu amorcito",
        mensaje="No sé como empezar la verdad. Todo este tiempo que he pasado contigo, conociéndote, aprendiendo a lidiar con los problemas que hemos tenido, todo este tiempo ha sido maravilloso ¿sabes? A pesar de las dificultades que han aparecido, me alegra que hayamos podido avanzar juntos hacia adelante"
        "No encuentro palabras para decir lo feliz que me hace poder decir que te amo, y que eres mía. lo único que quiero es simplemente caminar a tu lado; que seamos dos bueyes atados a un mismo yugo, y sigamos aprendiendo a caminar al mismo ritmo. Juntos. "
        "Y bueno, sé que esta es una pregunta que esperas de hace un tiempo jeje. ¿Quieres ser mi novia?"
    )


if __name__ == "__main__":
    app.run(debug=True)
