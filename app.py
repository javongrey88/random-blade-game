# app.py (Phase 3)
from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_random_key"

# app.py (top)
warriors = [
    {"id": 1,  "name": "Horis",     "image": "warrior1.png"},
    {"id": 2,  "name": "Vetra",         "image": "warrior2.png"},
    {"id": 3,  "name": "Shinto",    "image": "warrior3.png"},
    {"id": 4,  "name": "Petra",        "image": "warrior4.png"},
    {"id": 5,  "name": "Tidus",        "image": "warrior5.png"},
    {"id": 6,  "name": "Hilda",    "image": "warrior6.png"},
    {"id": 7,  "name": "Jaguar",       "image": "warrior7.png"},
    {"id": 8,  "name": "Betty",      "image": "warrior8.png"},
    {"id": 9,  "name": "William","image": "warrior9.png"},
    {"id": 10, "name": "0387",     "image": "warrior10.png"}
]


@app.route("/", methods=["GET", "POST"])
def select_warrior():
    if request.method == "POST":
        player_id = int(request.form.get("warrior_id"))
        session["player_id"] = player_id
        session["player_health"] = 100

        comp_id = random.randint(1, 10)
        session["computer_id"] = comp_id
        session["computer_health"] = 100

        return redirect(url_for("battle"))
    return render_template("select.html", warriors=warriors)

@app.route("/battle", methods=["GET", "POST"])
def battle():
    player_id = session.get("player_id")
    computer_id = session.get("computer_id")
    player_health = session.get("player_health", 0)
    computer_health = session.get("computer_health", 0)

    if request.method == "POST":
        # Random 0/1 rolls
        player_roll = random.randint(0, 1)
        comp_roll = random.randint(0, 1)

        # Deduct 10 HP if roll == 0
        if player_roll == 0:
            player_health -= 10
        if comp_roll == 0:
            computer_health -= 10

        session["player_health"] = player_health
        session["computer_health"] = computer_health

        # Check for outcome
        if player_health <= 0 or computer_health <= 0:
            if player_health <= 0 and computer_health <= 0:
                result = "Draw"
            elif player_health <= 0:
                result = "Defeated"
            else:
                result = "Victory"
            return render_template(
                "battle.html",
                warriors=warriors,
                player_id=player_id,
                comp_id=computer_id,
                player_health=player_health,
                computer_health=computer_health,
                result=result
            )

    # Ongoing or initial GET
    return render_template(
        "battle.html",
        warriors=warriors,
        player_id=player_id,
        comp_id=computer_id,
        player_health=player_health,
        computer_health=computer_health,
        result=None
    )

@app.route("/reset")
def reset_game():
    session.clear()
    return redirect(url_for("select_warrior"))

if __name__ == "__main__":
    app.run(debug=True)
