from flask import Flask, render_template, request, make_response
import random

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=['GET'])
def play():
    secret_number = request.cookies.get("secret_number")
    response = make_response(render_template("game.html"))

    if not secret_number:
        new_number = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_number))
    return response

@app.route("/result", methods=['POST'])
def result():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        outcome = f"That's right! The number was {secret_number}!"
        response = make_response(render_template("result.html", outcome=outcome))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response
    elif guess > secret_number:
        outcome = f"That's too high, try something smaller."
        response = make_response(render_template("result.html", outcome=outcome))
        return response
    elif guess < secret_number:
        outcome = f"That's too low, try something bigger."
        response = make_response(render_template("result.html", outcome=outcome))
        return response


if __name__ == '__main__':
    app.run(use_reloader=True)
